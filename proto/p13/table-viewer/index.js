var $ = require("jquery");
var d3 = require("d3");


function buildTable(selector, spec) {

    // Clear previous table
    var div = $(selector);
    div.find('table').remove();
    var table = $("<table>");
    var tbody = $("<tbody>");
    var firstRow = $("<tr>");
    table.append(tbody);
    div.append(table);

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
          .data(function(d) { 
              return d; 
          })
          .enter()
            .append("td")
            .text(function(d) { return d.data; })
            .classed('violation', function(d) {
                return (d.satisfies === false);
            });

    // Add the header only after all data rows have been added to the table
    tbody.prepend(firstRow);

}

/*
function selectColumns(selector, columnNames) {

    var selectedColIndexes = [];
    d3.select(selector).select("tr")
      .each(function(d, i) {

      });

    d3.select(selector).selectAll("tr");

}
*/

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
                buildTable('div.start_table_cont', tableSpec.original);
                buildTable('div.selected_table_cont', tableSpec.selected);
            }
        });
    });

});
