 $(document).ready(function () {
            // document is loaded and DOM is ready
            var sendcountryini = document.getElementById('country').value;
            var url = window.location.origin;
            $.ajax({
                async: false,
                method: 'GET',
                url: url + '/hotel/address/update/getstate',
                data: {'sendcountry': sendcountryini},
                dataType: 'json',
                success: function (data) {
                    var ParsedData = JSON.parse(data);
                    $.each(ParsedData, function (i, obj) {
                        $('#state').append($('<option>').text(obj.fields.name).attr('value', obj.pk));
                    });
                }
            }).done((result) => {
                console.log("------done------");
            }).fail((error) => {
                console.log("------fail------");
                console.log(error);
            });
        });
        $(document).on("change", "#country", function () {
            var countryId = this.value;
            var sendcountry = countryId;
            var url = window.location.origin;
            $.ajax({
                async: false,
                method: 'GET',
                url: url + '/hotel/address/update/getstate',
                data: {'sendcountry': sendcountry},
                dataType: 'json',
                success: function (data) {
                    console.log('success from select country')
                    var ParsedData = JSON.parse(data);
                    $('#state').empty();
                    $('#state').append($('<option>').text("Select"));
                    $.each(ParsedData, function (i, obj) {
                        $('#state').append($('<option>').text(obj.fields.name).attr('value', obj.pk));
                    });
                }
            }).done((result) => {
                console.log("------done------");
            }).fail((error) => {
                console.log("------fail------");
                console.log(error);
            });
        });