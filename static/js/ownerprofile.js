   $(document).ready(function () {
            getfilename();
            init();
        });

        let init = function () {
            is_manager = $('#hidden_is_manager').val();
            if (is_manager == 'True') {
                $('#is_manager').prop('checked', true);
            }
            is_owner = $('#hidden_is_owner').val();
            if (is_owner == 'True') {
                $('#is_owner').prop('checked', true);
            }
            country = $('#hidden_country').val();
            $('#country').val(country);

            document_type = $('#hidden_document_type').val();
            $("input[name=document_type][value=" + document_type + "]").attr('checked', 'checked');

        }

        let getfilename = function () {
            $('#document').change(function (e) {
                var fileName = e.target.files[0].name;
                $('#file_name').text('Uploaded File:' + fileName);
            });

        }