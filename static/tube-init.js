var container = d3.select('#tube-map');
var width = 1600;
var height = 1000;

var map = d3
  .tubeMap()
  .width(width)
  .height(height)
  .margin({
    top: 20,
    right: 20,
    bottom: 40,
    left: 100,
  })
  .on('click', function (label) {
    displayStationInfo(label);
  });

var urlParams = new URLSearchParams(window.location.search);

if (urlParams.has("file-selector")) {
  fn = urlParams.get("file-selector");
} else {
  fn = "demo";
}

d3.json('/data/'+fn).then(function (data) {
  container.datum(data).call(map);

  var svg = container.select('svg');

  zoom = d3.zoom().scaleExtent([0.5, 6]).on('zoom', zoomed);

  var zoomContainer = svg.call(zoom);
  var initialScale = -3;
  var initialTranslate = [0, 0];

  zoom.scaleTo(zoomContainer, initialScale);
  zoom.translateTo(
    zoomContainer,
    initialTranslate[0],
    initialTranslate[1]
  );

  function zoomed(event) {
    svg.select('g').attr('transform', event.transform.toString());
  }
});