import React from 'react';
import './Flashcard.css';

function Flashcard() {
  // Implement your flashcard generation logic here based on the text passed to the component
  // You can use the text value to generate and display a flashcard
  console.log('display flashcards')
  const data = [
    { text: 'Flashcard 1' },
    { text: 'Flashcard 2' },
    { text: 'Flashcard 3' },
  ];

  return (
    <div>
      {data.map((card, index) => (
        <div key={index} className="flashcard">
          {card.text}
        </div>
      ))}
    </div>
  );
}

export default Flashcard;