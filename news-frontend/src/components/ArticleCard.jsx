// // src/components/ArticleCard.jsx
// import React from "react";
// import { Link } from "react-router-dom";
// import "../styles/ArticleCard.css";

// const ArticleCard = ({ article }) => {
//   const { id, headline, summary, image_url, category } = article;

//   return (
//     <div className="article-card">
//       <img src={image_url} alt={headline} className="article-image" />
//       <div className="article-content">
//         <span className="article-category">{category}</span>
//         <h2 className="article-headline">{headline}</h2>
//         <p className="article-summary">{summary}</p>
//         <Link to={`/news/${id}`} className="read-more">Read More</Link>
//       </div>
//     </div>
//   );
// };

// export default ArticleCard;

// src/components/ArticleCard.jsx
import React from "react";
import { useNavigate } from "react-router-dom";
import "../styles/ArticleCard.css";

const ArticleCard = ({ article }) => {
  const { id, headline, summary, image_url, category } = article;
  const navigate = useNavigate();

  // Navigate to article details page
  const handleReadMore = () => {
    navigate(`/article/${id}`);
  };

  return (
    <div className="article-card">
      <img src={image_url} alt={headline} className="article-image" />
      <div className="article-content">
        <span className="article-category">{category}</span>
        <h2 className="article-headline">{headline}</h2>
        <p className="article-summary">{summary}</p>
        <button onClick={handleReadMore} className="read-more-button">
          Read More
        </button>
      </div>
    </div>
  );
};

export default ArticleCard;
