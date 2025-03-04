// import React from 'react';
// import { Link } from 'react-router-dom';
// import '../styles/Navbar.css';

// const Navbar = () => {
//   return (
//     <nav className="navbar">
//       <div className="navbar-logo">
//         <Link to="/">News Website</Link>
//       </div>
//       <ul className="navbar-links">
//         <li><Link to="/category/politics">Politics</Link></li>
//         <li><Link to="/category/innovation">Innovation</Link></li>
//         <li><Link to="/category/culture">Culture</Link></li>
//         <li><Link to="/category/travel">Travel</Link></li>
//         <li><Link to="/category/arts">Arts</Link></li>
//         <li><Link to="/category/business">Business</Link></li>
//       </ul>
//     </nav>
//   );
// };

// export default Navbar;

// import React, { useState } from 'react';
// import { Link, useNavigate } from 'react-router-dom';
// import '../styles/Navbar.css';

// const Navbar = () => {
//   const [searchQuery, setSearchQuery] = useState('');
//   const navigate = useNavigate();

//   // Handle search submission
//   const handleSearch = (e) => {
//     e.preventDefault();
//     if (searchQuery.trim()) {
//       navigate(`/search/${searchQuery}`);
//       setSearchQuery('');
//     }
//   };

//   return (
//     <nav className="navbar">
//       <div className="navbar-logo">
//         <Link to="/">News Website</Link>
//       </div>
//       <ul className="navbar-links">
//         <li><Link to="/category/politics">Politics</Link></li>
//         <li><Link to="/category/innovation">Innovation</Link></li>
//         <li><Link to="/category/culture">Culture</Link></li>
//         <li><Link to="/category/travel">Travel</Link></li>
//         <li><Link to="/category/arts">Arts</Link></li>
//         <li><Link to="/category/business">Business</Link></li>
//       </ul>

//       {/* Search Form */}
//       <form className="navbar-search" onSubmit={handleSearch}>
//         <input
//           type="text"
//           value={searchQuery}
//           onChange={(e) => setSearchQuery(e.target.value)}
//           placeholder="Search news..."
//           required
//         />
//         <button type="submit">🔍</button>
//       </form>
//     </nav>
//   );
// };

// export default Navbar;

// src/components/Navbar.jsx
import React, { useState } from 'react'; 
import { Link, useNavigate } from 'react-router-dom';
import '../styles/Navbar.css';

const Navbar = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const navigate = useNavigate();

  const handleSearch = (e) => {
    e.preventDefault();
    if (searchQuery.trim()) {
      navigate(`/search/${searchQuery}`);
    }
  };

  return (
    <nav className="navbar">
      <div className="navbar-logo">
        <h2>Times News</h2>
      </div>

      <ul className="navbar-links">
        <li><Link to="/">Home</Link></li>
        <li><Link to="/category/politics">Politics</Link></li>
        <li><Link to="/category/innovation">Innovation</Link></li>
        <li><Link to="/category/culture">Culture</Link></li>
        <li><Link to="/category/travel">Travel</Link></li>
        <li><Link to="/category/business">Business</Link></li>
      </ul>

      <form onSubmit={handleSearch} className="search-form">
        <input
          type="text"
          placeholder="Search articles..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
        />
        <button type="submit">Search</button>
      </form>
    </nav>
  );
};

export default Navbar;
