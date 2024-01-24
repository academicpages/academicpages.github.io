const purgecss = {
  content: ["./hugo_stats.json"],
  defaultExtractor: (content) => {
    const elements = JSON.parse(content).htmlElements;
    return [
      ...(elements.tags || []),
      ...(elements.classes || []),
      ...(elements.ids || []),
    ];
  },
  safelist: [
    /^swiper-/,
    /^lb-/,
    /^gl/,
    /^go/,
    /^gc/,
    /^gs/,
    /^gi/,
    /^gz/,
    /^gprev/,
    /^gnext/,
    /^desc/,
    /^zoom/,
    /^search/,
    /^:is/,
    /dark/,
    /show/,
    /dragging/,
    /fullscreen/,
    /loaded/,
    /visible/,
    /current/,
    /active/,
  ],
};

module.exports = {
  plugins: {
    tailwindcss: {},
    "@fullhuman/postcss-purgecss":
      process.env.HUGO_ENVIRONMENT === "production" ? purgecss : false,
    autoprefixer: process.env.HUGO_ENVIRONMENT === "production" ? {} : false,
  },
};
