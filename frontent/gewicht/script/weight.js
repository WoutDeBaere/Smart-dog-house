'use strict';

let socket
let weight
let min
let sec
let duur
console.log("piemel")

let lanIP = '169.254.10.1';
const getSocketConnection = function(){
    socket = io(`http://${lanIP}:5000`);

    setInterval(livedata, 5500);

    socket.on('giveweight',function(data){
        console.log(data)
        console.log(weight)
        min = Math.floor(data/60)
        sec = data%60
        duur = "min: " + min + " sec: " + sec
        weight.innerHTML = duur;
    });
};
const livedata = function(){
    socket.emit('getweight');
};

const init = function(){
    weight = document.querySelector('#weight');
    getSocketConnection();
    livedata();
}

// const drawChart = function(data, options) {
//    new Chartist.Line('.ct-chart', data, options);
//  };

// const drawChart= function(data, options) {
//     new Chartist.Line('.ct-chart', {
//         labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
//         series: [
//           [12, 9, 7, 8, 5],
//           [2, 1, 3.5, 7, 3],
//           [1, 3, 4, 5, 6]
//         ]
//       }, {
//         fullWidth: true,
//         chartPadding: {
//           right: 40
//         }
//       });
//     }
// const 

// const generatechart = function(){
//     let labels = ['bench','zetel','overig'];
//     let values = ['18000','54000','14400'];
    
//     console.log(labels);
//     console.log(values);
//     const options = {
      
//         scales: {
//             yAxes: [{
//                 ticks: {
//                     beginAtZero: true
//                 }
//             }]
//         }
    
//     };

//   drawChart(values,options);
// };
    

document.addEventListener('DOMContentLoaded', function() {
    console.info('DOM geladen');
    init();  
}); 