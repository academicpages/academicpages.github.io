#include <nokogiri.h>

VALUE cNokogiriXmlCData;

/*
 * call-seq:
 *  new(document, content)
 *
 * Create a new CDATA element on the +document+ with +content+
 *
 * If +content+ cannot be implicitly converted to a string, this method will
 * raise a TypeError exception.
 */
static VALUE
new (int argc, VALUE *argv, VALUE klass)
{
  xmlDocPtr xml_doc;
  xmlNodePtr node;
  VALUE doc;
  VALUE content;
  VALUE rest;
  VALUE rb_node;
  xmlChar *content_str = NULL;
  int content_str_len = 0;

  rb_scan_args(argc, argv, "2*", &doc, &content, &rest);

  Noko_Node_Get_Struct(doc, xmlDoc, xml_doc);

  if (!NIL_P(content)) {
    content_str = (xmlChar *)StringValuePtr(content);
    content_str_len = RSTRING_LEN(content);
  }

  node = xmlNewCDataBlock(xml_doc->doc, content_str, content_str_len);

  noko_xml_document_pin_node(node);

  rb_node = noko_xml_node_wrap(klass, node);
  rb_obj_call_init(rb_node, argc, argv);

  if (rb_block_given_p()) { rb_yield(rb_node); }

  return rb_node;
}

void
noko_init_xml_cdata()
{
  assert(cNokogiriXmlText);
  /*
   * CData represents a CData node in an xml document.
   */
  cNokogiriXmlCData = rb_define_class_under(mNokogiriXml, "CDATA", cNokogiriXmlText);

  rb_define_singleton_method(cNokogiriXmlCData, "new", new, -1);
}
