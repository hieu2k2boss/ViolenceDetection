// src/components/About.js

import React from "react";
import "../App.css";
import Footer from "./Footer";

const Camera = () => {
  return (
    <div className="Camera">
      <div style={{ display: "flex", justifyContent:"space-between" ,}}>
        <div
          style={{ borderRadius: "5px", borderWidth: 2, borderColor: "black"}}
        >
          <h2>Camera real time</h2>
          <img
            id="webcam-feed"
            src="http://127.0.0.1:8000/webcam_feed/"
            width="640px"
            height="480px"
          />
          <label>Vui lòng tải lại trang nếu không thấy hình</label>
        </div>
        <div
          style={{ borderRadius: "5px", borderWidth: 2, borderColor: "black" }}
        > <h2>Camera real time</h2>
          <img
            id="webcam-feed"
            src="http://127.0.0.1:8000/webcam_feed/"
            width="640px"
            height="480px"
          />
          <label>Vui lòng tải lại trang nếu không thấy hình</label>
        </div>
      </div>

      <Footer />
    </div>
  );
};

export default Camera;
