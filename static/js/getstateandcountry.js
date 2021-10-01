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
      $("#country").change(function () {
          var sendcountryini = $(this).children("option:selected").val();
          $.ajax({
              async: false,
              method: 'GET',
              url: url + '/hotel/address/update/getCountryPhone',
              data: {'sendcountry': sendcountryini},
              dataType: 'json',
              success: function (data) {
                  var ParsedData = JSON.parse(data);
                  $.each(ParsedData, function (i, obj) {
                      var existingValue = $('#contact1').val();
                      console.log(existingValue)
                      if (existingValue.indexOf('-') != -1) {
                           var s = existingValue.split('-', existingValue.length);
                           existingValue = s[1]
                      }
                      var existingValue1 = $('#contact2').val();
                      if (existingValue1.indexOf('-') != -1) {
                           var s = existingValue1.split('-', existingValue1.length);
                           existingValue1 = s[1]
                      }
                      $('#contact1').val(obj.fields.code + '-' + existingValue);
                      $('#contact2').val(obj.fields.code + '-' + existingValue1);
                  });
              }
          }).done((result) => {
              console.log("------done------");
          }).fail((error) => {
              console.log("------fail------");
              console.log(error);
          });
      });

      var sendstate = document.getElementById('state').value;

                $.ajax({
                    async: false,
                    method: 'GET',
                    url: url + '/hotel/address/update/getcity',
                    data: {'sendstate': sendstate},
                    dataType: 'json',
                    success: function (data) {
                        var ParsedData = JSON.parse(data);
                        console.log('Parsed Data: for city:')
                        console.log(ParsedData)
                        $.each(ParsedData, function (i, obj) {
                            $('#city').append($('<option>').text(obj.fields.name).attr('value', obj.pk));
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
                        var ParsedData = JSON.parse(data);
                        $('#state').empty();
                        $('#state').append($('<option>').text("Select"));
                        $('#city').empty();
                        $('#city').append($('<option>').text("Select"));
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

            $(document).on("change", "#state", function () {
                var stateId = this.value;
                var sendstate = stateId;
                var url = window.location.origin;
                $.ajax({
                    async: false,
                    method: 'GET',
                    url: url + '/hotel/address/update/getcity',
                    data: {'sendstate': sendstate},
                    dataType: 'json',
                    success: function (data) {
                        var ParsedData = JSON.parse(data);
                        $('#city').empty();
                        $('#city').append($('<option>').text("Select"));
                        $.each(ParsedData, function (i, obj) {
                            $('#city').append($('<option>').text(obj.fields.name).attr('value', obj.pk));
                        });
                    }
                }).done((result) => {
                    console.log("------done------");

                }).fail((error) => {
                    console.log("------fail------");
                    console.log(error);
                });
            });