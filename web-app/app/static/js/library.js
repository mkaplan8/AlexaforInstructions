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
