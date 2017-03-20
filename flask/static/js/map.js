function googleMap()
{
    var canvas= document.getElementById("home_map");
    var myCenter= new google.maps.LatLng(53.355122,-6.24922)
    var options= {center: myCenter, zoom:13}
    var map= new google.maps.Map(canvas,options);
    var mapLabel=new google.maps.InfoWindow({position: new google.maps.LatLng(53.356, -6.26)});
}