import React, { useState } from 'react';
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

  const [currentCardIndex, setCurrentCardIndex] = useState(0);

  const handleCardClick = () => {
    setCurrentCardIndex((prevIndex) => (prevIndex + 1) % data.length);
  };

  const currentCard = data[currentCardIndex];

  return (
    <div>
      <div className="flashcard" onClick={handleCardClick}>
        {currentCard.text}
      </div>
      <div className="counter">
        {currentCardIndex + 1}/{data.length}
      </div>
    </div>
  );
}

export default Flashcard;