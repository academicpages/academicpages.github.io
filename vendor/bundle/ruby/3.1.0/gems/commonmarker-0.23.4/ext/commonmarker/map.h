#ifndef CMARK_MAP_H
#define CMARK_MAP_H

#include "chunk.h"

#ifdef __cplusplus
extern "C" {
#endif

struct cmark_map_entry {
  struct cmark_map_entry *next;
  unsigned char *label;
  unsigned int age;
};

typedef struct cmark_map_entry cmark_map_entry;

struct cmark_map;

typedef void (*cmark_map_free_f)(struct cmark_map *, cmark_map_entry *);

struct cmark_map {
  cmark_mem *mem;
  cmark_map_entry *refs;
  cmark_map_entry **sorted;
  unsigned int size;
  cmark_map_free_f free;
};

typedef struct cmark_map cmark_map;

unsigned char *normalize_map_label(cmark_mem *mem, cmark_chunk *ref);
cmark_map *cmark_map_new(cmark_mem *mem, cmark_map_free_f free);
void cmark_map_free(cmark_map *map);
cmark_map_entry *cmark_map_lookup(cmark_map *map, cmark_chunk *label);

#ifdef __cplusplus
}
#endif

#endif
