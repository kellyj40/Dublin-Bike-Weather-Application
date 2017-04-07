function googleMap(){
            var canvas= document.getElementById("home_map");
            var myCenter= new google.maps.LatLng(53.3473,-6.2588);
            var myStyles =[{featureType: "poi", elementType: "labels", stylers: [{ visibility: "off" }]}];
            var options= {center: myCenter, zoom:13, styles: myStyles};
            var map= new google.maps.Map(canvas,options);
            var markerColour="";
            var markers=[];

            setMarkers(-1);

            function setMarkers(selected){ <!--Function for adding markers to map based on occupancy and selected status-->
                {% for item in locations %} <!-- setting the colour for the markers based on number of available bikes -->
                    if( {{ current_data[item[0]|string][6] }} ==0){
                        markerColour="red";
                    }
                    else if( {{ current_data[item[0]|string][6] }} <5){
                        markerColour="orange";
                    }
                    else{
                        markerColour="green";
                    }

                    var myPosition= new google.maps.LatLng({{ item[2] }}, {{ item[3] }}); <!-- initialising marker -->
                    var marker = new google.maps.Marker({position: myPosition});
                    marker.setMap(map);
                    if( {{ item[0] }} == selected){
                        var image= { <!-- setting size to be bigger than unselected markers -->
                        url:'static/images/'+markerColour+'_bike.png',
                        origin: new google.maps.Point(0,0),
                        anchor: new google.maps.Point(17,34),
                        scaledSize: new google.maps.Size(65,65)
                        };
                    }
                    else{
                        var image= { <!-- setting custom image to take place of marker, based on markerColour from above -->
                        url:'static/images/'+markerColour+'_bike.png',
                        origin: new google.maps.Point(0,0),
                        anchor: new google.maps.Point(17,34),
                        scaledSize: new google.maps.Size(35,35)
                        };
                    }
                    markers.push(marker); <!--adding marker to array so it can be removed later -->
                    marker.setIcon(image);
                    marker.addListener("click", function() { changeMap( {{ item[0] }} ); textBox( {{  item[0]  }} );}); <!-- calling changeMap() on click of marker -->
                {% endfor %}
            }

            function clearMarkers(){ <!-- Function for removing all previous map markers -->
                while(markers[0]){
                    markers.pop().setMap(null);
                }
            }

            function changeMap(place){ <!-- changing map based on "place" location being selected -->
                var x = document.getElementById('home_button');
                x.style.display = 'block';
                map.setZoom(16);
                {% for item in locations %}
                    if( {{ item[0] }} == place.toString()){
                        var newCenter=new google.maps.LatLng( {{ item[2] }}, {{ item[3] }} );
                        map.setCenter(newCenter);
                        }
                {% endfor %}
                clearMarkers();
                setMarkers(place);
            }
            googleMap.changeMap=changeMap;
        }
        function textBox(x){
            {% for item in locations %}
		if ( {{ item[0] }} == x ){
		    var update = {{ current_data[item[0]|string][7] }} + " MINUTES AGO";
                    var current = "TOTAL BIKES: " + {{ current_data[item[0]|string][4] }} + "<br> AVAILABLE BIKES: "+ {{ current_data[item[0]|string][6] }} + "<br> FREE BIKE STANDS: "+ {{ current_data[item[0]|string][5] }} + "<br> LAST UPDATED " + update;
                    document.getElementById("text").innerHTML = "SELECTED LOCATION: {{ item[1] }} <br>" + current;
                }            {% endfor %}
        }