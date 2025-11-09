import { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [status, setStatus] = useState(null);

  useEffect(() => {
    const interval = setInterval(() => {
      axios.get("http://localhost:8000/predict")
        .then(res => setStatus(res.data.prediction))
        .catch(err => console.error(err));
    }, 2000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>DDoS Detection Dashboard</h1>
      {status === 1 ? (
        <h2 style={{ color: "red" }}>🚨 DDoS Attack Detected!</h2>
      ) : status === 0 ? (
        <h2 style={{ color: "green" }}>✅ Normal Traffic</h2>
      ) : (
        <h2>🔄 Checking...</h2>
      )}
    </div>
  );
}

export default App;