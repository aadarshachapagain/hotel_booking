let imageCrop = $(function () {

    /* SCRIPT TO OPEN THE MODAL WITH THE PREVIEW */
    let filesToUpload = [];
    $("#id_file").change(function () {
        if (this.files && this.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $("#image").attr("src", e.target.result);
                $("#modalCrop").modal("show");
            };
            reader.readAsDataURL(this.files[0]);
            filesToUpload.push(this.files[0]);
        }

    });

    /* SCRIPTS TO HANDLE THE CROPPER BOX */
    var $image = $("#image");
    var cropBoxData;
    var canvasData;
    $("#modalCrop").on("shown.bs.modal", function () {
        $image.cropper({
            viewMode:1,
            aspectRatio: 16 / 9,
            // preview: '.imagePreview',
            ready: function () {
                $image.cropper("setCanvasData", canvasData);
                $image.cropper("setCropBoxData", cropBoxData);
            }
        });
    }).on("hidden.bs.modal", function () {
        $image.cropper("destroy");
        // $('#id_file').val('');
    });

// Enable zoom in button
    $(".js-zoom-in").click(function () {
        $image.cropper("zoom", 0.1);
    });

// Enable zoom out button
    $(".js-zoom-out").click(function () {
        $image.cropper("zoom", -0.1);
    });

    /* SCRIPT TO COLLECT THE DATA */
    $(".js-crop-and-upload").click(function () {
        var cropData = $image.cropper("getData");
        // let url = URL.createObjectURL($image);
        $imagePreview = $(".imagePreview");
        let formData = new FormData();
        for (file of filesToUpload) {
            formData.append('image', file);
        }
        formData.append('model',$("input[name='modelForCrop']").val());
        formData.append('x',cropData["x"]);
        formData.append('y',cropData["y"]);
        formData.append('height',cropData["height"]);
        formData.append('width',cropData["width"]);
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
            $imagePreview.css('background-image' , "url('"+ result.img_content+"'");

        }).fail((error) => {
            console.log("------fail------");
            $('#loader').css('display', 'none');
            console.log(error);
        });
        $("input[name='x']").val(cropData["x"]);
        $("input[name='y']").val(cropData["y"]);
        $("input[name='height']").val(cropData["height"]);
        $("input[name='width']").val(cropData["width"]);
        $("#modalCrop").modal('toggle');
        // $("#formUpload").submit();
    });

});