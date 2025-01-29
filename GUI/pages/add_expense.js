import React, { useEffect, useState } from "react"

export default function AddExpense() {
    
  const [description, setDescription] = useState('');
  const [amount, setAmount] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    const expense = {
      description,
      amount: parseFloat(amount),
    };

    try {
      const response = await fetch('http://localhost:5002/expenses', {
        method: 'POST',
        body: JSON.stringify(expense),
      });

      alert(response.json)

      if (response.ok) {
        alert('Expense added successfully!');
        setDescription('');
        setAmount('');
      } else {
        alert('Failed to add expense.');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred while adding the expense.');
    }
  };

  return (
    <div className="max-w-md mx-auto mt-10 p-4 border rounded-lg shadow-md">
      <h1 className="text-xl font-bold mb-4">Add Expense</h1>
      <form onSubmit={handleSubmit}>
        <div className="mb-4">
          <label htmlFor="description" className="block text-sm font-medium mb-1">
            Expense Description
          </label>
          <input
            type="text"
            id="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            className="w-full p-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Enter expense description"
            required
          />
        </div>
        <div className="mb-4">
          <label htmlFor="amount" className="block text-sm font-medium mb-1">
            Amount
          </label>
          <input
            type="number"
            id="amount"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            className="w-full p-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Enter amount"
            required
            step="0.01"
          />
        </div>
        <button
          type="submit"
          className="w-full bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600 transition"
        >
          Add Expense
        </button>
      </form>
    </div>
  );
}
