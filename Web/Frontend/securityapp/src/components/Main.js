import "../Css/Main.css";
import { useState } from "react";


function Main() {
    const [Path_Video, setPath_Video] = useState("");
    const [Path_Model, setPath_Model] = useState("H:/DaiHoc/DoAn/Code/ViolenceDetection/model/violence_mobile_net.h5");
    const [WebCam , setWebCam] = useState(false)

const handleFileInput = ()=>{
    document.getElementById('fileInput_Video').click();
}

const displayFileNameVideo = () =>{
    const input = document.getElementById("fileInput_Video");
    const fileName = input.files[0].name;
    const uploadText = document.querySelector(".upload-text");
    uploadText.textContent = fileName;
    setPath_Video("H:/DaiHoc/DoAn/Code/ViolenceDetection/Video_Test/"+fileName)
    console.log(Path_Video);
}

const handleFileInputModel = ()=>{
    document.getElementById('fileInput_Model').click();
}

const displayFileNameModel = () =>{
    const input = document.getElementById("fileInput_Model");
    const fileName = input.files[0].name;
    const uploadText = document.querySelector(".upload-text-model");
    uploadText.textContent = fileName;
    setPath_Model("H:/DaiHoc/DoAn/Code/ViolenceDetection/model/"+fileName)
    console.log(Path_Model);
}

const HandelAPI = ()=>{
    const apiUrl = "http://127.0.0.1:8000/MyAPI/";
    const newData =  {
      "id": 1,
      "path_video": Path_Video,
      "path_model": Path_Model
    };
    const requestOptions = {
      method: 'PUT',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify(newData)
    };
    async function updateApi() {
      try {
          // Gửi request PATCH để cập nhật thông tin
          const response = await fetch(apiUrl, requestOptions);
  
          // Kiểm tra mã trạng thái của response
          if (response.ok) {
              console.log("Cập nhật thành công!");
          } else {
              console.log("Cập nhật thất bại. Mã lỗi:", response.status);
          }
      } catch (error) {
          console.error("Đã xảy ra lỗi khi cập nhật:", error);
      }
    }
    updateApi();
}

const HandelWebCam = ()=>{
    setWebCam(true)
    console.log(WebCam)
}

  return (
    <div className="Main">
      <form action="/search" method="get">
        <input
          type="text"
          id="shortText"
          name="shortText"
          placeholder="Nhập gì đó"
        />
        <button type="submit">
          <img src="path_to_your_logo.png" alt="Tìm kiếm" />
        </button>
      </form>
      <div class="content">
        <div id="left">
          <div
            class="custom-upload"
            onClick={handleFileInput}
          >
            <i class="fas fa-cloud-upload-alt upload-icon"></i>
            <span class="upload-text">Chọn Video</span>
            <input type="file" id="fileInput_Video" onChange={displayFileNameVideo}/>
          </div>
          <div
            class="custom-upload"
            onClick={handleFileInputModel}
          >
            <i class="fas fa-cloud-upload-alt upload-icon"></i>
            <span class="upload-text-model">Chọn Model</span>
            <input type="file" id="fileInput_Model" onChange={displayFileNameModel}/>
          </div>
          <button onClick={HandelWebCam}>Bật Web cam</button>
          <button onClick={HandelAPI}>Submit</button>
        </div>
        <div id="center">
          {" "}
          <div id="webcam-feed">
            <img
              src="http://127.0.0.1:8000/webcam_feed/"
              height="350px"
              width="500px"
              alt="Webcam Feed"
            />
          </div>
        </div>
        <div id="right"></div>
      </div>
    </div>
  );
}

export default Main;
