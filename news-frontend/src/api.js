// import axios from 'axios';

// const API_URL = 'http://localhost:5000/api/news';

// // Fetch all articles
// export const fetchAllArticles = async () => {
//   try {
//     const response = await axios.get(API_URL);
//     return response.data;
//   } catch (error) {
//     console.error('Error fetching articles:', error);
//     return [];
//   }
// };

// // Fetch articles by category
// export const fetchArticlesByCategory = async (category) => {
//   try {
//     const response = await axios.get(`${API_URL}/category/${category}`);
//     return response.data;
//   } catch (error) {
//     console.error(`Error fetching ${category} articles:`, error);
//     return [];
//   }
// };

// // Search news articles
// export const searchNews = async (query) => {
//   try {
//     const response = await axios.get(`${API_URL}/search`, {
//       params: { q: query },
//     });
//     return response.data;
//   } catch (error) {
//     console.error('Error searching news:', error);
//     return [];
//   }
// };


import axios from 'axios';

const API_URL = 'http://localhost:5000/api/news';

// Fetch all articles
export const fetchAllArticles = async () => {
  try {
    const response = await axios.get(API_URL);
    return response.data;
  } catch (error) {
    console.error('Error fetching articles:', error);
    return [];
  }
};

// Fetch articles by category
export const fetchArticlesByCategory = async (category) => {
  try {
    const response = await axios.get(`${API_URL}/category/${category}`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching ${category} articles:`, error);
    return [];
  }
};

// Search news articles
export const searchNews = async (query) => {
  try {
    const response = await axios.get(`${API_URL}/search`, {
      params: { q: query },
    });
    return response.data;
  } catch (error) {
    console.error('Error searching news:', error);
    return [];
  }
};

// Fetch article by ID
export const fetchArticleById = async (id) => {
  try {
    const response = await axios.get(`${API_URL}/${id}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching article by ID:', error);
    return null;
  }
};
const api = {
  fetchAllArticles,
  fetchArticlesByCategory,
  searchNews,
  fetchArticleById,
};

export default api;
