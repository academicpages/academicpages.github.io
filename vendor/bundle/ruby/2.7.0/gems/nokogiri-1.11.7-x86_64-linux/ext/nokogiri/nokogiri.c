#include <nokogiri.h>

VALUE mNokogiri ;
VALUE mNokogiriHtml ;
VALUE mNokogiriHtmlSax ;
VALUE mNokogiriXml ;
VALUE mNokogiriXmlSax ;
VALUE mNokogiriXmlXpath ;
VALUE mNokogiriXslt ;

VALUE cNokogiriSyntaxError;
VALUE cNokogiriXmlCharacterData;
VALUE cNokogiriXmlElement;
VALUE cNokogiriXmlXpathSyntaxError;

void noko_init_xml_attr();
void noko_init_xml_attribute_decl();
void noko_init_xml_cdata();
void noko_init_xml_comment();
void noko_init_xml_document();
void noko_init_xml_document_fragment();
void noko_init_xml_dtd();
void noko_init_xml_element_content();
void noko_init_xml_element_decl();
void noko_init_xml_encoding_handler();
void noko_init_xml_entity_decl();
void noko_init_xml_entity_reference();
void noko_init_xml_namespace();
void noko_init_xml_node();
void noko_init_xml_node_set();
void noko_init_xml_processing_instruction();
void noko_init_xml_reader();
void noko_init_xml_relax_ng();
void noko_init_xml_sax_parser();
void noko_init_xml_sax_parser_context();
void noko_init_xml_sax_push_parser();
void noko_init_xml_schema();
void noko_init_xml_syntax_error();
void noko_init_xml_text();
void noko_init_xml_xpath_context();
void noko_init_xslt_stylesheet();
void noko_init_html_document();
void noko_init_html_element_description();
void noko_init_html_entity_lookup();
void noko_init_html_sax_parser_context();
void noko_init_html_sax_push_parser();
void noko_init_test_global_handlers();

static ID id_read, id_write;


#ifndef HAVE_VASPRINTF
/*
 * Thank you Geoffroy Couprie for this implementation of vasprintf!
 */
int
vasprintf(char **strp, const char *fmt, va_list ap)
{
  /* Mingw32/64 have a broken vsnprintf implementation that fails when
   * using a zero-byte limit in order to retrieve the required size for malloc.
   * So we use a one byte buffer instead.
   */
  char tmp[1];
  int len = vsnprintf(tmp, 1, fmt, ap) + 1;
  char *res = (char *)malloc((unsigned int)len);
  if (res == NULL) {
    return -1;
  }
  *strp = res;
  return vsnprintf(res, (unsigned int)len, fmt, ap);
}
#endif


static VALUE
read_check(VALUE val)
{
  VALUE *args = (VALUE *)val;
  return rb_funcall(args[0], id_read, 1, args[1]);
}


static VALUE
read_failed(VALUE arg, VALUE exc)
{
  return Qundef;
}


int
noko_io_read(void *ctx, char *buffer, int len)
{
  VALUE string, args[2];
  size_t str_len, safe_len;

  args[0] = (VALUE)ctx;
  args[1] = INT2NUM(len);

  string = rb_rescue(read_check, (VALUE)args, read_failed, 0);

  if (NIL_P(string)) { return 0; }
  if (string == Qundef) { return -1; }
  if (TYPE(string) != T_STRING) { return -1; }

  str_len = (size_t)RSTRING_LEN(string);
  safe_len = str_len > (size_t)len ? (size_t)len : str_len;
  memcpy(buffer, StringValuePtr(string), safe_len);

  return (int)safe_len;
}


static VALUE
write_check(VALUE val)
{
  VALUE *args = (VALUE *)val;
  return rb_funcall(args[0], id_write, 1, args[1]);
}


static VALUE
write_failed(VALUE arg, VALUE exc)
{
  return Qundef;
}


int
noko_io_write(void *ctx, char *buffer, int len)
{
  VALUE args[2], size;

  args[0] = (VALUE)ctx;
  args[1] = rb_str_new(buffer, (long)len);

  size = rb_rescue(write_check, (VALUE)args, write_failed, 0);

  if (size == Qundef) { return -1; }

  return NUM2INT(size);
}


int
noko_io_close(void *ctx)
{
  return 0;
}


void
Init_nokogiri()
{
  mNokogiri         = rb_define_module("Nokogiri");
  mNokogiriXml      = rb_define_module_under(mNokogiri, "XML");
  mNokogiriHtml     = rb_define_module_under(mNokogiri, "HTML");
  mNokogiriXslt     = rb_define_module_under(mNokogiri, "XSLT");
  mNokogiriXmlXpath = rb_define_module_under(mNokogiriXml, "XPath");
  mNokogiriXmlSax   = rb_define_module_under(mNokogiriXml, "SAX");
  mNokogiriHtmlSax  = rb_define_module_under(mNokogiriHtml, "SAX");

  rb_const_set(mNokogiri, rb_intern("LIBXML_COMPILED_VERSION"), NOKOGIRI_STR_NEW2(LIBXML_DOTTED_VERSION));
  rb_const_set(mNokogiri, rb_intern("LIBXML_LOADED_VERSION"), NOKOGIRI_STR_NEW2(xmlParserVersion));

  rb_const_set(mNokogiri, rb_intern("LIBXSLT_COMPILED_VERSION"), NOKOGIRI_STR_NEW2(LIBXSLT_DOTTED_VERSION));
  rb_const_set(mNokogiri, rb_intern("LIBXSLT_LOADED_VERSION"), NOKOGIRI_STR_NEW2(xsltEngineVersion));

#ifdef NOKOGIRI_PACKAGED_LIBRARIES
  rb_const_set(mNokogiri, rb_intern("PACKAGED_LIBRARIES"), Qtrue);
#  ifdef NOKOGIRI_PRECOMPILED_LIBRARIES
  rb_const_set(mNokogiri, rb_intern("PRECOMPILED_LIBRARIES"), Qtrue);
#  else
  rb_const_set(mNokogiri, rb_intern("PRECOMPILED_LIBRARIES"), Qfalse);
#  endif
  rb_const_set(mNokogiri, rb_intern("LIBXML2_PATCHES"), rb_str_split(NOKOGIRI_STR_NEW2(NOKOGIRI_LIBXML2_PATCHES), " "));
  rb_const_set(mNokogiri, rb_intern("LIBXSLT_PATCHES"), rb_str_split(NOKOGIRI_STR_NEW2(NOKOGIRI_LIBXSLT_PATCHES), " "));
#else
  rb_const_set(mNokogiri, rb_intern("PACKAGED_LIBRARIES"), Qfalse);
  rb_const_set(mNokogiri, rb_intern("PRECOMPILED_LIBRARIES"), Qfalse);
  rb_const_set(mNokogiri, rb_intern("LIBXML2_PATCHES"), Qnil);
  rb_const_set(mNokogiri, rb_intern("LIBXSLT_PATCHES"), Qnil);
#endif

#ifdef LIBXML_ICONV_ENABLED
  rb_const_set(mNokogiri, rb_intern("LIBXML_ICONV_ENABLED"), Qtrue);
#else
  rb_const_set(mNokogiri, rb_intern("LIBXML_ICONV_ENABLED"), Qfalse);
#endif

#ifdef NOKOGIRI_OTHER_LIBRARY_VERSIONS
  rb_const_set(mNokogiri, rb_intern("OTHER_LIBRARY_VERSIONS"), NOKOGIRI_STR_NEW2(NOKOGIRI_OTHER_LIBRARY_VERSIONS));
#endif

#if defined(_WIN32) && !defined(NOKOGIRI_PACKAGED_LIBRARIES)
  /*
   *  We choose *not* to do use Ruby's memory management functions with windows DLLs because of this
   *  issue in libxml 2.9.12:
   *
   *    https://github.com/sparklemotion/nokogiri/issues/2241
   *
   *  If the atexit() issue gets fixed in a future version of libxml2, then we may be able to skip
   *  this config only for the specific libxml2 versions 2.9.12.
   *
   *  Alternatively, now that Ruby has a generational GC, it might be OK to let libxml2 use its
   *  default memory management functions (recall that this config was introduced to reduce memory
   *  bloat and allow Ruby to GC more often); but we should *really* test with production workloads
   *  before making that kind of a potentially-invasive change.
   */
  rb_const_set(mNokogiri, rb_intern("LIBXML_MEMORY_MANAGEMENT"), NOKOGIRI_STR_NEW2("default"));
#else
  rb_const_set(mNokogiri, rb_intern("LIBXML_MEMORY_MANAGEMENT"), NOKOGIRI_STR_NEW2("ruby"));
  xmlMemSetup((xmlFreeFunc)ruby_xfree, (xmlMallocFunc)ruby_xmalloc, (xmlReallocFunc)ruby_xrealloc, ruby_strdup);
#endif

  xmlInitParser();

  cNokogiriSyntaxError = rb_define_class_under(mNokogiri, "SyntaxError", rb_eStandardError);
  noko_init_xml_syntax_error();
  assert(cNokogiriXmlSyntaxError);
  cNokogiriXmlXpathSyntaxError = rb_define_class_under(mNokogiriXmlXpath, "SyntaxError", cNokogiriXmlSyntaxError);

  noko_init_xml_element_content();
  noko_init_xml_encoding_handler();
  noko_init_xml_namespace();
  noko_init_xml_node_set();
  noko_init_xml_reader();
  noko_init_xml_sax_parser();
  noko_init_xml_xpath_context();
  noko_init_xslt_stylesheet();
  noko_init_html_element_description();
  noko_init_html_entity_lookup();

  noko_init_xml_schema();
  noko_init_xml_relax_ng();

  noko_init_xml_sax_parser_context();
  noko_init_html_sax_parser_context();

  noko_init_xml_sax_push_parser();
  noko_init_html_sax_push_parser();

  noko_init_xml_node();
  noko_init_xml_attr();
  noko_init_xml_attribute_decl();
  noko_init_xml_dtd();
  noko_init_xml_element_decl();
  noko_init_xml_entity_decl();
  noko_init_xml_entity_reference();
  noko_init_xml_processing_instruction();
  assert(cNokogiriXmlNode);
  cNokogiriXmlElement = rb_define_class_under(mNokogiriXml, "Element", cNokogiriXmlNode);
  cNokogiriXmlCharacterData = rb_define_class_under(mNokogiriXml, "CharacterData", cNokogiriXmlNode);
  noko_init_xml_comment();
  noko_init_xml_text();
  noko_init_xml_cdata();

  noko_init_xml_document_fragment();
  noko_init_xml_document();
  noko_init_html_document();

  noko_init_test_global_handlers();

  id_read = rb_intern("read");
  id_write = rb_intern("write");
}
