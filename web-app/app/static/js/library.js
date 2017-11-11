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
        if (row[5] == 0) {
            visibility = "Public";
        } else {
            visibility = "Private";
        }
        $("#tasks-data").append(`
            <tr>
                <th>`+ row[2] +`</th>
                <th>`+ row[3] +`</th>
                <th>`+ row[4] +`</th>
                <th>`+ visibility +`</th>
            </tr>
        `);
    });
    $("#tasks-table").DataTable();
}).fail(function(res){
    $("#tasks-table").DataTable();
    console.log(res.responseText);
});
