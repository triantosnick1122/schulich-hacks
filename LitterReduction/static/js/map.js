const apiToken = "pk.eyJ1IjoiYXJtYW4tc2NodWxpY2giLCJhIjoiY2xoMWlzZHE3MTNwazNxcnQ2ZGl0a3EwYSJ9.kliHpkp_lGbzNYBTQj_DqA";
mapboxgl.accessToken = apiToken;
var map = new mapboxgl.Map({
 container: 'map',
 style: 'mapbox://styles/mapbox/outdoors-v12', 
center: [-114.08, 51.05], // center around calgary
 zoom: 9,
 bearing: 0, 
 height: '100%'
});


let locations = JSON.parse(document.getElementById("locations").dataset.locations); 
let other_comments = JSON.parse(document.getElementById("other_comments").dataset.otherComments); 
let garbage_amounts = JSON.parse(document.getElementById("garbage_amounts").dataset.garbageAmounts);
let garbage_types = JSON.parse(document.getElementById("garbage_types").dataset.garbageTypes);
let images = JSON.parse(document.getElementById("images").dataset.images); 




// creates clickable "popup" markers on the map for each report that show the image and other info about the litter report when clicked on. 
for (let i = 0; i < locations.length; i++) {

    var img = document.createElement("img");
    img.src = "https://resources.reduce-recycle.com.au/bswwrrg/wp-content/uploads/2019/08/28233636/Marine-litter2-1.jpg"; 

    var popup = new mapboxgl.Popup({
        className: 'my-popup'}).setHTML(`<h1>Litter Report</h1> <p>Litter Type: ${garbage_types[i]}</p> <p>Amount of Litter: ${garbage_amounts[i]}</p>
                    <p>Other Comments: ${other_comments[i]}</p>`);

    // Add the image element to the popup content
    popup._content.appendChild(img);

    const marker = new mapboxgl.Marker()
        .setLngLat(locations[i])
        .setPopup(popup).addTo(map);
}
