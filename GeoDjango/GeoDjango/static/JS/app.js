var myMap = L.map('map').setView([22.9074872, 79.07306671], 5);
const titleUrl = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';

const tiles = L.tileLayer(titleUrl);
tiles.addTo(myMap);


// const icon = L.icon({
//     iconUrl: 'images/pizza.jpg',
//     iconSize: [100, 80]
// })

// const marker = L.marker([22.9074872, 79.07306671], {
//     icon: icon
// });



// function onEachFeature(feature, layer) {
//     layer.bindPopup('Hello');
// }

// const shopsLayer = L.geoJSON(storeList, {
//     onEachFeature: onEachFeature,
//     pointToLayer: function(feature, latlng) {
//         return L.marker(latlng);
//     }
// });
// shopsLayer.addTo(myMap);



function makePopupContent(shop) {
        return `
                <div>
                    <h4>Temperature: ${shop.properties.Temperature}</h4>
                    <h4>Humidity: ${shop.properties.Humidity}</h4>
                    <h4>Location: ${shop.properties.Location}</h4>
                </div>
        `;
}

function onEachFeature(feature, layer) {
    layer.bindPopup(makePopupContent(feature));
}

const shopsLayer = L.geoJSON(storeList, {
    onEachFeature: onEachFeature,
    pointToLayer: function(feature, latlng) {
        return L.marker(latlng);
    }
});
shopsLayer.addTo(myMap);




// function makePopupContent(shop) {
//     return `
//             <div>
//                 <h4>Temperature: ${shop.properties.Temperature}</h4>
//                 <h4>Humidity: ${shop.properties.Humidity}</h4>
//                 <h4>Location: ${shop.properties.Location}</h4>
//             </div>
//     `;
// }

// function onEachFeature(feature, layer) {
// layer.bindPopup(makePopupContent(feature));
// }

// const shopsLayer = L.geoJSON(storeList2, {
// onEachFeature: onEachFeature,
// pointToLayer: function(feature, latlng) {
//     return L.marker(latlng);
// }
// });
// shopsLayer.addTo(myMap);







