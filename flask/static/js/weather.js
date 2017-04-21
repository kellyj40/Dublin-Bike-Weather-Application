 function weather(x){
    var icon = "<img id='weather_icon' src='http://openweathermap.org/img/w/"+x['Dublin'][3]+".png'>";
    var temp = parseInt(x['Dublin'][0]- 273.15);
    var weather = "Dublin, Ireland   "+temp+"<sup>o</sup>C";
    document.getElementById("weather").innerHTML = weather;
    document.getElementById("weather_icon").innerHTML = icon;

}