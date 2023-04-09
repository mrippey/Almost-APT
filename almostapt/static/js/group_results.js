<script>
  const groupCountry = "{{ country }}";

  if (groupCountry !== 'UNK') {
    mapboxgl.accessToken = 'YOUR TOKEN';
  const map = new mapboxgl.Map({
    container: 'map',
  style: 'mapbox://styles/mapbox/dark-v10',
  zoom: 2,
  center: [0, 0]
                    });

  fetch(`https://api.mapbox.com/geocoding/v5/mapbox.places/${groupCountry}.json?access_token=${mapboxgl.accessToken}&language=en`)
                        .then(response => response.json())
                        .then(data => {
                            if (data.features.length > 0) {
                                const coordinates = data.features[0].center;

  map.setCenter(coordinates);

  new mapboxgl.Marker().setLngLat(coordinates).addTo(map);

  map.addSource('country', {
    'type': 'geojson',
  'data': {
    'type': 'Feature',
  'properties': { },
  'geometry': {
    'type': 'Point',
  'coordinates': coordinates
                                        }
                                    }
                                });

  map.addLayer({
    'id': 'country-layer',
  'type': 'fill',
  'source': 'country',
  'paint': {
    'fill-color': '#f00',
  'fill-opacity': 0.5
                                    }
                                });
                            } else {
    console.error('Could not find country coordinates');
                            }
                        })
                        .catch(error => {
    console.error('Error fetching country coordinates:', error);
                        });
                } else {
    mapboxgl.accessToken = 'YOUR TOKEN';
  const map = new mapboxgl.Map({
    container: 'map',
  style: 'mapbox://styles/mapbox/dark-v10',
  zoom: 2,
  center: [0, 0]
                    });
                }
</script>