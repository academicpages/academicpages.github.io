// src/pages/Home.jsx
import React from 'react';
import { Link } from 'react-router-dom';

export default function Home() {
  return (
    <div className="home-container">
      <section className="bio-section">
        <h1>Haidong Chen</h1>
        {/*<p className="subtitle">Associate Professor of Computer Science</p>*/}
        <p>
          My research focuses on data visualization, visual analytics, and human-computer
          interaction. I develop interactive visual analysis methods to help people explore,
          understand, and communicate data.
        </p>
        <div className="action-links">
          <Link to="/research" className="btn">Research</Link>
          <Link to="/publications" className="btn">Publications</Link>
        </div>
      </section>

      <section className="news-section">
        <h2>News</h2>
        <ul className="news-list">
          {/*<li>*/}
          {/*  <span className="news-date">June 2024</span>*/}
          {/*  <span className="news-content">Paper "Visual Analytics for Large-Scale Data" accepted at IEEE VIS 2024.</span>*/}
          {/*</li>*/}
          {/*<li>*/}
          {/*  <span className="news-date">May 2024</span>*/}
          {/*  <span className="news-content">Received the Outstanding Teaching Award for Spring 2024.</span>*/}
          {/*</li>*/}
          {/*<li>*/}
          {/*  <span className="news-date">April 2024</span>*/}
          {/*  <span className="news-content">Invited talk at Stanford University on "The Future of Visual Analytics".</span>*/}
          {/*</li>*/}
          {/*<li>*/}
          {/*  <span className="news-date">March 2024</span>*/}
          {/*  <span className="news-content">New research grant approved for project on "Interactive Visual Analysis for Scientific Data".</span>*/}
          {/*</li>*/}
        </ul>
      </section>
    </div>
  );
}