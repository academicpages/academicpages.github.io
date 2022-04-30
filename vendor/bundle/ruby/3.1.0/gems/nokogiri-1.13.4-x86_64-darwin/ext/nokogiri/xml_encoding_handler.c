#include <nokogiri.h>

VALUE cNokogiriEncodingHandler;


static void
_xml_encoding_handler_dealloc(xmlCharEncodingHandlerPtr c_handler)
{
  /* make sure iconv handlers are cleaned up and freed */
  xmlCharEncCloseFunc(c_handler);
}


/*
 * call-seq: Nokogiri::EncodingHandler.[](name)
 *
 * Get the encoding handler for +name+
 */
static VALUE
rb_xml_encoding_handler_s_get(VALUE klass, VALUE key)
{
  xmlCharEncodingHandlerPtr handler;

  handler = xmlFindCharEncodingHandler(StringValueCStr(key));
  if (handler) {
    return Data_Wrap_Struct(klass, NULL, _xml_encoding_handler_dealloc, handler);
  }

  return Qnil;
}


/*
 * call-seq: Nokogiri::EncodingHandler.delete(name)
 *
 * Delete the encoding alias named +name+
 */
static VALUE
rb_xml_encoding_handler_s_delete(VALUE klass, VALUE name)
{
  if (xmlDelEncodingAlias(StringValueCStr(name))) { return Qnil; }

  return Qtrue;
}


/*
 * call-seq: Nokogiri::EncodingHandler.alias(from, to)
 *
 * Alias encoding handler with name +from+ to name +to+
 */
static VALUE
rb_xml_encoding_handler_s_alias(VALUE klass, VALUE from, VALUE to)
{
  xmlAddEncodingAlias(StringValueCStr(from), StringValueCStr(to));

  return to;
}


/*
 * call-seq: Nokogiri::EncodingHandler.clear_aliases!
 *
 * Remove all encoding aliases.
 */
static VALUE
rb_xml_encoding_handler_s_clear_aliases(VALUE klass)
{
  xmlCleanupEncodingAliases();

  return klass;
}


/*
 * call-seq: name
 *
 * Get the name of this EncodingHandler
 */
static VALUE
rb_xml_encoding_handler_name(VALUE self)
{
  xmlCharEncodingHandlerPtr handler;

  Data_Get_Struct(self, xmlCharEncodingHandler, handler);

  return NOKOGIRI_STR_NEW2(handler->name);
}


void
noko_init_xml_encoding_handler()
{
  cNokogiriEncodingHandler = rb_define_class_under(mNokogiri, "EncodingHandler", rb_cObject);

  rb_undef_alloc_func(cNokogiriEncodingHandler);

  rb_define_singleton_method(cNokogiriEncodingHandler, "[]", rb_xml_encoding_handler_s_get, 1);
  rb_define_singleton_method(cNokogiriEncodingHandler, "delete", rb_xml_encoding_handler_s_delete, 1);
  rb_define_singleton_method(cNokogiriEncodingHandler, "alias", rb_xml_encoding_handler_s_alias, 2);
  rb_define_singleton_method(cNokogiriEncodingHandler, "clear_aliases!", rb_xml_encoding_handler_s_clear_aliases, 0);

  rb_define_method(cNokogiriEncodingHandler, "name", rb_xml_encoding_handler_name, 0);
}
