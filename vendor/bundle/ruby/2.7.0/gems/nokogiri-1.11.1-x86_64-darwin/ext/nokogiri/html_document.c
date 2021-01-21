#include <html_document.h>

static ID id_encoding_found;
static ID id_to_s;

/*
 * call-seq:
 *  new
 *
 * Create a new document
 */
static VALUE
rb_html_document_s_new(int argc, VALUE *argv, VALUE klass)
{
  VALUE uri, external_id, rest, rb_doc;
  htmlDocPtr doc;

  rb_scan_args(argc, argv, "0*", &rest);
  uri = rb_ary_entry(rest, (long)0);
  external_id = rb_ary_entry(rest, (long)1);

  doc = htmlNewDoc(
          RTEST(uri) ? (const xmlChar *)StringValueCStr(uri) : NULL,
          RTEST(external_id) ? (const xmlChar *)StringValueCStr(external_id) : NULL
        );
  rb_doc = Nokogiri_wrap_xml_document(klass, doc);
  rb_obj_call_init(rb_doc, argc, argv);
  return rb_doc ;
}

/*
 * call-seq:
 *  read_io(io, url, encoding, options)
 *
 * Read the HTML document from +io+ with given +url+, +encoding+,
 * and +options+.  See Nokogiri::HTML.parse
 */
static VALUE
rb_html_document_s_read_io(VALUE klass, VALUE rb_io, VALUE rb_url, VALUE rb_encoding, VALUE rb_options)
{
  VALUE rb_doc;
  VALUE rb_error_list = rb_ary_new();
  htmlDocPtr c_doc;
  const char *c_url = NIL_P(rb_url) ? NULL : StringValueCStr(rb_url);
  const char *c_encoding = NIL_P(rb_encoding) ? NULL : StringValueCStr(rb_encoding);
  int options = NUM2INT(rb_options);

  xmlSetStructuredErrorFunc((void *)rb_error_list, Nokogiri_error_array_pusher);

  c_doc = htmlReadIO(io_read_callback, io_close_callback, (void *)rb_io, c_url, c_encoding, options);

  xmlSetStructuredErrorFunc(NULL, NULL);

  /*
   * If EncodingFound has occurred in EncodingReader, make sure to do
   * a cleanup and propagate the error.
   */
  if (rb_respond_to(rb_io, id_encoding_found)) {
    VALUE encoding_found = rb_funcall(rb_io, id_encoding_found, 0);
    if (!NIL_P(encoding_found)) {
      xmlFreeDoc(c_doc);
      rb_exc_raise(encoding_found);
    }
  }

  if ((c_doc == NULL) || (!(options & XML_PARSE_RECOVER) && (RARRAY_LEN(rb_error_list) > 0))) {
    VALUE rb_error ;

    xmlFreeDoc(c_doc);

    rb_error = rb_ary_entry(rb_error_list, 0);
    if (rb_error == Qnil) {
      rb_raise(rb_eRuntimeError, "Could not parse document");
    } else {
      VALUE exception_message = rb_funcall(rb_error, id_to_s, 0);
      exception_message = rb_str_concat(rb_str_new2("Parser without recover option encountered error or warning: "),
                                        exception_message);
      rb_exc_raise(rb_class_new_instance(1, &exception_message, cNokogiriXmlSyntaxError));
    }

    return Qnil;
  }

  rb_doc = Nokogiri_wrap_xml_document(klass, c_doc);
  rb_iv_set(rb_doc, "@errors", rb_error_list);
  return rb_doc;
}

/*
 * call-seq:
 *  read_memory(string, url, encoding, options)
 *
 * Read the HTML document contained in +string+ with given +url+, +encoding+,
 * and +options+.  See Nokogiri::HTML.parse
 */
static VALUE
rb_html_document_s_read_memory(VALUE klass, VALUE rb_html, VALUE rb_url, VALUE rb_encoding, VALUE rb_options)
{
  VALUE rb_doc;
  VALUE rb_error_list = rb_ary_new();
  htmlDocPtr c_doc;
  const char *c_buffer = StringValuePtr(rb_html);
  const char *c_url = NIL_P(rb_url) ? NULL : StringValueCStr(rb_url);
  const char *c_encoding = NIL_P(rb_encoding) ? NULL : StringValueCStr(rb_encoding);
  int html_len = (int)RSTRING_LEN(rb_html);
  int options = NUM2INT(rb_options);

  xmlSetStructuredErrorFunc((void *)rb_error_list, Nokogiri_error_array_pusher);

  c_doc = htmlReadMemory(c_buffer, html_len, c_url, c_encoding, options);

  xmlSetStructuredErrorFunc(NULL, NULL);

  if ((c_doc == NULL) || (!(options & XML_PARSE_RECOVER) && (RARRAY_LEN(rb_error_list) > 0))) {
    VALUE rb_error ;

    xmlFreeDoc(c_doc);

    rb_error = rb_ary_entry(rb_error_list, 0);
    if (rb_error == Qnil) {
      rb_raise(rb_eRuntimeError, "Could not parse document");
    } else {
      VALUE exception_message = rb_funcall(rb_error, id_to_s, 0);
      exception_message = rb_str_concat(rb_str_new2("Parser without recover option encountered error or warning: "),
                                        exception_message);
      rb_exc_raise(rb_class_new_instance(1, &exception_message, cNokogiriXmlSyntaxError));
    }

    return Qnil;
  }

  rb_doc = Nokogiri_wrap_xml_document(klass, c_doc);
  rb_iv_set(rb_doc, "@errors", rb_error_list);
  return rb_doc;
}

/*
 * call-seq:
 *  type
 *
 * The type for this document
 */
static VALUE
rb_html_document_type(VALUE self)
{
  htmlDocPtr doc;
  Data_Get_Struct(self, xmlDoc, doc);
  return INT2NUM((long)doc->type);
}

VALUE cNokogiriHtmlDocument ;

void
init_html_document()
{
  VALUE nokogiri = rb_define_module("Nokogiri");
  VALUE nokogiri_xml = rb_define_module_under(nokogiri, "XML");
  VALUE nokogiri_xml_node = rb_define_class_under(nokogiri_xml, "Node", rb_cObject);
  VALUE nokogiri_xml_document = rb_define_class_under(nokogiri_xml, "Document", nokogiri_xml_node);
  VALUE nokogiri_html = rb_define_module_under(nokogiri, "HTML");
  cNokogiriHtmlDocument = rb_define_class_under(nokogiri_html, "Document", nokogiri_xml_document);

  rb_define_singleton_method(cNokogiriHtmlDocument, "read_memory", rb_html_document_s_read_memory, 4);
  rb_define_singleton_method(cNokogiriHtmlDocument, "read_io", rb_html_document_s_read_io, 4);
  rb_define_singleton_method(cNokogiriHtmlDocument, "new", rb_html_document_s_new, -1);

  rb_define_method(cNokogiriHtmlDocument, "type", rb_html_document_type, 0);

  id_encoding_found = rb_intern("encoding_found");
  id_to_s = rb_intern("to_s");
}
