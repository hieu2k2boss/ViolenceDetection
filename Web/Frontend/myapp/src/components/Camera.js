// src/components/About.js

import React from "react";
import "../App.css";
import Footer from "./Footer";
import BarChart from "./BarChart"
const Camera = () => {
  return (
    <div className="Camera">
      <div style={{ display: "flex", justifyContent:"space-between", padding:"50px" ,}}>
        <div
          style={{ borderRadius: "5px", borderWidth: 2, borderColor: "black"}}
        >
          <h2>Camera real time</h2>
          <img
            id="webcam-feed"
            src="http://127.0.0.1:8000/webcam_feed/"
            width="640px"
            height="480px"
            style={{borderRadius:"5px"}}
          />
          
        </div>
        <div
          style={{ borderRadius: "5px", borderWidth: 2, borderColor: "black", display:"flex",flexDirection:"column" }}
        > 
        <h2>Lưu lượng người</h2>
          <BarChart/>
        </div>
        
      </div>

      <Footer />
    </div>
  );
};

export default Camera;



