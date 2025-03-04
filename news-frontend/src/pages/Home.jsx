import React, { useEffect, useState } from 'react';
import ArticleCard from '../components/ArticleCard';
import Loader from '../components/Loader';
import '../styles/CategoryPage.css';
import { fetchAllArticles } from '../api';

const Home = () => {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const getArticles = async () => {
      try {
        const data = await fetchAllArticles();
        setArticles(data);
      } catch (error) {
        console.error('Error fetching articles:', error);
      } finally {
        setLoading(false);
      }
    };
    getArticles();
  }, []);

  return (
    <div>
      <h1>Latest News</h1>
      {loading ? (
        <Loader />
      ) : (
        <div className="article-list">
          {articles.map((article) => (
            <ArticleCard key={article.id} article={article} />
          ))}
        </div>
      )}
    </div>
  );
};

export default Home;
