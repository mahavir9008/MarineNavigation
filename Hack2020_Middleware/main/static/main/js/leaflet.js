angular.module('myApp', ['ngMaterial']).config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
}).controller('AppCtrl', ['$scope', '$http', function($scope, $http) {
  $scope.coordinates=[];
  $scope.disabled=true;
  $scope.rowNum = -1;
  $scope.coords = [];

  $scope.expandMenu = function(rowNum){
    console.log(rowNum);
    $scope.rowNum = ($scope.rowNum===rowNum ? -1 : rowNum);
  };

  var mymap = L.map('mapid').setView([38,26.5],8);

  L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    // maxZoom: 18,
    id: 'mapbox/streets-v11',
    // tileSize: 512,
    // zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoibWlrZXNvbG93IiwiYSI6ImNrYTExZzJkNDA3Zngzb3A2YWtrMXAwa2YifQ.gtV85gxNT53Gmw7Buy6Thw'
  }).addTo(mymap);

  mymap.on('dblclick', function(e) {
    $scope.popup = L.popup();
    $scope.popup
      .setLatLng(e.latlng)
      .setContent('Coordinates: ' + e.latlng.toString())
      .openOn(mymap)
  });

  mymap.on('click', function(e) {
    $scope.coord=e.latlng.toString();
    $scope.coordinat=$scope.coord.replace('LatLng(',"")
    $scope.coordinates=$scope.coordinat.replace(')',"").split(',')
  });

  $scope.openMenu = function() {
    $scope.disabled=false;
  };

  $scope.setCoord = function() {
    var marker=0;
    marker = L.marker([$scope.coordinates[0], $scope.coordinates[1]], {
      draggable: true,
      title: "Resource location",
      alt: "Resource Location",
      riseOnHover: true
    }).addTo(mymap)
    mymap.flyTo([$scope.coordinates[0], $scope.coordinates[1]], 15)
  };

  $scope.crtRoot = function(){
    console.log($scope.coords);
  };

}]);
//
//
//
//
// //initialize leaflet map
// const leafmap = L.map('mapid')
//
//
// //Run on page load
// window.addEventListener('DOMContentLoaded', (event) => {
//
//     //initialize tileLayer provider
//     L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
//                 attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
//                 maxZoom: 18,
//                 id: 'mapbox/streets-v11',
//                 tileSize: 512,
//                 zoomOffset: -1,
//                 accessToken: 'pk.eyJ1IjoibWlrZXNvbG93IiwiYSI6ImNrYTExZzJkNDA3Zngzb3A2YWtrMXAwa2YifQ.gtV85gxNT53Gmw7Buy6Thw'
//             }).addTo(leafmap);
//
//     //set view of initial map
//     leafmap.setView([38,26.5],8)
// //
//     // add onmapclick event
//     leafmap.on('click', onMapClick);
//
//     //add sidebar tool
//     leafmap.pm.addControls({
//     position: 'topleft',
//     drawCircle: false,
// });
//
// //output list of drawn wps
// // sxolio12
// const markedPath = []
// leafmap.on('pm:drawstart', ({ workingLayer }) => {
//   workingLayer.on('pm:vertexadded', e => {
//       markedPath.push(e.latlng)
//   });
// });
//
// })
//
//
// //PopUp function
// var popup = L.popup();
// function onMapClick(e) {
//         popup
//             .setLatLng(e.latlng)
//             .setContent('Coordinates: '+e.latlng.toString())
//             .openOn(leafmap)
//
//
// }
//
// //search and mark function
// const btn = document.querySelector('button')
// btn.onclick =  function () {
//     var lat = parseFloat(document.getElementById('lat').value)
//     var long = parseFloat(document.getElementById('lng').value)
//
//     var marker = L.marker([lat,long], {
// 	 	    draggable: true,
// 	 	    title: "Resource location",
// 	 	    alt: "Resource Location",
// 	 	    riseOnHover: true
//     }).addTo(leafmap)
//      leafmap.flyTo([lat,long],15)
// }


/*GeoJSON input & draw layer
example voyage coordinates
var wp1 = [37.935905, 23.649831].reverse()
var wp2 = [37.935905, 23.649831].reverse()
var wp3 = [37.93563, 23.64901].reverse()
var wp4 = [37.932123, 23.649176].reverse()
var wp5 = [37.932123, 23.649176].reverse()
var wp6 = [37.932758, 23.654208].reverse()
var wp7 = [37.932758, 23.654208].reverse()
var wp8 = [37.821175, 23.748150].reverse()

var planned_route = [
[wp1,wp2],
[wp3,wp4],
[wp5,wp6],
[wp7,wp8],
]

var voyageJSON = [{
"type": "Feature",
'geometry': {
'type': 'MultiLineString',
"coordinates": planned_route
}}]

var routelayer = L.geoJSON().addTo(leafmap);
routelayer.addData(voyageJSON);
*/

/* GeoJSON draw example with chlorophel

//example Data input as GeoJSON
var statesData =
{"type":"FeatureCollection","features":
{"type":"Feature","id":"01","properties":
{"name":"Alabama","density":94.65},
"geometry":{"type":"Polygon",
"coordinates":
[[[-87.359296,35.00118],[-85.606675,34.984749],
[-85.431413,34.124869],[-85.184951,32.859696],[-85.069935,32.580372],
[-84.960397,32.421541],[-85.004212,32.322956],[-84.889196,32.262709],
[-85.058981,32.13674],[-85.053504,32.01077],[-85.141136,31.840985],
[-85.042551,31.539753],[-85.113751,31.27686],[-85.004212,31.003013],
[-85.497137,30.997536],[-87.600282,30.997536],[-87.633143,30.86609],
[-87.408589,30.674397],[-87.446927,30.510088],[-87.37025,30.427934],
[-87.518128,30.280057],[-87.655051,30.247195],[-87.90699,30.411504],
[-87.934375,30.657966],[-88.011052,30.685351],[-88.10416,30.499135],
[-88.137022,30.318396],[-88.394438,30.367688],[-88.471115,31.895754],
[-88.241084,33.796253],[-88.098683,34.891641],[-88.202745,34.995703],
[-87.359296,35.00118]]]
}}

//set Colors & styles for areas of display
function getColor(d){
return d<30 ? '#0033cc':
d<20 ? '#4d79ff':
d<10 ? '#ff9980':
d<5  ? '#ff471a':
'#cc2900';
}
function style(feature) {
return {
fillColor: getColor(feature.properties.density),
weight: 2,
opacity: 1,
color: 'white',
dashArray: '3',
fillOpacity: 0.7
};
}

//Initialize leafmap object with geoJSON features
L.geoJSON(statesData, {style:style}).addTo(leafmap);
*/
