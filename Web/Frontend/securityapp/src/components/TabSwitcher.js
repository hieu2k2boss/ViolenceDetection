import React, { useState } from "react";
import Chart from "./Chart";
import "../Css/App.css";
import Main from "./Main";
function TabSwitcher() {
  const [activeTab, setActiveTab] = useState(1);

  const handleTabChange = (tabNumber) => {
    setActiveTab(tabNumber);
  };

  return (
    <div>
      <div className="tab">
        <button
          className={activeTab === 1 ? "active" : ""}
          onClick={() => handleTabChange(1)}
        >
          Theo dõi CCTV
        </button>
        <button
          className={activeTab === 2 ? "active" : ""}
          onClick={() => handleTabChange(2)}
        >
          Lượng người ra vào
        </button>
        <button
          className={activeTab === 3 ? "active" : ""}
          onClick={() => handleTabChange(3)}
        >
          Image
        </button>
      </div>
      <div className="tab-content">
        {activeTab === 1 && <Main/>}
        {activeTab === 2 && <Chart />}
        {activeTab === 3 && <p>Content for Tab 3</p>}
      </div>
    </div>
  );
}

export default TabSwitcher;
