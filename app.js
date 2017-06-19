const vm = new Vue({
  el: '#app',
  data(){
    return {}
  },
  template: `
    <div></div>
  `
}) 

function getCSV(){
  const req = new XMLHttpRequest();
  req.open("get", "ponta.csv", true);
  req.send(null);
  
  req.onload = function() {
    convertCSVtoArray(req.responseText);
  }
}

function convertCSVtoArray(str){
  let result = [];
  let tmp = str.split("\n");
  
  tmp.forEach(function(val, index){
    result[index] = tmp[index].split(',');
  });
  
  return result;
}

const dataArray = getCSV();








