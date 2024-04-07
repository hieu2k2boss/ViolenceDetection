import React from "react";
import "../App.css"

function Footer() {
  return (
    <footer
      className="footer bg-dark text-white"
      style={{ marginTop: "50px", height: "100px" }}
    >
      <div
        style={{
          display: "flex",
          flexDirection: "row",
          justifyContent: "space-between",
          alignItems:"center"
        }}
      >
        <div  className="FooterRight">
        <a href="https://uet.vnu.edu.vn/">
            <img src={"/LogoUet.png"} width="50px" height="50px" />
          </a>
        </div>
        <div>
          <span> © 2024 All rights reserved</span>
        </div>
        <div
          style={{
            display: "flex",
            flexDirection: "row",
            justifyContent: "space-between",
            alignItems:"center",
           
          }}
          className="FooterRight"
        >

          <a href="https://www.facebook.com/profile.php?id=100008664642659">
            <img src={"/facebook.png"} width="50px" height="50px" />
          </a>
          <a href="https://github.com/hieu2k2boss">
            <img src={"/LogoGit.png"} width="50px" height="50px" />
          </a>
        </div>
      </div>
    </footer>
  );
}

export default Footer;
