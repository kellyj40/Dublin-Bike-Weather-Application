 function weather(x){
    var icon = "<img src='http://openweathermap.org/img/w/"+x[3]+".png'>";
    var temp = x[0]- 273.15;
    var weather = icon + "<br> "+ x[2] + "<br>Temperature: " + temp +
    "<sup>o</sup>C<br> Windspeed: "+x[1] +" m/s<br> Last Update: "+x[4]+" minutes ago";

    document.getElementById("weather").innerHTML = weather;
}