var $ = require("jquery");
var d3 = require("d3");


function addTable(selector, spec) {

    // Clear previous table
    var div = $(selector);
    div.find('table').remove();
    var table = $("<table>");
    var tbody = $("<tbody>");
    var firstRow = $("<tr>");
    table.append(tbody);
    div.append(table);
    tbody.append(firstRow);

    d3.select(firstRow[0]).selectAll('th')
        .data(spec.columnNames)
      .enter()
        .append("th")
        .text(function(d) { return d; });

    d3.select(tbody[0]).selectAll("tr")
        .data(spec.rows)
      .enter()
        .append("tr")
        .on("mouseover", function() {
            d3.select(this).classed("hovered", true);
        })
        .on("mouseout", function() {
            d3.select(this).classed("hovered", false);
        })
        .selectAll("td")
          .data(function(d) { return d; })
          .enter()
            .append("td")
            .text(function(d) { return d.data; })
            .classed('violation', function(d) {
                return (d.satisfies === false);
            });

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
                addTable('div.start_table_cont', tableSpec.original);
                addTable('div.selected_table_cont', tableSpec.selected);
            }
        });
    });

});
