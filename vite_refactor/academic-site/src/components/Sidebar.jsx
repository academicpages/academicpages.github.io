// src/components/Sidebar.jsx
import React from 'react';

export default function Sidebar() {
  return (
    <div className="sidebar">
      <div className="sidebar-content">
        <img
          src="/profile.png"
          alt="Haidong Chen"
          className="profile-image"
          onError={(e) => e.target.src = 'https://via.placeholder.com/200'}
        />
        <h2>Haidong Chen</h2>
        <p className="title">Director of Solution Architecture</p>
        <p className="bio-text">
          Focused on Gen-AI solutions, E-commerce Industry Solutions,
          Cloud Native, Data Infrastructure, and Web3.0 technologies.
        </p>

        <div className="social-links">
          <a href="https://github.com/daviddhc20120601" target="_blank" rel="noopener noreferrer" className="social-link">
            <i className="social-icon github-icon"></i>
            <span>GitHub</span>
          </a>
          <a href="https://www.linkedin.com/in/davidhaidongchen/" target="_blank" rel="noopener noreferrer" className="social-link">
            <i className="social-icon linkedin-icon"></i>
            <span>LinkedIn</span>
          </a>
        </div>
      </div>
    </div>
  );
}