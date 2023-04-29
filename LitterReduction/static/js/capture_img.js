let getLatitudeLongitude = new Promise((resolve, reject) => {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
            resolve(
                {
                    latitude: position.coords.latitude,
                    longitude: position.coords.longitude,
                }
            )
        })
    } else {
        reject("Browser does not support geolocation.");
    }
})

$(document).ready(function() {
    $("#capture").click(function() {
        getLatitudeLongitude.then((position) => {
            var latitude = position.latitude;
            var longitude = position.longitude;
            $.ajax({
                url: "../capture_img",
                type: "GET",
                datatype: "json",
                data: {
                    "latitude": latitude,
                    "longitude": longitude,
                },
                success: function(response) {
                    console.log(response);
                },
                error: function(xhr, status, error) {
                    console.error(error);
                }
            })
        }).catch((err) => {
            console.log(err)
        })
    });
});