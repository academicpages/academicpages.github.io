#include <nokogiri.h>

VALUE cNokogiriXmlElementContent;

/*
 * call-seq:
 *  name
 *
 * Get the require element +name+
 */
static VALUE
get_name(VALUE self)
{
  xmlElementContentPtr elem;
  Data_Get_Struct(self, xmlElementContent, elem);

  if (!elem->name) { return Qnil; }
  return NOKOGIRI_STR_NEW2(elem->name);
}

/*
 * call-seq:
 *  type
 *
 * Get the element content +type+.  Possible values are PCDATA, ELEMENT, SEQ,
 * or OR.
 */
static VALUE
get_type(VALUE self)
{
  xmlElementContentPtr elem;
  Data_Get_Struct(self, xmlElementContent, elem);

  return INT2NUM((long)elem->type);
}

/*
 * call-seq:
 *  c1
 *
 * Get the first child.
 */
static VALUE
get_c1(VALUE self)
{
  xmlElementContentPtr elem;
  Data_Get_Struct(self, xmlElementContent, elem);

  if (!elem->c1) { return Qnil; }
  return noko_xml_element_content_wrap(rb_iv_get(self, "@document"), elem->c1);
}

/*
 * call-seq:
 *  c2
 *
 * Get the first child.
 */
static VALUE
get_c2(VALUE self)
{
  xmlElementContentPtr elem;
  Data_Get_Struct(self, xmlElementContent, elem);

  if (!elem->c2) { return Qnil; }
  return noko_xml_element_content_wrap(rb_iv_get(self, "@document"), elem->c2);
}

/*
 * call-seq:
 *  occur
 *
 * Get the element content +occur+ flag.  Possible values are ONCE, OPT, MULT
 * or PLUS.
 */
static VALUE
get_occur(VALUE self)
{
  xmlElementContentPtr elem;
  Data_Get_Struct(self, xmlElementContent, elem);

  return INT2NUM((long)elem->ocur);
}

/*
 * call-seq:
 *  prefix
 *
 * Get the element content namespace +prefix+.
 */
static VALUE
get_prefix(VALUE self)
{
  xmlElementContentPtr elem;
  Data_Get_Struct(self, xmlElementContent, elem);

  if (!elem->prefix) { return Qnil; }

  return NOKOGIRI_STR_NEW2(elem->prefix);
}

VALUE
noko_xml_element_content_wrap(VALUE doc, xmlElementContentPtr element)
{
  VALUE elem = Data_Wrap_Struct(cNokogiriXmlElementContent, 0, 0, element);

  /* Setting the document is necessary so that this does not get GC'd until */
  /* the document is GC'd */
  rb_iv_set(elem, "@document", doc);

  return elem;
}

void
noko_init_xml_element_content()
{
  cNokogiriXmlElementContent = rb_define_class_under(mNokogiriXml, "ElementContent", rb_cObject);

  rb_undef_alloc_func(cNokogiriXmlElementContent);

  rb_define_method(cNokogiriXmlElementContent, "name", get_name, 0);
  rb_define_method(cNokogiriXmlElementContent, "type", get_type, 0);
  rb_define_method(cNokogiriXmlElementContent, "occur", get_occur, 0);
  rb_define_method(cNokogiriXmlElementContent, "prefix", get_prefix, 0);

  rb_define_private_method(cNokogiriXmlElementContent, "c1", get_c1, 0);
  rb_define_private_method(cNokogiriXmlElementContent, "c2", get_c2, 0);
}
