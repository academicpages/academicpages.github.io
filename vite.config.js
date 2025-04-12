// vite.config.js
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import fs from 'fs';
import path from 'path';

// https://vitejs.dev/config/
export default defineConfig({
  base: '/',
  plugins: [
    react(),
    {
      name: 'markdown-directory-listing',
      configureServer(server) {
        server.middlewares.use((req, res, next) => {
          if (req.url.startsWith('/api/list-files/')) {
            const directory = req.url.replace('/api/list-files/', '');
            const dirPath = path.join('public/content', directory);

            try {
              if (fs.existsSync(dirPath)) {
                const files = fs.readdirSync(dirPath)
                  .filter(file => file.endsWith('.md'));
                res.setHeader('Content-Type', 'application/json');
                res.end(JSON.stringify({ files }));
                return;
              }
            } catch (error) {
              console.error(`Error listing directory ${dirPath}:`, error);
            }

            res.statusCode = 404;
            res.end(JSON.stringify({ error: 'Directory not found' }));
            return;
          }
          next();
        });
      }
    }
  ]
});