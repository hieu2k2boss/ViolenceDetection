// scripts.js
window.onload = function() {
    var video = document.querySelector('video');

    video.onplay = function() {
        console.log('Video is playing');
    }

    video.onpause = function() {
        console.log('Video is paused');
    }
}



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



  var ctx = document.getElementById('salesChart').getContext('2d');
  var salesChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
      datasets: [{
        label: 'Sales',
        data: [1000, 1200, 1100, 1300, 1400, 1600, 1500],
        borderColor: 'rgb(54, 162, 235)',
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        tension: 0.4, // Điều chỉnh độ cong của đường
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true // Bắt đầu từ giá trị 0 ở trục y
        }
      }
    }
  });
