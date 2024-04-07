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
              Thống kê lượng người ra vào tại các thời điểm. Từ đó đưa ra các chính sách, chiến lược phù hợp.
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
              Hệ thống giúp phát hiện các hành vi bạo lực, giúp ngăn ngừa sớm các nguy hiểm. 
            </p>

          </div>
        </div>
      </div>
    </div>
  );
};

export default Content;
