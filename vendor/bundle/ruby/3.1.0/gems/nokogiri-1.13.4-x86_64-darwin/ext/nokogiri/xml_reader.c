#include <nokogiri.h>

VALUE cNokogiriXmlReader;

static void
dealloc(xmlTextReaderPtr reader)
{
  NOKOGIRI_DEBUG_START(reader);
  xmlFreeTextReader(reader);
  NOKOGIRI_DEBUG_END(reader);
}

static int
has_attributes(xmlTextReaderPtr reader)
{
  /*
   *  this implementation of xmlTextReaderHasAttributes explicitly includes
   *  namespaces and properties, because some earlier versions ignore
   *  namespaces.
   */
  xmlNodePtr node ;
  node = xmlTextReaderCurrentNode(reader);
  if (node == NULL) {
    return (0);
  }

  if ((node->type == XML_ELEMENT_NODE) &&
      ((node->properties != NULL) || (node->nsDef != NULL))) {
    return (1);
  }
  return (0);
}

static void
Nokogiri_xml_node_namespaces(xmlNodePtr node, VALUE attr_hash)
{
  xmlNsPtr ns;
  VALUE key;

  if (node->type != XML_ELEMENT_NODE) { return ; }

  ns = node->nsDef;
  while (ns != NULL) {

    key = rb_enc_str_new_cstr(XMLNS_PREFIX, rb_utf8_encoding());
    if (ns->prefix) {
      rb_str_cat_cstr(key, ":");
      rb_str_cat_cstr(key, (const char *)ns->prefix);
    }

    key = rb_str_conv_enc(key, rb_utf8_encoding(), rb_default_internal_encoding());
    rb_hash_aset(attr_hash,
                 key,
                 (ns->href ? NOKOGIRI_STR_NEW2(ns->href) : Qnil)
                );
    ns = ns->next ;
  }
}


/*
 * call-seq:
 *   default?
 *
 * Was an attribute generated from the default value in the DTD or schema?
 */
static VALUE
default_eh(VALUE self)
{
  xmlTextReaderPtr reader;
  int eh;

  Data_Get_Struct(self, xmlTextReader, reader);
  eh = xmlTextReaderIsDefault(reader);
  if (eh == 0) { return Qfalse; }
  if (eh == 1) { return Qtrue; }

  return Qnil;
}

/*
 * call-seq:
 *   value?
 *
 * Does this node have a text value?
 */
static VALUE
value_eh(VALUE self)
{
  xmlTextReaderPtr reader;
  int eh;

  Data_Get_Struct(self, xmlTextReader, reader);
  eh = xmlTextReaderHasValue(reader);
  if (eh == 0) { return Qfalse; }
  if (eh == 1) { return Qtrue; }

  return Qnil;
}

/*
 * call-seq:
 *   attributes?
 *
 * Does this node have attributes?
 */
static VALUE
attributes_eh(VALUE self)
{
  xmlTextReaderPtr reader;
  int eh;

  Data_Get_Struct(self, xmlTextReader, reader);
  eh = has_attributes(reader);
  if (eh == 0) { return Qfalse; }
  if (eh == 1) { return Qtrue; }

  return Qnil;
}

/*
 * call-seq:
 *   namespaces
 *
 * Get a hash of namespaces for this Node
 */
static VALUE
namespaces(VALUE self)
{
  xmlTextReaderPtr reader;
  xmlNodePtr ptr;
  VALUE attr ;

  Data_Get_Struct(self, xmlTextReader, reader);

  attr = rb_hash_new() ;

  if (! has_attributes(reader)) {
    return attr ;
  }

  ptr = xmlTextReaderExpand(reader);
  if (ptr == NULL) { return Qnil; }

  Nokogiri_xml_node_namespaces(ptr, attr);

  return attr ;
}

/*
  :call-seq: attribute_nodes() → Array<Nokogiri::XML::Attr>

  Get the attributes of the current node as an Array of Attr
 */
static VALUE
rb_xml_reader_attribute_nodes(VALUE rb_reader)
{
  xmlTextReaderPtr c_reader;
  xmlNodePtr c_node;
  VALUE attr_nodes;
  int j;

  Data_Get_Struct(rb_reader, xmlTextReader, c_reader);

  if (! has_attributes(c_reader)) {
    return rb_ary_new() ;
  }

  c_node = xmlTextReaderExpand(c_reader);
  if (c_node == NULL) {
    return Qnil;
  }

  attr_nodes = noko_xml_node_attrs(c_node);

  /* ensure that the Reader won't be GCed as long as a node is referenced */
  for (j = 0 ; j < RARRAY_LEN(attr_nodes) ; j++) {
    rb_iv_set(rb_ary_entry(attr_nodes, j), "@reader", rb_reader);
  }

  return attr_nodes;
}

/*
 * call-seq:
 *   attribute_at(index)
 *
 * Get the value of attribute at +index+
 */
static VALUE
attribute_at(VALUE self, VALUE index)
{
  xmlTextReaderPtr reader;
  xmlChar *value;
  VALUE rb_value;

  Data_Get_Struct(self, xmlTextReader, reader);

  if (NIL_P(index)) { return Qnil; }
  index = rb_Integer(index);

  value = xmlTextReaderGetAttributeNo(
            reader,
            (int)NUM2INT(index)
          );
  if (value == NULL) { return Qnil; }

  rb_value = NOKOGIRI_STR_NEW2(value);
  xmlFree(value);
  return rb_value;
}

/*
 * call-seq:
 *   attribute(name)
 *
 * Get the value of attribute named +name+
 */
static VALUE
reader_attribute(VALUE self, VALUE name)
{
  xmlTextReaderPtr reader;
  xmlChar *value ;
  VALUE rb_value;

  Data_Get_Struct(self, xmlTextReader, reader);

  if (NIL_P(name)) { return Qnil; }
  name = StringValue(name) ;

  value = xmlTextReaderGetAttribute(reader, (xmlChar *)StringValueCStr(name));
  if (value == NULL) { return Qnil; }

  rb_value = NOKOGIRI_STR_NEW2(value);
  xmlFree(value);
  return rb_value;
}

/*
 * call-seq:
 *   attribute_count
 *
 * Get the number of attributes for the current node
 */
static VALUE
attribute_count(VALUE self)
{
  xmlTextReaderPtr reader;
  int count;

  Data_Get_Struct(self, xmlTextReader, reader);
  count = xmlTextReaderAttributeCount(reader);
  if (count == -1) { return Qnil; }

  return INT2NUM((long)count);
}

/*
 * call-seq:
 *   depth
 *
 * Get the depth of the node
 */
static VALUE
depth(VALUE self)
{
  xmlTextReaderPtr reader;
  int depth;

  Data_Get_Struct(self, xmlTextReader, reader);
  depth = xmlTextReaderDepth(reader);
  if (depth == -1) { return Qnil; }

  return INT2NUM((long)depth);
}

/*
 * call-seq:
 *   xml_version
 *
 * Get the XML version of the document being read
 */
static VALUE
xml_version(VALUE self)
{
  xmlTextReaderPtr reader;
  const char *version;

  Data_Get_Struct(self, xmlTextReader, reader);
  version = (const char *)xmlTextReaderConstXmlVersion(reader);
  if (version == NULL) { return Qnil; }

  return NOKOGIRI_STR_NEW2(version);
}

/*
 * call-seq:
 *   lang
 *
 * Get the xml:lang scope within which the node resides.
 */
static VALUE
lang(VALUE self)
{
  xmlTextReaderPtr reader;
  const char *lang;

  Data_Get_Struct(self, xmlTextReader, reader);
  lang = (const char *)xmlTextReaderConstXmlLang(reader);
  if (lang == NULL) { return Qnil; }

  return NOKOGIRI_STR_NEW2(lang);
}

/*
 * call-seq:
 *   value
 *
 * Get the text value of the node if present. Returns a utf-8 encoded string.
 */
static VALUE
value(VALUE self)
{
  xmlTextReaderPtr reader;
  const char *value;

  Data_Get_Struct(self, xmlTextReader, reader);
  value = (const char *)xmlTextReaderConstValue(reader);
  if (value == NULL) { return Qnil; }

  return NOKOGIRI_STR_NEW2(value);
}

/*
 * call-seq:
 *   prefix
 *
 * Get the shorthand reference to the namespace associated with the node.
 */
static VALUE
prefix(VALUE self)
{
  xmlTextReaderPtr reader;
  const char *prefix;

  Data_Get_Struct(self, xmlTextReader, reader);
  prefix = (const char *)xmlTextReaderConstPrefix(reader);
  if (prefix == NULL) { return Qnil; }

  return NOKOGIRI_STR_NEW2(prefix);
}

/*
 * call-seq:
 *   namespace_uri
 *
 * Get the URI defining the namespace associated with the node
 */
static VALUE
namespace_uri(VALUE self)
{
  xmlTextReaderPtr reader;
  const char *uri;

  Data_Get_Struct(self, xmlTextReader, reader);
  uri = (const char *)xmlTextReaderConstNamespaceUri(reader);
  if (uri == NULL) { return Qnil; }

  return NOKOGIRI_STR_NEW2(uri);
}

/*
 * call-seq:
 *   local_name
 *
 * Get the local name of the node
 */
static VALUE
local_name(VALUE self)
{
  xmlTextReaderPtr reader;
  const char *name;

  Data_Get_Struct(self, xmlTextReader, reader);
  name = (const char *)xmlTextReaderConstLocalName(reader);
  if (name == NULL) { return Qnil; }

  return NOKOGIRI_STR_NEW2(name);
}

/*
 * call-seq:
 *   name
 *
 * Get the name of the node. Returns a utf-8 encoded string.
 */
static VALUE
name(VALUE self)
{
  xmlTextReaderPtr reader;
  const char *name;

  Data_Get_Struct(self, xmlTextReader, reader);
  name = (const char *)xmlTextReaderConstName(reader);
  if (name == NULL) { return Qnil; }

  return NOKOGIRI_STR_NEW2(name);
}

/*
 * call-seq:
 * base_uri
 *
 * Get the xml:base of the node
 */
static VALUE
rb_xml_reader_base_uri(VALUE rb_reader)
{
  VALUE rb_base_uri;
  xmlTextReaderPtr c_reader;
  xmlChar *c_base_uri;

  Data_Get_Struct(rb_reader, xmlTextReader, c_reader);

  c_base_uri = xmlTextReaderBaseUri(c_reader);
  if (c_base_uri == NULL) {
    return Qnil;
  }

  rb_base_uri = NOKOGIRI_STR_NEW2(c_base_uri);
  xmlFree(c_base_uri);

  return rb_base_uri;
}

/*
 * call-seq:
 *   state
 *
 * Get the state of the reader
 */
static VALUE
state(VALUE self)
{
  xmlTextReaderPtr reader;
  Data_Get_Struct(self, xmlTextReader, reader);
  return INT2NUM((long)xmlTextReaderReadState(reader));
}

/*
 * call-seq:
 *   node_type
 *
 * Get the type of readers current node
 */
static VALUE
node_type(VALUE self)
{
  xmlTextReaderPtr reader;
  Data_Get_Struct(self, xmlTextReader, reader);
  return INT2NUM((long)xmlTextReaderNodeType(reader));
}

/*
 * call-seq:
 *   read
 *
 * Move the Reader forward through the XML document.
 */
static VALUE
read_more(VALUE self)
{
  xmlTextReaderPtr reader;
  xmlErrorPtr error;
  VALUE error_list;
  int ret;

  Data_Get_Struct(self, xmlTextReader, reader);

  error_list = rb_funcall(self, rb_intern("errors"), 0);

  xmlSetStructuredErrorFunc((void *)error_list, Nokogiri_error_array_pusher);
  ret = xmlTextReaderRead(reader);
  xmlSetStructuredErrorFunc(NULL, NULL);

  if (ret == 1) { return self; }
  if (ret == 0) { return Qnil; }

  error = xmlGetLastError();
  if (error) {
    rb_exc_raise(Nokogiri_wrap_xml_syntax_error(error));
  } else {
    rb_raise(rb_eRuntimeError, "Error pulling: %d", ret);
  }

  return Qnil;
}

/*
 * call-seq:
 *   inner_xml
 *
 * Read the contents of the current node, including child nodes and markup.
 * Returns a utf-8 encoded string.
 */
static VALUE
inner_xml(VALUE self)
{
  xmlTextReaderPtr reader;
  xmlChar *value;
  VALUE str;

  Data_Get_Struct(self, xmlTextReader, reader);

  value = xmlTextReaderReadInnerXml(reader);

  str = Qnil;
  if (value) {
    str = NOKOGIRI_STR_NEW2((char *)value);
    xmlFree(value);
  }

  return str;
}

/*
 * call-seq:
 *   outer_xml
 *
 * Read the current node and its contents, including child nodes and markup.
 * Returns a utf-8 encoded string.
 */
static VALUE
outer_xml(VALUE self)
{
  xmlTextReaderPtr reader;
  xmlChar *value;
  VALUE str = Qnil;

  Data_Get_Struct(self, xmlTextReader, reader);

  value = xmlTextReaderReadOuterXml(reader);

  if (value) {
    str = NOKOGIRI_STR_NEW2((char *)value);
    xmlFree(value);
  }
  return str;
}

/*
 * call-seq:
 *   from_memory(string, url = nil, encoding = nil, options = 0)
 *
 * Create a new reader that parses +string+
 */
static VALUE
from_memory(int argc, VALUE *argv, VALUE klass)
{
  VALUE rb_buffer, rb_url, encoding, rb_options;
  xmlTextReaderPtr reader;
  const char *c_url      = NULL;
  const char *c_encoding = NULL;
  int c_options           = 0;
  VALUE rb_reader, args[3];

  rb_scan_args(argc, argv, "13", &rb_buffer, &rb_url, &encoding, &rb_options);

  if (!RTEST(rb_buffer)) { rb_raise(rb_eArgError, "string cannot be nil"); }
  if (RTEST(rb_url)) { c_url = StringValueCStr(rb_url); }
  if (RTEST(encoding)) { c_encoding = StringValueCStr(encoding); }
  if (RTEST(rb_options)) { c_options = (int)NUM2INT(rb_options); }

  reader = xmlReaderForMemory(
             StringValuePtr(rb_buffer),
             (int)RSTRING_LEN(rb_buffer),
             c_url,
             c_encoding,
             c_options
           );

  if (reader == NULL) {
    xmlFreeTextReader(reader);
    rb_raise(rb_eRuntimeError, "couldn't create a parser");
  }

  rb_reader = Data_Wrap_Struct(klass, NULL, dealloc, reader);
  args[0] = rb_buffer;
  args[1] = rb_url;
  args[2] = encoding;
  rb_obj_call_init(rb_reader, 3, args);

  return rb_reader;
}

/*
 * call-seq:
 *   from_io(io, url = nil, encoding = nil, options = 0)
 *
 * Create a new reader that parses +io+
 */
static VALUE
from_io(int argc, VALUE *argv, VALUE klass)
{
  VALUE rb_io, rb_url, encoding, rb_options;
  xmlTextReaderPtr reader;
  const char *c_url      = NULL;
  const char *c_encoding = NULL;
  int c_options           = 0;
  VALUE rb_reader, args[3];

  rb_scan_args(argc, argv, "13", &rb_io, &rb_url, &encoding, &rb_options);

  if (!RTEST(rb_io)) { rb_raise(rb_eArgError, "io cannot be nil"); }
  if (RTEST(rb_url)) { c_url = StringValueCStr(rb_url); }
  if (RTEST(encoding)) { c_encoding = StringValueCStr(encoding); }
  if (RTEST(rb_options)) { c_options = (int)NUM2INT(rb_options); }

  reader = xmlReaderForIO(
             (xmlInputReadCallback)noko_io_read,
             (xmlInputCloseCallback)noko_io_close,
             (void *)rb_io,
             c_url,
             c_encoding,
             c_options
           );

  if (reader == NULL) {
    xmlFreeTextReader(reader);
    rb_raise(rb_eRuntimeError, "couldn't create a parser");
  }

  rb_reader = Data_Wrap_Struct(klass, NULL, dealloc, reader);
  args[0] = rb_io;
  args[1] = rb_url;
  args[2] = encoding;
  rb_obj_call_init(rb_reader, 3, args);

  return rb_reader;
}

/*
 * call-seq:
 *   reader.empty_element? # => true or false
 *
 * Returns true if the current node is empty, otherwise false.
 */
static VALUE
empty_element_p(VALUE self)
{
  xmlTextReaderPtr reader;

  Data_Get_Struct(self, xmlTextReader, reader);

  if (xmlTextReaderIsEmptyElement(reader)) {
    return Qtrue;
  }

  return Qfalse;
}

static VALUE
rb_xml_reader_encoding(VALUE rb_reader)
{
  xmlTextReaderPtr c_reader;
  const char *parser_encoding;
  VALUE constructor_encoding;

  constructor_encoding = rb_iv_get(rb_reader, "@encoding");
  if (RTEST(constructor_encoding)) {
    return constructor_encoding;
  }

  Data_Get_Struct(rb_reader, xmlTextReader, c_reader);
  parser_encoding = (const char *)xmlTextReaderConstEncoding(c_reader);
  if (parser_encoding == NULL) { return Qnil; }
  return NOKOGIRI_STR_NEW2(parser_encoding);
}

void
noko_init_xml_reader()
{
  /*
   * The Reader parser allows you to effectively pull parse an XML document.
   * Once instantiated, call Nokogiri::XML::Reader#each to iterate over each
   * node.  Note that you may only iterate over the document once!
   */
  cNokogiriXmlReader = rb_define_class_under(mNokogiriXml, "Reader", rb_cObject);

  rb_undef_alloc_func(cNokogiriXmlReader);

  rb_define_singleton_method(cNokogiriXmlReader, "from_memory", from_memory, -1);
  rb_define_singleton_method(cNokogiriXmlReader, "from_io", from_io, -1);

  rb_define_method(cNokogiriXmlReader, "attribute", reader_attribute, 1);
  rb_define_method(cNokogiriXmlReader, "attribute_at", attribute_at, 1);
  rb_define_method(cNokogiriXmlReader, "attribute_count", attribute_count, 0);
  rb_define_method(cNokogiriXmlReader, "attribute_nodes", rb_xml_reader_attribute_nodes, 0);
  rb_define_method(cNokogiriXmlReader, "attributes?", attributes_eh, 0);
  rb_define_method(cNokogiriXmlReader, "base_uri", rb_xml_reader_base_uri, 0);
  rb_define_method(cNokogiriXmlReader, "default?", default_eh, 0);
  rb_define_method(cNokogiriXmlReader, "depth", depth, 0);
  rb_define_method(cNokogiriXmlReader, "empty_element?", empty_element_p, 0);
  rb_define_method(cNokogiriXmlReader, "encoding", rb_xml_reader_encoding, 0);
  rb_define_method(cNokogiriXmlReader, "inner_xml", inner_xml, 0);
  rb_define_method(cNokogiriXmlReader, "lang", lang, 0);
  rb_define_method(cNokogiriXmlReader, "local_name", local_name, 0);
  rb_define_method(cNokogiriXmlReader, "name", name, 0);
  rb_define_method(cNokogiriXmlReader, "namespace_uri", namespace_uri, 0);
  rb_define_method(cNokogiriXmlReader, "namespaces", namespaces, 0);
  rb_define_method(cNokogiriXmlReader, "node_type", node_type, 0);
  rb_define_method(cNokogiriXmlReader, "outer_xml", outer_xml, 0);
  rb_define_method(cNokogiriXmlReader, "prefix", prefix, 0);
  rb_define_method(cNokogiriXmlReader, "read", read_more, 0);
  rb_define_method(cNokogiriXmlReader, "state", state, 0);
  rb_define_method(cNokogiriXmlReader, "value", value, 0);
  rb_define_method(cNokogiriXmlReader, "value?", value_eh, 0);
  rb_define_method(cNokogiriXmlReader, "xml_version", xml_version, 0);
}
