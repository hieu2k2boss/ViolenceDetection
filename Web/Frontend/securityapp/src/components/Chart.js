import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

const Chart = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/Result/');
        const jsonData = response.data;
        
        const newEntry = {
          time: jsonData[0].Date,
          number: jsonData[0].NumberPeople
        };

        setData(prevData => [...prevData, newEntry]);
        console.log(data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    // Fetch data initially
    fetchData();

    // Fetch data every 2 seconds
    const intervalId = setInterval(fetchData, 5000);

    // Clean up function to clear interval
    return () => clearInterval(intervalId);
  }, []); // Empty dependency array ensures effect is only run once

  return (
    <div>
      <h1>Số lượng người</h1>
      <BarChart width={600} height={300} data={data}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="time" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Bar dataKey="number" fill="#8884d8" />
      </BarChart>
    </div>
  );
};

export default Chart;