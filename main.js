/*$('#fecha').datepicker({
    uiLibrary: 'bootstrap4',
    format: 'dd-mm-yyyy',
    startView: "months",
    minViewMode: "months"
});*/

function clickDetails(obj) {
    let sensor_id = obj.getAttribute("data-sensor");
    document.getElementById("selected_sensor_id").value = sensor_id;

    let commune_id = obj.getAttribute("data-commune");
    let sensor = sensors.find(e => e.id == sensor_id);
    let commune = communes[commune_id];

    //gm-ui-hover-effect
    
    let parent = obj.closest(".gm-style-iw").nextSibling.click();

    let data = [];
    sensor.data.forEach(element => {
        data.push({"Temperatura": element[0], "Fecha": element[4]});   
    });

    $("#filter-graph").css("display", "block");
    $("#chartContainer").html("");
    let svg = dimple.newSvg("#chartContainer", 1200, 300);
    let chart = new dimple.chart(svg, data);
    let x = chart.addCategoryAxis("x", "Fecha");
    let y = chart.addMeasureAxis("y", "Temperatura");

    x.addOrderRule("Fecha");

    chart.addSeries(null, dimple.plot.line);
    chart.draw();

}

function loadDataSensor() {
    let sensor_id = document.getElementById("selected_sensor_id").value;
    let sensor = sensors.find(e => e.id == sensor_id);

    var fecha = document.getElementById("fecha").value;
    var eje_y = document.getElementById("eje_y").value;
    

    let data = [];
    let text_eje_y;
    
    switch(eje_y){
        case "Temperatura":
            sensor.data.forEach(element => {
                if(fecha == "00") {
                    data.push({"Temperatura": element[0], "Fecha": element[4]});
                }
                else if(element[4].split('-')[1] == fecha) {
                    data.push({"Temperatura": element[0], "Fecha": element[4].split('-')[2]});   
                }
            });
            text_eje_y = "Temperatura";
            break;
        case "Humedad":
            sensor.data.forEach(element => {
                if(fecha == "00") {
                    data.push({"Humedad": element[1], "Fecha": element[4]});
                }
                else if(element[4].split('-')[1] == fecha) {
                    data.push({"Humedad": element[1], "Fecha": element[4].split('-')[2]});   
                }
            });
            text_eje_y = "Humedad";
            break;
        case "Co2":
            sensor.data.forEach(element => {
                if(fecha == "00") {
                    data.push({"Co2": element[2], "Fecha": element[4]});
                }
                else if(element[4].split('-')[1] == fecha) {
                    data.push({"Co2": element[2], "Fecha": element[4].split('-')[2]}); 
                }  
            });
            text_eje_y = "Co2";
            break;
        case "Ruido": default:
            sensor.data.forEach(element => {
                if(fecha == "00") {
                    data.push({"Ruido": element[3], "Fecha": element[4]});
                }
                else if(element[4].split('-')[1] == fecha) {
                    data.push({"Ruido": element[3], "Fecha": element[4].split('-')[2]});   
                }
            });
            text_eje_y = "Ruido";
            break;
    }
    

    $("#filter-graph").css("display", "block");
    $("#chartContainer").html("");
    let svg = dimple.newSvg("#chartContainer", 1200, 300);
    let chart = new dimple.chart(svg, data);
    let x = chart.addCategoryAxis("x", "Fecha");
    let y = chart.addMeasureAxis("y", text_eje_y);

    x.addOrderRule("Fecha");

    chart.addSeries(null, dimple.plot.line);
    chart.draw();
}