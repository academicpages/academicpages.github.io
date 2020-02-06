const fs = require('fs');
const pkg = require('./package.json');
const filename = 'anchor.min.js';
const script = fs.readFileSync(filename);
const padStart = str => ('0' + str).slice(-2)
const dateObj = new Date;
const date = `${dateObj.getFullYear()}-${padStart(dateObj.getMonth() + 1)}-${padStart(dateObj.getDate())}`;
const banner = `/**
 * AnchorJS - v${pkg.version} - ${date}
 * ${pkg.homepage}
 * Copyright (c) ${dateObj.getFullYear()} Bryan Braun; Licensed ${pkg.license}
 */
`;

if (script.slice(0, 3) != '/**') {
  fs.writeFileSync(filename, banner + script);
}
