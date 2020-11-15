#ifndef CMARK_GFM_CORE_EXTENSIONS_H
#define CMARK_GFM_CORE_EXTENSIONS_H

#ifdef __cplusplus
extern "C" {
#endif

#include "cmark-gfm-extension_api.h"
#include "cmark-gfm-extensions_export.h"
#include <stdint.h>

CMARK_GFM_EXTENSIONS_EXPORT
void cmark_gfm_core_extensions_ensure_registered(void);

CMARK_GFM_EXTENSIONS_EXPORT
uint16_t cmark_gfm_extensions_get_table_columns(cmark_node *node);

CMARK_GFM_EXTENSIONS_EXPORT
uint8_t *cmark_gfm_extensions_get_table_alignments(cmark_node *node);

#ifdef __cplusplus
}
#endif

#endif
