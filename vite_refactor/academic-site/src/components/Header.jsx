// src/components/Header.jsx
import React from 'react';
import { Link, useLocation } from 'react-router-dom';

export default function Header() {
  const location = useLocation();

  return (
    <header>
      <nav>
        <Link to="/" className={location.pathname === '/' ? 'active' : ''}>Home</Link>
        <Link to="/about" className={location.pathname === '/about' ? 'active' : ''}>About</Link>
        <Link to="/research" className={location.pathname === '/research' ? 'active' : ''}>Research</Link>
        <Link to="/publications" className={location.pathname === '/publications' ? 'active' : ''}>Publications</Link>
        <Link to="/teaching" className={location.pathname === '/teaching' ? 'active' : ''}>Teaching</Link>
        <Link to="/talks" className={location.pathname === '/talks' ? 'active' : ''}>Talks</Link>
        <Link to="/cv" className={location.pathname === '/cv' ? 'active' : ''}>CV</Link>
      </nav>
    </header>
  );
}