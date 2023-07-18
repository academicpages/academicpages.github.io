#include <nokogiri.h>

VALUE cNokogiriXmlElementDecl;

static ID id_document;

/*
 * call-seq:
 *  element_type
 *
 * The element_type
 */
static VALUE
element_type(VALUE self)
{
  xmlElementPtr node;
  Noko_Node_Get_Struct(self, xmlElement, node);
  return INT2NUM((long)node->etype);
}

/*
 * call-seq:
 *  content
 *
 * The allowed content for this ElementDecl
 */
static VALUE
content(VALUE self)
{
  xmlElementPtr node;
  Noko_Node_Get_Struct(self, xmlElement, node);

  if (!node->content) { return Qnil; }

  return noko_xml_element_content_wrap(
           rb_funcall(self, id_document, 0),
           node->content
         );
}

/*
 * call-seq:
 *  prefix
 *
 * The namespace prefix for this ElementDecl
 */
static VALUE
prefix(VALUE self)
{
  xmlElementPtr node;
  Noko_Node_Get_Struct(self, xmlElement, node);

  if (!node->prefix) { return Qnil; }

  return NOKOGIRI_STR_NEW2(node->prefix);
}

void
noko_init_xml_element_decl()
{
  assert(cNokogiriXmlNode);
  cNokogiriXmlElementDecl = rb_define_class_under(mNokogiriXml, "ElementDecl", cNokogiriXmlNode);

  rb_define_method(cNokogiriXmlElementDecl, "element_type", element_type, 0);
  rb_define_method(cNokogiriXmlElementDecl, "content", content, 0);
  rb_define_method(cNokogiriXmlElementDecl, "prefix", prefix, 0);

  id_document = rb_intern("document");
}
