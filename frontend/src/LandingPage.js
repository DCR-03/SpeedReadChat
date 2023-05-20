import React, { useState } from 'react';

function FlashcardGenerator() {
  const [selectedOption, setSelectedOption] = useState('whole');
  const [startChapter, setStartChapter] = useState('');
  const [endChapter, setEndChapter] = useState('');

  const handleOptionChange = (event) => {
    setSelectedOption(event.target.value);
  };

  const handleStartChapterChange = (event) => {
    setStartChapter(event.target.value);
  };

  const handleEndChapterChange = (event) => {
    setEndChapter(event.target.value);
  };

  const handleGenerateFlashcards = () => {
    // Implement your flashcard generation logic here based on the selected options
    // You can use the selectedOption, startChapter, and endChapter values to generate flashcards
    // and display the preview in the component.
  };

  return (
    <div>
      <h1>Speed Read Chat</h1>
      <div>
        <label htmlFor="pdfUpload">Upload PDF:</label>
        <input type="file" id="pdfUpload" accept=".pdf" />
      </div>
      <div>
        <input
          type="radio"
          id="wholeTextbook"
          name="flashcardType"
          value="whole"
          checked={selectedOption === 'whole'}
          onChange={handleOptionChange}
        />
        <label htmlFor="wholeTextbook">Use Whole Textbook</label>
      </div>
      <div>
        <input
          type="radio"
          id="certainChapters"
          name="flashcardType"
          value="certain"
          checked={selectedOption === 'certain'}
          onChange={handleOptionChange}
        />
        <label htmlFor="certainChapters">Use Certain Chapters</label>
        {selectedOption === 'certain' && (
          <div>
            <label htmlFor="startChapter">Chapters</label>
            <input
              type="text"
              id="startChapter"
              value={startChapter}
              onChange={handleStartChapterChange}
            />
            <span>through</span>
            <input
              type="text"
              id="endChapter"
              value={endChapter}
              onChange={handleEndChapterChange}
            />
          </div>
        )}
      </div>
      <button onClick={handleGenerateFlashcards}>Generate</button>
      {/* 
      Display the flashcard preview generated on button click
      Call backend API function, pass in text
       */}
       
    </div>
  );
}

export default FlashcardGenerator;
