// scripts.js
console.log("hello")


window.onload = function () {
  var video = document.querySelector("video");

  video.onplay = function () {
    console.log("Video is playing");
  };

  video.onpause = function () {
    console.log("Video is paused");
  };
};

function openTab(evt, tabName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].classList.remove("active");
  }
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.classList.add("active");
}

// Open the default tab on page load
document.getElementById("tab1").style.display = "block";
document.getElementsByClassName("tablink")[0].classList.add("active");



var data = {
  labels: [],
  datasets: [
    {
      label: "Random Data 1",
      backgroundColor: "rgba(255, 99, 132, 0.2)",
      borderColor: "rgba(255, 99, 132, 1)",
      borderWidth: 1,
      data: [],
    },
    {
      label: "Random Data 2",
      backgroundColor: "rgba(54, 162, 235, 0.2)",
      borderColor: "rgba(54, 162, 235, 1)",
      borderWidth: 1,
      data: [],
    },
  ],
};

// Khởi tạo biểu đồ
var ctx = document.getElementById("myChart").getContext("2d");
var myChart = new Chart(ctx, {
  type: "line",
  data: data,
  options: {
    responsive: true,
    scales: {
      y: {
        scaleLabel: {
          display: true,
          labelString: "Random Number",
        },
      },
    },
  },
});

// Hàm cập nhật dữ liệu
function updateData() {
  // Thêm thời gian hiện tại vào mảng labels
  data.labels.push(new Date().toLocaleTimeString());
  // Thêm số ngẫu nhiên vào mảng data
  data.datasets.forEach((dataset) => {
    dataset.data.push(Math.random());
  });
  // Giới hạn số lượng dữ liệu hiển thị trên biểu đồ (vd: chỉ hiển thị 10 điểm dữ liệu gần nhất)
  const maxLen = 10;
  if (data.labels.length > maxLen) {
    data.labels.shift(); // Xóa phần tử đầu tiên trong mảng labels
    data.datasets.forEach((dataset) => {
      dataset.data.shift(); // Xóa phần tử đầu tiên trong mảng data
    });
  }
  // Cập nhật biểu đồ
  myChart.update();
}
// Cập nhật dữ liệu mỗi 2 giây
setInterval(updateData, 2000);

function displayFileName() {
  const input = document.getElementById("fileInput");
  const fileName = input.files[0].name;
  const uploadText = document.querySelector(".upload-text");
  uploadText.textContent = fileName;
  var file = fileName.substring(fileName.lastIndexOf("\\") + 1); // Sử dụng substring
  console.log(fileName);

}

function updateSliderValue() {
  var slider = document.getElementById("mySlider");
  var output = document.getElementById("sliderValue");
  console.log(slider)
  output.textContent = slider.value;
}

