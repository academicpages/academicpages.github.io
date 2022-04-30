#include <nokogiri.h>

VALUE cNokogiriXmlSchema;

static void
dealloc(xmlSchemaPtr schema)
{
  NOKOGIRI_DEBUG_START(schema);
  xmlSchemaFree(schema);
  NOKOGIRI_DEBUG_END(schema);
}

/*
 * call-seq:
 *  validate_document(document)
 *
 * Validate a Nokogiri::XML::Document against this Schema.
 */
static VALUE
validate_document(VALUE self, VALUE document)
{
  xmlDocPtr doc;
  xmlSchemaPtr schema;
  xmlSchemaValidCtxtPtr valid_ctxt;
  VALUE errors;

  Data_Get_Struct(self, xmlSchema, schema);
  Data_Get_Struct(document, xmlDoc, doc);

  errors = rb_ary_new();

  valid_ctxt = xmlSchemaNewValidCtxt(schema);

  if (NULL == valid_ctxt) {
    /* we have a problem */
    rb_raise(rb_eRuntimeError, "Could not create a validation context");
  }

#ifdef HAVE_XMLSCHEMASETVALIDSTRUCTUREDERRORS
  xmlSchemaSetValidStructuredErrors(
    valid_ctxt,
    Nokogiri_error_array_pusher,
    (void *)errors
  );
#endif

  xmlSchemaValidateDoc(valid_ctxt, doc);

  xmlSchemaFreeValidCtxt(valid_ctxt);

  return errors;
}

/*
 * call-seq:
 *  validate_file(filename)
 *
 * Validate a file against this Schema.
 */
static VALUE
validate_file(VALUE self, VALUE rb_filename)
{
  xmlSchemaPtr schema;
  xmlSchemaValidCtxtPtr valid_ctxt;
  const char *filename ;
  VALUE errors;

  Data_Get_Struct(self, xmlSchema, schema);
  filename = (const char *)StringValueCStr(rb_filename) ;

  errors = rb_ary_new();

  valid_ctxt = xmlSchemaNewValidCtxt(schema);

  if (NULL == valid_ctxt) {
    /* we have a problem */
    rb_raise(rb_eRuntimeError, "Could not create a validation context");
  }

#ifdef HAVE_XMLSCHEMASETVALIDSTRUCTUREDERRORS
  xmlSchemaSetValidStructuredErrors(
    valid_ctxt,
    Nokogiri_error_array_pusher,
    (void *)errors
  );
#endif

  xmlSchemaValidateFile(valid_ctxt, filename, 0);

  xmlSchemaFreeValidCtxt(valid_ctxt);

  return errors;
}

/*
 * call-seq:
 *  read_memory(string)
 *
 * Create a new Schema from the contents of +string+
 */
static VALUE
read_memory(int argc, VALUE *argv, VALUE klass)
{
  VALUE content;
  VALUE parse_options;
  int parse_options_int;
  xmlSchemaParserCtxtPtr ctx;
  xmlSchemaPtr schema;
  VALUE errors;
  VALUE rb_schema;
  int scanned_args = 0;
  xmlExternalEntityLoader old_loader = 0;

  scanned_args = rb_scan_args(argc, argv, "11", &content, &parse_options);
  if (scanned_args == 1) {
    parse_options = rb_const_get_at(rb_const_get_at(mNokogiriXml, rb_intern("ParseOptions")), rb_intern("DEFAULT_SCHEMA"));
  }
  parse_options_int = (int)NUM2INT(rb_funcall(parse_options, rb_intern("to_i"), 0));

  ctx = xmlSchemaNewMemParserCtxt((const char *)StringValuePtr(content), (int)RSTRING_LEN(content));

  errors = rb_ary_new();
  xmlSetStructuredErrorFunc((void *)errors, Nokogiri_error_array_pusher);

#ifdef HAVE_XMLSCHEMASETPARSERSTRUCTUREDERRORS
  xmlSchemaSetParserStructuredErrors(
    ctx,
    Nokogiri_error_array_pusher,
    (void *)errors
  );
#endif

  if (parse_options_int & XML_PARSE_NONET) {
    old_loader = xmlGetExternalEntityLoader();
    xmlSetExternalEntityLoader(xmlNoNetExternalEntityLoader);
  }

  schema = xmlSchemaParse(ctx);

  if (old_loader) {
    xmlSetExternalEntityLoader(old_loader);
  }

  xmlSetStructuredErrorFunc(NULL, NULL);
  xmlSchemaFreeParserCtxt(ctx);

  if (NULL == schema) {
    xmlErrorPtr error = xmlGetLastError();
    if (error) {
      Nokogiri_error_raise(NULL, error);
    } else {
      rb_raise(rb_eRuntimeError, "Could not parse document");
    }

    return Qnil;
  }

  rb_schema = Data_Wrap_Struct(klass, 0, dealloc, schema);
  rb_iv_set(rb_schema, "@errors", errors);
  rb_iv_set(rb_schema, "@parse_options", parse_options);

  return rb_schema;
}

/* Schema creation will remove and deallocate "blank" nodes.
 * If those blank nodes have been exposed to Ruby, they could get freed
 * out from under the VALUE pointer.  This function checks to see if any of
 * those nodes have been exposed to Ruby, and if so we should raise an exception.
 */
static int
has_blank_nodes_p(VALUE cache)
{
  long i;

  if (NIL_P(cache)) {
    return 0;
  }

  for (i = 0; i < RARRAY_LEN(cache); i++) {
    xmlNodePtr node;
    VALUE element = rb_ary_entry(cache, i);
    Data_Get_Struct(element, xmlNode, node);
    if (xmlIsBlankNode(node)) {
      return 1;
    }
  }

  return 0;
}

/*
 * call-seq:
 *  from_document(doc)
 *
 * Create a new Schema from the Nokogiri::XML::Document +doc+
 */
static VALUE
from_document(int argc, VALUE *argv, VALUE klass)
{
  VALUE document;
  VALUE parse_options;
  int parse_options_int;
  xmlDocPtr doc;
  xmlSchemaParserCtxtPtr ctx;
  xmlSchemaPtr schema;
  VALUE errors;
  VALUE rb_schema;
  int scanned_args = 0;
  xmlExternalEntityLoader old_loader = 0;

  scanned_args = rb_scan_args(argc, argv, "11", &document, &parse_options);

  Data_Get_Struct(document, xmlDoc, doc);
  doc = doc->doc; /* In case someone passes us a node. ugh. */

  if (scanned_args == 1) {
    parse_options = rb_const_get_at(rb_const_get_at(mNokogiriXml, rb_intern("ParseOptions")), rb_intern("DEFAULT_SCHEMA"));
  }
  parse_options_int = (int)NUM2INT(rb_funcall(parse_options, rb_intern("to_i"), 0));

  if (has_blank_nodes_p(DOC_NODE_CACHE(doc))) {
    rb_raise(rb_eArgError, "Creating a schema from a document that has blank nodes exposed to Ruby is dangerous");
  }

  ctx = xmlSchemaNewDocParserCtxt(doc);

  errors = rb_ary_new();
  xmlSetStructuredErrorFunc((void *)errors, Nokogiri_error_array_pusher);

#ifdef HAVE_XMLSCHEMASETPARSERSTRUCTUREDERRORS
  xmlSchemaSetParserStructuredErrors(
    ctx,
    Nokogiri_error_array_pusher,
    (void *)errors
  );
#endif

  if (parse_options_int & XML_PARSE_NONET) {
    old_loader = xmlGetExternalEntityLoader();
    xmlSetExternalEntityLoader(xmlNoNetExternalEntityLoader);
  }

  schema = xmlSchemaParse(ctx);

  if (old_loader) {
    xmlSetExternalEntityLoader(old_loader);
  }

  xmlSetStructuredErrorFunc(NULL, NULL);
  xmlSchemaFreeParserCtxt(ctx);

  if (NULL == schema) {
    xmlErrorPtr error = xmlGetLastError();
    if (error) {
      Nokogiri_error_raise(NULL, error);
    } else {
      rb_raise(rb_eRuntimeError, "Could not parse document");
    }

    return Qnil;
  }

  rb_schema = Data_Wrap_Struct(klass, 0, dealloc, schema);
  rb_iv_set(rb_schema, "@errors", errors);
  rb_iv_set(rb_schema, "@parse_options", parse_options);

  return rb_schema;

  return Qnil;
}

void
noko_init_xml_schema()
{
  cNokogiriXmlSchema = rb_define_class_under(mNokogiriXml, "Schema", rb_cObject);

  rb_undef_alloc_func(cNokogiriXmlSchema);

  rb_define_singleton_method(cNokogiriXmlSchema, "read_memory", read_memory, -1);
  rb_define_singleton_method(cNokogiriXmlSchema, "from_document", from_document, -1);

  rb_define_private_method(cNokogiriXmlSchema, "validate_document", validate_document, 1);
  rb_define_private_method(cNokogiriXmlSchema, "validate_file",     validate_file, 1);
}
