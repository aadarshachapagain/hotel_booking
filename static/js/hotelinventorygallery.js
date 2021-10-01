$(document).ready(() => {
    // Maintain global object array for image files and its member count
    function myFunction(x) {
        if (x.matches) { // If media query matches
            $('.signature').html("Remove");
        } else {
            $('.signature').html("X")
        }
    }
    var x = window.matchMedia("(max-width: 575px)");
    myFunction(x); // Call listener function at run time
    x.addListener(myFunction); // Attach listener function on state changes

    let filesToUpload = [];
    let title = [];
    let filesToUploadCounter = 0;

    // Element HTML for Image Preview

    let getImgPreview = (imgSrc, id) => {
        return `                
                <div class="form-group mb-3 p-3" style="background-color: #fcfcfc">
                    <div class="form-row form-row-1">
                        <div class="custom-image-preview" style="background-image:url('${imgSrc}'); border: 1px solid gainsboro"></div>
                    </div>
                        <div class="form-row form-row-1 ">
                            <label for="cname">Title *</label>
                            <input style="height: 40px" type="text" name="title" class="input-text" value="">
                        </div>
                    <div class="form-row form-row-1 " style="width: 5%">
                        <button class="signature remove " data-id='${id}'>X</button>
                    </div>
                </div>
                `;
    };

    // Triggers when (new) images are selected with 'Choose files'
    $('#image').on('change', (e) => {
        for (file of e.target.files) {
            let fileDataId = file.dataId = filesToUploadCounter++; // Update global counter of image files and set dataId member of current file to current count
            filesToUpload.push(file); // Push the current file with unique dataId to global image files object array
            a = readAndPreview(file, fileDataId);
        }

        function readAndPreview(file, fileId) {
                //createObjectURL used instead of file reader and readDataURL because createObjectURL is synchronous.
                var url = URL.createObjectURL(file);
                $('#boxes').append(getImgPreview(url, fileId));
        }
    });

    // Triggers when 'x' (Remove) button is clicked
    $(document).on('click', '.remove', (e) => {
        let fileDataId = $(e.target).data('id'); // Get the dataId value of image to be removed
        $(e.target).closest('.imgContainer').remove(); // Remove the image preview element from DOM#}
        $(e.target).parent().parent().remove();

        // Filters image files from global object array by returning only those objects with dataId not equal to dataId of selected image to be removed
        filesToUpload = filesToUpload.filter(file => file.dataId != fileDataId);
        // alert(filesToUpload.dataId);
    });


    // Triggers when 'Upload' button is clicked
    $('#drop-images').on('submit', (e) => {
        e.preventDefault();
        let formData = new FormData();

        // Put the array of files (image objects) into the FormData object
        for (file of filesToUpload) {
            formData.append('files[]', file);
        }
        $('input[name^="title"]').each(function () {
            title.push($(this).val());

        });
        for (t of title) {
            formData.append('title[]', t);
        }
        var hotel_inventory_id = $('#hotel_inventory_id').val();
        title = $('.title').val();
        formData.append('hotelInventoryId', hotel_inventory_id);
        register = $("input[type=submit][clicked=true]").val();
        //send value of submit button
        formData.append('register', register);

        // Send the FormData object to server
        // url = '{% url \'travel_tour:tour-package-gallery-store\' %}'
        var url = window.location.origin;
        $('#loader').css('display', 'block');

        $.ajax({
            async: true,
            method: 'POST',
            url: url + '/hotel/invgallery/store/',
            data: formData,
            processData: false, // IMPORTANT: Without this, ajax will not send formData object correctly
            contentType: false, // IMPORTANT: Without this, ajax will not send formData object correctly
        }).done((result) => {
            console.log("------done------");
            console.log(result.a);
            window.location.href = result.a;

        }).fail((error) => {
            console.log("------fail------");
            $('#loader').css('display', 'none');

            console.log(error);
        });
    });
});

