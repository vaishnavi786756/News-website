// src/index.jsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import './App.css'; // Ensure global styles are imported
import App from './App';
import reportWebVitals from './reportWebVitals';

// Create root and render the App component
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// Measure performance metrics (optional)
reportWebVitals();
