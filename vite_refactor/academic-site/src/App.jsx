// src/App.jsx
import { HashRouter as Router, Routes, Route } from "react-router-dom";
import Header from "./components/Header";
import Sidebar from "./components/Sidebar";
import Home from "./pages/Home";
import Publications from "./pages/Publications";
import Publication from "./pages/Publication";
import Talks from "./pages/Talks";
import Talk from "./pages/Talk";
import MarkdownPage from "./components/MarkdownPage";
import React from "react";

function App() {
  return (
    <Router>
      <div className="app">
        <Header />
        <div className="layout-container">
          <Sidebar />
          <main className="main-content">
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/about" element={<MarkdownPage filePath="/content/pages/about.md" />} />
              <Route path="/research" element={<MarkdownPage filePath="/content/pages/research.md" />} />
              <Route path="/publications" element={<Publications />} />
              <Route path="/publication/:id" element={<Publication />} />
              <Route path="/talks" element={<Talks />} />
              <Route path="/talk/:id" element={<Talk />} />
              <Route path="*" element={<div>Page not found</div>} />
            </Routes>
          </main>
        </div>
      </div>
    </Router>
  );
}

export default App;