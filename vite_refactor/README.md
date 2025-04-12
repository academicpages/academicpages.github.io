# Refactoring to Vite React with Markdown Support

Here's how to convert your Jekyll academic website to a Vite React app with robust Markdown support:

## 1. Set up the project

```bash
# Create a new Vite React project
npm create vite@latest academic-site -y -- --template react
cd academic-site
npm install
```

- added credentials in remote dev env

## 2. Add Markdown support

```bash
# Install necessary packages
npm install react-markdown rehype-raw rehype-sanitize remark-gfm vite-plugin-markdown
```

## 3. Configure Vite for Markdown

```javascript
// vite.config.js
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import markdown from 'vite-plugin-markdown';

export default defineConfig({
  plugins: [
    react(),
    markdown({ mode: 'react' })
  ],
  base: './'
});
```

## 4. Create Markdown content structure

```bash
mkdir -p src/content/pages src/content/publications src/content/talks
```

## 5. Create a Markdown loader component

```jsx
// src/components/MarkdownPage.jsx
import React, { useEffect, useState } from 'react';
import ReactMarkdown from 'react-markdown';
import rehypeRaw from 'rehype-raw';
import rehypeSanitize from 'rehype-sanitize';
import remarkGfm from 'remark-gfm';

export default function MarkdownPage({ filePath }) {
  const [content, setContent] = useState('');

  useEffect(() => {
    fetch(filePath)
      .then(response => response.text())
      .then(text => setContent(text))
      .catch(error => console.error('Error loading markdown:', error));
  }, [filePath]);

  return (
    <div className="markdown-content">
      <ReactMarkdown
        rehypePlugins={[rehypeRaw, rehypeSanitize]}
        remarkPlugins={[remarkGfm]}
      >
        {content}
      </ReactMarkdown>
    </div>
  );
}
```

## 6. Set up routing for Markdown pages

```jsx
// src/App.jsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Home from './pages/Home';
import MarkdownPage from './components/MarkdownPage';

function App() {
  return (
    <BrowserRouter>
      <Header />
      <main className="container">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<MarkdownPage filePath="/content/pages/about.md" />} />
          <Route path="/publications" element={<MarkdownPage filePath="/content/publications/index.md" />} />
          <Route path="/talks" element={<MarkdownPage filePath="/content/talks/index.md" />} />
        </Routes>
      </main>
    </BrowserRouter>
  );
}

export default App;
```

## 7. Create sample Markdown content

```markdown
// public/content/pages/about.md
# About Me

I am a researcher specializing in...
```

## 8. Add dynamic Markdown file loading

```jsx
// src/pages/Publication.jsx
import React from 'react';
import { useParams } from 'react-router-dom';
import MarkdownPage from '../components/MarkdownPage';

export default function Publication() {
  const { id } = useParams();
  return <MarkdownPage filePath={`/content/publications/${id}.md`} />;
}
```

## 9. Configure GitHub Pages deployment

```bash
npm install gh-pages --save-dev
```

Update `package.json`:

```json
"scripts": {
  "dev": "vite",
  "build": "vite build",
  "preview": "vite preview",
  "predeploy": "npm run build",
  "deploy": "gh-pages -d dist"
},
```

This approach provides a modern React application that can load Markdown content just like your previous Jekyll site, but with the benefits of a modern frontend stack.