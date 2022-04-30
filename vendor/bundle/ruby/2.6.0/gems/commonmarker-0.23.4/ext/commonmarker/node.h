#ifndef CMARK_NODE_H
#define CMARK_NODE_H

#ifdef __cplusplus
extern "C" {
#endif

#include <stdio.h>
#include <stdint.h>

#include "cmark-gfm.h"
#include "cmark-gfm-extension_api.h"
#include "buffer.h"
#include "chunk.h"

typedef struct {
  cmark_list_type list_type;
  int marker_offset;
  int padding;
  int start;
  cmark_delim_type delimiter;
  unsigned char bullet_char;
  bool tight;
  bool checked; // For task list extension
} cmark_list;

typedef struct {
  cmark_chunk info;
  cmark_chunk literal;
  uint8_t fence_length;
  uint8_t fence_offset;
  unsigned char fence_char;
  int8_t fenced;
} cmark_code;

typedef struct {
  int level;
  bool setext;
} cmark_heading;

typedef struct {
  cmark_chunk url;
  cmark_chunk title;
} cmark_link;

typedef struct {
  cmark_chunk on_enter;
  cmark_chunk on_exit;
} cmark_custom;

enum cmark_node__internal_flags {
  CMARK_NODE__OPEN = (1 << 0),
  CMARK_NODE__LAST_LINE_BLANK = (1 << 1),
  CMARK_NODE__LAST_LINE_CHECKED = (1 << 2),
};

struct cmark_node {
  cmark_strbuf content;

  struct cmark_node *next;
  struct cmark_node *prev;
  struct cmark_node *parent;
  struct cmark_node *first_child;
  struct cmark_node *last_child;

  void *user_data;
  cmark_free_func user_data_free_func;

  int start_line;
  int start_column;
  int end_line;
  int end_column;
  int internal_offset;
  uint16_t type;
  uint16_t flags;

  cmark_syntax_extension *extension;

  union {
    int ref_ix;
    int def_count;
  } footnote;

  cmark_node *parent_footnote_def;

  union {
    cmark_chunk literal;
    cmark_list list;
    cmark_code code;
    cmark_heading heading;
    cmark_link link;
    cmark_custom custom;
    int html_block_type;
    void *opaque;
  } as;
};

static CMARK_INLINE cmark_mem *cmark_node_mem(cmark_node *node) {
  return node->content.mem;
}
CMARK_GFM_EXPORT int cmark_node_check(cmark_node *node, FILE *out);

static CMARK_INLINE bool CMARK_NODE_TYPE_BLOCK_P(cmark_node_type node_type) {
	return (node_type & CMARK_NODE_TYPE_MASK) == CMARK_NODE_TYPE_BLOCK;
}

static CMARK_INLINE bool CMARK_NODE_BLOCK_P(cmark_node *node) {
	return node != NULL && CMARK_NODE_TYPE_BLOCK_P((cmark_node_type) node->type);
}

static CMARK_INLINE bool CMARK_NODE_TYPE_INLINE_P(cmark_node_type node_type) {
	return (node_type & CMARK_NODE_TYPE_MASK) == CMARK_NODE_TYPE_INLINE;
}

static CMARK_INLINE bool CMARK_NODE_INLINE_P(cmark_node *node) {
	return node != NULL && CMARK_NODE_TYPE_INLINE_P((cmark_node_type) node->type);
}

CMARK_GFM_EXPORT bool cmark_node_can_contain_type(cmark_node *node, cmark_node_type child_type);

#ifdef __cplusplus
}
#endif

#endif
