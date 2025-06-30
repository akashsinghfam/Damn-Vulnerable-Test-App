import React, { useState } from 'react';
import { fetchWeather } from './api';

// FAKE_SECRET_FOR_TESTING: sk_test_51H8EXAMPLESECRET

function storeToken(token) {
  localStorage.setItem('token', token);
}

function redirectToUrl() {
  const params = new URLSearchParams(window.location.search);
  const url = params.get('redirect');
  if (url) window.location.href = url;
}

function getRandomToken() {
  // Insecure randomness
  return Math.random().toString(36).substring(2);
}

function App() {
  const [city, setCity] = useState('');
  const [weather, setWeather] = useState(null);
  const [message, setMessage] = useState('');

  const handleSearch = () => {
    fetchWeather(city).then(data => setWeather(data));
  };

  const handleMessage = (e) => {
    setMessage(e.target.value);
  };

  return (
    <div>
      <h1>Vulnerable Weather App</h1>
      <input value={city} onChange={e => setCity(e.target.value)} placeholder="Enter city" />
      <button onClick={handleSearch}>Search</button>
      {weather && <pre>{JSON.stringify(weather, null, 2)}</pre>}
      <hr />
      <h2>Leave a message (XSS Demo)</h2>
      <input value={message} onChange={handleMessage} placeholder="Type anything..." />
      <div dangerouslySetInnerHTML={{ __html: message }} />
      <hr />
      <h2>CSRF Demo</h2>
      <form action="http://localhost:5000/hash" method="POST">
        <input name="password" placeholder="Password" />
        <button type="submit">Submit (no CSRF token)</button>
      </form>
      <button onClick={() => storeToken(getRandomToken())}>Store Random Token (insecure)</button>
      <button onClick={redirectToUrl}>Open Redirect (from ?redirect=)</button>
    </div>
  );
}

export default App; 