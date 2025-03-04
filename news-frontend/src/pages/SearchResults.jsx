// // src/pages/SearchResults.jsx
// import React from 'react';
// import ArticleCard from '../components/ArticleCard';
// import '../styles/SearchResults.css';

// const SearchResults = ({ searchQuery, articles }) => {
//   return (
//     <div className="search-results-container">
//       <h1>Search Results for: "{searchQuery}"</h1>
//       {articles.length === 0 ? (
//         <p>No articles found. Try another search!</p>
//       ) : (
//         <div className="results-grid">
//           {articles.map((article) => (
//             <ArticleCard key={article.id} article={article} />
//           ))}
//         </div>
//       )}
//     </div>
//   );
// };

// export default SearchResults;

// src/pages/SearchResults.jsx
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import ArticleCard from '../components/ArticleCard';
import '../styles/SearchResults.css';

const SearchResults = () => {
  const { query } = useParams();
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchSearchResults = async () => {
      try {
        const response = await axios.get(`http://localhost:5000/api/news/search?q=${query}`);
        setResults(response.data);
      } catch (error) {
        console.error('Error fetching search results:', error);
        setError('No articles found for your search.');
      } finally {
        setLoading(false);
      }
    };
    fetchSearchResults();
  }, [query]);

  if (loading) return <p>Loading search results...</p>;
  if (error) return <p>{error}</p>;

  return (
    <div className="search-results-container">
      <h2>Search Results for: "{query}"</h2>
      {results.length === 0 ? (
        <p>No articles found.</p>
      ) : (
        <div className="article-list">
          {results.map((article) => (
            <ArticleCard key={article.id} article={article} />
          ))}
        </div>
      )}
    </div>
  );
};

export default SearchResults;

