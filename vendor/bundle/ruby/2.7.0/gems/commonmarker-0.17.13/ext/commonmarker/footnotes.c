#include "cmark-gfm.h"
#include "parser.h"
#include "footnotes.h"
#include "inlines.h"
#include "chunk.h"

static void footnote_free(cmark_map *map, cmark_map_entry *_ref) {
  cmark_footnote *ref = (cmark_footnote *)_ref;
  cmark_mem *mem = map->mem;
  if (ref != NULL) {
    mem->free(ref->entry.label);
    if (ref->node)
      cmark_node_free(ref->node);
    mem->free(ref);
  }
}

void cmark_footnote_create(cmark_map *map, cmark_node *node) {
  cmark_footnote *ref;
  unsigned char *reflabel = normalize_map_label(map->mem, &node->as.literal);

  /* empty footnote name, or composed from only whitespace */
  if (reflabel == NULL)
    return;

  assert(map->sorted == NULL);

  ref = (cmark_footnote *)map->mem->calloc(1, sizeof(*ref));
  ref->entry.label = reflabel;
  ref->node = node;
  ref->entry.age = map->size;
  ref->entry.next = map->refs;

  map->refs = (cmark_map_entry *)ref;
  map->size++;
}

cmark_map *cmark_footnote_map_new(cmark_mem *mem) {
  return cmark_map_new(mem, footnote_free);
}
