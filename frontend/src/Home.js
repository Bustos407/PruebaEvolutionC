// src/Home.js

import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Home = () => {
  const [message, setMessage] = useState('');
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchMessage = async () => {
      try {
        const response = await axios.get('http://localhost:5000/api/test');
        setMessage(response.data.message);
      } catch (err) {
        setError(err.message);
      }
    };

    fetchMessage();
  }, []);

  return (
    <div>
      <h1>Página Principal</h1>
      {error && <p>Error: {error}</p>}
      {message && <p>{message}</p>}
    </div>
  );
};

export default Home;
