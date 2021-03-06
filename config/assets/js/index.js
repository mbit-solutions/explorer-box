$(function () {        
    toastr.options.closeButton = true;
    toastr.options.progressBar = true;
    toastr.options.timeOut = 1000;

    var configuration;   

    var scheduleSaveConfigurationTimeout = null;

    function scheduleSaveConfiguration() {
        if (scheduleSaveConfigurationTimeout) {
            clearTimeout(scheduleSaveConfigurationTimeout);
        }

        scheduleSaveConfigurationTimeout = setTimeout(saveConfiguration, 500);
    }

    //load configuration from config file and initialize inputs
    function loadConfiguration() {
        $.getJSON("config?rand=" + performance.now(), function (data) {

            if (data) {
                configuration = data;

                $("#windowWidthAndHeight").val(data.window_width + "x" + data.window_height);
                $("#depthMin").val(data.depth_mm_min);
                $("#depthMax").val(data.depth_mm_max);
                $("#framerate").val(data.depth_frame_rate);
                $("#depthThreshold").val(data.depth_mm_threshold_diff);
                $("#depthPxQtyIgnore").val(data.depth_px_qty_ignore);
                $("#depthPosterizeQuantity").val(data.depth_posterize_qty);
                $("#borderTop").val(data.border_top);
                $("#borderRight").val(data.border_right);
                $("#borderBottom").val(data.border_bottom);
                $("#borderLeft").val(data.border_left);
                $("#colorMap").val(data.color_map);
                $("#enablePosterize").prop("checked", data.enable_posterize);
                $("#enableContourize").prop("checked", data.enable_contourize);

                if(configuration.picture_frequency > 0) {
                    setInterval(getImage, 1000);
                }
                else {
                    $(".btn-preview-image").hide();
                }
            }
        }, function (error) {
            console.error(error);
        });
    }

    function saveConfiguration() {

        //validate and normalize
        buildConfiguration();
        normalizeConfiguration();
        
        //call nodeJs Server, that writes into file
        $.ajax({
            type: "POST",
            url: "config",
            data: JSON.stringify(configuration),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
          });

        toastr.success('Config saved')
    }

    function buildConfiguration() {
        var windowWidthAndHeight = $("#windowWidthAndHeight").val().split("x");
        configuration.window_width = parseInt(windowWidthAndHeight[0]) | 0;
        configuration.window_height = parseInt(windowWidthAndHeight[1]) | 0;
        configuration.depth_mm_min = parseInt($("#depthMin").val()) | 0;
        configuration.depth_mm_max = parseInt($("#depthMax").val()) | 0;
        configuration.depth_frame_rate = parseFloat($("#framerate").val());
        configuration.depth_mm_threshold_diff = parseInt($("#depthThreshold").val()) | 0;
        configuration.depth_px_qty_ignore = parseInt($("#depthPxQtyIgnore").val()) | 0;
        configuration.depth_posterize_qty = parseInt($("#depthPosterizeQuantity").val()) | 0;
        configuration.border_top = parseInt($("#borderTop").val()) | 0;
        configuration.border_right = parseInt($("#borderRight").val()) | 0;
        configuration.border_bottom = parseInt($("#borderBottom").val()) | 0;
        configuration.border_left = parseInt($("#borderLeft").val()) | 0;
        configuration.color_map = $("#colorMap").val();
        configuration.enable_posterize = $("#enablePosterize").is(":checked");
        configuration.enable_contourize = $("#enableContourize").is(":checked");
    }

    function normalizeConfiguration() {
        //depth_mm_min
        if (configuration.depth_mm_min < 0) {
            configuration.depth_mm_min = 0;
        }
        if (configuration.depth_mm_min > 3000) {
            configuration.depth_mm_min = 3000;
        }
        
        //depth_mm_max
        if (configuration.depth_mm_max < 0) {
            configuration.depth_mm_max = 0;
        }
        if (configuration.depth_mm_max > 3000) {
            configuration.depth_mm_max = 3000;
        }

        //depth_frame_rate
        if (configuration.depth_frame_rate < 0.01) {
            configuration.depth_frame_rate = 0.01;
        }
        if (configuration.depth_frame_rate > 3) {
            configuration.depth_frame_rate = 3;
        }

        //depth_posterize_qty
        if (configuration.depth_posterize_qty < 1) {
            configuration.depth_posterize_qty = 1;
        }
        if (configuration.depth_posterize_qty > 20) {
            configuration.depth_posterize_qty = 20;
        }
    }

    function togglePreview() {
        $("#preview").toggle();
    }

    function getImage() {
        var image = "image?rand=" + performance.now();
        $("#preview-img").attr("src", image);
    }

    loadConfiguration();

    function loadLogs()
    {
        $.get("logs?nocache="+performance.now(), null, function(data) {
            if(data)
            {
                $("#logWindow").val(data);
                //$("#logWindow").scrollTop($("#logWindow")[0].scrollHeight);
            }
        });
    }
    setInterval(loadLogs, 2500);

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
    $("#enablePosterize").on("change", scheduleSaveConfiguration);
    $("#enableContourize").on("change", scheduleSaveConfiguration);

    $(".btn-preview-image").on("click", togglePreview);
});
