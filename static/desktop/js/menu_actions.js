$(document).ready(function () {

    $('#new_folder').click(function () {
        var fold_name = prompt("Enter the folder Name ", "UntitledFolder");
        if (fold_name == null || fold_name == "") {
            txt = "User cancelled the prompt.";
        } 
        else {
            $.post("/desktop/menu-action/", { action: 'new_folder', name:fold_name }, function (result) {
                // do something with result
                alert(result)
            });
        }
        
    });

    $('#new_doc').click(function () {
        var file_name = prompt("Enter the File Name ", "textfile.txt");
        if (file_name == null || file_name == "") {
            txt = "User cancelled the prompt.";
        } 
        else {
            $.post("/desktop/menu-action/", { action: 'new_doc', name : file_name }, function (result) {
                // do something with result
                alert(result);
            });
        }
    });
});