$('#fecha').datepicker({
    uiLibrary: 'bootstrap4',
    format: 'dd-mm-yyyy'
});

function clickDetails(obj) {
    let sensor_id = obj.getAttribute("data-sensor");
    let commune_id = obj.getAttribute("data-commune");
    let sensor = sensors.find(e => e.id == sensor_id);
    let commune = communes[commune_id];
    //gm-ui-hover-effect
    
    let parent = obj.closest(".gm-style-iw").nextSibling.click();

    let data = [];
    sensor.data.forEach(element => {
        data.push({"Temperatura": element.Text, "Hora": element[4].split(" ")[1]});   
    });

    $("#filter-graph").css("display", "block");
    $("#chartContainer").html("");
    let svg = dimple.newSvg("#chartContainer", 1200, 300);
    let chart = new dimple.chart(svg, data);
    let x = chart.addCategoryAxis("x", "Hora");
    let y = chart.addMeasureAxis("y", "Temperatura");

    x.addOrderRule("Hora");

    chart.addSeries(null, dimple.plot.line);
    chart.draw();

}

function myFunction() {
    $("#chartContainer").html("");
    //Get data from html
    var fecha = document.getElementById("fecha").value;
    var eje_x = document.getElementById("eje_x").value;
    var eje_y = document.getElementById("eje_y").value;
    var sensores = document.getElementById("sensores").value;

    var svg = dimple.newSvg("#chartContainer", 700, 500);
    d3.csv("/data/test.csv", function (data) {
        data = dimple.filterData(data, "Vivienda ID", [sensores]);

        // Formatting Data
        data.forEach(function(d) {
            d["Vivienda ID"] = parseInt(d["Vivienda ID"]);
            d["Temperatura Interior"] = parseInt(d["Humedad Interior"]) - 60;
            d["Temperatura Exterior"] = parseInt(d["Humedad Exterior"]) - 60;
            d["Humedad Interior"] = parseInt(d["Humedad Interior"]);
            d["Humedad Exterior"] = parseInt(d["Humedad Exterior"]);
            d["Co2"] = parseFloat(d["Co2"]);
            d["Ruido"] = parseFloat(d["Ruido"]);
            d["Pm10"] = parseFloat(d["Pm10"]);
            d["Pm25"] = parseFloat(d["Pm25"]);
            d["Potencia"] = parseFloat(d["Potencia"]);
            d["Energia"] = parseFloat(d["Energia"]);

            var  splitted_date = d["Measured At"].split(" ");
            var fecha = splitted_date[0];
            var hora = splitted_date[1];
            d["Fecha"] = fecha;
            d["Hora"] = hora;
            delete d["Measured At"];
        });

        //Plotting
        data = dimple.filterData(data, "Fecha", [fecha]);
        var myChart = new dimple.chart(svg, data);
        myChart.setBounds(60, 30, 505, 305);
        var x = myChart.addCategoryAxis("x", eje_x);
        x.addOrderRule("Hora");
        var y1 = myChart.addMeasureAxis("y", eje_y);
        var temp_ext = myChart.addSeries("Vivienda ID", dimple.plot.line);
        myChart.addLegend(60, 10, 500, 20, "right", [temp_ext]);
        myChart.draw();
    });
}