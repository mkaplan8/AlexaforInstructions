function datetime() {
    var d = new Date(),
        minutes = d.getMinutes().toString().length == 1 ? '0'+d.getMinutes() : d.getMinutes(),
        hours = d.getHours().toString().length == 1 ? '0'+d.getHours() : d.getHours(),
        ampm = d.getHours() >= 12 ? 'pm' : 'am',
        months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
        days = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
    document.getElementById("date-time").innerHTML = days[d.getDay()]+' '+months[d.getMonth()]+' '+d.getDate()+', '+d.getFullYear()+', '+hours+':'+minutes+':'+d.getSeconds()+ampm;
}
setInterval(datetime,1);
var i = 4;
function newStep() {
    $("#man-up").append('<div class="stacked"><label for="step'+i+'">Step '+i+': </label><textarea class="step" id="step'+i+'" name="step'+i+'"></textarea></div>');
    i++;
}
$("#more-steps").on("click", newStep);
