// import React, { useEffect, useState } from 'react';
// import { useParams } from 'react-router-dom';
// import ArticleCard from '../components/ArticleCard';
// import Loader from '../components/Loader';
// import '../styles/CategoryPage.css';
// import { fetchArticlesByCategory } from '../api';

// const CategoryPage = () => {
//   const { category } = useParams(); // Get category from URL params
//   const [articles, setArticles] = useState([]);
//   const [loading, setLoading] = useState(true);

//   useEffect(() => {
//     const getCategoryArticles = async () => {
//       try {
//         console.log(`Fetching articles for category: ${category}`);
//         const formattedCategory = category.toLowerCase();
//         const data = await fetchArticlesByCategory(formattedCategory);
//         console.log('Fetched Data:', data);
//         setArticles(data);
//       } catch (error) {
//         console.error(`Error fetching ${category} articles:`, error);
//       } finally {
//         setLoading(false);
//       }
//     };
//     getCategoryArticles();
//   }, [category]);

//   return (
//     <div>
//       <h1>{category.charAt(0).toUpperCase() + category.slice(1)} News</h1>
//       {loading ? (
//         <Loader />
//       ) : articles.length === 0 ? (
//         <p>No articles found for this category.</p>
//       ) : (
//         <div className="article-list">
//           {articles.map((article) => (
//             <ArticleCard key={article.id} article={article} />
//           ))}
//         </div>
//       )}
//     </div>
//   );
// };

// export default CategoryPage;


import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import ArticleCard from '../components/ArticleCard';
import Loader from '../components/Loader';
import '../styles/CategoryPage.css';
import { fetchArticlesByCategory } from '../api';

const CategoryPage = () => {
  const { category } = useParams(); // Get category from URL params
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const getCategoryArticles = async () => {
      try {
        console.log(`Fetching articles for category: ${category}`);
        const formattedCategory = category.toLowerCase();
        const data = await fetchArticlesByCategory(formattedCategory);
        console.log('Fetched Data:', data);

        // ⭐️ Filter out articles without a headline
        const filteredArticles = data.filter((article) => article.headline);
        
        setArticles(filteredArticles); // ⭐️ Update state with filtered articles
      } catch (error) {
        console.error(`Error fetching ${category} articles:`, error);
      } finally {
        setLoading(false);
      }
    };
    getCategoryArticles();
  }, [category]);

  return (
    <div>
      <h1>{category.charAt(0).toUpperCase() + category.slice(1)} News</h1>
      {loading ? (
        <Loader />
      ) : articles.length === 0 ? (
        <p>No articles found for this category.</p>
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

export default CategoryPage;
