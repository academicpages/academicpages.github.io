#include <xml_relax_ng.h>

static void dealloc(xmlRelaxNGPtr schema)
{
  NOKOGIRI_DEBUG_START(schema);
  xmlRelaxNGFree(schema);
  NOKOGIRI_DEBUG_END(schema);
}

/*
 * call-seq:
 *  validate_document(document)
 *
 * Validate a Nokogiri::XML::Document against this RelaxNG schema.
 */
static VALUE validate_document(VALUE self, VALUE document)
{
  xmlDocPtr doc;
  xmlRelaxNGPtr schema;
  VALUE errors;
  xmlRelaxNGValidCtxtPtr valid_ctxt;

  Data_Get_Struct(self, xmlRelaxNG, schema);
  Data_Get_Struct(document, xmlDoc, doc);

  errors = rb_ary_new();

  valid_ctxt = xmlRelaxNGNewValidCtxt(schema);

  if(NULL == valid_ctxt) {
    /* we have a problem */
    rb_raise(rb_eRuntimeError, "Could not create a validation context");
  }

#ifdef HAVE_XMLRELAXNGSETVALIDSTRUCTUREDERRORS
  xmlRelaxNGSetValidStructuredErrors(
    valid_ctxt,
    Nokogiri_error_array_pusher,
    (void *)errors
  );
#endif

  xmlRelaxNGValidateDoc(valid_ctxt, doc);

  xmlRelaxNGFreeValidCtxt(valid_ctxt);

  return errors;
}

/*
 * call-seq:
 *  read_memory(string)
 *
 * Create a new RelaxNG from the contents of +string+
 */
static VALUE read_memory(int argc, VALUE *argv, VALUE klass)
{
  VALUE content;
  VALUE parse_options;
  xmlRelaxNGParserCtxtPtr ctx;
  xmlRelaxNGPtr schema;
  VALUE errors;
  VALUE rb_schema;
  int scanned_args = 0;

  scanned_args = rb_scan_args(argc, argv, "11", &content, &parse_options);
  if (scanned_args == 1) {
    parse_options = rb_const_get(rb_const_get(mNokogiriXml, rb_intern("ParseOptions")), rb_intern("DEFAULT_SCHEMA"));
  }

  ctx = xmlRelaxNGNewMemParserCtxt((const char *)StringValuePtr(content), (int)RSTRING_LEN(content));

  errors = rb_ary_new();
  xmlSetStructuredErrorFunc((void *)errors, Nokogiri_error_array_pusher);

#ifdef HAVE_XMLRELAXNGSETPARSERSTRUCTUREDERRORS
  xmlRelaxNGSetParserStructuredErrors(
    ctx,
    Nokogiri_error_array_pusher,
    (void *)errors
  );
#endif

  schema = xmlRelaxNGParse(ctx);

  xmlSetStructuredErrorFunc(NULL, NULL);
  xmlRelaxNGFreeParserCtxt(ctx);

  if(NULL == schema) {
    xmlErrorPtr error = xmlGetLastError();
    if(error)
      Nokogiri_error_raise(NULL, error);
    else
      rb_raise(rb_eRuntimeError, "Could not parse document");

    return Qnil;
  }

  rb_schema = Data_Wrap_Struct(klass, 0, dealloc, schema);
  rb_iv_set(rb_schema, "@errors", errors);
  rb_iv_set(rb_schema, "@parse_options", parse_options);

  return rb_schema;
}

/*
 * call-seq:
 *  from_document(doc)
 *
 * Create a new RelaxNG schema from the Nokogiri::XML::Document +doc+
 */
static VALUE from_document(int argc, VALUE *argv, VALUE klass)
{
  VALUE document;
  VALUE parse_options;
  xmlDocPtr doc;
  xmlRelaxNGParserCtxtPtr ctx;
  xmlRelaxNGPtr schema;
  VALUE errors;
  VALUE rb_schema;
  int scanned_args = 0;

  scanned_args = rb_scan_args(argc, argv, "11", &document, &parse_options);

  Data_Get_Struct(document, xmlDoc, doc);
  doc = doc->doc; /* In case someone passes us a node. ugh. */

  if (scanned_args == 1) {
    parse_options = rb_const_get(rb_const_get(mNokogiriXml, rb_intern("ParseOptions")), rb_intern("DEFAULT_SCHEMA"));
  }

  ctx = xmlRelaxNGNewDocParserCtxt(doc);

  errors = rb_ary_new();
  xmlSetStructuredErrorFunc((void *)errors, Nokogiri_error_array_pusher);

#ifdef HAVE_XMLRELAXNGSETPARSERSTRUCTUREDERRORS
  xmlRelaxNGSetParserStructuredErrors(
    ctx,
    Nokogiri_error_array_pusher,
    (void *)errors
  );
#endif

  schema = xmlRelaxNGParse(ctx);

  xmlSetStructuredErrorFunc(NULL, NULL);
  xmlRelaxNGFreeParserCtxt(ctx);

  if(NULL == schema) {
    xmlErrorPtr error = xmlGetLastError();
    if(error)
      Nokogiri_error_raise(NULL, error);
    else
      rb_raise(rb_eRuntimeError, "Could not parse document");

    return Qnil;
  }

  rb_schema = Data_Wrap_Struct(klass, 0, dealloc, schema);
  rb_iv_set(rb_schema, "@errors", errors);
  rb_iv_set(rb_schema, "@parse_options", parse_options);

  return rb_schema;
}

VALUE cNokogiriXmlRelaxNG;
void init_xml_relax_ng()
{
  VALUE nokogiri = rb_define_module("Nokogiri");
  VALUE xml = rb_define_module_under(nokogiri, "XML");
  VALUE klass = rb_define_class_under(xml, "RelaxNG", cNokogiriXmlSchema);

  cNokogiriXmlRelaxNG = klass;

  rb_define_singleton_method(klass, "read_memory", read_memory, -1);
  rb_define_singleton_method(klass, "from_document", from_document, -1);
  rb_define_private_method(klass, "validate_document", validate_document, 1);
}
