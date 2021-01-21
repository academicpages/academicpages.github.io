#ifndef NOKOGIRI_XML_SYNTAX_ERROR
#define NOKOGIRI_XML_SYNTAX_ERROR

#include <nokogiri.h>

typedef struct _libxmlStructuredErrorHandlerState {
  void *user_data;
  xmlStructuredErrorFunc handler;
} libxmlStructuredErrorHandlerState ;

void init_xml_syntax_error();

void Nokogiri_structured_error_func_save(libxmlStructuredErrorHandlerState *handler_state);
void Nokogiri_structured_error_func_save_and_set(libxmlStructuredErrorHandlerState *handler_state,
                                                 void *user_data,
                                                 xmlStructuredErrorFunc handler);
void Nokogiri_structured_error_func_restore(libxmlStructuredErrorHandlerState *handler_state);

VALUE Nokogiri_wrap_xml_syntax_error(xmlErrorPtr error);
void Nokogiri_error_array_pusher(void *ctx, xmlErrorPtr error);
NORETURN(void Nokogiri_error_raise(void *ctx, xmlErrorPtr error));

extern VALUE cNokogiriXmlSyntaxError;

#endif /* NOKOGIRI_XML_SYNTAX_ERROR */
