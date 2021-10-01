$(document).ready(() => {
window.onbeforeunload = null;
    // $('#loader').css({'display': 'block'});

    // Maintain global object array for image files and its member count
    let filesToUpload = [];
    let title = [];
    let filesToUploadCounter = 0;

    // Element HTML for Image Preview

    let getImgPreview = (imgSrc, id) => {
        return `
                <div class="row" style="width:100%">
                    <div class="col-md-3">
                        <div class="custom-image-preview" style="background-image:url('${imgSrc}')"></div>
                    </div>
                    <div class="col-md-7" style="margin:auto">
                        <div class="form-group row custom-form-group">
                            <label class="custom-form-label">Image Title</label>
                            <div class="col-md-9">
                                <input class="form-control custom-input-box" type="text" name="title" value="" required>
                                <small class="custom-form-hint">Example: Travel Route"</small>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-2">
                        <button class="signature remove" data-id='${id}'>X</button>
                    </div>
                </div>
                `;
    };

     // Triggers when (new) images are selected with 'Choose files'
    $('#image').on('change', (e) => {
        console.log(e.target.files);
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
        e.returnValue = '';
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
        var travelID = $('#travel_id').val();
        title = $('.title').val();
        formData.append('travelID', travelID);

        // Send the FormData object to server
        // url = '{% url \'travel_tour:tour-package-gallery-store\' %}'
        var url = window.location.origin;
        $('#loader').css('display', 'block');

        $.ajax({
            async: false,
            method: 'POST',
            url: url + '/travel_tour/gallery/store/',
            data: formData,
            processData: false, // IMPORTANT: Without this, ajax will not send formData object correctly
            contentType: false, // IMPORTANT: Without this, ajax will not send formData object correctly
        }).done((result) => {
            // $('#loader').css('display', 'none');
            console.log("------done------");
            console.log(result.c);
            window.location.href = result.c;

        }).fail((error) => {
            console.log("------fail------");
            $('#loader').css('display', 'none');
            console.log(error);
        });
    });
});

