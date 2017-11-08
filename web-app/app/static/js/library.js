function datetime() {
    var d = new Date(),
        seconds = d.getSeconds().toString().length == 1 ? '0'+d.getSeconds() : d.getSeconds(),
        minutes = d.getMinutes().toString().length == 1 ? '0'+d.getMinutes() : d.getMinutes(),
        hours = d.getHours().toString().length == 1 ? '0'+d.getHours() : d.getHours(),
        ampm = d.getHours() >= 12 ? 'pm' : 'am',
        months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
        days = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
    document.getElementById("date-time").innerHTML = days[d.getDay()]+' '+months[d.getMonth()]+' '+d.getDate()+', '+d.getFullYear()+', '+hours+':'+minutes+':'+seconds+ampm;
}
setInterval(datetime,1);

$.get('/library/tasks').done(function(data) {
    data.tasks.forEach(function(row) {
        var visibility = "";
        if (row.visibility == 0){
            visibility = "Public";
        } else {
            visibility = "Private";
        }
        var stepsData = row.steps.split("<~>");
        console.log(stepsData);
        var steps = "";
        for (i = 1; i < stepsData.length; i++) {
            steps += "(Step " + i + ": " + stepsData[i] + ")\n";
        }
        $("#tasks-data").append(`
            <tr>
                <th>`+ row.title +`</th>
                <th>`+ row.materials +`</th>
                <th>`+ steps +`</th>
                <th>`+ visibility +`</th>
            </tr>
        `);
    });
    $("#tasks-table").DataTable();
}).fail(function(res){
    console.log(res.responseText);
});
