// src/components/Contact.js

import React from "react";
import Footer from "./Footer";
const Contact = () => {
  return (
    <div>
      <div
        style={{
          flexDirection: "row",
          display: "flex",
          marginTop: "50px",
          justifyContent: "center",
        }}
      >
        <img src={"/cong-nghe-ai-camera-1.jpg"} width="640px" height="500px" style={{borderRadius:"10px"}}/>
        <div style={{ margin: "40px" }}>
          <h1>About me</h1>
          <label>
            Nếu có vấn đề thắc mắc vui lòng liên hệ theo các địa chỉ bên dưới
          </label>
          <h5>Address: Cau Giay, Ha Noi City</h5>
          <h5>Email: hieupham2k2uet@gmail.com</h5>
          <h5>Website: https://github.com/hieu2k2boss</h5>
          <div
            style={{
              flexDirection: "column",
              display: "flex",
              marginTop: "50px",
              justifyContent: "center",
              alignItems: "center",
            }}
          >
            <a href="https://www.facebook.com/profile.php?id=100008664642659">
              <img src={"/facebook.png"} width="100px" height="100px" />
            </a>
          </div>
        </div>

      </div>

      <Footer/>
    </div>
  );
};

export default Contact;
