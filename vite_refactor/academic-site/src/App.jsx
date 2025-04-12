// src/App.jsx
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Header from "./components/Header";
import Home from "./pages/Home";
import MarkdownPage from "./components/MarkdownPage";

function App() {
  return (
    <BrowserRouter>
      <Header />
      <main className="container">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<MarkdownPage filePath="/content/pages/about.md" />} />
          <Route path="/publications" element={<MarkdownPage filePath="/content/pages/publications.md" />} />
          <Route path="/talks" element={<MarkdownPage filePath="/content/pages/talks.md" />} />
        </Routes>
      </main>
    </BrowserRouter>
  );
}

export default App;