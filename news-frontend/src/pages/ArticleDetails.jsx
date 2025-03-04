// // src/components/ArticleDetails.jsx
// import React, { useEffect, useState } from 'react';
// import { useParams } from 'react-router-dom';
// import '../styles/ArticleDetails.css';
// import api from '../api'; // Assuming you have an API utility for fetching data

// const ArticleDetails = () => {
//   const { id } = useParams();
//   const [article, setArticle] = useState(null);
//   const [loading, setLoading] = useState(true);
//   const [error, setError] = useState(null);

//   useEffect(() => {
//     const fetchArticle = async () => {
//       try {
//         const response = await api.get(`/news/${id}`);
//         setArticle(response.data);
//       } catch (err) {
//         setError('Failed to fetch article. Please try again later.');
//       } finally {
//         setLoading(false);
//       }
//     };
//     fetchArticle();
//   }, [id]);

//   if (loading) return <p className="loading">Loading article...</p>;
//   if (error) return <p className="error">{error}</p>;
//   if (!article) return <p className="not-found">Article not found.</p>;

//   const { headline, author, publishedDate, imageUrl, summary, content, sourceLink, category } = article;

//   return (
//     <div className="article-details-container">
//       <h1 className="article-title">{headline}</h1>
//       <p className="article-meta">
//         <span>{author || 'Unknown Author'}</span> | <span>{publishedDate || 'Unknown Date'}</span>
//       </p>
//       <img src={imageUrl} alt={headline} className="article-image" />
//       <span className="article-category">{category}</span>
//       <p className="article-summary">{summary}</p>
//       <div className="article-content">{content}</div>
//       {sourceLink && (
//         <a href={sourceLink} target="_blank" rel="noopener noreferrer" className="source-link">
//           Read Original Article
//         </a>
//       )}
//     </div>
//   );
// };

// export default ArticleDetails;

// src/pages/ArticleDetails.jsx
import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import "../styles/ArticleDetails.css";

const ArticleDetails = () => {
  const { id } = useParams(); // Extract news_id from URL
  const [article, setArticle] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchArticle = async () => {
      try {
        console.log("Fetching article with news_id:", id);
        const response = await axios.get(`http://localhost:5000/api/news/${id}`);
        setArticle(response.data);
      } catch (error) {
        console.error("Error fetching article:", error);
        setError("Article not found");
      } finally {
        setLoading(false);
      }
    };

    fetchArticle();
  }, [id]);

  if (loading) return <p>Loading article...</p>;
  if (error) return <p>{error}</p>;

  return (
    <div className="article-details-container">
      <h2>{article.headline}</h2>
      <img src={article.image_url} alt={article.headline} className="article-image" />
      <p>{article.content}</p>
    </div>
  );
};

export default ArticleDetails;

