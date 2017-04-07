 function weather(x){
    var icon = "<img src='http://openweathermap.org/img/w/"+x['Dublin'][3]+".png'>";
    var temp = parseInt(x['Dublin'][0]- 273.15);
    var weather = icon + "<br> "+ x['Dublin'][2] + "<br>Temperature: " + temp +
    "<sup>o</sup>C<br> Windspeed: "+x['Dublin'][1] +" m/s<br> Last Update: "+x['Dublin'][4]+" minutes ago";

    document.getElementById("weather").innerHTML = weather;
}