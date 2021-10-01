$('#searchForm').on('submit', (e) => {
    $('#loader').css('display', 'block');
    e.preventDefault();
    var url = window.location.origin;
    // let formData = new FormData();
    formData = $('#searchForm').serialize();
    $("#roomSearchTable").empty();
    $("#resultHeading").remove();
    $.ajax({
        async: true,
        method: 'POST',
        url: url + '/hotel/check_available/',
        data: formData,
        dataType: 'json',
        // processData: false, // IMPORTANT: Without this, ajax will not send formData object correctly
        // contentType: false, // IMPORTANT: Without this, ajax will not send formData object correctly
    }).done((result) => {
        console.log("------done------");
        // console.log(result.myData.length);
        $('.resultWrapper').show();
        // $('.checkSearch').css('grid-template-rows','1fr 2fr');
        $(".resultChild").prepend('<div id="resultHeading" style="letter-spacing: 0.9px;    border-top: 1px solid gainsboro; padding-left: 25px; padding-top: 24px !important;"><p style="color: black; ">Rooms Available <br/> <span style="font-size: 12px; color: #9d9d9d">From ' + result.myData[0].start_date + ' To ' + result.myData[0].end_date + '.</span></p><hr style="border-bottom: 1px solid #68153c"></div>');
        // $('#resultHeading').append('\n');
        if (result.message != 'success') {
            $("#roomSearchTable").append('<p style="padding: 6px;">We are sorry there are no any rooms available for provided data.</p>');
        } else {

            var myContent = "<tbody>";
            for (i = 1; i < result.myData.length; i++) {
                myContent += '<tr>' +
                    '<td width="20%">' + i + '.</td>' +
                    '<td width="80%" >' + result.myData[i].name + '</td>' +
                    '</tr>' +
                    '<tr>'+
                    '<td></td>'+
                    '<td style="color: #68153c"><li>'+result.myData[i].available + ' Available.</li></td>' +
                    '</tr>' +
                    '<br/>';
            }
            myContent += "</tbody>";
            $("#roomSearchTable").append(myContent);
        $('#loader').css('display', 'none');
        }
    }).fail((error) => {
        console.log("------fail------");
        $('#loader').css('display', 'none');
        console.log(error);
    });
});


