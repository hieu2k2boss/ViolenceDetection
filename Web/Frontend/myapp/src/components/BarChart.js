import React, { useState, useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

const BarChart = () => {
  const [data, setData] = useState([
    { time: '00:00', people: 10 },
    { time: '03:00', people: 20 },
    { time: '06:00', people: 15 },
    { time: '09:00', people: 25 },
    { time: '12:00', people: 30 },
    { time: '15:00', people: 20 },
    { time: '18:00', people: 35 },
    { time: '21:00', people: 40 },
  ]);

  useEffect(() => {
    const interval = setInterval(() => {
      // Tạo dữ liệu mới ở đây, ví dụ: random số người
      const newDataPoint = {
        time: new Date().toLocaleTimeString(),
        people: Math.floor(Math.random() * 50) + 1, // Số người ngẫu nhiên từ 1 đến 50
      };
      // Cập nhật dữ liệu mới
      setData(prevData => [...prevData, newDataPoint]);
    }, 5000); // Thực hiện mỗi 5 giây

    return () => clearInterval(interval);
  }, []); // useEffect chỉ chạy một lần sau khi component được render

  return (
    <LineChart
      width={640}
      height={480}
      data={data}
    >
      <XAxis dataKey="time" />
      <YAxis />
      <CartesianGrid strokeDasharray="3 3" />
      <Tooltip />
      <Legend />
      <Line type="monotone" dataKey="people" stroke="#8884d8" activeDot={{ r: 8 }} />
    </LineChart>
  );
}

export default BarChart;
