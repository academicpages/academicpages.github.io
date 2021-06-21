#include <nokogiri.h>

VALUE cNokogiriXmlNode ;

static ID id_decorate, id_decorate_bang;

#ifdef DEBUG
static void
debug_node_dealloc(xmlNodePtr x)
{
  NOKOGIRI_DEBUG_START(x)
  NOKOGIRI_DEBUG_END(x)
}
#else
#  define debug_node_dealloc 0
#endif

static void
mark(xmlNodePtr node)
{
  xmlDocPtr doc = node->doc;
  if (doc->type == XML_DOCUMENT_NODE || doc->type == XML_HTML_DOCUMENT_NODE) {
    if (DOC_RUBY_OBJECT_TEST(doc)) {
      rb_gc_mark(DOC_RUBY_OBJECT(doc));
    }
  } else if (node->doc->_private) {
    rb_gc_mark((VALUE)doc->_private);
  }
}

/* :nodoc: */
typedef xmlNodePtr(*pivot_reparentee_func)(xmlNodePtr, xmlNodePtr);

/* :nodoc: */
static void
relink_namespace(xmlNodePtr reparented)
{
  xmlNodePtr child;

  if (reparented->type != XML_ATTRIBUTE_NODE &&
      reparented->type != XML_ELEMENT_NODE) { return; }

  if (reparented->ns == NULL || reparented->ns->prefix == NULL) {
    xmlNsPtr ns = NULL;
    xmlChar *name = NULL, *prefix = NULL;

    name = xmlSplitQName2(reparented->name, &prefix);

    if (reparented->type == XML_ATTRIBUTE_NODE) {
      if (prefix == NULL || strcmp((char *)prefix, XMLNS_PREFIX) == 0) {
        xmlFree(name);
        xmlFree(prefix);
        return;
      }
    }

    ns = xmlSearchNs(reparented->doc, reparented, prefix);

    if (ns != NULL) {
      xmlNodeSetName(reparented, name);
      xmlSetNs(reparented, ns);
    }

    xmlFree(name);
    xmlFree(prefix);
  }

  /* Avoid segv when relinking against unlinked nodes. */
  if (reparented->type != XML_ELEMENT_NODE || !reparented->parent) { return; }

  /* Make sure that our reparented node has the correct namespaces */
  if (!reparented->ns && reparented->doc != (xmlDocPtr)reparented->parent) {
    xmlSetNs(reparented, reparented->parent->ns);
  }

  /* Search our parents for an existing definition */
  if (reparented->nsDef) {
    xmlNsPtr curr = reparented->nsDef;
    xmlNsPtr prev = NULL;

    while (curr) {
      xmlNsPtr ns = xmlSearchNsByHref(
                      reparented->doc,
                      reparented->parent,
                      curr->href
                    );
      /* If we find the namespace is already declared, remove it from this
       * definition list. */
      if (ns && ns != curr && xmlStrEqual(ns->prefix, curr->prefix)) {
        if (prev) {
          prev->next = curr->next;
        } else {
          reparented->nsDef = curr->next;
        }
        noko_xml_document_pin_namespace(curr, reparented->doc);
      } else {
        prev = curr;
      }
      curr = curr->next;
    }
  }

  /*
   *  Search our parents for an existing definition of current namespace,
   *  because the definition it's pointing to may have just been removed nsDef.
   *
   *  And although that would technically probably be OK, I'd feel better if we
   *  referred to a namespace that's still present in a node's nsDef somewhere
   *  in the doc.
   */
  if (reparented->ns) {
    xmlNsPtr ns = xmlSearchNs(reparented->doc, reparented, reparented->ns->prefix);
    if (ns
        && ns != reparented->ns
        && xmlStrEqual(ns->prefix, reparented->ns->prefix)
        && xmlStrEqual(ns->href, reparented->ns->href)
       ) {
      xmlSetNs(reparented, ns);
    }
  }

  /* Only walk all children if there actually is a namespace we need to */
  /* reparent. */
  if (NULL == reparented->ns) { return; }

  /* When a node gets reparented, walk it's children to make sure that */
  /* their namespaces are reparented as well. */
  child = reparented->children;
  while (NULL != child) {
    relink_namespace(child);
    child = child->next;
  }

  if (reparented->type == XML_ELEMENT_NODE) {
    child = (xmlNodePtr)((xmlElementPtr)reparented)->attributes;
    while (NULL != child) {
      relink_namespace(child);
      child = child->next;
    }
  }
}

/* :nodoc: */
static xmlNodePtr
xmlReplaceNodeWrapper(xmlNodePtr pivot, xmlNodePtr new_node)
{
  xmlNodePtr retval ;

  retval = xmlReplaceNode(pivot, new_node) ;

  if (retval == pivot) {
    retval = new_node ; /* return semantics for reparent_node_with */
  }

  /* work around libxml2 issue: https://bugzilla.gnome.org/show_bug.cgi?id=615612 */
  if (retval && retval->type == XML_TEXT_NODE) {
    if (retval->prev && retval->prev->type == XML_TEXT_NODE) {
      retval = xmlTextMerge(retval->prev, retval);
    }
    if (retval->next && retval->next->type == XML_TEXT_NODE) {
      retval = xmlTextMerge(retval, retval->next);
    }
  }

  return retval ;
}

/* :nodoc: */
static VALUE
reparent_node_with(VALUE pivot_obj, VALUE reparentee_obj, pivot_reparentee_func prf)
{
  VALUE reparented_obj ;
  xmlNodePtr reparentee, pivot, reparented, next_text, new_next_text, parent ;
  int original_ns_prefix_is_default = 0 ;

  if (!rb_obj_is_kind_of(reparentee_obj, cNokogiriXmlNode)) {
    rb_raise(rb_eArgError, "node must be a Nokogiri::XML::Node");
  }
  if (rb_obj_is_kind_of(reparentee_obj, cNokogiriXmlDocument)) {
    rb_raise(rb_eArgError, "node must be a Nokogiri::XML::Node");
  }

  Data_Get_Struct(reparentee_obj, xmlNode, reparentee);
  Data_Get_Struct(pivot_obj, xmlNode, pivot);

  /*
   * Check if nodes given are appropriate to have a parent-child
   * relationship, based on the DOM specification.
   *
   * cf. http://www.w3.org/TR/2004/REC-DOM-Level-3-Core-20040407/core.html#ID-1590626202
   */
  if (prf == xmlAddChild) {
    parent = pivot;
  } else {
    parent = pivot->parent;
  }

  if (parent) {
    switch (parent->type) {
    case XML_DOCUMENT_NODE:
    case XML_HTML_DOCUMENT_NODE:
      switch (reparentee->type) {
      case XML_ELEMENT_NODE:
      case XML_PI_NODE:
      case XML_COMMENT_NODE:
      case XML_DOCUMENT_TYPE_NODE:
      /*
       * The DOM specification says no to adding text-like nodes
       * directly to a document, but we allow it for compatibility.
       */
      case XML_TEXT_NODE:
      case XML_CDATA_SECTION_NODE:
      case XML_ENTITY_REF_NODE:
        goto ok;
      default:
        break;
      }
      break;
    case XML_DOCUMENT_FRAG_NODE:
    case XML_ENTITY_REF_NODE:
    case XML_ELEMENT_NODE:
      switch (reparentee->type) {
      case XML_ELEMENT_NODE:
      case XML_PI_NODE:
      case XML_COMMENT_NODE:
      case XML_TEXT_NODE:
      case XML_CDATA_SECTION_NODE:
      case XML_ENTITY_REF_NODE:
        goto ok;
      default:
        break;
      }
      break;
    case XML_ATTRIBUTE_NODE:
      switch (reparentee->type) {
      case XML_TEXT_NODE:
      case XML_ENTITY_REF_NODE:
        goto ok;
      default:
        break;
      }
      break;
    case XML_TEXT_NODE:
      /*
       * xmlAddChild() breaks the DOM specification in that it allows
       * adding a text node to another, in which case text nodes are
       * coalesced, but since our JRuby version does not support such
       * operation, we should inhibit it.
       */
      break;
    default:
      break;
    }

    rb_raise(rb_eArgError, "cannot reparent %s there", rb_obj_classname(reparentee_obj));
  }

ok:
  xmlUnlinkNode(reparentee);

  if (reparentee->doc != pivot->doc || reparentee->type == XML_TEXT_NODE) {
    /*
     *  if the reparentee is a text node, there's a very good chance it will be
     *  merged with an adjacent text node after being reparented, and in that case
     *  libxml will free the underlying C struct.
     *
     *  since we clearly have a ruby object which references the underlying
     *  memory, we can't let the C struct get freed. let's pickle the original
     *  reparentee by rooting it; and then we'll reparent a duplicate of the
     *  node that we don't care about preserving.
     *
     *  alternatively, if the reparentee is from a different document than the
     *  pivot node, libxml2 is going to get confused about which document's
     *  "dictionary" the node's strings belong to (this is an otherwise
     *  uninteresting libxml2 implementation detail). as a result, we cannot
     *  reparent the actual reparentee, so we reparent a duplicate.
     */
    if (reparentee->type == XML_TEXT_NODE && reparentee->_private) {
      /*
       *  additionally, since we know this C struct isn't going to be related to
       *  a Ruby object anymore, let's break the relationship on this end as
       *  well.
       *
       *  this is not absolutely necessary unless libxml-ruby is also in effect,
       *  in which case its global callback `rxml_node_deregisterNode` will try
       *  to do things to our data.
       *
       *  for more details on this particular (and particularly nasty) edge
       *  case, see:
       *
       *    https://github.com/sparklemotion/nokogiri/issues/1426
       */
      reparentee->_private = NULL ;
    }

    if (reparentee->ns != NULL && reparentee->ns->prefix == NULL) {
      original_ns_prefix_is_default = 1;
    }

    noko_xml_document_pin_node(reparentee);

    if (!(reparentee = xmlDocCopyNode(reparentee, pivot->doc, 1))) {
      rb_raise(rb_eRuntimeError, "Could not reparent node (xmlDocCopyNode)");
    }

    if (original_ns_prefix_is_default && reparentee->ns != NULL && reparentee->ns->prefix != NULL) {
      /*
       *  issue #391, where new node's prefix may become the string "default"
       *  see libxml2 tree.c xmlNewReconciliedNs which implements this behavior.
       */
      xmlFree((xmlChar *)reparentee->ns->prefix);
      reparentee->ns->prefix = NULL;
    }
  }

  if (prf != xmlAddPrevSibling && prf != xmlAddNextSibling
      && reparentee->type == XML_TEXT_NODE && pivot->next && pivot->next->type == XML_TEXT_NODE) {
    /*
     *  libxml merges text nodes in a right-to-left fashion, meaning that if
     *  there are two text nodes who would be adjacent, the right (or following,
     *  or next) node will be merged into the left (or preceding, or previous)
     *  node.
     *
     *  and by "merged" I mean the string contents will be concatenated onto the
     *  left node's contents, and then the node will be freed.
     *
     *  which means that if we have a ruby object wrapped around the right node,
     *  its memory would be freed out from under it.
     *
     *  so, we detect this edge case and unlink-and-root the text node before it gets
     *  merged. then we dup the node and insert that duplicate back into the
     *  document where the real node was.
     *
     *  yes, this is totally lame.
     */
    next_text     = pivot->next ;
    new_next_text = xmlDocCopyNode(next_text, pivot->doc, 1) ;

    xmlUnlinkNode(next_text);
    noko_xml_document_pin_node(next_text);

    xmlAddNextSibling(pivot, new_next_text);
  }

  if (!(reparented = (*prf)(pivot, reparentee))) {
    rb_raise(rb_eRuntimeError, "Could not reparent node");
  }

  /*
   *  make sure the ruby object is pointed at the just-reparented node, which
   *  might be a duplicate (see above) or might be the result of merging
   *  adjacent text nodes.
   */
  DATA_PTR(reparentee_obj) = reparented ;

  relink_namespace(reparented);

  reparented_obj = noko_xml_node_wrap(Qnil, reparented);

  rb_funcall(reparented_obj, id_decorate_bang, 0);

  return reparented_obj ;
}


/*
 * call-seq:
 *  document
 *
 * Get the document for this Node
 */
static VALUE
document(VALUE self)
{
  xmlNodePtr node;
  Data_Get_Struct(self, xmlNode, node);
  return DOC_RUBY_OBJECT(node->doc);
}

/*
 * call-seq:
 *  pointer_id
 *
 * Get the internal pointer number
 */
static VALUE
pointer_id(VALUE self)
{
  xmlNodePtr node;
  Data_Get_Struct(self, xmlNode, node);

  return INT2NUM((long)(node));
}

/*
 * call-seq:
 *  encode_special_chars(string)
 *
 * Encode any special characters in +string+
 */
static VALUE
encode_special_chars(VALUE self, VALUE string)
{
  xmlNodePtr node;
  xmlChar *encoded;
  VALUE encoded_str;

  Data_Get_Struct(self, xmlNode, node);
  encoded = xmlEncodeSpecialChars(
              node->doc,
              (const xmlChar *)StringValueCStr(string)
            );

  encoded_str = NOKOGIRI_STR_NEW2(encoded);
  xmlFree(encoded);

  return encoded_str;
}

/*
 * call-seq:
 *  create_internal_subset(name, external_id, system_id)
 *
 * Create the internal subset of a document.
 *
 *   doc.create_internal_subset("chapter", "-//OASIS//DTD DocBook XML//EN", "chapter.dtd")
 *   # => <!DOCTYPE chapter PUBLIC "-//OASIS//DTD DocBook XML//EN" "chapter.dtd">
 *
 *   doc.create_internal_subset("chapter", nil, "chapter.dtd")
 *   # => <!DOCTYPE chapter SYSTEM "chapter.dtd">
 */
static VALUE
create_internal_subset(VALUE self, VALUE name, VALUE external_id, VALUE system_id)
{
  xmlNodePtr node;
  xmlDocPtr doc;
  xmlDtdPtr dtd;

  Data_Get_Struct(self, xmlNode, node);

  doc = node->doc;

  if (xmlGetIntSubset(doc)) {
    rb_raise(rb_eRuntimeError, "Document already has an internal subset");
  }

  dtd = xmlCreateIntSubset(
          doc,
          NIL_P(name)        ? NULL : (const xmlChar *)StringValueCStr(name),
          NIL_P(external_id) ? NULL : (const xmlChar *)StringValueCStr(external_id),
          NIL_P(system_id)   ? NULL : (const xmlChar *)StringValueCStr(system_id)
        );

  if (!dtd) { return Qnil; }

  return noko_xml_node_wrap(Qnil, (xmlNodePtr)dtd);
}

/*
 * call-seq:
 *  create_external_subset(name, external_id, system_id)
 *
 * Create an external subset
 */
static VALUE
create_external_subset(VALUE self, VALUE name, VALUE external_id, VALUE system_id)
{
  xmlNodePtr node;
  xmlDocPtr doc;
  xmlDtdPtr dtd;

  Data_Get_Struct(self, xmlNode, node);

  doc = node->doc;

  if (doc->extSubset) {
    rb_raise(rb_eRuntimeError, "Document already has an external subset");
  }

  dtd = xmlNewDtd(
          doc,
          NIL_P(name)        ? NULL : (const xmlChar *)StringValueCStr(name),
          NIL_P(external_id) ? NULL : (const xmlChar *)StringValueCStr(external_id),
          NIL_P(system_id)   ? NULL : (const xmlChar *)StringValueCStr(system_id)
        );

  if (!dtd) { return Qnil; }

  return noko_xml_node_wrap(Qnil, (xmlNodePtr)dtd);
}

/*
 * call-seq:
 *  external_subset
 *
 * Get the external subset
 */
static VALUE
external_subset(VALUE self)
{
  xmlNodePtr node;
  xmlDocPtr doc;
  xmlDtdPtr dtd;

  Data_Get_Struct(self, xmlNode, node);

  if (!node->doc) { return Qnil; }

  doc = node->doc;
  dtd = doc->extSubset;

  if (!dtd) { return Qnil; }

  return noko_xml_node_wrap(Qnil, (xmlNodePtr)dtd);
}

/*
 * call-seq:
 *  internal_subset
 *
 * Get the internal subset
 */
static VALUE
internal_subset(VALUE self)
{
  xmlNodePtr node;
  xmlDocPtr doc;
  xmlDtdPtr dtd;

  Data_Get_Struct(self, xmlNode, node);

  if (!node->doc) { return Qnil; }

  doc = node->doc;
  dtd = xmlGetIntSubset(doc);

  if (!dtd) { return Qnil; }

  return noko_xml_node_wrap(Qnil, (xmlNodePtr)dtd);
}

/*
 * call-seq:
 *  dup
 *  dup(depth)
 *  dup(depth, new_parent_doc)
 *
 * Copy this node.
 * An optional depth may be passed in. 0 is a shallow copy, 1 (the default) is a deep copy.
 * An optional new_parent_doc may also be passed in, which will be the new
 * node's parent document. Defaults to the current node's document.
 * current document.
 */
static VALUE
duplicate_node(int argc, VALUE *argv, VALUE self)
{
  VALUE r_level, r_new_parent_doc;
  int level;
  int n_args;
  xmlDocPtr new_parent_doc;
  xmlNodePtr node, dup;

  Data_Get_Struct(self, xmlNode, node);

  n_args = rb_scan_args(argc, argv, "02", &r_level, &r_new_parent_doc);

  if (n_args < 1) {
    r_level = INT2NUM((long)1);
  }
  level = (int)NUM2INT(r_level);

  if (n_args < 2) {
    new_parent_doc = node->doc;
  } else {
    Data_Get_Struct(r_new_parent_doc, xmlDoc, new_parent_doc);
  }

  dup = xmlDocCopyNode(node, new_parent_doc, level);
  if (dup == NULL) { return Qnil; }

  noko_xml_document_pin_node(dup);

  return noko_xml_node_wrap(rb_obj_class(self), dup);
}

/*
 * call-seq:
 *  unlink
 *
 * Unlink this node from its current context.
 */
static VALUE
unlink_node(VALUE self)
{
  xmlNodePtr node;
  Data_Get_Struct(self, xmlNode, node);
  xmlUnlinkNode(node);
  noko_xml_document_pin_node(node);
  return self;
}

/*
 * call-seq:
 *  blank?
 *
 * Is this node blank?
 */
static VALUE
blank_eh(VALUE self)
{
  xmlNodePtr node;
  Data_Get_Struct(self, xmlNode, node);
  return (1 == xmlIsBlankNode(node)) ? Qtrue : Qfalse ;
}

/*
 * call-seq:
 *  next_sibling
 *
 * Returns the next sibling node
 */
static VALUE
next_sibling(VALUE self)
{
  xmlNodePtr node, sibling;
  Data_Get_Struct(self, xmlNode, node);

  sibling = node->next;
  if (!sibling) { return Qnil; }

  return noko_xml_node_wrap(Qnil, sibling) ;
}

/*
 * call-seq:
 *  previous_sibling
 *
 * Returns the previous sibling node
 */
static VALUE
previous_sibling(VALUE self)
{
  xmlNodePtr node, sibling;
  Data_Get_Struct(self, xmlNode, node);

  sibling = node->prev;
  if (!sibling) { return Qnil; }

  return noko_xml_node_wrap(Qnil, sibling);
}

/*
 * call-seq:
 *  next_element
 *
 * Returns the next Nokogiri::XML::Element type sibling node.
 */
static VALUE
next_element(VALUE self)
{
  xmlNodePtr node, sibling;
  Data_Get_Struct(self, xmlNode, node);

  sibling = xmlNextElementSibling(node);
  if (!sibling) { return Qnil; }

  return noko_xml_node_wrap(Qnil, sibling);
}

/*
 * call-seq:
 *  previous_element
 *
 * Returns the previous Nokogiri::XML::Element type sibling node.
 */
static VALUE
previous_element(VALUE self)
{
  xmlNodePtr node, sibling;
  Data_Get_Struct(self, xmlNode, node);

  /*
   *  note that we don't use xmlPreviousElementSibling here because it's buggy pre-2.7.7.
   */
  sibling = node->prev;
  if (!sibling) { return Qnil; }

  while (sibling && sibling->type != XML_ELEMENT_NODE) {
    sibling = sibling->prev;
  }

  return sibling ? noko_xml_node_wrap(Qnil, sibling) : Qnil ;
}

/* :nodoc: */
static VALUE
replace(VALUE self, VALUE new_node)
{
  VALUE reparent = reparent_node_with(self, new_node, xmlReplaceNodeWrapper);

  xmlNodePtr pivot;
  Data_Get_Struct(self, xmlNode, pivot);
  noko_xml_document_pin_node(pivot);

  return reparent;
}

/*
 * call-seq:
 *  children
 *
 * Get the list of children for this node as a NodeSet
 */
static VALUE
children(VALUE self)
{
  xmlNodePtr node;
  xmlNodePtr child;
  xmlNodeSetPtr set;
  VALUE document;
  VALUE node_set;

  Data_Get_Struct(self, xmlNode, node);

  child = node->children;
  set = xmlXPathNodeSetCreate(child);

  document = DOC_RUBY_OBJECT(node->doc);

  if (!child) { return noko_xml_node_set_wrap(set, document); }

  child = child->next;
  while (NULL != child) {
    xmlXPathNodeSetAddUnique(set, child);
    child = child->next;
  }

  node_set = noko_xml_node_set_wrap(set, document);

  return node_set;
}

/*
 * call-seq:
 *  element_children
 *
 * Get the list of children for this node as a NodeSet.  All nodes will be
 * element nodes.
 *
 * Example:
 *
 *   @doc.root.element_children.all? { |x| x.element? } # => true
 */
static VALUE
element_children(VALUE self)
{
  xmlNodePtr node;
  xmlNodePtr child;
  xmlNodeSetPtr set;
  VALUE document;
  VALUE node_set;

  Data_Get_Struct(self, xmlNode, node);

  child = xmlFirstElementChild(node);
  set = xmlXPathNodeSetCreate(child);

  document = DOC_RUBY_OBJECT(node->doc);

  if (!child) { return noko_xml_node_set_wrap(set, document); }

  child = xmlNextElementSibling(child);
  while (NULL != child) {
    xmlXPathNodeSetAddUnique(set, child);
    child = xmlNextElementSibling(child);
  }

  node_set = noko_xml_node_set_wrap(set, document);

  return node_set;
}

/*
 * call-seq:
 *  child
 *
 * Returns the child node
 */
static VALUE
child(VALUE self)
{
  xmlNodePtr node, child;
  Data_Get_Struct(self, xmlNode, node);

  child = node->children;
  if (!child) { return Qnil; }

  return noko_xml_node_wrap(Qnil, child);
}

/*
 * call-seq:
 *  first_element_child
 *
 * Returns the first child node of this node that is an element.
 *
 * Example:
 *
 *   @doc.root.first_element_child.element? # => true
 */
static VALUE
first_element_child(VALUE self)
{
  xmlNodePtr node, child;
  Data_Get_Struct(self, xmlNode, node);

  child = xmlFirstElementChild(node);
  if (!child) { return Qnil; }

  return noko_xml_node_wrap(Qnil, child);
}

/*
 * call-seq:
 *  last_element_child
 *
 * Returns the last child node of this node that is an element.
 *
 * Example:
 *
 *   @doc.root.last_element_child.element? # => true
 */
static VALUE
last_element_child(VALUE self)
{
  xmlNodePtr node, child;
  Data_Get_Struct(self, xmlNode, node);

  child = xmlLastElementChild(node);
  if (!child) { return Qnil; }

  return noko_xml_node_wrap(Qnil, child);
}

/*
 * call-seq:
 *  key?(attribute)
 *
 * Returns true if +attribute+ is set
 */
static VALUE
key_eh(VALUE self, VALUE attribute)
{
  xmlNodePtr node;
  Data_Get_Struct(self, xmlNode, node);
  if (xmlHasProp(node, (xmlChar *)StringValueCStr(attribute))) {
    return Qtrue;
  }
  return Qfalse;
}

/*
 * call-seq:
 *  namespaced_key?(attribute, namespace)
 *
 * Returns true if +attribute+ is set with +namespace+
 */
static VALUE
namespaced_key_eh(VALUE self, VALUE attribute, VALUE namespace)
{
  xmlNodePtr node;
  Data_Get_Struct(self, xmlNode, node);
  if (xmlHasNsProp(node, (xmlChar *)StringValueCStr(attribute),
                   NIL_P(namespace) ? NULL : (xmlChar *)StringValueCStr(namespace))) {
    return Qtrue;
  }
  return Qfalse;
}

/*
 * call-seq:
 *  []=(property, value)
 *
 * Set the +property+ to +value+
 */
static VALUE
set(VALUE self, VALUE property, VALUE value)
{
  xmlNodePtr node, cur;
  xmlAttrPtr prop;
  Data_Get_Struct(self, xmlNode, node);

  /* If a matching attribute node already exists, then xmlSetProp will destroy
   * the existing node's children. However, if Nokogiri has a node object
   * pointing to one of those children, we are left with a broken reference.
   *
   * We can avoid this by unlinking these nodes first.
   */
  if (node->type != XML_ELEMENT_NODE) {
    return (Qnil);
  }
  prop = xmlHasProp(node, (xmlChar *)StringValueCStr(property));
  if (prop && prop->children) {
    for (cur = prop->children; cur; cur = cur->next) {
      if (cur->_private) {
        noko_xml_document_pin_node(cur);
        xmlUnlinkNode(cur);
      }
    }
  }

  xmlSetProp(node, (xmlChar *)StringValueCStr(property),
             (xmlChar *)StringValueCStr(value));

  return value;
}

/*
 * call-seq:
 *   get(attribute)
 *
 * Get the value for +attribute+
 */
static VALUE
get(VALUE self, VALUE rattribute)
{
  xmlNodePtr node;
  xmlChar *value = 0;
  VALUE rvalue;
  xmlChar *colon;
  xmlChar *attribute, *attr_name, *prefix;
  xmlNsPtr ns;

  if (NIL_P(rattribute)) { return Qnil; }

  Data_Get_Struct(self, xmlNode, node);
  attribute = xmlCharStrdup(StringValueCStr(rattribute));

  colon = (xmlChar *)(uintptr_t)xmlStrchr(attribute, (const xmlChar)':');
  if (colon) {
    /* split the attribute string into separate prefix and name by
     * null-terminating the prefix at the colon */
    prefix = attribute;
    attr_name = colon + 1;
    (*colon) = 0;

    ns = xmlSearchNs(node->doc, node, prefix);
    if (ns) {
      value = xmlGetNsProp(node, attr_name, ns->href);
    } else {
      value = xmlGetProp(node, (xmlChar *)StringValueCStr(rattribute));
    }
  } else {
    value = xmlGetNoNsProp(node, attribute);
  }

  xmlFree((void *)attribute);
  if (!value) { return Qnil; }

  rvalue = NOKOGIRI_STR_NEW2(value);
  xmlFree((void *)value);

  return rvalue ;
}

/*
 * call-seq:
 *   set_namespace(namespace)
 *
 * Set the namespace to +namespace+
 */
static VALUE
set_namespace(VALUE self, VALUE namespace)
{
  xmlNodePtr node;
  xmlNsPtr ns = NULL;

  Data_Get_Struct(self, xmlNode, node);

  if (!NIL_P(namespace)) {
    Data_Get_Struct(namespace, xmlNs, ns);
  }

  xmlSetNs(node, ns);

  return self;
}

/*
 * call-seq:
 *   attribute(name)
 *
 * Get the attribute node with +name+
 */
static VALUE
attr(VALUE self, VALUE name)
{
  xmlNodePtr node;
  xmlAttrPtr prop;
  Data_Get_Struct(self, xmlNode, node);
  prop = xmlHasProp(node, (xmlChar *)StringValueCStr(name));

  if (! prop) { return Qnil; }
  return noko_xml_node_wrap(Qnil, (xmlNodePtr)prop);
}

/*
 * call-seq:
 *   attribute_with_ns(name, namespace)
 *
 * Get the attribute node with +name+ and +namespace+
 */
static VALUE
attribute_with_ns(VALUE self, VALUE name, VALUE namespace)
{
  xmlNodePtr node;
  xmlAttrPtr prop;
  Data_Get_Struct(self, xmlNode, node);
  prop = xmlHasNsProp(node, (xmlChar *)StringValueCStr(name),
                      NIL_P(namespace) ? NULL : (xmlChar *)StringValueCStr(namespace));

  if (! prop) { return Qnil; }
  return noko_xml_node_wrap(Qnil, (xmlNodePtr)prop);
}

/*
 * @overload attribute_nodes()
 *   Get the attributes for a Node
 *   @return [Array<Nokogiri::XML::Attr>] containing the Node's attributes.
 */
static VALUE
attribute_nodes(VALUE rb_node)
{
  xmlNodePtr c_node;

  Data_Get_Struct(rb_node, xmlNode, c_node);

  return noko_xml_node_attrs(c_node);
}


/*
 *  call-seq:
 *    namespace()
 *
 *  returns the namespace of the element or attribute node as a Namespace
 *  object, or nil if there is no namespace for the element or attribute.
 */
static VALUE
noko_xml_node_namespace(VALUE rb_node)
{
  xmlNodePtr c_node ;
  Data_Get_Struct(rb_node, xmlNode, c_node);

  if (c_node->ns) {
    return noko_xml_namespace_wrap(c_node->ns, c_node->doc);
  }

  return Qnil ;
}

/*
 *  call-seq:
 *    namespace_definitions()
 *
 *  returns namespaces defined on self element directly, as an array of Namespace objects. Includes both a default namespace (as in"xmlns="), and prefixed namespaces (as in "xmlns:prefix=").
 */
static VALUE
namespace_definitions(VALUE rb_node)
{
  /* this code in the mode of xmlHasProp() */
  xmlNodePtr c_node ;
  xmlNsPtr c_namespace;
  VALUE definitions = rb_ary_new();

  Data_Get_Struct(rb_node, xmlNode, c_node);

  c_namespace = c_node->nsDef;
  if (!c_namespace) {
    return definitions;
  }

  while (c_namespace != NULL) {
    rb_ary_push(definitions, noko_xml_namespace_wrap(c_namespace, c_node->doc));
    c_namespace = c_namespace->next;
  }

  return definitions;
}

/*
 *  call-seq:
 *    namespace_scopes()
 *
 * returns namespaces in scope for self -- those defined on self element
 * directly or any ancestor node -- as an array of Namespace objects.  Default
 * namespaces ("xmlns=" style) for self are included in this array; Default
 * namespaces for  ancestors, however, are not. See also #namespaces
 */
static VALUE
namespace_scopes(VALUE rb_node)
{
  xmlNodePtr c_node ;
  xmlNsPtr *namespaces;
  VALUE scopes = rb_ary_new();
  int j;

  Data_Get_Struct(rb_node, xmlNode, c_node);

  namespaces = xmlGetNsList(c_node->doc, c_node);
  if (!namespaces) {
    return scopes;
  }

  for (j = 0 ; namespaces[j] != NULL ; ++j) {
    rb_ary_push(scopes, noko_xml_namespace_wrap(namespaces[j], c_node->doc));
  }

  xmlFree(namespaces);
  return scopes;
}

/*
 * call-seq:
 *  node_type
 *
 * Get the type for this Node
 */
static VALUE
node_type(VALUE self)
{
  xmlNodePtr node;
  Data_Get_Struct(self, xmlNode, node);
  return INT2NUM((long)node->type);
}

/*
 * call-seq:
 *  content=
 *
 * Set the content for this Node
 */
static VALUE
set_native_content(VALUE self, VALUE content)
{
  xmlNodePtr node, child, next ;
  Data_Get_Struct(self, xmlNode, node);

  child = node->children;
  while (NULL != child) {
    next = child->next ;
    xmlUnlinkNode(child) ;
    noko_xml_document_pin_node(child);
    child = next ;
  }

  xmlNodeSetContent(node, (xmlChar *)StringValueCStr(content));
  return content;
}

/*
 * call-seq:
 *  content
 *
 * Returns the plaintext content for this Node. Note that entities will always
 * be expanded in the returned string.
 */
static VALUE
get_native_content(VALUE self)
{
  xmlNodePtr node;
  xmlChar *content;

  Data_Get_Struct(self, xmlNode, node);

  content = xmlNodeGetContent(node);
  if (content) {
    VALUE rval = NOKOGIRI_STR_NEW2(content);
    xmlFree(content);
    return rval;
  }
  return Qnil;
}

/*
 * call-seq:
 *  lang=
 *
 * Set the language of a node, i.e. the values of the xml:lang attribute.
 */
static VALUE
set_lang(VALUE self_rb, VALUE lang_rb)
{
  xmlNodePtr self ;
  xmlChar *lang ;

  Data_Get_Struct(self_rb, xmlNode, self);
  lang = (xmlChar *)StringValueCStr(lang_rb);

  xmlNodeSetLang(self, lang);

  return Qnil ;
}

/*
 * call-seq:
 *  lang
 *
 * Searches the language of a node, i.e. the values of the xml:lang attribute or
 * the one carried by the nearest ancestor.
 */
static VALUE
get_lang(VALUE self_rb)
{
  xmlNodePtr self ;
  xmlChar *lang ;
  VALUE lang_rb ;

  Data_Get_Struct(self_rb, xmlNode, self);

  lang = xmlNodeGetLang(self);
  if (lang) {
    lang_rb = NOKOGIRI_STR_NEW2(lang);
    xmlFree(lang);
    return lang_rb ;
  }

  return Qnil ;
}

/* :nodoc: */
static VALUE
add_child(VALUE self, VALUE new_child)
{
  return reparent_node_with(self, new_child, xmlAddChild);
}

/*
 * call-seq:
 *  parent
 *
 * Get the parent Node for this Node
 */
static VALUE
get_parent(VALUE self)
{
  xmlNodePtr node, parent;
  Data_Get_Struct(self, xmlNode, node);

  parent = node->parent;
  if (!parent) { return Qnil; }

  return noko_xml_node_wrap(Qnil, parent) ;
}

/*
 * call-seq:
 *  name=(new_name)
 *
 * Set the name for this Node
 */
static VALUE
set_name(VALUE self, VALUE new_name)
{
  xmlNodePtr node;
  Data_Get_Struct(self, xmlNode, node);
  xmlNodeSetName(node, (xmlChar *)StringValueCStr(new_name));
  return new_name;
}

/*
 * call-seq:
 *  name
 *
 * Returns the name for this Node
 */
static VALUE
get_name(VALUE self)
{
  xmlNodePtr node;
  Data_Get_Struct(self, xmlNode, node);
  if (node->name) {
    return NOKOGIRI_STR_NEW2(node->name);
  }
  return Qnil;
}

/*
 * call-seq:
 *  path
 *
 * Returns the path associated with this Node
 */
static VALUE
noko_xml_node_path(VALUE rb_node)
{
  xmlNodePtr c_node;
  xmlChar *c_path ;
  VALUE rval;

  Data_Get_Struct(rb_node, xmlNode, c_node);

  c_path = xmlGetNodePath(c_node);
  if (c_path == NULL) {
    // see https://github.com/sparklemotion/nokogiri/issues/2250
    // this behavior is clearly undesirable, but is what libxml <= 2.9.10 returned, and so we
    // do this for now to preserve the behavior across libxml2 versions.
    rval = NOKOGIRI_STR_NEW2("?");
  } else {
    rval = NOKOGIRI_STR_NEW2(c_path);
    xmlFree(c_path);
  }

  return rval ;
}

/* :nodoc: */
static VALUE
add_next_sibling(VALUE self, VALUE new_sibling)
{
  return reparent_node_with(self, new_sibling, xmlAddNextSibling) ;
}

/* :nodoc: */
static VALUE
add_previous_sibling(VALUE self, VALUE new_sibling)
{
  return reparent_node_with(self, new_sibling, xmlAddPrevSibling) ;
}

/*
 * call-seq:
 *  native_write_to(io, encoding, options)
 *
 * Write this Node to +io+ with +encoding+ and +options+
 */
static VALUE
native_write_to(
  VALUE self,
  VALUE io,
  VALUE encoding,
  VALUE indent_string,
  VALUE options
)
{
  xmlNodePtr node;
  const char *before_indent;
  xmlSaveCtxtPtr savectx;

  Data_Get_Struct(self, xmlNode, node);

  xmlIndentTreeOutput = 1;

  before_indent = xmlTreeIndentString;

  xmlTreeIndentString = StringValueCStr(indent_string);

  savectx = xmlSaveToIO(
              (xmlOutputWriteCallback)noko_io_write,
              (xmlOutputCloseCallback)noko_io_close,
              (void *)io,
              RTEST(encoding) ? StringValueCStr(encoding) : NULL,
              (int)NUM2INT(options)
            );

  xmlSaveTree(savectx, node);
  xmlSaveClose(savectx);

  xmlTreeIndentString = before_indent;
  return io;
}

/*
 * call-seq:
 *  line
 *
 * Returns the line for this Node
 */
static VALUE
line(VALUE self)
{
  xmlNodePtr node;
  Data_Get_Struct(self, xmlNode, node);

  return INT2NUM(xmlGetLineNo(node));
}

/*
 * call-seq:
 *  line=(num)
 *
 * Sets the line for this Node. num must be less than 65535.
 */
static VALUE
set_line(VALUE self, VALUE num)
{
  xmlNodePtr node;
  int value = NUM2INT(num);

  Data_Get_Struct(self, xmlNode, node);
  if (value < 65535) {
    node->line = value;
  }

  return num;
}

/*
 * call-seq:
 *  add_namespace_definition(prefix, href)
 *
 * Adds a namespace definition with +prefix+ using +href+ value. The result is
 * as if parsed XML for this node had included an attribute
 * 'xmlns:prefix=value'.  A default namespace for this node ("xmlns=") can be
 * added by passing 'nil' for prefix. Namespaces added this way will not
 * show up in #attributes, but they will be included as an xmlns attribute
 * when the node is serialized to XML.
 */
static VALUE
add_namespace_definition(VALUE rb_node, VALUE rb_prefix, VALUE rb_href)
{
  xmlNodePtr c_node, element;
  xmlNsPtr c_namespace;
  const xmlChar *c_prefix = (const xmlChar *)(NIL_P(rb_prefix) ? NULL : StringValueCStr(rb_prefix));

  Data_Get_Struct(rb_node, xmlNode, c_node);
  element = c_node ;

  c_namespace = xmlSearchNs(c_node->doc, c_node, c_prefix);

  if (!c_namespace) {
    if (c_node->type != XML_ELEMENT_NODE) {
      element = c_node->parent;
    }
    c_namespace = xmlNewNs(element, (const xmlChar *)StringValueCStr(rb_href), c_prefix);
  }

  if (!c_namespace) {
    return Qnil ;
  }

  if (NIL_P(rb_prefix) || c_node != element) {
    xmlSetNs(c_node, c_namespace);
  }

  return noko_xml_namespace_wrap(c_namespace, c_node->doc);
}

/*
 * @overload new(name, document)
 *   Create a new node with +name+ sharing GC lifecycle with +document+.
 *   @param name [String]
 *   @param document [Nokogiri::XML::Document]
 *   @yieldparam node [Nokogiri::XML::Node]
 *   @return [Nokogiri::XML::Node]
 *   @see Nokogiri::XML::Node#initialize
 */
static VALUE
rb_xml_node_new(int argc, VALUE *argv, VALUE klass)
{
  xmlDocPtr doc;
  xmlNodePtr node;
  VALUE name;
  VALUE document;
  VALUE rest;
  VALUE rb_node;

  rb_scan_args(argc, argv, "2*", &name, &document, &rest);

  Data_Get_Struct(document, xmlDoc, doc);

  node = xmlNewNode(NULL, (xmlChar *)StringValueCStr(name));
  node->doc = doc->doc;
  noko_xml_document_pin_node(node);

  rb_node = noko_xml_node_wrap(
              klass == cNokogiriXmlNode ? (VALUE)NULL : klass,
              node
            );
  rb_obj_call_init(rb_node, argc, argv);

  if (rb_block_given_p()) { rb_yield(rb_node); }

  return rb_node;
}

/*
 * call-seq:
 *  dump_html
 *
 * Returns the Node as html.
 */
static VALUE
dump_html(VALUE self)
{
  xmlBufferPtr buf ;
  xmlNodePtr node ;
  VALUE html;

  Data_Get_Struct(self, xmlNode, node);

  buf = xmlBufferCreate() ;
  htmlNodeDump(buf, node->doc, node);
  html = NOKOGIRI_STR_NEW2(buf->content);
  xmlBufferFree(buf);
  return html ;
}

/*
 * call-seq:
 *  compare(other)
 *
 * Compare this Node to +other+ with respect to their Document
 */
static VALUE
compare(VALUE self, VALUE _other)
{
  xmlNodePtr node, other;
  Data_Get_Struct(self, xmlNode, node);
  Data_Get_Struct(_other, xmlNode, other);

  return INT2NUM((long)xmlXPathCmpNodes(other, node));
}


/*
 * call-seq:
 *   process_xincludes(options)
 *
 * Loads and substitutes all xinclude elements below the node. The
 * parser context will be initialized with +options+.
 */
static VALUE
process_xincludes(VALUE self, VALUE options)
{
  int rcode ;
  xmlNodePtr node;
  VALUE error_list = rb_ary_new();

  Data_Get_Struct(self, xmlNode, node);

  xmlSetStructuredErrorFunc((void *)error_list, Nokogiri_error_array_pusher);
  rcode = xmlXIncludeProcessTreeFlags(node, (int)NUM2INT(options));
  xmlSetStructuredErrorFunc(NULL, NULL);

  if (rcode < 0) {
    xmlErrorPtr error;

    error = xmlGetLastError();
    if (error) {
      rb_exc_raise(Nokogiri_wrap_xml_syntax_error(error));
    } else {
      rb_raise(rb_eRuntimeError, "Could not perform xinclude substitution");
    }
  }

  return self;
}


/* TODO: DOCUMENT ME */
static VALUE
in_context(VALUE self, VALUE _str, VALUE _options)
{
  xmlNodePtr node, list = 0, tmp, child_iter, node_children, doc_children;
  xmlNodeSetPtr set;
  xmlParserErrors error;
  VALUE doc, err;
  int doc_is_empty;

  Data_Get_Struct(self, xmlNode, node);

  doc = DOC_RUBY_OBJECT(node->doc);
  err = rb_iv_get(doc, "@errors");
  doc_is_empty = (node->doc->children == NULL) ? 1 : 0;
  node_children = node->children;
  doc_children  = node->doc->children;

  xmlSetStructuredErrorFunc((void *)err, Nokogiri_error_array_pusher);

  /* Twiddle global variable because of a bug in libxml2.
   * http://git.gnome.org/browse/libxml2/commit/?id=e20fb5a72c83cbfc8e4a8aa3943c6be8febadab7
   */
#ifndef HTML_PARSE_NOIMPLIED
  htmlHandleOmittedElem(0);
#endif

  /* This function adds a fake node to the child of +node+.  If the parser
   * does not exit cleanly with XML_ERR_OK, the list is freed.  This can
   * leave the child pointers in a bad state if they were originally empty.
   *
   * http://git.gnome.org/browse/libxml2/tree/parser.c#n13177
   * */
  error = xmlParseInNodeContext(node, StringValuePtr(_str),
                                (int)RSTRING_LEN(_str),
                                (int)NUM2INT(_options), &list);

  /* xmlParseInNodeContext should not mutate the original document or node,
   * so reassigning these pointers should be OK.  The reason we're reassigning
   * is because if there were errors, it's possible for the child pointers
   * to be manipulated. */
  if (error != XML_ERR_OK) {
    node->doc->children = doc_children;
    node->children = node_children;
  }

  /* make sure parent/child pointers are coherent so an unlink will work
   * properly (#331)
   */
  child_iter = node->doc->children ;
  while (child_iter) {
    if (child_iter->parent != (xmlNodePtr)node->doc) {
      child_iter->parent = (xmlNodePtr)node->doc;
    }
    child_iter = child_iter->next;
  }

#ifndef HTML_PARSE_NOIMPLIED
  htmlHandleOmittedElem(1);
#endif

  xmlSetStructuredErrorFunc(NULL, NULL);

  /* Workaround for a libxml2 bug where a parsing error may leave a broken
   * node reference in node->doc->children.
   * This workaround is limited to when a parse error occurs, the document
   * went from having no children to having children, and the context node is
   * part of a document fragment.
   * https://bugzilla.gnome.org/show_bug.cgi?id=668155
   */
  if (error != XML_ERR_OK && doc_is_empty && node->doc->children != NULL) {
    child_iter = node;
    while (child_iter->parent) {
      child_iter = child_iter->parent;
    }

    if (child_iter->type == XML_DOCUMENT_FRAG_NODE) {
      node->doc->children = NULL;
    }
  }

  /* FIXME: This probably needs to handle more constants... */
  switch (error) {
  case XML_ERR_INTERNAL_ERROR:
  case XML_ERR_NO_MEMORY:
    rb_raise(rb_eRuntimeError, "error parsing fragment (%d)", error);
    break;
  default:
    break;
  }

  set = xmlXPathNodeSetCreate(NULL);

  while (list) {
    tmp = list->next;
    list->next = NULL;
    xmlXPathNodeSetAddUnique(set, list);
    noko_xml_document_pin_node(list);
    list = tmp;
  }

  return noko_xml_node_set_wrap(set, doc);
}


VALUE
noko_xml_node_wrap(VALUE rb_class, xmlNodePtr c_node)
{
  VALUE rb_document, rb_node_cache, rb_node;
  nokogiriTuplePtr node_has_a_document;
  xmlDocPtr c_doc;
  void (*mark_method)(xmlNodePtr) = NULL ;

  assert(c_node);

  if (c_node->type == XML_DOCUMENT_NODE || c_node->type == XML_HTML_DOCUMENT_NODE) {
    return DOC_RUBY_OBJECT(c_node->doc);
  }

  /* It's OK if the node doesn't have a fully-realized document (as in XML::Reader). */
  /* see https://github.com/sparklemotion/nokogiri/issues/95 */
  /* and https://github.com/sparklemotion/nokogiri/issues/439 */
  c_doc = c_node->doc;
  if (c_doc->type == XML_DOCUMENT_FRAG_NODE) { c_doc = c_doc->doc; }
  node_has_a_document = DOC_RUBY_OBJECT_TEST(c_doc);

  if (c_node->_private && node_has_a_document) {
    return (VALUE)c_node->_private;
  }

  if (!RTEST(rb_class)) {
    switch (c_node->type) {
    case XML_ELEMENT_NODE:
      rb_class = cNokogiriXmlElement;
      break;
    case XML_TEXT_NODE:
      rb_class = cNokogiriXmlText;
      break;
    case XML_ATTRIBUTE_NODE:
      rb_class = cNokogiriXmlAttr;
      break;
    case XML_ENTITY_REF_NODE:
      rb_class = cNokogiriXmlEntityReference;
      break;
    case XML_COMMENT_NODE:
      rb_class = cNokogiriXmlComment;
      break;
    case XML_DOCUMENT_FRAG_NODE:
      rb_class = cNokogiriXmlDocumentFragment;
      break;
    case XML_PI_NODE:
      rb_class = cNokogiriXmlProcessingInstruction;
      break;
    case XML_ENTITY_DECL:
      rb_class = cNokogiriXmlEntityDecl;
      break;
    case XML_CDATA_SECTION_NODE:
      rb_class = cNokogiriXmlCData;
      break;
    case XML_DTD_NODE:
      rb_class = cNokogiriXmlDtd;
      break;
    case XML_ATTRIBUTE_DECL:
      rb_class = cNokogiriXmlAttributeDecl;
      break;
    case XML_ELEMENT_DECL:
      rb_class = cNokogiriXmlElementDecl;
      break;
    default:
      rb_class = cNokogiriXmlNode;
    }
  }

  mark_method = node_has_a_document ? mark : NULL ;

  rb_node = Data_Wrap_Struct(rb_class, mark_method, debug_node_dealloc, c_node) ;
  c_node->_private = (void *)rb_node;

  if (node_has_a_document) {
    rb_document = DOC_RUBY_OBJECT(c_doc);
    rb_node_cache = DOC_NODE_CACHE(c_doc);
    rb_ary_push(rb_node_cache, rb_node);
    rb_funcall(rb_document, id_decorate, 1, rb_node);
  }

  return rb_node ;
}


/*
 *  return Array<Nokogiri::XML::Attr> containing the node's attributes
 */
VALUE
noko_xml_node_attrs(xmlNodePtr c_node)
{
  VALUE rb_properties = rb_ary_new();
  xmlAttrPtr c_property;

  c_property = c_node->properties ;
  while (c_property != NULL) {
    rb_ary_push(rb_properties, noko_xml_node_wrap(Qnil, (xmlNodePtr)c_property));
    c_property = c_property->next ;
  }

  return rb_properties;
}

void
noko_init_xml_node()
{
  cNokogiriXmlNode = rb_define_class_under(mNokogiriXml, "Node", rb_cObject);

  rb_define_singleton_method(cNokogiriXmlNode, "new", rb_xml_node_new, -1);

  rb_define_method(cNokogiriXmlNode, "add_namespace_definition", add_namespace_definition, 2);
  rb_define_method(cNokogiriXmlNode, "node_name", get_name, 0);
  rb_define_method(cNokogiriXmlNode, "document", document, 0);
  rb_define_method(cNokogiriXmlNode, "node_name=", set_name, 1);
  rb_define_method(cNokogiriXmlNode, "parent", get_parent, 0);
  rb_define_method(cNokogiriXmlNode, "child", child, 0);
  rb_define_method(cNokogiriXmlNode, "first_element_child", first_element_child, 0);
  rb_define_method(cNokogiriXmlNode, "last_element_child", last_element_child, 0);
  rb_define_method(cNokogiriXmlNode, "children", children, 0);
  rb_define_method(cNokogiriXmlNode, "element_children", element_children, 0);
  rb_define_method(cNokogiriXmlNode, "next_sibling", next_sibling, 0);
  rb_define_method(cNokogiriXmlNode, "previous_sibling", previous_sibling, 0);
  rb_define_method(cNokogiriXmlNode, "next_element", next_element, 0);
  rb_define_method(cNokogiriXmlNode, "previous_element", previous_element, 0);
  rb_define_method(cNokogiriXmlNode, "node_type", node_type, 0);
  rb_define_method(cNokogiriXmlNode, "path", noko_xml_node_path, 0);
  rb_define_method(cNokogiriXmlNode, "key?", key_eh, 1);
  rb_define_method(cNokogiriXmlNode, "namespaced_key?", namespaced_key_eh, 2);
  rb_define_method(cNokogiriXmlNode, "blank?", blank_eh, 0);
  rb_define_method(cNokogiriXmlNode, "attribute_nodes", attribute_nodes, 0);
  rb_define_method(cNokogiriXmlNode, "attribute", attr, 1);
  rb_define_method(cNokogiriXmlNode, "attribute_with_ns", attribute_with_ns, 2);
  rb_define_method(cNokogiriXmlNode, "namespace", noko_xml_node_namespace, 0);
  rb_define_method(cNokogiriXmlNode, "namespace_definitions", namespace_definitions, 0);
  rb_define_method(cNokogiriXmlNode, "namespace_scopes", namespace_scopes, 0);
  rb_define_method(cNokogiriXmlNode, "encode_special_chars", encode_special_chars, 1);
  rb_define_method(cNokogiriXmlNode, "dup", duplicate_node, -1);
  rb_define_method(cNokogiriXmlNode, "unlink", unlink_node, 0);
  rb_define_method(cNokogiriXmlNode, "internal_subset", internal_subset, 0);
  rb_define_method(cNokogiriXmlNode, "external_subset", external_subset, 0);
  rb_define_method(cNokogiriXmlNode, "create_internal_subset", create_internal_subset, 3);
  rb_define_method(cNokogiriXmlNode, "create_external_subset", create_external_subset, 3);
  rb_define_method(cNokogiriXmlNode, "pointer_id", pointer_id, 0);
  rb_define_method(cNokogiriXmlNode, "line", line, 0);
  rb_define_method(cNokogiriXmlNode, "line=", set_line, 1);
  rb_define_method(cNokogiriXmlNode, "content", get_native_content, 0);
  rb_define_method(cNokogiriXmlNode, "native_content=", set_native_content, 1);
  rb_define_method(cNokogiriXmlNode, "lang", get_lang, 0);
  rb_define_method(cNokogiriXmlNode, "lang=", set_lang, 1);

  rb_define_private_method(cNokogiriXmlNode, "process_xincludes", process_xincludes, 1);
  rb_define_private_method(cNokogiriXmlNode, "in_context", in_context, 2);
  rb_define_private_method(cNokogiriXmlNode, "add_child_node", add_child, 1);
  rb_define_private_method(cNokogiriXmlNode, "add_previous_sibling_node", add_previous_sibling, 1);
  rb_define_private_method(cNokogiriXmlNode, "add_next_sibling_node", add_next_sibling, 1);
  rb_define_private_method(cNokogiriXmlNode, "replace_node", replace, 1);
  rb_define_private_method(cNokogiriXmlNode, "dump_html", dump_html, 0);
  rb_define_private_method(cNokogiriXmlNode, "native_write_to", native_write_to, 4);
  rb_define_private_method(cNokogiriXmlNode, "get", get, 1);
  rb_define_private_method(cNokogiriXmlNode, "set", set, 2);
  rb_define_private_method(cNokogiriXmlNode, "set_namespace", set_namespace, 1);
  rb_define_private_method(cNokogiriXmlNode, "compare", compare, 1);

  id_decorate      = rb_intern("decorate");
  id_decorate_bang = rb_intern("decorate!");
}

/* vim: set noet sw=4 sws=4 */
