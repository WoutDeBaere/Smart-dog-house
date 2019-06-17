'use strict';

const drawChart = function(data, options) {
  new Chartist.Line('.ct-chart', data, options);
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
    width: '100%',
    height: '400px',
    low: 350,
    high: 1150,
    lineSmooth: Chartist.Interpolation.cardinal({ tension: 0.2 })
  };

  drawChart(new_data, options);
};

const init = function() {
  handleData('http://127.0.0.1:5500/Chartist_start.js/iphone.json', processData);
};

document.addEventListener('DOMContentLoaded', function() {
  console.info('DOM geladen');
  init();
});
