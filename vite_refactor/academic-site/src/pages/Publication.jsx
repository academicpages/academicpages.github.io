// src/pages/Publication.jsx
import React from 'react';
import { useParams } from 'react-router-dom';
import MarkdownPage from '../components/MarkdownPage';

export default function Publication() {
    const { id } = useParams();
    return <MarkdownPage filePath={`/content/publications/${id}.md`} />;
}
