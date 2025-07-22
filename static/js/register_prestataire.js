// static/js/register_prestataire.js

$(document).on("submit", "#prestataire-form", function (e) {
    e.preventDefault();
    let form = $(this);
    let formData = new FormData(this);

    $.ajax({
        type: "POST",
        url: form.attr("action"),
        data: formData,
        processData: false,
        contentType: false,
        success: function (response) {
            if (response.success) {
                $("#registerModalPrestataire").modal("hide");
                window.location.href = response.redirect_url;
            } else {
                $("#modalBodyPrestataire").html(response.html);
            }
        },
        error: function (xhr) {
            $("#modalBodyPrestataire").html("<p class='text-danger'>حدث خطأ أثناء الإرسال.</p>");
        },
    });
});
