// Địa chỉ URL của API cần cập nhật
const apiUrl = "http://127.0.0.1:8000/MyAPI/";

// Dữ liệu mới cần cập nhật
const newData =     {
    "id": 1,
    "path_video": "H:/DaiHoc/DoAn/Code/ViolenceDetection/Video_Test/Video10.avi",
    "path_model": "H:/DaiHoc/DoAn/Code/ViolenceDetection/model/violence_mobile_net.h5"
};


const requestOptions = {
    method: 'PUT',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(newData)
};

// Hàm để cập nhật dữ liệu trong API
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
