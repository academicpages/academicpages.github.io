# Optional Thumbnail Carousel for Archive Items

AcademicPages supports an optional multi-image thumbnail carousel for portfolio entries and other archive collections.

## Configuration

Add a `thumbnails` array to the YAML front matter of a collection item:

```yaml
---
title: "Example Research Project"
collection: portfolio
permalink: /portfolio/example-project/

thumbnails:
  - src: "/images/project/architecture.png"
    alt: "Project architecture"
  - src: "/images/project/results.png"
    alt: "Experimental results"
  - src: "/images/project/visualization.png"
    alt: "Visualization of the results"
---
```

Each thumbnail supports:

- `src`: Image path, relative to the website root, or an absolute URL.
- `alt`: Alternative text describing the image.

## Behavior

- The first image is displayed initially.
- Previous and next buttons navigate between images.
- The image counter indicates the current position.
- Navigation wraps around when reaching the first or last image.
- Left and right arrow keys provide keyboard navigation when the carousel has focus.
- The carousel does not autoplay.

## Backward Compatibility

The `thumbnails` field is optional.

Archive entries without this field retain their existing appearance, including their configured single-image teaser.

## Notes

Use optimized images to keep archive pages lightweight. Provide meaningful alternative text for accessibility.
