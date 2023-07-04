#include <nokogiri.h>

VALUE cNokogiriXmlNodeSet ;

static ID decorate ;

static void
Check_Node_Set_Node_Type(VALUE node)
{
  if (!(rb_obj_is_kind_of(node, cNokogiriXmlNode) ||
        rb_obj_is_kind_of(node, cNokogiriXmlNamespace))) {
    rb_raise(rb_eArgError, "node must be a Nokogiri::XML::Node or Nokogiri::XML::Namespace");
  }
}


static
VALUE
ruby_object_get(xmlNodePtr c_node)
{
  /* see xmlElementType in libxml2 tree.h */
  switch (c_node->type) {
    case XML_NAMESPACE_DECL:
      /* _private is later in the namespace struct */
      return (VALUE)(((xmlNsPtr)c_node)->_private);

    case XML_DOCUMENT_NODE:
    case XML_HTML_DOCUMENT_NODE:
      /* in documents we use _private to store a tuple */
      if (DOC_RUBY_OBJECT_TEST(((xmlDocPtr)c_node))) {
        return DOC_RUBY_OBJECT((xmlDocPtr)c_node);
      }
      return (VALUE)NULL;

    default:
      return (VALUE)(c_node->_private);
  }
}


static void
mark(xmlNodeSetPtr node_set)
{
  VALUE rb_node;
  int jnode;

  for (jnode = 0; jnode < node_set->nodeNr; jnode++) {
    rb_node = ruby_object_get(node_set->nodeTab[jnode]);
    if (rb_node) {
      rb_gc_mark(rb_node);
    }
  }
}

static void
xpath_node_set_del(xmlNodeSetPtr cur, xmlNodePtr val)
{
  /*
   * For reasons outlined in xml_namespace.c, here we reproduce xmlXPathNodeSetDel() except for the
   * offending call to xmlXPathNodeSetFreeNs().
   */
  int i;

  if (cur == NULL) { return; }
  if (val == NULL) { return; }

  /*
   * find node in nodeTab
   */
  for (i = 0; i < cur->nodeNr; i++)
    if (cur->nodeTab[i] == val) { break; }

  if (i >= cur->nodeNr) {	/* not found */
    return;
  }
  cur->nodeNr--;
  for (; i < cur->nodeNr; i++) {
    cur->nodeTab[i] = cur->nodeTab[i + 1];
  }
  cur->nodeTab[cur->nodeNr] = NULL;
}


static void
deallocate(xmlNodeSetPtr node_set)
{
  /*
   * For reasons outlined in xml_namespace.c, here we reproduce xmlXPathFreeNodeSet() except for the
   * offending call to xmlXPathNodeSetFreeNs().
   */
  NOKOGIRI_DEBUG_START(node_set) ;
  if (node_set->nodeTab != NULL) {
    xmlFree(node_set->nodeTab);
  }

  xmlFree(node_set);
  NOKOGIRI_DEBUG_END(node_set) ;
}


static VALUE
allocate(VALUE klass)
{
  return noko_xml_node_set_wrap(xmlXPathNodeSetCreate(NULL), Qnil);
}


/*
 * call-seq:
 *  dup
 *
 * Duplicate this NodeSet. Note that the Nodes contained in the NodeSet are not
 * duplicated (similar to how Array and other Enumerable classes work).
 */
static VALUE
duplicate(VALUE self)
{
  xmlNodeSetPtr node_set;
  xmlNodeSetPtr dupl;

  Data_Get_Struct(self, xmlNodeSet, node_set);

  dupl = xmlXPathNodeSetMerge(NULL, node_set);

  return noko_xml_node_set_wrap(dupl, rb_iv_get(self, "@document"));
}

/*
 * call-seq:
 *  length
 *
 * Get the length of the node set
 */
static VALUE
length(VALUE self)
{
  xmlNodeSetPtr node_set;

  Data_Get_Struct(self, xmlNodeSet, node_set);

  return node_set ? INT2NUM(node_set->nodeNr) : INT2NUM(0);
}

/*
 * call-seq:
 *  push(node)
 *
 * Append +node+ to the NodeSet.
 */
static VALUE
push(VALUE self, VALUE rb_node)
{
  xmlNodeSetPtr node_set;
  xmlNodePtr node;

  Check_Node_Set_Node_Type(rb_node);

  Data_Get_Struct(self, xmlNodeSet, node_set);
  Noko_Node_Get_Struct(rb_node, xmlNode, node);

  xmlXPathNodeSetAdd(node_set, node);

  return self;
}

/*
 *  call-seq:
 *    delete(node)
 *
 *  Delete +node+ from the Nodeset, if it is a member. Returns the deleted node
 *  if found, otherwise returns nil.
 */
static VALUE
delete (VALUE self, VALUE rb_node)
{
  xmlNodeSetPtr node_set;
  xmlNodePtr node;

  Check_Node_Set_Node_Type(rb_node);

  Data_Get_Struct(self, xmlNodeSet, node_set);
  Noko_Node_Get_Struct(rb_node, xmlNode, node);

  if (xmlXPathNodeSetContains(node_set, node)) {
    xpath_node_set_del(node_set, node);
    return rb_node;
  }
  return Qnil ;
}


/*
 * call-seq:
 *  &(node_set)
 *
 * Set Intersection — Returns a new NodeSet containing nodes common to the two NodeSets.
 */
static VALUE
intersection(VALUE self, VALUE rb_other)
{
  xmlNodeSetPtr node_set, other ;
  xmlNodeSetPtr intersection;

  if (!rb_obj_is_kind_of(rb_other, cNokogiriXmlNodeSet)) {
    rb_raise(rb_eArgError, "node_set must be a Nokogiri::XML::NodeSet");
  }

  Data_Get_Struct(self, xmlNodeSet, node_set);
  Data_Get_Struct(rb_other, xmlNodeSet, other);

  intersection = xmlXPathIntersection(node_set, other);
  return noko_xml_node_set_wrap(intersection, rb_iv_get(self, "@document"));
}


/*
 * call-seq:
 *  include?(node)
 *
 *  Returns true if any member of node set equals +node+.
 */
static VALUE
include_eh(VALUE self, VALUE rb_node)
{
  xmlNodeSetPtr node_set;
  xmlNodePtr node;

  Check_Node_Set_Node_Type(rb_node);

  Data_Get_Struct(self, xmlNodeSet, node_set);
  Noko_Node_Get_Struct(rb_node, xmlNode, node);

  return (xmlXPathNodeSetContains(node_set, node) ? Qtrue : Qfalse);
}


/*
 * call-seq:
 *  |(node_set)
 *
 * Returns a new set built by merging the set and the elements of the given
 * set.
 */
static VALUE
rb_xml_node_set_union(VALUE rb_node_set, VALUE rb_other)
{
  xmlNodeSetPtr c_node_set, c_other;
  xmlNodeSetPtr c_new_node_set;

  if (!rb_obj_is_kind_of(rb_other, cNokogiriXmlNodeSet)) {
    rb_raise(rb_eArgError, "node_set must be a Nokogiri::XML::NodeSet");
  }

  Data_Get_Struct(rb_node_set, xmlNodeSet, c_node_set);
  Data_Get_Struct(rb_other, xmlNodeSet, c_other);

  c_new_node_set = xmlXPathNodeSetMerge(NULL, c_node_set);
  c_new_node_set = xmlXPathNodeSetMerge(c_new_node_set, c_other);

  return noko_xml_node_set_wrap(c_new_node_set, rb_iv_get(rb_node_set, "@document"));
}

/*
 * call-seq:
 *  -(node_set)
 *
 *  Difference - returns a new NodeSet that is a copy of this NodeSet, removing
 *  each item that also appears in +node_set+
 */
static VALUE
minus(VALUE self, VALUE rb_other)
{
  xmlNodeSetPtr node_set, other;
  xmlNodeSetPtr new;
  int j ;

  if (!rb_obj_is_kind_of(rb_other, cNokogiriXmlNodeSet)) {
    rb_raise(rb_eArgError, "node_set must be a Nokogiri::XML::NodeSet");
  }

  Data_Get_Struct(self, xmlNodeSet, node_set);
  Data_Get_Struct(rb_other, xmlNodeSet, other);

  new = xmlXPathNodeSetMerge(NULL, node_set);
  for (j = 0 ; j < other->nodeNr ; ++j) {
    xpath_node_set_del(new, other->nodeTab[j]);
  }

  return noko_xml_node_set_wrap(new, rb_iv_get(self, "@document"));
}


static VALUE
index_at(VALUE self, long offset)
{
  xmlNodeSetPtr node_set;

  Data_Get_Struct(self, xmlNodeSet, node_set);

  if (offset >= node_set->nodeNr || abs((int)offset) > node_set->nodeNr) {
    return Qnil;
  }

  if (offset < 0) { offset += node_set->nodeNr ; }

  return noko_xml_node_wrap_node_set_result(node_set->nodeTab[offset], self);
}

static VALUE
subseq(VALUE self, long beg, long len)
{
  long j;
  xmlNodeSetPtr node_set;
  xmlNodeSetPtr new_set ;

  Data_Get_Struct(self, xmlNodeSet, node_set);

  if (beg > node_set->nodeNr) { return Qnil ; }
  if (beg < 0 || len < 0) { return Qnil ; }

  if ((beg + len) > node_set->nodeNr) {
    len = node_set->nodeNr - beg ;
  }

  new_set = xmlXPathNodeSetCreate(NULL);
  for (j = beg ; j < beg + len ; ++j) {
    xmlXPathNodeSetAddUnique(new_set, node_set->nodeTab[j]);
  }
  return noko_xml_node_set_wrap(new_set, rb_iv_get(self, "@document"));
}

/*
 * call-seq:
 *  [index] -> Node or nil
 *  [start, length] -> NodeSet or nil
 *  [range] -> NodeSet or nil
 *  slice(index) -> Node or nil
 *  slice(start, length) -> NodeSet or nil
 *  slice(range) -> NodeSet or nil
 *
 * Element reference - returns the node at +index+, or returns a NodeSet
 * containing nodes starting at +start+ and continuing for +length+ elements, or
 * returns a NodeSet containing nodes specified by +range+. Negative +indices+
 * count backward from the end of the +node_set+ (-1 is the last node). Returns
 * nil if the +index+ (or +start+) are out of range.
 */
static VALUE
slice(int argc, VALUE *argv, VALUE self)
{
  VALUE arg ;
  long beg, len ;
  xmlNodeSetPtr node_set;

  Data_Get_Struct(self, xmlNodeSet, node_set);

  if (argc == 2) {
    beg = NUM2LONG(argv[0]);
    len = NUM2LONG(argv[1]);
    if (beg < 0) {
      beg += node_set->nodeNr ;
    }
    return subseq(self, beg, len);
  }

  if (argc != 1) {
    rb_scan_args(argc, argv, "11", NULL, NULL);
  }
  arg = argv[0];

  if (FIXNUM_P(arg)) {
    return index_at(self, FIX2LONG(arg));
  }

  /* if arg is Range */
  switch (rb_range_beg_len(arg, &beg, &len, (long)node_set->nodeNr, 0)) {
    case Qfalse:
      break;
    case Qnil:
      return Qnil;
    default:
      return subseq(self, beg, len);
  }

  return index_at(self, NUM2LONG(arg));
}


/*
 * call-seq:
 *  to_a
 *
 * Return this list as an Array
 */
static VALUE
to_array(VALUE self)
{
  xmlNodeSetPtr node_set ;
  VALUE list;
  int i;

  Data_Get_Struct(self, xmlNodeSet, node_set);

  list = rb_ary_new2(node_set->nodeNr);
  for (i = 0; i < node_set->nodeNr; i++) {
    VALUE elt = noko_xml_node_wrap_node_set_result(node_set->nodeTab[i], self);
    rb_ary_push(list, elt);
  }

  return list;
}

/*
 *  call-seq:
 *    unlink
 *
 * Unlink this NodeSet and all Node objects it contains from their current context.
 */
static VALUE
unlink_nodeset(VALUE self)
{
  xmlNodeSetPtr node_set;
  int j, nodeNr ;

  Data_Get_Struct(self, xmlNodeSet, node_set);

  nodeNr = node_set->nodeNr ;
  for (j = 0 ; j < nodeNr ; j++) {
    if (! NOKOGIRI_NAMESPACE_EH(node_set->nodeTab[j])) {
      VALUE node ;
      xmlNodePtr node_ptr;
      node = noko_xml_node_wrap(Qnil, node_set->nodeTab[j]);
      rb_funcall(node, rb_intern("unlink"), 0); /* modifies the C struct out from under the object */
      Noko_Node_Get_Struct(node, xmlNode, node_ptr);
      node_set->nodeTab[j] = node_ptr ;
    }
  }
  return self ;
}


VALUE
noko_xml_node_set_wrap(xmlNodeSetPtr c_node_set, VALUE document)
{
  int j;
  VALUE rb_node_set ;

  if (c_node_set == NULL) {
    c_node_set = xmlXPathNodeSetCreate(NULL);
  }

  rb_node_set = Data_Wrap_Struct(cNokogiriXmlNodeSet, mark, deallocate, c_node_set);

  if (!NIL_P(document)) {
    rb_iv_set(rb_node_set, "@document", document);
    rb_funcall(document, decorate, 1, rb_node_set);
  }

  /* make sure we create ruby objects for all the results, so they'll be marked during the GC mark phase */
  for (j = 0 ; j < c_node_set->nodeNr ; j++) {
    noko_xml_node_wrap_node_set_result(c_node_set->nodeTab[j], rb_node_set);
  }

  return rb_node_set ;
}

VALUE
noko_xml_node_wrap_node_set_result(xmlNodePtr node, VALUE node_set)
{
  if (NOKOGIRI_NAMESPACE_EH(node)) {
    return noko_xml_namespace_wrap_xpath_copy((xmlNsPtr)node);
  } else {
    return noko_xml_node_wrap(Qnil, node);
  }
}


void
noko_init_xml_node_set(void)
{
  cNokogiriXmlNodeSet = rb_define_class_under(mNokogiriXml, "NodeSet", rb_cObject);

  rb_define_alloc_func(cNokogiriXmlNodeSet, allocate);

  rb_define_method(cNokogiriXmlNodeSet, "length", length, 0);
  rb_define_method(cNokogiriXmlNodeSet, "[]", slice, -1);
  rb_define_method(cNokogiriXmlNodeSet, "slice", slice, -1);
  rb_define_method(cNokogiriXmlNodeSet, "push", push, 1);
  rb_define_method(cNokogiriXmlNodeSet, "|", rb_xml_node_set_union, 1);
  rb_define_method(cNokogiriXmlNodeSet, "-", minus, 1);
  rb_define_method(cNokogiriXmlNodeSet, "unlink", unlink_nodeset, 0);
  rb_define_method(cNokogiriXmlNodeSet, "to_a", to_array, 0);
  rb_define_method(cNokogiriXmlNodeSet, "dup", duplicate, 0);
  rb_define_method(cNokogiriXmlNodeSet, "delete", delete, 1);
  rb_define_method(cNokogiriXmlNodeSet, "&", intersection, 1);
  rb_define_method(cNokogiriXmlNodeSet, "include?", include_eh, 1);

  decorate = rb_intern("decorate");
}
