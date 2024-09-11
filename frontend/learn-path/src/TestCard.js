import React from 'react';

const TestCard = ({ test }) => (
  <div className="test-card">
    <h2>Test #{test.id}</h2>
    <p><strong>Topic:</strong> {test.topic}</p>
    <p><strong>Number of Questions:</strong> {test.number_of_questions}</p>
    <p><strong>Difficulty:</strong> {test.difficulty}</p>
    <p><strong>Passing Score:</strong> {test.passing_score}%</p>
  </div>
);

export default TestCard;
