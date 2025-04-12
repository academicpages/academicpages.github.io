// src/App.jsx
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Header from "./components/Header";
import Sidebar from "./components/Sidebar";
import Home from "./pages/Home";
import MarkdownPage from "./components/MarkdownPage";

function App() {
  return (
    <BrowserRouter>
      <Header />
      <div className="layout-container">
        <Sidebar />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<MarkdownPage filePath="/content/pages/about.md" />} />
            <Route path="/research" element={<MarkdownPage filePath="/content/pages/research.md" />} />
            <Route path="/publications" element={<MarkdownPage filePath="/content/pages/publications.md" />} />
            <Route path="/teaching" element={<MarkdownPage filePath="/content/pages/teaching.md" />} />
            <Route path="/talks" element={<MarkdownPage filePath="/content/pages/talks.md" />} />
            <Route path="/cv" element={<MarkdownPage filePath="/content/pages/cv.md" />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}

export default App;