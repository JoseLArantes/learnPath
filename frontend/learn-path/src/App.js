import React, { useState, useEffect } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [tests, setTests] = useState([]);
  const [token, setToken] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/api-token-auth/', {
        username,
        password
      });
      setToken(response.data.token);
    } catch (error) {
      console.error('Login failed:', error);
    }
  };

  useEffect(() => {
    const fetchTests = async () => {
      if (!token) return;

      try {
        const response = await axios.get('http://localhost:8000/study/api/tests/', {
          headers: { Authorization: `Token ${token}` }
        });
        setTests(response.data);
      } catch (error) {
        console.error('Error fetching tests:', error);
      }
    };

    fetchTests();
  }, [token]);

  return (
    <div className="App">
      <header className="App-header">
        {!token ? (
          <form onSubmit={handleLogin}>
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              placeholder="Username"
            />
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Password"
            />
            <button type="submit">Login</button>
          </form>
        ) : (
          <>
            <h1>Available Tests</h1>
            <ul>
              {tests.map((test) => (
                  <li key={test.id}>{JSON.stringify(test)}</li>
              ))}
            </ul>
          </>
        )}
      </header>
    </div>
  );
}

export default App;