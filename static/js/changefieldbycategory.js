let changefieldbycategory = function () {
    if (document.getElementById('vehicle_category')) {
        selectedcategory = $("#vehicle_category option:selected").text().toLowerCase();
        if (selectedcategory.includes('mountain bike')) {
            $(".forcycle").show();
            $(".notforcycleorbike").hide();
            $(".forbikeandothervehicle").hide();
        } else if (selectedcategory.includes('motorbike')) {
            $(".notforcycleorbike").hide();
            $(".forbikeandothervehicle").show();
        } else {
            $(".forcycle").hide();
            $(".notforcycleorbike").show();
            $(".forbikeandothervehicle").show();
        }
    }
}


let viewfieldbycategory = function () {
    if (document.getElementById('vehicle_category')) {
        // selectedcategory = $("#vehicle_category option:selected").text().toLowerCase();
        selectedcategory = $("#vehicle_category").val().toLowerCase();
        if (selectedcategory.includes('mountain bike')) {
            $(".forcycle").show();
            $(".notforcycleorbike").hide();
            $(".forbikeandothervehicle").hide();
        } else if (selectedcategory.includes('motorbike')) {
            $(".notforcycleorbike").hide();
            $(".forbikeandothervehicle").show();
        } else {
            $(".forcycle").hide();
            $(".notforcycleorbike").show();
            $(".forbikeandothervehicle").show();
        }
    }
}


