import React, { useState, useEffect } from 'react';
import './App.css';
import axios from 'axios';
import { useAuth } from './useAuth';

function App() {
  const { token, storeToken } = useAuth();
  const [tests, setTests] = useState([]);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/api-token-auth/', {
        username,
        password
      });
      storeToken(response.data.token);
    } catch (error) {
      console.error('Login failed:', error.response ? error.response.data : error.message);
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
            <div className="tests-container">
              {tests.map((test) => (
                <div key={test.id} className="test-card">
                  <h2>Test #{test.id}</h2>
                  <p><strong>Topic:</strong> {test.topic}</p>
                  <p><strong>Number of Questions:</strong> {test.number_of_questions}</p>
                  <p><strong>Difficulty:</strong> {test.difficulty}</p>
                  <p><strong>Passing Score:</strong> {test.passing_score}%</p>
                </div>
              ))}
            </div>
          </>
        )}
      </header>
    </div>
  );
}

export default App;
