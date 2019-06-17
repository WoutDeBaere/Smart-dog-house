'use strict';



const drawChart = function(data, labels) {
  let ctx = document.getElementById('myChart').getContext('2d');
const chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
      labels: labels,
      datasets: [{
          
          label: 'price',
          backgroundColor: 'lightgray',
          borderColor: 'green',
          data: data
      }]
  },
    
      

    // Configuration options go here
    options: {}
});
};


const init = function() {
  handleData('http://127.0.0.1:5500/iphone.json', processData);
};


const processData = function(data) {
  console.log(data);
  let converted_data = [];
  let converted_labels = [];

  for (const iphone of data) {
    converted_labels.push(iphone.unit);
    converted_data.push(iphone.price);
  }

  console.log(converted_data);

  const new_data = { labels: converted_labels, series: [converted_data] };
  const options = {
    
      scales: {
          yAxes: [{
              ticks: {
                  beginAtZero: true
              }
          }]
      }
  
  };

  drawChart(converted_data,converted_labels);
};


document.addEventListener('DOMContentLoaded', function() {
  console.info('DOM geladen');
  init()
});