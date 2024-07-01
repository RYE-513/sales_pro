// custom.js

$(document).ready(function() {
    // Handle form submission when the "Save" button is clicked in the modal
    $("#propertyForm").on("submit", function(e) {
        e.preventDefault();

        const formData = $(this).serialize();

        $.ajax({
            type: "POST",
            url: "{% url 'properties:add_property' %}",
            data: formData,
            success: function(response) {
                if (response.success) {
                    // Property added successfully, close the modal and perform any necessary updates on the page
                    $("#addPropertyModal").modal("hide");
                    // You may need to reload the page or update the property list table here
                } else {
                    // Handle the case where property addition failed
                    alert("Failed to add property. Please try again.");
                }
            },
            error: function() {
                // Handle the case where AJAX request failed
                alert("Error: Unable to process the request.");
            }
        });
    });
});
