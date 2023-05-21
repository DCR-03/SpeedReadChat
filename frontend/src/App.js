import logo from './logo.svg';
import './App.css';
import LandingPage from './LandingPage';
import Flashcard from './Flashcard'
import React from 'react'
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';


function App() {
  return (
    <Router>
    <div className="App">
    <Routes>
          <Route exact path="/" element={<LandingPage/>}/>
          <Route exact path="/frontend/src/Flashcard.js" element={<Flashcard/>}/>
        </Routes>
    </div>
    </Router>
  );
}

export default App;
