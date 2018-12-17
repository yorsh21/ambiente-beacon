$('#fecha').datepicker({
    uiLibrary: 'bootstrap4',
    format: 'dd-mm-yyyy'
});

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
        if(element.date.split(" ")[1].split(":")[1] == "00") {
            data.push({"Temperatura": element.Text, "Hora": element.date.split(" ")[1]});
        }   
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

function loadDataSensor() {
    let sensor_id = document.getElementById("selected_sensor_id").value;
    let sensor = sensors.find(e => e.id == sensor_id);

    var fecha = document.getElementById("fecha").value;
    var eje_y = document.getElementById("eje_y").value;

    let data = [];
    let text_eje_y;
    
    switch(eje_y){
        case "Temperatura Exterior":
            text_eje_y = "Temperatura";
            sensor.data.forEach(element => {
                if(element.date.split(" ")[0] == fecha && element.date.split(" ")[1].split(":")[1] == "00") {
                    data.push({"Temperatura": element.Text, "Hora": element.date.split(" ")[1]});   
                }
            });
            break;
        case "Temperatura Interior":
            text_eje_y = "Temperatura";
            sensor.data.forEach(element => {
                if(element.date.split(" ")[0] == fecha && element.date.split(" ")[1].split(":")[1] == "00") {
                    data.push({"Temperatura": element.Tint, "Hora": element.date.split(" ")[1]});   
                }
            });
            break;
        case "Humedad Exterior":
            text_eje_y = "Humedad";
            sensor.data.forEach(element => {
                if(element.date.split(" ")[0] == fecha && element.date.split(" ")[1].split(":")[1] == "00") {
                    data.push({"Humedad": element.Hext, "Hora": element.date.split(" ")[1]});   
                }
            });
            break;
        case "Humedad Interior":
            text_eje_y = "Humedad";
            sensor.data.forEach(element => {
                if(element.date.split(" ")[0] == fecha && element.date.split(" ")[1].split(":")[1] == "00") {
                    data.push({"Humedad": element.Hint, "Hora": element.date.split(" ")[1]});   
                }
            });
            break;
        case "Co2":
            sensor.data.forEach(element => {
                
                if(element.date.split(" ")[0] == fecha && element.date.split(" ")[1].split(":")[1] == "00") {
                    data.push({"Co2": element.Co2, "Hora": element.date.split(" ")[1]}); 
                }  
            });
            text_eje_y = "Co2";
            break;
        case "Ruido":
            sensor.data.forEach(element => {
                if(element.date.split(" ")[0] == fecha && element.date.split(" ")[1].split(":")[1] == "00") {
                    data.push({"Ruido": element.Ruid, "Hora": element.date.split(" ")[1]});   
                }
            });
            text_eje_y = "Ruido";
            break;
        case "Pm10":
            sensor.data.forEach(element => {
                if(element.date.split(" ")[0] == fecha && element.date.split(" ")[1].split(":")[1] == "00") {
                    data.push({"Pm10": element.Pm10, "Hora": element.date.split(" ")[1]});   
                }
            });
            text_eje_y = "Humedad";
            break;
        case "Pm25":
            sensor.data.forEach(element => {
                if(element.date.split(" ")[0] == fecha && element.date.split(" ")[1].split(":")[1] == "00") {
                    data.push({"Pm25": element.Pm25, "Hora": element.date.split(" ")[1]});   
                }
            });
            text_eje_y = "Pm25";
            break;
        case "Potencia":
            sensor.data.forEach(element => {
                if(element.date.split(" ")[0] == fecha && element.date.split(" ")[1].split(":")[1] == "00") {
                    data.push({"Potencia": element.Powr, "Hora": element.date.split(" ")[1]});   
                }
            });
            text_eje_y = "Potencia";
            break;
        case "Energia": default:
            sensor.data.forEach(element => {
                if(element.date.split(" ")[0] == fecha && element.date.split(" ")[1].split(":")[1] == "00") {
                    data.push({"Energia": element.Egy, "Hora": element.date.split(" ")[1]});   
                }
            });
            text_eje_y = "Energia";
            break;
    }
    

    $("#filter-graph").css("display", "block");
    $("#chartContainer").html("");
    let svg = dimple.newSvg("#chartContainer", 1200, 300);
    let chart = new dimple.chart(svg, data);
    let x = chart.addCategoryAxis("x", "Hora");


    let y = chart.addMeasureAxis("y", text_eje_y);

    x.addOrderRule("Hora");

    chart.addSeries(null, dimple.plot.line);
    chart.draw();
}