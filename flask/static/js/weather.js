 function weather(x){
    var icon = "<img src='http://openweathermap.org/img/w/"+x['Dublin'][3]+".png'>";
    var temp = parseInt(x['Dublin'][0]- 273.15);
    var weather = "<table><tr><td>Current Weather</td><td id='weather_icon_cell'>"+icon+"</td></tr><tr><td>Temperature: </td><td>" + temp +
    "<sup>o</sup>C</td></tr><tr><td>Last Update: </td><td>"+x['Dublin'][4]+" minutes ago</td></tr><table>";

    document.getElementById("weather").innerHTML = weather;
}