// 

// src/App.jsx
import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import CategoryPage from './pages/CategoryPage';
import SearchResults from './pages/SearchResults';
import ArticleDetails from './pages/ArticleDetails';
import Loader from './components/Loader';
import './App.css';
import { fetchAllArticles } from './api';

const App = () => {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadArticles = async () => {
      try {
        const data = await fetchAllArticles();
        setArticles(data);
      } catch (error) {
        console.error('Error fetching articles:', error);
        setError('Failed to load articles. Please try again later.');
      } finally {
        setLoading(false);
      }
    };
    loadArticles();
  }, []);

  if (loading) return <Loader />;
  if (error) return <p className="error-message">{error}</p>;

  return (
    <Router>
      <div className="app-container">
        <Navbar />
        <Routes>
          <Route path="/" element={<Home articles={articles} />} />
          <Route path="/category/:category" element={<CategoryPage articles={articles} />} />
          <Route path="/search/:query" element={<SearchResults />} />
          <Route path="/article/:id" element={<ArticleDetails />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
