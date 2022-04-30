#include <nokogiri.h>

VALUE cNokogiriXmlXpathContext;

/*
 * these constants have matching declarations in
 * ext/java/nokogiri/internals/NokogiriNamespaceContext.java
 */
static const xmlChar *NOKOGIRI_BUILTIN_PREFIX = (const xmlChar *)"nokogiri-builtin";
static const xmlChar *NOKOGIRI_BUILTIN_URI = (const xmlChar *)"https://www.nokogiri.org/default_ns/ruby/builtins";

static void
deallocate(xmlXPathContextPtr ctx)
{
  NOKOGIRI_DEBUG_START(ctx);
  xmlXPathFreeContext(ctx);
  NOKOGIRI_DEBUG_END(ctx);
}

/* find a CSS class in an HTML element's `class` attribute */
static const xmlChar *
builtin_css_class(const xmlChar *str, const xmlChar *val)
{
  int val_len;

  if (str == NULL) { return (NULL); }
  if (val == NULL) { return (NULL); }

  val_len = xmlStrlen(val);
  if (val_len == 0) { return (str); }

  while (*str != 0) {
    if ((*str == *val) && !xmlStrncmp(str, val, val_len)) {
      const xmlChar *next_byte = str + val_len;

      /* only match if the next byte is whitespace or end of string */
      if ((*next_byte == 0) || (IS_BLANK_CH(*next_byte))) {
        return ((const xmlChar *)str);
      }
    }

    /* advance str to whitespace */
    while ((*str != 0) && !IS_BLANK_CH(*str)) {
      str++;
    }

    /* advance str to start of next word or end of string */
    while ((*str != 0) && IS_BLANK_CH(*str)) {
      str++;
    }
  }

  return (NULL);
}

/* xmlXPathFunction to wrap builtin_css_class() */
static void
xpath_builtin_css_class(xmlXPathParserContextPtr ctxt, int nargs)
{
  xmlXPathObjectPtr hay, needle;

  CHECK_ARITY(2);

  CAST_TO_STRING;
  needle = valuePop(ctxt);
  if ((needle == NULL) || (needle->type != XPATH_STRING)) {
    xmlXPathFreeObject(needle);
    XP_ERROR(XPATH_INVALID_TYPE);
  }

  CAST_TO_STRING;
  hay = valuePop(ctxt);
  if ((hay == NULL) || (hay->type != XPATH_STRING)) {
    xmlXPathFreeObject(hay);
    xmlXPathFreeObject(needle);
    XP_ERROR(XPATH_INVALID_TYPE);
  }

  if (builtin_css_class(hay->stringval, needle->stringval)) {
    valuePush(ctxt, xmlXPathNewBoolean(1));
  } else {
    valuePush(ctxt, xmlXPathNewBoolean(0));
  }

  xmlXPathFreeObject(hay);
  xmlXPathFreeObject(needle);
}


/* xmlXPathFunction to select nodes whose local name matches, for HTML5 CSS queries that should ignore namespaces */
static void
xpath_builtin_local_name_is(xmlXPathParserContextPtr ctxt, int nargs)
{
  xmlXPathObjectPtr element_name;

  assert(ctxt->context->node);

  CHECK_ARITY(1);
  CAST_TO_STRING;
  CHECK_TYPE(XPATH_STRING);
  element_name = valuePop(ctxt);

  valuePush(ctxt, xmlXPathNewBoolean(xmlStrEqual(ctxt->context->node->name, element_name->stringval)));

  xmlXPathFreeObject(element_name);
}


/*
 * call-seq:
 *  register_ns(prefix, uri)
 *
 * Register the namespace with +prefix+ and +uri+.
 */
static VALUE
register_ns(VALUE self, VALUE prefix, VALUE uri)
{
  xmlXPathContextPtr ctx;
  Data_Get_Struct(self, xmlXPathContext, ctx);

  xmlXPathRegisterNs(ctx,
                     (const xmlChar *)StringValueCStr(prefix),
                     (const xmlChar *)StringValueCStr(uri)
                    );
  return self;
}

/*
 * call-seq:
 *  register_variable(name, value)
 *
 * Register the variable +name+ with +value+.
 */
static VALUE
register_variable(VALUE self, VALUE name, VALUE value)
{
  xmlXPathContextPtr ctx;
  xmlXPathObjectPtr xmlValue;
  Data_Get_Struct(self, xmlXPathContext, ctx);

  xmlValue = xmlXPathNewCString(StringValueCStr(value));

  xmlXPathRegisterVariable(ctx,
                           (const xmlChar *)StringValueCStr(name),
                           xmlValue
                          );

  return self;
}


/*
 *  convert an XPath object into a Ruby object of the appropriate type.
 *  returns Qundef if no conversion was possible.
 */
static VALUE
xpath2ruby(xmlXPathObjectPtr xobj, xmlXPathContextPtr xctx)
{
  VALUE retval;

  assert(xctx->doc);
  assert(DOC_RUBY_OBJECT_TEST(xctx->doc));

  switch (xobj->type) {
    case XPATH_STRING:
      retval = NOKOGIRI_STR_NEW2(xobj->stringval);
      xmlFree(xobj->stringval);
      return retval;

    case XPATH_NODESET:
      return noko_xml_node_set_wrap(xobj->nodesetval,
                                    DOC_RUBY_OBJECT(xctx->doc));

    case XPATH_NUMBER:
      return rb_float_new(xobj->floatval);

    case XPATH_BOOLEAN:
      return (xobj->boolval == 1) ? Qtrue : Qfalse;

    default:
      return Qundef;
  }
}

void
Nokogiri_marshal_xpath_funcall_and_return_values(xmlXPathParserContextPtr ctx, int nargs, VALUE handler,
    const char *function_name)
{
  VALUE result, doc;
  VALUE *argv;
  VALUE node_set = Qnil;
  xmlNodeSetPtr xml_node_set = NULL;
  xmlXPathObjectPtr obj;

  assert(ctx->context->doc);
  assert(DOC_RUBY_OBJECT_TEST(ctx->context->doc));

  argv = (VALUE *)calloc((size_t)nargs, sizeof(VALUE));
  for (int j = 0 ; j < nargs ; ++j) {
    rb_gc_register_address(&argv[j]);
  }

  doc = DOC_RUBY_OBJECT(ctx->context->doc);

  for (int j = nargs - 1 ; j >= 0 ; --j) {
    obj = valuePop(ctx);
    argv[j] = xpath2ruby(obj, ctx->context);
    if (argv[j] == Qundef) {
      argv[j] = NOKOGIRI_STR_NEW2(xmlXPathCastToString(obj));
    }
    xmlXPathFreeNodeSetList(obj);
  }

  result = rb_funcall2(handler, rb_intern((const char *)function_name), nargs, argv);

  for (int j = 0 ; j < nargs ; ++j) {
    rb_gc_unregister_address(&argv[j]);
  }
  free(argv);

  switch (TYPE(result)) {
    case T_FLOAT:
    case T_BIGNUM:
    case T_FIXNUM:
      xmlXPathReturnNumber(ctx, NUM2DBL(result));
      break;
    case T_STRING:
      xmlXPathReturnString(
        ctx,
        xmlCharStrdup(StringValueCStr(result))
      );
      break;
    case T_TRUE:
      xmlXPathReturnTrue(ctx);
      break;
    case T_FALSE:
      xmlXPathReturnFalse(ctx);
      break;
    case T_NIL:
      break;
    case T_ARRAY: {
      VALUE args[2];
      args[0] = doc;
      args[1] = result;
      node_set = rb_class_new_instance(2, args, cNokogiriXmlNodeSet);
      Data_Get_Struct(node_set, xmlNodeSet, xml_node_set);
      xmlXPathReturnNodeSet(ctx, xmlXPathNodeSetMerge(NULL, xml_node_set));
    }
    break;
    case T_DATA:
      if (rb_obj_is_kind_of(result, cNokogiriXmlNodeSet)) {
        Data_Get_Struct(result, xmlNodeSet, xml_node_set);
        /* Copy the node set, otherwise it will get GC'd. */
        xmlXPathReturnNodeSet(ctx, xmlXPathNodeSetMerge(NULL, xml_node_set));
        break;
      }
    default:
      rb_raise(rb_eRuntimeError, "Invalid return type");
  }
}

static void
ruby_funcall(xmlXPathParserContextPtr ctx, int nargs)
{
  VALUE handler = Qnil;
  const char *function = NULL ;

  assert(ctx);
  assert(ctx->context);
  assert(ctx->context->userData);
  assert(ctx->context->function);

  handler = (VALUE)(ctx->context->userData);
  function = (const char *)(ctx->context->function);

  Nokogiri_marshal_xpath_funcall_and_return_values(ctx, nargs, handler, function);
}

static xmlXPathFunction
lookup(void *ctx,
       const xmlChar *name,
       const xmlChar *ns_uri)
{
  VALUE xpath_handler = (VALUE)ctx;
  if (rb_respond_to(xpath_handler, rb_intern((const char *)name))) {
    return ruby_funcall;
  }

  return NULL;
}

NORETURN(static void xpath_generic_exception_handler(void *ctx, const char *msg, ...));
static void
xpath_generic_exception_handler(void *ctx, const char *msg, ...)
{
  char *message;

  va_list args;
  va_start(args, msg);
  vasprintf(&message, msg, args);
  va_end(args);

  rb_raise(rb_eRuntimeError, "%s", message);
}

/*
 * call-seq:
 *  evaluate(search_path, handler = nil)
 *
 * Evaluate the +search_path+ returning an XML::XPath object.
 */
static VALUE
evaluate(int argc, VALUE *argv, VALUE self)
{
  VALUE search_path, xpath_handler;
  VALUE retval = Qnil;
  xmlXPathContextPtr ctx;
  xmlXPathObjectPtr xpath;
  xmlChar *query;

  Data_Get_Struct(self, xmlXPathContext, ctx);

  if (rb_scan_args(argc, argv, "11", &search_path, &xpath_handler) == 1) {
    xpath_handler = Qnil;
  }

  query = (xmlChar *)StringValueCStr(search_path);

  if (Qnil != xpath_handler) {
    /* FIXME: not sure if this is the correct place to shove private data. */
    ctx->userData = (void *)xpath_handler;
    xmlXPathRegisterFuncLookup(ctx, lookup, (void *)xpath_handler);
  }

  xmlResetLastError();
  xmlSetStructuredErrorFunc(NULL, Nokogiri_error_raise);

  /* For some reason, xmlXPathEvalExpression will blow up with a generic error */
  /* when there is a non existent function. */
  xmlSetGenericErrorFunc(NULL, xpath_generic_exception_handler);

  xpath = xmlXPathEvalExpression(query, ctx);
  xmlSetStructuredErrorFunc(NULL, NULL);
  xmlSetGenericErrorFunc(NULL, NULL);

  if (xpath == NULL) {
    xmlErrorPtr error = xmlGetLastError();
    rb_exc_raise(Nokogiri_wrap_xml_syntax_error(error));
  }

  retval = xpath2ruby(xpath, ctx);
  if (retval == Qundef) {
    retval = noko_xml_node_set_wrap(NULL, DOC_RUBY_OBJECT(ctx->doc));
  }

  xmlXPathFreeNodeSetList(xpath);

  return retval;
}

/*
 * call-seq:
 *  new(node)
 *
 * Create a new XPathContext with +node+ as the reference point.
 */
static VALUE
new (VALUE klass, VALUE nodeobj)
{
  xmlNodePtr node;
  xmlXPathContextPtr ctx;
  VALUE self;

  Data_Get_Struct(nodeobj, xmlNode, node);

  xmlXPathInit();

  ctx = xmlXPathNewContext(node->doc);
  ctx->node = node;

  xmlXPathRegisterNs(ctx, NOKOGIRI_BUILTIN_PREFIX, NOKOGIRI_BUILTIN_URI);
  xmlXPathRegisterFuncNS(ctx, (const xmlChar *)"css-class", NOKOGIRI_BUILTIN_URI,
                         xpath_builtin_css_class);
  xmlXPathRegisterFuncNS(ctx, (const xmlChar *)"local-name-is", NOKOGIRI_BUILTIN_URI,
                         xpath_builtin_local_name_is);

  self = Data_Wrap_Struct(klass, 0, deallocate, ctx);
  return self;
}

void
noko_init_xml_xpath_context(void)
{
  /*
   * XPathContext is the entry point for searching a Document by using XPath.
   */
  cNokogiriXmlXpathContext = rb_define_class_under(mNokogiriXml, "XPathContext", rb_cObject);

  rb_undef_alloc_func(cNokogiriXmlXpathContext);

  rb_define_singleton_method(cNokogiriXmlXpathContext, "new", new, 1);

  rb_define_method(cNokogiriXmlXpathContext, "evaluate", evaluate, -1);
  rb_define_method(cNokogiriXmlXpathContext, "register_variable", register_variable, 2);
  rb_define_method(cNokogiriXmlXpathContext, "register_ns", register_ns, 2);
}
