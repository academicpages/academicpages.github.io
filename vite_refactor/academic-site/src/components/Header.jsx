// src/components/Header.jsx
import React from 'react';
import { Link } from 'react-router-dom';

export default function Header() {
  return (
    <header>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
        <Link to="/publications">Publications</Link>
        <Link to="/talks">Talks</Link>
      </nav>
    </header>
  );
}