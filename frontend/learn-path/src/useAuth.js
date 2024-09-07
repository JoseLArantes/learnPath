import { useState, useEffect } from 'react';

export const useAuth = () => {
  const [token, setToken] = useState('');

  const storeToken = (newToken) => {
    sessionStorage.setItem('authToken', newToken);
    setToken(newToken);
  };

  const getStoredToken = () => {
    return sessionStorage.getItem('authToken');
  };

  const clearToken = () => {
    sessionStorage.removeItem('authToken');
    setToken('');
  };

  useEffect(() => {
    const storedToken = getStoredToken();
    if (storedToken) {
      setToken(storedToken);
    }
  }, []);

  return { token, storeToken, clearToken };
};
