$(document).ready(function () {

    $('#new_folder').click(function () {
        $.post("/desktop/menu-action/", { action: 'new_folder', folder:'new folder' }, function (result) {
            // do something with result
        });
    });

    $('#new_doc').click(function () {
        alert(2);
    });
});