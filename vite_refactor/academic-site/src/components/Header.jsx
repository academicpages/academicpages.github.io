// src/components/Header.jsx
import React from 'react';
import { Link, useLocation } from 'react-router-dom';

export default function Header() {
  const location = useLocation();

  // Function to determine active status with exact matching for home
  const isActive = (path) => {
    if (path === '/') {
      return location.pathname === '/';
    }
    return location.pathname === path || location.pathname.startsWith(`${path}/`);
  };

  return (
    <header>
      <nav>
        <Link to="/" className={isActive('/') ? 'active' : ''}>Home</Link>
        <Link to="/about" className={isActive('/about') ? 'active' : ''}>About</Link>
        <Link to="/publications" className={isActive('/publications') ? 'active' : ''}>Publications</Link>
        <Link to="/talks" className={isActive('/talks') ? 'active' : ''}>Talks</Link>
        <Link to="/research" className={isActive('/research') ? 'active' : ''}>Research</Link>
      </nav>
    </header>
  );
}