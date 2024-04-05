import React from "react";
import "../App.css";
import "bootstrap/dist/css/bootstrap.min.css";

const Content = () => {
  return (
    <div className="Content">
      <h1>Hệ thống giám sát an ninh</h1>
      <div
        style={{
          display: "flex",
          flexDirection: "row",
          justifyContent: "space-between",
          alignItems: "center",
        }}
      >
        <div class="card" style={{width: "18rem", margin:"50px"}}>
          <img
            class="card-img-top"
            src={"/manager.png"}
            alt="security image cap"
          />
          <div class="card-body">
            <h5 class="card-title">Manage</h5>
            <p class="card-text">
              Hệ thống được xây dựng với mục đích tự động hóa quá trình giám sát an ninh
            </p>

          </div>
        </div>
        <div class="card" style={{width: "18rem", margin:"50px"}}>
          <img
            class="card-img-top"
            src={"/chart.png"}
            alt="security image cap"
          />
          <div class="card-body">
            <h5 class="card-title">Statistics</h5>
            <p class="card-text">
              Some quick example text to build on the card title and make up the
              bulk of the card's content.
            </p>
  
          </div>
        </div>
        <div class="card" style={{width: "18rem", margin:"50px"}}>
          <img
            class="card-img-top"
            src={"/security.png"}
            alt="security image cap"
          />
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">
              Some quick example text to build on the card title and make up the
              bulk of the card's content.
            </p>
         
          </div>
        </div>
      </div>
    </div>
  );
};

export default Content;
