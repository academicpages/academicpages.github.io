// src/pages/Home.jsx
import React from 'react';
import { Link } from 'react-router-dom';

export default function Home() {
  return (
    <div className="home-container">
      <section className="bio-section">
        <h1>Haidong Chen</h1>
        <p className="subtitle">Director of Solution Architecture</p>
        <p>
          With over 7 years of experience in generative AI, infrastructure, data, security,
          and wallet systems. I focus on delivering innovative solutions that drive business
          value through cutting-edge technology. I have a proven track record of leading large
          teams and delivering successful projects with exceptional results.
        </p>
        <div className="action-links">
          <Link to="/about" className="btn">About Me</Link>
          <Link to="/talks" className="btn">Speaking</Link>
        </div>
      </section>

      <section className="news-section">
        <h2>Expertise</h2>
        <ul className="news-list">
          <li>
            <span className="news-date">Gen-AI</span>
            <span className="news-content">Agentic AI with RAG ReAct, LLM-ops, Cloud-Native solutions</span>
          </li>
          <li>
            <span className="news-date">Data</span>
            <span className="news-content">Data lakes, mid-platforms, governance, Flink, Spark, Doris, Hudi</span>
          </li>
          <li>
            <span className="news-date">Infrastructure</span>
            <span className="news-content">DevOps, SRE, Kubernetes, Docker, Terraform, CI/CD pipelines</span>
          </li>
          <li>
            <span className="news-date">Security</span>
            <span className="news-content">SOC, SIEM, WAF, Anti-DDoS, Compliance, GDPR, ISO 27001</span>
          </li>
          <li>
            <span className="news-date">Blockchain</span>
            <span className="news-content">Digital Wallet, Payment Gateway, Smart Contract, DeFi, NFT</span>
          </li>
        </ul>
      </section>

      <section className="achievements-section">
        <h2>Highlights</h2>
        <ul className="news-list">
          <li>
            <span className="news-date">Alibaba</span>
            <span className="news-content">Led a team of 40 people for World Cup Cricket ICC T20 Livestream event on Daraz, reducing hosting costs by 30%</span>
          </li>
          <li>
            <span className="news-date">AI Product</span>
            <span className="news-content">Built and released "Chat with PDF" (HaidongGPT) as an official product on Alibaba Cloud</span>
          </li>
          <li>
            <span className="news-date">Speaker</span>
            <span className="news-content">Frequent speaker at Cloud Expo Asia, Alibaba Cloud Developer Summit, and Alibaba Cloud Academy</span>
          </li>
        </ul>
      </section>
    </div>
  );
}