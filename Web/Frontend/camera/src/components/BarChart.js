import React from 'react';
import { Bar } from 'react-chartjs-2';

class BarChart extends React.Component {
    render() {
        const data = {
            labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
            datasets: [
                {
                    label: 'Sample Data',
                    backgroundColor: 'rgba(75,192,192,1)',
                    borderColor: 'rgba(0,0,0,1)',
                    borderWidth: 2,
                    data: [65, 59, 80, 81, 56, 55, 40]
                }
            ]
        };

        const options = {
            title: {
                display: true,
                text: 'Bar Chart Example',
                fontSize: 20
            },
            legend: {
                display: true,
                position: 'top'
            }
        };

        return (
            <div>
                <Bar
                    data={data}
                    options={options}
                />
            </div>
        );
    }
}

export default BarChart;