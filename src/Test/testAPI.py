import requests
import time

def fetch_data_from_api(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            print("Error:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

def main():
    api_url = "http://127.0.0.1:8000/Result/"
    
    data = fetch_data_from_api(api_url)
    if data:
        print("Data:", data[0]['path_video'])
        if (data[0]['path_video'] =="0"):
            print("Bật Cam")
        if (data[0]['path_video'] =="0"):
            print("Bật Video")
        
        # Chờ 2 giây trước khi gửi yêu cầu tiếp theo
        time.sleep(2)
if __name__ == "__main__":
    main()
