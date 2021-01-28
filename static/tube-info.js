function displayStationInfo(n) {
    displayedName = $("#station-info > #station-title").text();
    if (displayedName == n) {
        $("#station-info").hide();
    } else {
        $("#station-info").show();
        $("#station-info > #station-title").text(n);
    }
}