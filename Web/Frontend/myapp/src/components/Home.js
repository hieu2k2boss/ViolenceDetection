import React, { useState, useEffect } from "react";
import SwipeableViews from "react-swipeable-views-react-18-fix";
import "../App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import Footer from "./Footer";
import Content from "./Content";

const Home = ({ handleClick }) => {
  const [index, setIndex] = useState(0);

  // Hàm này sẽ được gọi mỗi giây
  useEffect(() => {
    const interval = setInterval(() => {
      // Tăng index lên 1, hoặc quay lại 0 nếu đã ở slide cuối cùng
      setIndex((prevIndex) => (prevIndex + 1) % 3); // 3 là số lượng slide
    }, 5000); // 1000 milliseconds = 1 giây

    // Xóa interval khi component unmount
    return () => clearInterval(interval);
  }, []); // [] để chỉ gọi useEffect 1 lần khi component mount

  return (
    <div>
      <div className="centered">
        <SwipeableViews index={index} className="swiper">
          <div className="Slider" id="Slider1">
            <h1>Closed-circuit television - CCTV</h1>
            <label>
              hệ thống giám sát anh ninh giúp phát hiện những bất thường xảy ra
            </label>
            <button
              type="button"
              class="btn btn-primary"
              style={{ height: 40, width: 120 }}
              onClick={() => handleClick('about')}
            >
              Start camera
            </button>
          </div>
          <div className="Slider" id="Slider2">
            {" "}
            <h1>Closed-circuit television - CCTV</h1>
            <label>
              hệ thống giám sát anh ninh giúp phát hiện những bất thường xảy ra
            </label>
            <button
              type="button"
              class="btn btn-primary"
              style={{ height: 40, width: 120 }}
              onClick={() => handleClick('about')}
            >
              Start camera
            </button>
          </div>
          <div className="Slider" id="Slider3">
            {" "}
            <h1>Closed-circuit television - CCTV</h1>
            <label>
              hệ thống giám sát anh ninh giúp phát hiện những bất thường xảy ra
            </label>
            <button
              type="button"
              class="btn btn-primary"
              style={{ height: 40, width: 120 }}
              onClick={() => handleClick('about')}
            >
              Start camera
            </button>
          </div>
        </SwipeableViews>
      </div>
      <div>
        <h1>Hình ảnh demo</h1>
        <SwipeableViews index={index} className="swiper">
          <div className="Slider">
            <h2>Closed-circuit television - CCTV</h2>
          </div>
          <div className="Slider">Slide 2</div>
          <div className="Slider">Slide 3</div>
        </SwipeableViews>
      </div>
      <Content />

      <Footer />
    </div>
  );
};

export default Home;
