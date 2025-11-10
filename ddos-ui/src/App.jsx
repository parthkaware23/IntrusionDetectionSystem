import { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [status, setStatus] = useState(null);
  const [lastChecked, setLastChecked] = useState(new Date());

  useEffect(() => {
    const interval = setInterval(() => {
      axios
        .get("http://localhost:8000/predict")
        .then(res => {
          setStatus(res.data.prediction);
          setLastChecked(new Date());
        })
        .catch(err => console.error(err));
    }, 2000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="dashboard-container">
      <div className="grid-background"></div>

      <div className="content-wrapper">
        <div className="header">
          <h1
            className={`main-title ${
              status === 1 ? 'attack' : status === 0 ? 'secure' : 'scanning'
            }`}
          >
            NETWORK SENTINEL
          </h1>
          <p className="subtitle">REAL-TIME THREAT DETECTION SYSTEM</p>
        </div>

        <div
          className={`status-card ${
            status === 1 ? 'attack' : status === 0 ? 'secure' : 'scanning'
          }`}
        >
          <div className="scan-line"></div>

          <div className="icon-container">
            {status === 1 ? (
              <span className="icon attack-icon">⚠</span>
            ) : status === 0 ? (
              <span className="icon secure-icon">🛡</span>
            ) : (
              <span className="icon scanning-icon">📡</span>
            )}
          </div>

          <h2 className="status-text">
            {status === 1
              ? '🚨 DDoS ATTACK DETECTED'
              : status === 0
              ? '✅ SYSTEM SECURE'
              : '🔄 SCANNING NETWORK'}
          </h2>

          <div className="stats-grid">
            <div className="stat-item">
              <p className="stat-label">STATUS</p>
              <p className="stat-value">
                {status === 1
                  ? 'CRITICAL'
                  : status === 0
                  ? 'NORMAL'
                  : 'ACTIVE'}
              </p>
            </div>
            <div className="stat-item">
              <p className="stat-label">SCAN RATE</p>
              <p className="stat-value">2.0s</p>
            </div>
            <div className="stat-item">
              <p className="stat-label">LAST CHECK</p>
              <p className="stat-value">
                {lastChecked.toLocaleTimeString()}
              </p>
            </div>
          </div>
        </div>

        <div className="footer">
          <div className="footer-left">
            <div
              className={`status-indicator ${
                status === 1
                  ? 'attack'
                  : status === 0
                  ? 'secure'
                  : 'scanning'
              }`}
            ></div>
            <span>MONITORING ACTIVE</span>
          </div>
          <span>ML-POWERED DETECTION</span>
        </div>
      </div>
    </div>
  );
}

export default App;
