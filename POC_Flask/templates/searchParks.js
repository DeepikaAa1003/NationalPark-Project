console.log("Inside Javascript");
console.log("Display data")
//console.log(list);

// var tbody = document.getElementById('tbody');

// for (var i = 0; i < Parks_data.length; i++) {
//     k+= '<tr>';
//     k+= '<td>' + Parks_data[i].fullName + '</td>';
//     k+= '<td>' + Parks_data[i].parkCode + '</td>';
//     k+= '<td>' + Parks_data[i].url + '</td>';
//     k+= '</tr>';
// }
list.map(item =>{
    console.log(item);
});

// document.getElementById('tbody').innerHTML = k;
// list.map(item => {
// var tbody = d3.select("tbody");
// var trow = d3.select("tbody").append("tr");
// Object.values(item).forEach(value => {

//     trow.append('td').text(value);
// });
// });