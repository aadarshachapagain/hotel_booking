$(document).ready(() => {
    // Maintain global object array for image files and its member count
    function myFunction(z) {
        if (z.matches) { // If media query matches
            $('.signature').html("Remove");
        } else {
            $('.signature').html("X")
        }
    }

    var z = window.matchMedia("(max-width: 575px)");
    myFunction(z); // Call listener function at run time
    z.addListener(myFunction); // Attach listener function on state changes

    //global variable
    let x = [];
    let y = [];
    let height = [];
    let width = [];
    let filesToUpload = [];
    let title = [];
    let filesToUploadCounter = 0;

    // Element HTML for Image Preview

    let getImgPreview = (imgSrc, id, titlee) => {
        return `                
                <div class="form-group mb-3 p-3 imgContainer" >
                    <div class="form-row form-row-1">
                        <div class="custom-image-preview" style="background-image:url('${imgSrc}'); border: 1px solid gainsboro"></div>
                        <button type="button" style="background-color: #676767" class="ml-3 signature remove " data-id='${id}'>X</button>
                        <button type="button" style="background-color: #777879"  class="ml-3 cropModal custom-button" data-id='${id}'>Crop This Image</button>
                        
                    </div>
                    <input style="height: 40px" type="hidden" name="title" class="input-text" value="${titlee}" data-id='${id}'>
                    <input style="height: 40px" type="hidden" name="x" class="input-text" value="" data-id='${id}'>
                    <input style="height: 40px" type="hidden" name="y" class="input-text" value="" data-id='${id}'>
                    <input style="height: 40px" type="hidden" name="height" class="input-text" value="" data-id='${id}'>
                    <input style="height: 40px" type="hidden" name="width" class="input-text" value="" data-id='${id}'>
                </div>
                `;
    };

    // Triggers when (new) images are selected with 'Choose files'
    $('.uploadFileHotel').on('change', (e) => {
        for (file of e.target.files) {
            let fileDataId = file.dataId = filesToUploadCounter++; // Update global counter of image files and set dataId member of current file to current count
            filesToUpload.push(file); // Push the current file with unique dataId to global image files object array
            a = readAndPreview(file, fileDataId);
        }
        $('.uploadFileHotel').val('');

        function readAndPreview(file, fileId) {
            //createObjectURL used instead of file reader and readDataURL because createObjectURL is synchronous.
            let url = URL.createObjectURL(file);
            let titlee = $(e.target).parent().parent().find('.ind-title').val();
            $(e.target).parent().parent().parent().parent().find('#boxes').append(getImgPreview(url, fileId, titlee));
        }
    });

    // Triggers when 'x' (Remove) button is clicked
    $(document).on('click', '.remove', (e) => {
        let fileDataId = $(e.target).data('id'); // Get the dataId value of image to be removed
        $(e.target).closest('.imgContainer').remove(); // Remove the image preview element from DOM#}
        // Filters image files from global object array by returning only those objects with dataId not equal to dataId of selected image to be removed
        filesToUpload = filesToUpload.filter(file => file.dataId != fileDataId);
    });
    let golbalE;
    let globalefileDataId;
    $(document).on('click', '.cropModal', (e) => {
        golbalE = e;
        let fileDataId = $(e.target).data('id'); // Get the dataId value of image
        globalefileDataId = fileDataId;
        fileToCrop = filesToUpload.filter(file => file.dataId == fileDataId);
        let url = URL.createObjectURL(fileToCrop[0]);
        $("#image").attr("src", url);
        $("#modalCrop").modal("show");

    });
    $(".js-crop-and-upload").click(function () {
        e = golbalE;
        fileDataId = globalefileDataId;
        let cropData = $image.cropper("getData");
        $(e.target).parent().parent().find('input[name="x"][data-id="' + fileDataId + '"] ').val(cropData["x"]);
        $(e.target).parent().parent().find('input[name="y"][data-id="' + fileDataId + '"]').val(cropData["y"]);
        $(e.target).parent().parent().find('input[name="height"][data-id="' + fileDataId + '"]').val(cropData["height"]);
        $(e.target).parent().parent().find('input[name="width"][data-id="' + fileDataId + '"]').val(cropData["width"]);

        //ajax call for image preview
        $imagePreview = $(e.target).parent().parent().find(".custom-image-preview");
        let formData = new FormData();
        fileToCrop = filesToUpload.filter(file => file.dataId == fileDataId);
        formData.append('model', 'hotel_inventory');
        formData.append('image', fileToCrop[0]);
        formData.append('x', cropData["x"]);
        formData.append('y', cropData["y"]);
        formData.append('height', cropData["height"]);
        formData.append('width', cropData["width"]);
        var url = window.location.origin;
        $('#loader').css('display', 'block');
        $.ajax({
            async: true,
            method: 'POST',
            url: url + '/myCropper/',
            data: formData,
            processData: false, // IMPORTANT: Without this, ajax will not send formData object correctly
            contentType: false, // IMPORTANT: Without this, ajax will not send formData object correctly
        }).done((result) => {
            console.log("------done------");
            console.log(result.img_content);
            $('#loader').css('display', 'none');
            $imagePreview.css('background-image', "url('" + result.img_content + "'");

        }).fail((error) => {
            console.log("------fail------");
            $('#loader').css('display', 'none');
            console.log(error);
        });
        $("#modalCrop").modal('toggle');
    });
    let $image = $("#image");
    let cropBoxData;
    let canvasData;
    $("#modalCrop").on("shown.bs.modal", function () {
        $image.cropper({
            viewMode: 1,
            aspectRatio: 16 / 9,
            // preview: '.imagePreview',
            ready: function () {
                $image.cropper("setCanvasData", canvasData);
                $image.cropper("setCropBoxData", cropBoxData);
            }
        });
    }).on("hidden.bs.modal", function () {
        $image.cropper("destroy");
    });


    // Triggers when 'Upload' button is clicked
    $('#drop-images').on('submit', (e) => {
        // debugger;


        e.preventDefault();
        $('#submitvalue').val('hello');
        // console.log('here');
        // console.log($(this).val());
        // alert('check console');

        let formData = new FormData();

        // Put the array of files (image objects) into the FormData object
        for (file of filesToUpload) {
            formData.append('files[]', file);
            title.splice(file.dataId, 0, $('input[name^="title"][data-id^=' + file.dataId + ']').val());
            x.splice(file.dataId, 0, $('input[name^="x"][data-id^=' + file.dataId + ']').val());
            y.splice(file.dataId, 0, $('input[name^="y"][data-id^=' + file.dataId + ']').val());
            height.splice(file.dataId, 0, $('input[name^="height"][data-id^=' + file.dataId + ']').val());
            width.splice(file.dataId, 0, $('input[name^="width"][data-id^=' + file.dataId + ']').val());
        }
        for (t of title) {
            formData.append('title[]', t);
        }
        for (xcord of x) {
            formData.append('x[]', xcord);
        }
        for (ycord of y) {
            formData.append('y[]', ycord);
        }
        for (h of height) {
            formData.append('height[]', h);
        }
        for (w of width) {
            formData.append('width[]', w);
        }
        var hotel_id = $('#hotel_id').val();
        title = $('.title').val();
        formData.append('hotel_id', hotel_id);
        register = $(document.activeElement).val();
        //send value of submit button
        formData.append('register', register);
        // Send the FormData object to server
        // url = '{% url \'travel_tour:tour-package-gallery-store\' %}'
        var url = window.location.origin;
        $('#loader').css('display', 'block');
        $.ajax({
            async: true,
            method: 'POST',
            url: url + '/hotel/gallery/store/',
            data: formData,
            processData: false, // IMPORTANT: Without this, ajax will not send formData object correctly
            contentType: false, // IMPORTANT: Without this, ajax will not send formData object correctly
        }).done((result) => {
            console.log("------done------");
            console.log(result.a);
            $('#loader').css('display', 'block');
            window.location.href = result.a;

        }).fail((error) => {
            console.log("------fail------");
            $('#loader').css('display', 'none');
            console.log(error);
        });

    });
});

