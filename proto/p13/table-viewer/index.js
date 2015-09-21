var $ = require("jquery");


function addTable(div, spec) {

    div.find('table').remove();
    var table = $("<table>");
    var tbody = $("<tbody>");
    table.append(tbody);
    div.append(table);

    var i,j;
    var firstRow = $("<tr>");
    for (i = 0; i < spec.columnNames.length; i++) {
        firstRow.append($("<th>").text(spec.columnNames[i]));
    }
    tbody.append(firstRow);

    var rowSpec;
    var row;
    for (i = 0; i < spec.rows.length; i++) {
        rowSpec = spec.rows[i];
        row = $("<tr>");
        for (j = 0; j < rowSpec.length; j++) {
            row.append($("<td>").text(rowSpec[j]));
        }
        tbody.append(row);
    }

}


$(function() {

    $("input.explain_button").on("click", function() {
        $.ajax({
            url: "http://127.0.0.1:8008",
            data: { sql: $("input.query_field").val() }, 
            dataType: "jsonp",
            jsonpCallback: 'callback',
            contentType: "application/json",
            success: function (tableSpec) {
                $('div.table_cont').css('display', 'block');
                addTable($('div.start_table_cont'), tableSpec.original);
                addTable($('div.selected_table_cont'), tableSpec.selected);
            }
        });
    });

});
