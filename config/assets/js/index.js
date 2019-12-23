$(function () {
    var configFileName = "config.json";
    var configuration;
    var nodeServerUrl = "http://localhost:1337/";

    var scheduleSaveConfigurationTimeout = null;

    function scheduleSaveConfiguration() {
        if (scheduleSaveConfigurationTimeout) {
            clearTimeout(scheduleSaveConfigurationTimeout);
        }

        scheduleSaveConfigurationTimeout = setTimeout(saveConfiguration, 500);
    }

    //load configuration from config file and initialize inputs
    function loadConfiguration() {
        $.getJSON(configFileName, function (data) {

            if (data) {
                configuration = data;

                $("#windowWidthAndHeight").val(data.window_width + "x" + data.window_height);
                $("#depthMin").val(data.depth_mm_min);
                $("#depthMax").val(data.depth_mm_max);
                $("#framerate").val(data.depth_frame_rate); //todo comma values???
                $("#depthThreshold").val(data.depth_mm_threshold_diff);
                $("#depthPxQtyIgnore").val(data.depth_px_qty_ignore);
                $("#depthPosterizeQuantity").val(data.depth_posterize_qty);
                $("#borderTop").val(data.border_top);
                $("#borderRight").val(data.border_right);
                $("#borderBottom").val(data.border_bottom);
                $("#borderLeft").val(data.border_left);
                $("#colorMap").val(data.color_map);
            }
        }, function (error) {
            console.error(error);
        });
    }

    function saveConfiguration() {

        //validate and normalize
        var windowWidthAndHeight = $("#windowWidthAndHeight").val().split("x");
        configuration.window_width = parseInt(windowWidthAndHeight[0]) | 0;
        configuration.window_height = parseInt(windowWidthAndHeight[1]) | 0;
        configuration.depth_mm_min = parseInt($("#depthMin").val()) | 0;
        configuration.depth_mm_max = parseInt($("#depthMax").val()) | 0;
        configuration.depth_frame_rate = parseFloat($("#framerate").val());
        if (configuration.depth_frame_rate <= 0) { //validate and set to standard value 
            configuration.depth_frame_rate = 0.3;
        }
        configuration.depth_mm_threshold_diff = parseInt($("#depthThreshold").val()) | 0;
        configuration.depth_px_qty_ignore = parseInt($("#depthPxQtyIgnore").val()) | 0;
        configuration.depth_posterize_qty = parseInt($("#depthPosterizeQuantity").val()) | 0;
        configuration.border_top = parseInt($("#borderTop").val()) | 0;
        configuration.border_right = parseInt($("#borderRight").val()) | 0;
        configuration.border_bottom = parseInt($("#borderBottom").val()) | 0;
        configuration.border_left = parseInt($("#borderLeft").val()) | 0;
        configuration.color_map = $("#colorMap").val();

        var data = JSON.stringify(configuration);

        //call nodeJs Server, that writes into file
        $.post(nodeServerUrl, { "data": data }, function(erro, resultr) {
            console.log("error", error);
            toastr.info("test");
        });
    }

    loadConfiguration();

    //listen to events
    $("#windowWidthAndHeight").on("change", scheduleSaveConfiguration);
    $("#depthMin").on("input", scheduleSaveConfiguration);
    $("#depthMax").on("input", scheduleSaveConfiguration);
    $("#framerate").on("input", scheduleSaveConfiguration);
    $("#depthThreshold").on("input", scheduleSaveConfiguration);
    $("#depthPxQtyIgnore").on("input", scheduleSaveConfiguration);
    $("#depthPosterizeQuantity").on("input", scheduleSaveConfiguration);
    $("#borderTop").on("input", scheduleSaveConfiguration);
    $("#borderRight").on("input", scheduleSaveConfiguration);
    $("#borderBottom").on("input", scheduleSaveConfiguration);
    $("#borderLeft").on("input", scheduleSaveConfiguration);
    $("#colorMap").on("change", scheduleSaveConfiguration);
});
