#include <nokogiri.h>

static VALUE cNokogiriHtmlEntityLookup;

/*
 * call-seq:
 *  get(key)
 *
 * Get the HTML::EntityDescription for +key+
 */
static VALUE
get(VALUE _, VALUE rb_entity_name)
{
  VALUE cNokogiriHtmlEntityDescription;
  const htmlEntityDesc *c_entity_desc;
  VALUE rb_constructor_args[3];

  c_entity_desc = htmlEntityLookup((const xmlChar *)StringValueCStr(rb_entity_name));
  if (NULL == c_entity_desc) {
    return Qnil;
  }

  rb_constructor_args[0] = INT2NUM((long)c_entity_desc->value);
  rb_constructor_args[1] = NOKOGIRI_STR_NEW2(c_entity_desc->name);
  rb_constructor_args[2] = NOKOGIRI_STR_NEW2(c_entity_desc->desc);

  cNokogiriHtmlEntityDescription = rb_const_get_at(mNokogiriHtml, rb_intern("EntityDescription"));
  return rb_class_new_instance(3, rb_constructor_args, cNokogiriHtmlEntityDescription);
}

void
noko_init_html_entity_lookup()
{
  cNokogiriHtmlEntityLookup = rb_define_class_under(mNokogiriHtml, "EntityLookup", rb_cObject);

  rb_define_method(cNokogiriHtmlEntityLookup, "get", get, 1);
}
