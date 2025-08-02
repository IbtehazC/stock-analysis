import React, { useState, useEffect } from 'react';
import './index.css';

function App() {
  const [stocks, setStocks] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch stock data from backend
    fetch('http://localhost:8000/api/stocks')
      .then(res => res.json())
      .then(data => {
        setStocks(data.stocks);
        setLoading(false);
      })
      .catch(err => {
        console.error('Failed to fetch stocks:', err);
        setLoading(false);
      });
  }, []);

  return (
    <div className="min-h-screen bg-gray-900 text-white">
      <header className="bg-gray-800 shadow-lg">
        <div className="container mx-auto px-4 py-6">
          <h1 className="text-3xl font-bold">ASX Analytics Dashboard</h1>
        </div>
      </header>
      <main className="container mx-auto px-4 py-8">
        {loading ? (
          <div className="text-center">Loading...</div>
        ) : (
          <div className="grid gap-4">
            <h2 className="text-xl mb-4">ASX Stock Prices</h2>
            {stocks.map(stock => (
              <div key={stock.code} className="bg-gray-800 p-4 rounded">
                <div className="flex justify-between">
                  <span className="font-semibold">{stock.code} - {stock.name}</span>
                  <span className="text-green-400">${stock.price}</span>
                </div>
              </div>
            ))}
          </div>
        )}
      </main>
    </div>
  );
}

export default App;