const withNextra = require('nextra')({
  theme: 'nextra-theme-docs',
  themeConfig: './theme.config.jsx',
});

/** @type {import('next').NextConfig} */
const nextConfig = {
  webpack: function (config) {
    config.externals = config.externals || {};
    config.externals["styletron-server"] = "styletron-server";
    return config;
  },
  // Optionally, add any other Next.js config below
  pageExtensions: ['js', 'jsx', 'mdx', 'ts', 'tsx'],
  output: "export",
};

// First apply withMDX to the nextConfig, then wrap the result with withNextra
module.exports = withNextra(nextConfig);
