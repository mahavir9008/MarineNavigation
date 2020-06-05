angular.module('myApp', ['ngMaterial']).config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
}).controller('AppCtrl', ['$scope', '$http', function($scope, $http) {
  $scope.coordinates = [];
  $scope.disabled = true;
  $scope.rowNum = -1;
  $scope.coords = [];

  $scope.expandMenu = function(rowNum) {
    $scope.rowNum = ($scope.rowNum === rowNum ? -1 : rowNum);
  };

  var mymap = L.map('mapid',{crs: L.CRS.EPSG3857}).setView([37.983810, 23.727539], 7);

  L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoibWlrZXNvbG93IiwiYSI6ImNrYTExZzJkNDA3Zngzb3A2YWtrMXAwa2YifQ.gtV85gxNT53Gmw7Buy6Thw'
  }).addTo(mymap);

  mymap.on('dblclick', function(e) {
    $scope.popup = L.popup();
    $scope.popup
      .setLatLng(e.latlng)
      .setContent('Coordinates: ' + e.latlng.toString())
      .openOn(mymap)
  });

  if ($scope.coordinates.length === 0) {
    mymap.on('click', function(e) {
      $scope.coord = e.latlng.toString();
      $scope.coordinat = $scope.coord.replace('LatLng(', "")
      $scope.coordinates = $scope.coordinat.replace(')', "").split(',')
    });
  }

  $scope.setCoord = function() {
    var marker = 0;
    marker = L.marker([$scope.coordinates[0], $scope.coordinates[1]], {
      draggable: true,
      title: "Resource location",
      alt: "Resource Location",
      riseOnHover: true
    }).addTo(mymap)
    mymap.flyTo([$scope.coordinates[0], $scope.coordinates[1]], 15)
  };

  $scope.crtRoot = function() {
    // console.log($scope.coords);

    $http({
      method:'GET',
      url:'./static/main/js/new.geojson'
    }).then(function(response){
console.log(response)


    // function getColor(d){
    //   return '#0033cc';
    // }
    //
    // function style(feature) {
    //     return {
    //         fillColor: getColor(feature),
    //         weight: 2,
    //         opacity: 1,
    //         color: 'white',
    //         dashArray: '3',
    //         fillOpacity: 0.7
    //     };
    // }
    // console.log(L.geoJSON(response).addTo(mymap));
    L.geoJSON(response).addTo(mymap);
    });
  };

  $scope.weatherFind = function() {
    var date = new Date();
    var timezoneOffset = date.getMinutes() + date.getTimezoneOffset();
    var timestamp = date.getTime() + timezoneOffset * 1000;
    var correctDate = new Date(timestamp);
    correctDate.setUTCHours(0, 0, 0, 0);
    var lat = $scope.coordinates[0];
    var lng = $scope.coordinates[1];
    var params = 'windSpeed,currentDirection,currentSpeed,swellDirection,swellHeight,swellPeriod,waterTemperature,waveDirection,waveHeight,wavePeriod,windDirection,gust';

    fetch(`https://api.stormglass.io/v2/weather/point?lat=${lat}&lng=${lng}&params=${params}`, {
      headers: {
        'Authorization': '45292256-a4fb-11ea-ac19-0242ac130002-4529231e-a4fb-11ea-ac19-0242ac130002'
      }
    }).then((response) => response.json()).then((jsonData) => {
      console.log(jsonData);
      angular.forEach(jsonData.hours, function(val, idx) {
        if (moment(val.time).toISOString() === correctDate.toISOString()) {
          $scope.popup = L.popup();
          $scope.popup
            .setLatLng($scope.coordinates)
            .setContent('<ul><li>Current Direction: ' + val.currentDirection.meto + '</li><li>Current Speed: ' + val.currentSpeed.meto + '</li><li>Gust: ' + val.gust.noaa + '</li><li>Swell Direction: '+val.swellDirection.icon +'</li><li>Swell Height: '+val.swellHeight.icon +'</li><li>Swell Period: '+val.swellPeriod.icon +'</li><li>Water Temperature: '+val.waterTemperature.noaa +'</li><li>Wave Direction: '+val.waveDirection.icon +'</li><li>Wave Height: '+val.waveHeight.icon +
            '</li><li>Wave Period: '+val.wavePeriod.icon +'</li><li>Wind Direction: '+val.windDirection.icon +'</li><li>Wind Speed: '+val.windSpeed.icon +'</li></ul>')
            .openOn(mymap)
          console.log($scope.popup);
        }
        $scope.coordinates = [];
      });
    });
  };

}]);
