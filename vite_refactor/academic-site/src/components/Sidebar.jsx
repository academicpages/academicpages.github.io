// src/components/Sidebar.jsx
import React from 'react';

export default function Sidebar() {
  return (
    <div className="sidebar">
      <div className="sidebar-content">
        <img
          src="/profile.png"
          alt="Profile"
          className="profile-image"
          onError={(e) => e.target.src = 'https://via.placeholder.com/200'}
        />
        <h2>Haidong Chen</h2>
        <p className="title">AI engineer</p>
          <p className="department">Haidong (David) Chen focuses on AIGC(Gen-AI) solutions and includes but not restricted to E-commerce Industry Solutions and Compliance, Cloud Native, and Data and Web3.0.</p>
        {/*<p className="department">Department of Computer Science</p>*/}
        {/*<p className="university">University of Science and Technology of China</p>*/}

        {/*<div className="contact-info">*/}
        {/*  <p><strong>Email:</strong> hchen@example.edu</p>*/}
        {/*  <p><strong>Office:</strong> Science Building, Room 3112</p>*/}
        {/*  <p><strong>Address:</strong><br />*/}
        {/*     Department of Computer Science<br />*/}
        {/*     University of Science and Technology<br />*/}
        {/*     Hefei, Anhui 230026, China</p>*/}
        {/*</div>*/}

        <div className="social-links">
          <a href="https://github.com/" target="_blank" rel="noopener noreferrer">GitHub</a>
            <a href="">linkedin</a>
          {/*<a href="https://scholar.google.com/" target="_blank" rel="noopener noreferrer">Google Scholar</a>*/}
          {/*<a href="/files/cv.pdf" target="_blank" rel="noopener noreferrer">CV</a>*/}
        </div>
      </div>
    </div>
  );
}