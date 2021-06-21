#include <nokogiri.h>

/*
 *  The lifecycle of a Namespace node is more complicated than other Nodes, for two reasons:
 *
 *  1. the underlying C structure has a different layout than all the other node structs, with the
 *     `_private` member where we store a pointer to Ruby object data not being in first position.
 *  2. xmlNs structures returned in an xmlNodeset from an XPath query are copies of the document's
 *     namespaces, and so do not share the same memory lifecycle as everything else in a document.
 *
 *  As a result of 1, you may see special handling of XML_NAMESPACE_DECL node types throughout the
 *  Nokogiri C code, though I intend to wrap up that logic in ruby_object_{get,set} functions
 *  shortly.
 *
 *  As a result of 2, you will see we have special handling in this file and in xml_node_set.c to
 *  carefully manage the memory lifecycle of xmlNs structs to match the Ruby object's GC
 *  lifecycle. In xml_node_set.c we have local versions of xmlXPathNodeSetDel() and
 *  xmlXPathFreeNodeSet() that avoid freeing xmlNs structs in the node set. In this file, we decide
 *  whether or not to call dealloc_namespace() depending on whether the xmlNs struct appears to be
 *  in an xmlNodeSet (and thus the result of an XPath query) or not.
 *
 *  Yes, this is madness.
 */

VALUE cNokogiriXmlNamespace ;

static void
dealloc_namespace(xmlNsPtr ns)
{
  /*
   * this deallocator is only used for namespace nodes that are part of an xpath
   * node set. see noko_xml_namespace_wrap().
   */
  NOKOGIRI_DEBUG_START(ns) ;
  if (ns->href) {
    xmlFree((xmlChar *)(uintptr_t)ns->href);
  }
  if (ns->prefix) {
    xmlFree((xmlChar *)(uintptr_t)ns->prefix);
  }
  xmlFree(ns);
  NOKOGIRI_DEBUG_END(ns) ;
}


/*
 * call-seq:
 *  prefix
 *
 * Get the prefix for this namespace.  Returns +nil+ if there is no prefix.
 */
static VALUE
prefix(VALUE self)
{
  xmlNsPtr ns;

  Data_Get_Struct(self, xmlNs, ns);
  if (!ns->prefix) { return Qnil; }

  return NOKOGIRI_STR_NEW2(ns->prefix);
}

/*
 * call-seq:
 *  href
 *
 * Get the href for this namespace
 */
static VALUE
href(VALUE self)
{
  xmlNsPtr ns;

  Data_Get_Struct(self, xmlNs, ns);
  if (!ns->href) { return Qnil; }

  return NOKOGIRI_STR_NEW2(ns->href);
}

VALUE
noko_xml_namespace_wrap(xmlNsPtr c_namespace, xmlDocPtr c_document)
{
  VALUE rb_namespace;

  if (c_namespace->_private) {
    return (VALUE)c_namespace->_private;
  }

  if (c_document) {
    rb_namespace = Data_Wrap_Struct(cNokogiriXmlNamespace, 0, 0, c_namespace);

    if (DOC_RUBY_OBJECT_TEST(c_document)) {
      rb_iv_set(rb_namespace, "@document", DOC_RUBY_OBJECT(c_document));
      rb_ary_push(DOC_NODE_CACHE(c_document), rb_namespace);
    }
  } else {
    rb_namespace = Data_Wrap_Struct(cNokogiriXmlNamespace, 0, dealloc_namespace, c_namespace);
  }

  c_namespace->_private = (void *)rb_namespace;

  return rb_namespace;
}

VALUE
noko_xml_namespace_wrap_xpath_copy(xmlNsPtr c_namespace)
{
  return noko_xml_namespace_wrap(c_namespace, NULL);
}

void
noko_init_xml_namespace()
{
  cNokogiriXmlNamespace = rb_define_class_under(mNokogiriXml, "Namespace", rb_cObject);

  rb_define_method(cNokogiriXmlNamespace, "prefix", prefix, 0);
  rb_define_method(cNokogiriXmlNamespace, "href", href, 0);
}
