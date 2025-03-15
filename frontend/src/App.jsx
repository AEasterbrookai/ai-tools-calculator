import React, { useState } from 'react';
import { Chart } from 'react-chartjs-2';
import axios from 'axios';
import Slider from 'react-slider';

const App = () => {
  const [toolName, setToolName] = useState('');
  const [firmSize, setFirmSize] = useState('small');
  const [priorities, setPriorities] = useState({
    performance: 5,
    cost: 5,
    compliance: 5,
    integration: 5
  });
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleEvaluate = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await axios.post('http://localhost:5000/api/evaluate', {
        tool: toolName,
        firm_size: firmSize,
        priorities
      });
      setResults(response.data);
    } catch (err) {
      setError('Failed to evaluate tool. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const chartData = {
    labels: results ? Object.keys(results.sub_scores) : [],
    datasets: [{
      label: 'Scores',
      data: results ? Object.values(results.sub_scores) : [],
      backgroundColor: 'rgba(54, 162, 235, 0.2)',
      borderColor: 'rgba(54, 162, 235, 1)',
      borderWidth: 1
    }]
  };

  return (
    <div className="container">
      <h1>Legal AI Evaluation Calculator</h1>
      
      <div className="input-section">
        <div className="form-group">
          <label>Tool Name:</label>
          <input
            type="text"
            value={toolName}
            onChange={(e) => setToolName(e.target.value)}
            placeholder="Enter legal AI tool name"
          />
        </div>

        <div className="form-group">
          <label>Firm Size:</label>
          <select value={firmSize} onChange={(e) => setFirmSize(e.target.value)}>
            <option value="small">Small</option>
            <option value="medium">Medium</option>
            <option value="large">Large</option>
          </select>
        </div>

        {Object.entries(priorities).map(([key, value]) => (
          <div className="form-group" key={key}>
            <label>{key.charAt(0).toUpperCase() + key.slice(1)} Priority:</label>
            <Slider
              value={value}
              onChange={(val) => setPriorities(prev => ({ ...prev, [key]: val }))}
              min={1}
              max={10}
            />
            <span>{value}</span>
          </div>
        ))}
      </div>

      <button onClick={handleEvaluate} disabled={loading}>
        {loading ? 'Evaluating...' : 'Evaluate Tool'}
      </button>

      {error && <div className="error">{error}</div>}

      {results && (
        <div className="results-section">
          <h2>Evaluation Results for {results.tool}</h2>
          <div className="overall-score">
            Overall Score: {results.overall_score.toFixed(1)}
          </div>
          <div className="chart-container">
            <Chart type="bar" data={chartData} />
          </div>
        </div>
      )}
    </div>
  );
};

export default App;
