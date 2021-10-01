<script>
        function removeRow(el) {
            var a = $(el).parent().parent().children().eq(0);
            var selectedFile = a.children().eq(1).prop('value');
            var fileUpload = document.getElementById("image");
            {#var array = [];#}

            for (var i = 0; i < fileUpload.files.length; i++) {
                var array = fileUpload.files[i];
                {#alert(array[i]);#}
            }
            for (var i = 0; i < array.length; i++) {
                if (array[i].name === selectedFile) {
                    array.splice(i, 1);
                }
            }
            for (var i = 0; i < array.length; i++) {
                var reader = new FileReader();
                var file = array[i];
                {#alert(array[i].name);#}
                {#var file = array[i];#}
                {#fileUpload.append("files", array[i]);#}
                {#alert(fileUpload.files[i].name);#}
                {#alert(array[i]);#}
            }
            $(el).parent().parent().remove();
        }


        var fileUpload = document.getElementById("image");
        fileUpload.onchange = function () {
            if (typeof (FileReader) != "undefined") {
                var parent = document.getElementById("boxes");
                var regex = /^([a-zA-Z0-9\s_\\.\-:])+(.jpg|.jpeg|.gif|.png|.bmp)$/;
                for (var i = 0; i < fileUpload.files.length; i++) {
                    var file = fileUpload.files[i];
                    if (regex.test(file.name.toLowerCase())) {
                        var reader = new FileReader();
                        let fileDataId = file.dataId = filesToUploadCounter++; // Update global counter of image files and set dataId member of current file to current count
                        filesToUpload.push(file); // Push the current file with unique dataId to global image files object array
                        var k = 0;
                        reader.onload = function (e) {
                            k = k + 1;

                            {#creating required fields for miltiple uploads.#}
                            var child = document.createElement("DIV");
                            var childDiv = document.createElement("DIV");
                            var imagePreview = document.createElement("DIV");
                            var imageName = document.createElement("INPUT");
                            var removeDiv = document.createElement("DIV");
                            var removeButton = document.createElement("BUTTON");
                            {#for title#}
                            var titleParentDiv = document.createElement("DIV");
                            var titleDiv = document.createElement("DIV");
                            var titleLabel = document.createElement("LABEL");
                            var titleChildDiv = document.createElement("DIV");
                            var titleInput = document.createElement("INPUT");
                            var titleHint = document.createElement("SMALL");
                            {#for title#}
                            {#creating required fields for miltiple uploads.#}

                            {# setting attribute for child div which holds all content #}
                            child.setAttribute('class', 'row');
                            child.style.width = "100%";
                            {# setting attribute for child div which holds all content #}


                            {#setting attributes for image preview#}
                            childDiv.setAttribute('class', 'col-md-3');
                            imagePreview.setAttribute('class', 'custom-image-preview');
                            imagePreview.style.backgroundImage = "url('" + e.target.result + "')";
                            {#setting attributes for image preview#}

                            {#setting attributes for image name input field#}
                            imageName.setAttribute('type', 'hidden');
                            imageName.setAttribute('name', 'imageName');
                            imageName.setAttribute('value', fileUpload.files[k - 1].name);
                            {#setting attributes for image name input field#}

                            {#setting attributes for image title box#}
                            titleParentDiv.setAttribute('class', 'col-md-7');
                            titleParentDiv.style.margin = "auto";
                            titleDiv.setAttribute('class', 'form-group row custom-form-group');
                            titleLabel.setAttribute('class', 'custom-form-label col-md-3');
                            titleLabel.innerHTML = "Image Title";
                            titleChildDiv.setAttribute('class', 'col-md-9');
                            titleInput.setAttribute('class', 'form-control custom-input-box');
                            titleInput.setAttribute('type', 'text');
                            titleInput.setAttribute('name', 'title');
                            titleHint.setAttribute('class', 'custom-form-hint');
                            titleHint.innerHTML = "Example: Travel Route";
                            {#setting attributes for image title box#}

                            {#setting attributes for remove button#}
                            removeDiv.setAttribute('class', 'col-md-2');
                            removeButton.innerHTML = "X";
                            removeButton.setAttribute('class', 'signature');
                            removeButton.setAttribute('onclick', 'removeRow(this)');
                            removeButton.setAttribute('type', 'button');
                            {#setting attributes for remove button#}

                            {# Append child to respective parent #}
                            parent.appendChild(child);
                            child.appendChild(childDiv);
                            childDiv.appendChild(imagePreview);
                            childDiv.appendChild(imageName);
                            child.appendChild(titleParentDiv);
                            child.appendChild(removeDiv);
                            removeDiv.appendChild(removeButton);
                            titleParentDiv.appendChild(titleDiv);
                            titleDiv.appendChild(titleLabel);
                            titleDiv.appendChild(titleChildDiv);
                            titleChildDiv.appendChild(titleInput);
                            titleChildDiv.appendChild(titleHint);
                            {# Append child to respective parent #}

                        };

                        reader.readAsDataURL(file);
                    } else {
                        alert(file.name + " is not a valid image file.");
                        return false;
                    }
                }
            } else {
                alert("This browser does not support HTML5 FileReader.");
            }
        };
    </script>