#include <nokogiri.h>

VALUE cNokogiriXmlText ;

/*
 * call-seq:
 *  new(content, document)
 *
 * Create a new Text element on the +document+ with +content+
 */
static VALUE
new (int argc, VALUE *argv, VALUE klass)
{
  xmlDocPtr doc;
  xmlNodePtr node;
  VALUE string;
  VALUE document;
  VALUE rest;
  VALUE rb_node;

  rb_scan_args(argc, argv, "2*", &string, &document, &rest);

  Data_Get_Struct(document, xmlDoc, doc);

  node = xmlNewText((xmlChar *)StringValueCStr(string));
  node->doc = doc->doc;

  noko_xml_document_pin_node(node);

  rb_node = noko_xml_node_wrap(klass, node) ;
  rb_obj_call_init(rb_node, argc, argv);

  if (rb_block_given_p()) { rb_yield(rb_node); }

  return rb_node;
}

void
noko_init_xml_text()
{
  assert(cNokogiriXmlCharacterData);
  /*
   * Wraps Text nodes.
   */
  cNokogiriXmlText = rb_define_class_under(mNokogiriXml, "Text", cNokogiriXmlCharacterData);

  rb_define_singleton_method(cNokogiriXmlText, "new", new, -1);
}
