import React, { useEffect, useState } from 'react';
import { getAllNews } from './api';

const NewsList = () => {
  const [news, setNews] = useState([]);

  useEffect(() => {
    const fetchNews = async () => {
      const data = await getAllNews();
      setNews(data);
    };
    fetchNews();
  }, []);

  return (
    <div>
      <h1>Latest News</h1>
      {news.map((article) => (
        <div key={article.id}>
          <h2>{article.headline}</h2>
          <p>{article.summary}</p>
          <a href={article.source_url} target="_blank" rel="noopener noreferrer">Read More</a>
        </div>
      ))}
    </div>
  );
};

export default NewsList;
