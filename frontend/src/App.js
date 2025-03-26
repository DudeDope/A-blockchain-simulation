
import React, { useState, useEffect } from 'react';

const App = () => {
  const [chain, setChain] = useState([]);
  const [transaction, setTransaction] = useState('');
  const [message, setMessage] = useState('');

  // Fetch the blockchain
  const fetchChain = async () => {
    const response = await fetch('http://localhost:5000/chain');
    const data = await response.json();
    setChain(data);
  };

  // Add transaction
  const addTransaction = async () => {
    const response = await fetch('http://localhost:5000/transaction', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ transaction }),
    });
    const result = await response.json();
    setMessage(result.message);
    fetchChain();
  };

  // Mine block
  const mineBlock = async () => {
    const response = await fetch('http://localhost:5000/mine', { method: 'POST' });
    const result = await response.json();
    setMessage(result.message || 'Block mined');
    fetchChain();
  };

  useEffect(() => {
    fetchChain();
  }, []);

  return (
    <div>
      <h1>Blockchain Viewer</h1>
      <h2>Blockchain</h2>
      <pre>{JSON.stringify(chain, null, 2)}</pre>
      <h2>Add Transaction</h2>
      <input
        type="text"
        value={transaction}
        onChange={(e) => setTransaction(e.target.value)}
      />
      <button onClick={addTransaction}>Add Transaction</button>
      <h2>Mine Block</h2>
      <button onClick={mineBlock}>Mine</button>
      {message && <p>{message}</p>}
    </div>
  );
};

export default App;
