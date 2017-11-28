removeStepEvent();

function newStep() {
    var stepsShown = $(".stacked.step").length;
    $("#man-up").append('<div class="stacked step"><span id="'+(++stepsShown)+'" class="remove-step">&#9746; </span><label for="step'+(stepsShown)+'">Step '+(stepsShown)+': </label><textarea class="step" id="step'+(stepsShown)+'" name="step'+(stepsShown)+'" required></textarea></div>');
    removeStepEvent();
}
$("#more-steps").on("click", newStep);

function removeStepEvent() {
    $(".remove-step").on("click", function() {
        $(this).parent().remove();
        var steps = [];
        $(".stacked.step textarea").each(function() {
            steps.push($(this).val());
        });
        var stepsLeft = $(".stacked.step").length;
        $(".stacked.step").remove();
        for (var i = 0; i < stepsLeft; i++) {
            $("#more-steps").click();
            $("#step"+(i+1)).val(steps[i]);
        }
    });
}

function parseFile() {
    var x = document.getElementById("file-upload");
    var txt = "";
    if ("files" in x) {
        if (x.files.length == 0) {
            txt = "Select an instruction set in a text format.";
        } else {
            var file = x.files[0];
            if ('name' in file) {
                txt += "File Name: " + file.name + "<br>";
            }
            if ('size' in file) {
                txt += "File Size: " + file.size + " bytes";
            }
        }
    } else {
        if (x.value == "") {
            txt += "Select an instruction set in a text format.";
        } else {
            txt += "The files property is not supported by your browser!";
            txt  += "<br>The path of the selected file: " + x.value; // If the browser does not support the files property, it will return the path of the selected file instead.
        }
    }
    document.getElementById("file-info").innerHTML = txt;
    var file = x.files[0];
    setTimeout(function(){
        document.getElementById("tname").value = "How to upload to A4I web-app using a file";
        document.getElementById("mats").innerHTML = "File, Computer, A4I web account";
        document.getElementById("step1").innerHTML = "Navigate to a web browser and open A4I website.";
        document.getElementById("step2").innerHTML = "Log into the A4I website.";
        document.getElementById("step3").innerHTML = 'Go to the "Upload" page.';
        $("#more-steps").click();
        document.getElementById("step4").innerHTML = 'Click the "Choose File" button.';
        $("#more-steps").click();
        document.getElementById("step5").innerHTML = "Select the file that contains the instructions you want to upload.";
        $("#more-steps").click();
        document.getElementById("step6").innerHTML = 'Click "Open".';
        $("#more-steps").click();
        document.getElementById("step7").innerHTML = "Edit anything that was not parsed correctly.";
    }, 2500);
}
