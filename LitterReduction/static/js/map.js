const apiToken = "pk.eyJ1IjoiYXJtYW4tc2NodWxpY2giLCJhIjoiY2xoMWlzZHE3MTNwazNxcnQ2ZGl0a3EwYSJ9.kliHpkp_lGbzNYBTQj_DqA";
mapboxgl.accessToken = apiToken;
var map = new mapboxgl.Map({
 container: 'map',
 style: 'mapbox://styles/mapbox/outdoors-v12', 
center: [30.5, 50.5],
 zoom: 9,
 bearing: 0, 
 height: '100%'
});
//const marker = new mapboxgl.Marker().setLngLat([30.5, 50.5]).addTo(map);
// const marker = new mapboxgl.Marker()
//   .setLngLat([30.5, 50.5])
//   .addTo(map)
//   .setPopup(new mapboxgl.Popup().setHTML("<h1>Marker Content</h1><img src='C:\Users\Arman Shroff\Documents'><p>Some other data</p>"))
//   .on('click', function() {
//     marker.togglePopup();
//   });

let locations = JSON.parse(document.getElementById("locations").dataset.locations); 
let descriptions = JSON.parse(document.getElementById("descriptions").dataset.descriptions); 

const center = [30.5, 50.5];
const radius = 0.5; // in degrees
const numMarkers = 100;
console.log(locations); 
for (let i = 0; i < locations.length; i++) {
    console.log(locations[i]);
    const marker = new mapboxgl.Marker()
        .setLngLat(locations[i])
        .setPopup(new mapboxgl.Popup({
        className: 'my-popup'}).setHTML(`<h1>Litter Report</h1><p>${descriptions[i]}</p>`))
        .addTo(map);
}
// for (let i = 0; i < numMarkers; i++) {
//   const lng = center[0] + (Math.random() * radius * 2 - radius);
//   const lat = center[1] + (Math.random() * radius * 2 - radius);
//   const marker = new mapboxgl.Marker().setLngLat([lng, lat]).addTo(map);
// }
