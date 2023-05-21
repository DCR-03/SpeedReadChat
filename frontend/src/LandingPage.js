import React, { useState } from 'react';

function FlashcardGenerator() {
  const [selectedOption, setSelectedOption] = useState('whole');
  const [startChapter, setStartChapter] = useState('');
  const [endChapter, setEndChapter] = useState('');
  const [selectedPDF, setSelectedPDF] = useState(null); 

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
    // Create a FormData object
    const formData = new FormData();

    // Append the selectedPDF to the FormData object
    formData.append('pdf', selectedPDF, 'textbook');

    // Append other data to the FormData object if needed
    formData.append('selectedOption', selectedOption);

    if (selectedOption === 'Certain') {
      formData.append('startChapter', startChapter);
      formData.append('endChapter', endChapter);
    }
    for (var pair of formData.entries()) {
      console.log(pair[0]+ ', ' + pair[1]); 
    }
   
    // Send the FormData object as part of a POST request to your Flask backend
    fetch('/your-flask-api-endpoint', {
      method: 'POST',
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        // Handle the response from the Flask backend
        console.log(data);
      })
      .catch((error) => {
        // Handle any errors
        console.error(error);
      });
  };

  const TestGenerate = (selectedOption, startChapter, endChapter) => {
    // Implement your flashcard generation logic here based on the selected options
    // Generate and return flashcards in the format of term: definition
  
    // Your flashcard generation logic goes here
    var flashcards = new Object();
    flashcards['term'] = 'definition'
    return flashcards;
  };

  const handlePDFUpload = (event) => {
    const file = event.target.files[0]; // Access the selected file
    setSelectedPDF(file); // Store the selected file in the state
  };

  return (
    <div>
      <h1>Speed Read Chat</h1>
      <div>
        <label htmlFor="pdfUpload">Upload PDF:</label>
        <input type="file" id="pdfUpload" accept=".pdf" onChange={handlePDFUpload}/>
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
       */
        // change state to flashcard 
      }
       
    </div>
  );
}

export default FlashcardGenerator;
