// src/App.js
import { Navbar, Nav } from 'react-bootstrap';
import React, { useState } from "react";
import "./App.css";
import Contact from "./components/Contact";
import Home from "./components/Home";
import 'bootstrap/dist/css/bootstrap.min.css';
import Camera from './components/Camera';
import BarChart from './components/BarChart';

function App() {
  const [currentPage, setCurrentPage] = useState('home');

  const handleClick = (pageName) => {
    setCurrentPage(pageName);
  }

  return (

    <div>
    <Navbar bg="dark" variant="dark">
        <Navbar.Brand href="#home">         
          Navbar</Navbar.Brand>
        <Nav className="mr-auto" >
          <Nav.Link onClick={() => handleClick('home')}>Home</Nav.Link>
          <Nav.Link onClick={() => handleClick('about')}>Camera</Nav.Link>
          <Nav.Link onClick={() => handleClick('contact')}>Contact</Nav.Link>
        </Nav>
      </Navbar>
      <div className='Main'>
        {currentPage === 'home' && <Home handleClick={handleClick}/>}
        {currentPage === 'about' && <Camera />}
        {currentPage === 'contact' && <Contact />}
      </div> 
      
    </div>
     
  );
}

export default App;
