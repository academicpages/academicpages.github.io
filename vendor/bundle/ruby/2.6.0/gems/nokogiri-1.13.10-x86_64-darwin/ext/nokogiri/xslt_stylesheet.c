#include <nokogiri.h>

VALUE cNokogiriXsltStylesheet ;

static void
mark(nokogiriXsltStylesheetTuple *wrapper)
{
  rb_gc_mark(wrapper->func_instances);
}

static void
dealloc(nokogiriXsltStylesheetTuple *wrapper)
{
  xsltStylesheetPtr doc = wrapper->ss;

  NOKOGIRI_DEBUG_START(doc);
  xsltFreeStylesheet(doc); /* commented out for now. */
  NOKOGIRI_DEBUG_END(doc);

  free(wrapper);
}

static void
xslt_generic_error_handler(void *ctx, const char *msg, ...)
{
  char *message;

  va_list args;
  va_start(args, msg);
  vasprintf(&message, msg, args);
  va_end(args);

  rb_str_cat2((VALUE)ctx, message);

  free(message);
}

VALUE
Nokogiri_wrap_xslt_stylesheet(xsltStylesheetPtr ss)
{
  VALUE self;
  nokogiriXsltStylesheetTuple *wrapper;

  self = Data_Make_Struct(cNokogiriXsltStylesheet, nokogiriXsltStylesheetTuple,
                          mark, dealloc, wrapper);

  ss->_private = (void *)self;
  wrapper->ss = ss;
  wrapper->func_instances = rb_ary_new();

  return self;
}

/*
 * call-seq:
 *   parse_stylesheet_doc(document)
 *
 * Parse a stylesheet from +document+.
 */
static VALUE
parse_stylesheet_doc(VALUE klass, VALUE xmldocobj)
{
  xmlDocPtr xml, xml_cpy;
  VALUE errstr, exception;
  xsltStylesheetPtr ss ;
  Data_Get_Struct(xmldocobj, xmlDoc, xml);

  errstr = rb_str_new(0, 0);
  xsltSetGenericErrorFunc((void *)errstr, xslt_generic_error_handler);

  xml_cpy = xmlCopyDoc(xml, 1); /* 1 => recursive */
  ss = xsltParseStylesheetDoc(xml_cpy);

  xsltSetGenericErrorFunc(NULL, NULL);

  if (!ss) {
    xmlFreeDoc(xml_cpy);
    exception = rb_exc_new3(rb_eRuntimeError, errstr);
    rb_exc_raise(exception);
  }

  return Nokogiri_wrap_xslt_stylesheet(ss);
}


/*
 * call-seq:
 *   serialize(document)
 *
 * Serialize +document+ to an xml string.
 */
static VALUE
serialize(VALUE self, VALUE xmlobj)
{
  xmlDocPtr xml ;
  nokogiriXsltStylesheetTuple *wrapper;
  xmlChar *doc_ptr ;
  int doc_len ;
  VALUE rval ;

  Data_Get_Struct(xmlobj, xmlDoc, xml);
  Data_Get_Struct(self, nokogiriXsltStylesheetTuple, wrapper);
  xsltSaveResultToString(&doc_ptr, &doc_len, xml, wrapper->ss);
  rval = NOKOGIRI_STR_NEW(doc_ptr, doc_len);
  xmlFree(doc_ptr);
  return rval ;
}

/*
 * call-seq:
 *   transform(document)
 *   transform(document, params = {})
 *
 * Apply an XSLT stylesheet to an XML::Document.
 *
 * [Parameters]
 * - +document+ (Nokogiri::XML::Document) the document to be transformed.
 * - +params+ (Hash, Array) strings used as XSLT parameters.
 *
 * [Returns] Nokogiri::XML::Document
 *
 * *Example* of basic transformation:
 *
 *   xslt = <<~XSLT
 *     <xsl:stylesheet version="1.0"
 *     xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
 *
 *     <xsl:param name="title"/>
 *
 *     <xsl:template match="/">
 *       <html>
 *         <body>
 *           <h1><xsl:value-of select="$title"/></h1>
 *           <ol>
 *             <xsl:for-each select="staff/employee">
 *               <li><xsl:value-of select="employeeId"></li>
 *             </xsl:for-each>
 *           </ol>
 *         </body>
 *       </html>
 *     </xsl:stylesheet>
 *   XSLT
 *
 *   xml = <<~XML
 *     <?xml version="1.0"?>
 *     <staff>
 *       <employee>
 *         <employeeId>EMP0001</employeeId>
 *         <position>Accountant</position>
 *       </employee>
 *       <employee>
 *         <employeeId>EMP0002</employeeId>
 *         <position>Developer</position>
 *       </employee>
 *     </staff>
 *   XML
 *
 *   doc = Nokogiri::XML::Document.parse(xml)
 *   stylesheet = Nokogiri::XSLT.parse(xslt)
 *
 * ⚠ Note that the +h1+ element is empty because no param has been provided!
 *
 *   stylesheet.transform(doc).to_xml
 *   # => "<html><body>\n" +
 *   #    "<h1></h1>\n" +
 *   #    "<ol>\n" +
 *   #    "<li>EMP0001</li>\n" +
 *   #    "<li>EMP0002</li>\n" +
 *   #    "</ol>\n" +
 *   #    "</body></html>\n"
 *
 * *Example* of using an input parameter hash:
 *
 * ⚠ The title is populated, but note how we need to quote-escape the value.
 *
 *   stylesheet.transform(doc, { "title" => "'Employee List'" }).to_xml
 *   # => "<html><body>\n" +
 *   #    "<h1>Employee List</h1>\n" +
 *   #    "<ol>\n" +
 *   #    "<li>EMP0001</li>\n" +
 *   #    "<li>EMP0002</li>\n" +
 *   #    "</ol>\n" +
 *   #    "</body></html>\n"
 *
 * *Example* using the XSLT.quote_params helper method to safely quote-escape strings:
 *
 *   stylesheet.transform(doc, Nokogiri::XSLT.quote_params({ "title" => "Aaron's List" })).to_xml
 *   # => "<html><body>\n" +
 *   #    "<h1>Aaron's List</h1>\n" +
 *   #    "<ol>\n" +
 *   #    "<li>EMP0001</li>\n" +
 *   #    "<li>EMP0002</li>\n" +
 *   #    "</ol>\n" +
 *   #    "</body></html>\n"
 *
 * *Example* using an array of XSLT parameters
 *
 * You can also use an array if you want to.
 *
 *   stylesheet.transform(doc, ["title", "'Employee List'"]).to_xml
 *   # => "<html><body>\n" +
 *   #    "<h1>Employee List</h1>\n" +
 *   #    "<ol>\n" +
 *   #    "<li>EMP0001</li>\n" +
 *   #    "<li>EMP0002</li>\n" +
 *   #    "</ol>\n" +
 *   #    "</body></html>\n"
 *
 * Or pass an array to XSLT.quote_params:
 *
 *   stylesheet.transform(doc, Nokogiri::XSLT.quote_params(["title", "Aaron's List"])).to_xml
 *   # => "<html><body>\n" +
 *   #    "<h1>Aaron's List</h1>\n" +
 *   #    "<ol>\n" +
 *   #    "<li>EMP0001</li>\n" +
 *   #    "<li>EMP0002</li>\n" +
 *   #    "</ol>\n" +
 *   #    "</body></html>\n"
 *
 * See: Nokogiri::XSLT.quote_params
 */
static VALUE
transform(int argc, VALUE *argv, VALUE self)
{
  VALUE xmldoc, paramobj, errstr, exception ;
  xmlDocPtr xml ;
  xmlDocPtr result ;
  nokogiriXsltStylesheetTuple *wrapper;
  const char **params ;
  long param_len, j ;
  int parse_error_occurred ;

  rb_scan_args(argc, argv, "11", &xmldoc, &paramobj);
  if (NIL_P(paramobj)) { paramobj = rb_ary_new2(0L) ; }
  if (!rb_obj_is_kind_of(xmldoc, cNokogiriXmlDocument)) {
    rb_raise(rb_eArgError, "argument must be a Nokogiri::XML::Document");
  }

  /* handle hashes as arguments. */
  if (T_HASH == TYPE(paramobj)) {
    paramobj = rb_funcall(paramobj, rb_intern("to_a"), 0);
    paramobj = rb_funcall(paramobj, rb_intern("flatten"), 0);
  }

  Check_Type(paramobj, T_ARRAY);

  Data_Get_Struct(xmldoc, xmlDoc, xml);
  Data_Get_Struct(self, nokogiriXsltStylesheetTuple, wrapper);

  param_len = RARRAY_LEN(paramobj);
  params = calloc((size_t)param_len + 1, sizeof(char *));
  for (j = 0 ; j < param_len ; j++) {
    VALUE entry = rb_ary_entry(paramobj, j);
    const char *ptr = StringValueCStr(entry);
    params[j] = ptr;
  }
  params[param_len] = 0 ;

  errstr = rb_str_new(0, 0);
  xsltSetGenericErrorFunc((void *)errstr, xslt_generic_error_handler);
  xmlSetGenericErrorFunc((void *)errstr, xslt_generic_error_handler);

  result = xsltApplyStylesheet(wrapper->ss, xml, params);
  free(params);

  xsltSetGenericErrorFunc(NULL, NULL);
  xmlSetGenericErrorFunc(NULL, NULL);

  parse_error_occurred = (Qfalse == rb_funcall(errstr, rb_intern("empty?"), 0));

  if (parse_error_occurred) {
    exception = rb_exc_new3(rb_eRuntimeError, errstr);
    rb_exc_raise(exception);
  }

  return noko_xml_document_wrap((VALUE)0, result) ;
}

static void
method_caller(xmlXPathParserContextPtr ctxt, int nargs)
{
  VALUE handler;
  const char *function_name;
  xsltTransformContextPtr transform;
  const xmlChar *functionURI;

  transform = xsltXPathGetTransformContext(ctxt);
  functionURI = ctxt->context->functionURI;
  handler = (VALUE)xsltGetExtData(transform, functionURI);
  function_name = (const char *)(ctxt->context->function);

  Nokogiri_marshal_xpath_funcall_and_return_values(ctxt, nargs, handler, (const char *)function_name);
}

static void *
initFunc(xsltTransformContextPtr ctxt, const xmlChar *uri)
{
  VALUE modules = rb_iv_get(mNokogiriXslt, "@modules");
  VALUE obj = rb_hash_aref(modules, rb_str_new2((const char *)uri));
  VALUE args = { Qfalse };
  VALUE methods = rb_funcall(obj, rb_intern("instance_methods"), 1, args);
  VALUE inst;
  nokogiriXsltStylesheetTuple *wrapper;
  int i;

  for (i = 0; i < RARRAY_LEN(methods); i++) {
    VALUE method_name = rb_obj_as_string(rb_ary_entry(methods, i));
    xsltRegisterExtFunction(ctxt,
                            (unsigned char *)StringValueCStr(method_name), uri, method_caller);
  }

  Data_Get_Struct((VALUE)ctxt->style->_private, nokogiriXsltStylesheetTuple,
                  wrapper);
  inst = rb_class_new_instance(0, NULL, obj);
  rb_ary_push(wrapper->func_instances, inst);

  return (void *)inst;
}

static void
shutdownFunc(xsltTransformContextPtr ctxt,
             const xmlChar *uri, void *data)
{
  nokogiriXsltStylesheetTuple *wrapper;

  Data_Get_Struct((VALUE)ctxt->style->_private, nokogiriXsltStylesheetTuple,
                  wrapper);

  rb_ary_clear(wrapper->func_instances);
}

/*
 *  call-seq:
 *    register(uri, custom_handler_class)
 *
 *  Register a class that implements custom XSLT transformation functions.
 */
static VALUE
registr(VALUE self, VALUE uri, VALUE obj)
{
  VALUE modules = rb_iv_get(self, "@modules");
  if (NIL_P(modules)) { rb_raise(rb_eRuntimeError, "wtf! @modules isn't set"); }

  rb_hash_aset(modules, uri, obj);
  xsltRegisterExtModule((unsigned char *)StringValueCStr(uri), initFunc, shutdownFunc);
  return self;
}

void
noko_init_xslt_stylesheet()
{
  rb_define_singleton_method(mNokogiriXslt, "register", registr, 2);
  rb_iv_set(mNokogiriXslt, "@modules", rb_hash_new());

  cNokogiriXsltStylesheet = rb_define_class_under(mNokogiriXslt, "Stylesheet", rb_cObject);

  rb_undef_alloc_func(cNokogiriXsltStylesheet);

  rb_define_singleton_method(cNokogiriXsltStylesheet, "parse_stylesheet_doc", parse_stylesheet_doc, 1);
  rb_define_method(cNokogiriXsltStylesheet, "serialize", serialize, 1);
  rb_define_method(cNokogiriXsltStylesheet, "transform", transform, -1);
}
