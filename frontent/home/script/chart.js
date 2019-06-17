'use strict';

const drawChart = function(data, options) {
    new Chartist.Line('.ct-chart', data, options);
  };

const drawDonut = function(data, options) {
    new Chartist.Pie('.ct-chart', {
        series: data
      }, {
        donut: true,
        donutWidth: 60,
        donutSolid: true,
        startAngle: 90,
        showLabel: true
      });
}


const generatechart = function(){
    let labels = ['bench','zetel','overig'];
    let values = [88000,44000,22000];
    
    console.log(labels);
    console.log(values);
    const options = {
      
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    
    };

  drawDonut(values,options);
};
    
const init = function(){
  weight = document.querySelector('#weight');
  getSocketConnection();
  livedata();
  generatechart(); 
}
document.addEventListener('DOMContentLoaded', function() {
    console.info('DOM geladen');
    init(); 
});

  