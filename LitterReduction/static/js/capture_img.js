$("#capture").click(function() {
    console.log("checkpt1")
    $.ajax({
        // AJAX call to backend to perform enrichment analysis.
        url: "../capture_img",
        type: "POST",
        success: function(response) {
            console.log(response);
        },
        error: function(xhr, status, error) {
            console.error(error);
        }
    })
});