$(document).ready(function () {
    $('#myFormHotel').on('submit', function (e) {
        $('#loader').css('display', 'block');
        e.preventDefault();
        var url = window.location.origin;
        var mytable = $('#datatable').DataTable();
        var rowsel = mytable.rows('.selected').ids();
        var arr = [];
        var myDict = {};
        var form = this;
        $.each(rowsel, function (index, id) {
            arr.push(id);
        });
        myDict['id'] = arr;
        console.log(myDict);
        $.ajax({
            async: true,
            method: 'POST',
            url: url + '/hotel/mass_active/',
            data: myDict,
            dataType: 'json',
        }).done((result) => {
            $('#loader').css('display', 'none');
            console.log("------done------");
            location.reload();

        }).fail((error) => {
            console.log("------fail------");
            $('#loader').css('display', 'none');
            console.log(error);
        });
    });
// mass active/inactive user
    $('#myFormUser').on('submit', function (e) {
        $('#loader').css('display', 'block');
        e.preventDefault();
        var url = window.location.origin;
        var mytable = $('#datatablee').DataTable();
        var rowsel = mytable.rows('.selected').ids();
        var arr = [];
        var myDict = {};
        var form = this;
        $.each(rowsel, function (index, id) {
            arr.push(id);
        });
        myDict['id'] = arr;
        console.log(myDict);
        $.ajax({
            async: true,
            method: 'POST',
            url: url + '/account/mass_active/',
            data: myDict,
            dataType: 'json',
        }).done((result) => {
            $('#loader').css('display', 'none');
            console.log("------done------");
            location.reload();

        }).fail((error) => {
            console.log("------fail------");
            $('#loader').css('display', 'none');
            console.log(error);
        });
    });
// {#mass active/inactive rental#}
    $('#myFormRental').on('submit', function (e) {
        $('#loader').css('display', 'block');
        e.preventDefault();
        var url = window.location.origin;
        var mytable = $('#datatable').DataTable();
        var rowsel = mytable.rows('.selected').ids();
        var arr = [];
        var myDict = {};
        var form = this;
        $.each(rowsel, function (index, id) {

            arr.push(id);
        });
        myDict['id'] = arr;
        console.log(myDict);
        $.ajax({
            async: true,
            method: 'POST',
            url: url + '/rental/company/mass_active/',
            data: myDict,
            dataType: 'json',
        }).done((result) => {
            $('#loader').css('display', 'none');
            console.log("------done------");
            location.reload();

        }).fail((error) => {
            console.log("------fail------");
            $('#loader').css('display', 'none');
            console.log(error);
        });
    });
// {#mass active/inactive travel#}
    $('#myFormTravel').on('submit', function (e) {
        $('#loader').css('display', 'block');
        e.preventDefault();
        var url = window.location.origin;
        var mytable = $('#datatable').DataTable();
        var rowsel = mytable.rows('.selected').ids();
        var arr = [];
        var myDict = {};
        var form = this;
        $.each(rowsel, function (index, id) {

            arr.push(id);
        });
        myDict['id'] = arr;
        console.log(myDict);
        $.ajax({
            async: true,
            method: 'POST',
            url: url + '/travel_tour/company/mass_active/',
            data: myDict,
            dataType: 'json',
        }).done((result) => {
            $('#loader').css('display', 'none');
            console.log("------done------");
            location.reload();

        }).fail((error) => {
            console.log("------fail------");
            $('#loader').css('display', 'none');
            console.log(error);
        });
    });
// {#mass active/inactive restaurant#}
    $('#myFormRestaurant').on('submit', function (e) {
        $('#loader').css('display', 'block');
        e.preventDefault();
        var url = window.location.origin;
        var mytable = $('#datatable').DataTable();
        var rowsel = mytable.rows('.selected').ids();
        var arr = [];
        var myDict = {};
        var form = this;
        $.each(rowsel, function (index, id) {

            arr.push(id);
        });
        myDict['id'] = arr;
        console.log(myDict);
        $.ajax({
            async: true,
            method: 'POST',
            url: url + '/restaurant/company/mass_active/',
            data: myDict,
            dataType: 'json',
        }).done((result) => {
            $('#loader').css('display', 'none');
            console.log("------done------");
            location.reload();

        }).fail((error) => {
            console.log("------fail------");
            $('#loader').css('display', 'none');
            console.log(error);
        });
    });
// {#mass active/inactive hotel approve#}
    $('#myFormHotelApprove').on('submit', function (e) {
        $('#loader').css('display', 'block');
        e.preventDefault();
        var url = window.location.origin;
        var mytable = $('#datatable').DataTable();
        var rowsel = mytable.rows('.selected').ids();
        var arr = [];
        var myDict = {};
        var form = this;
        $.each(rowsel, function (index, id) {

            arr.push(id);
        });
        myDict['id'] = arr;
        console.log(myDict);
        $.ajax({
            async: true,
            method: 'POST',
            url: url + '/hotel/mass_approve/',
            data: myDict,
            dataType: 'json',
        }).done((result) => {
            $('#loader').css('display', 'none');
            console.log("------done------");
            location.reload();

        }).fail((error) => {
            console.log("------fail------");
            $('#loader').css('display', 'none');
            console.log(error);
        });
    });
// {#mass active/inactive hotelinv approve#}
    $('#myFormHotelInvApprove').on('submit', function (e) {
        $('#loader').css('display', 'block');
        e.preventDefault();
        var url = window.location.origin;
        var mytable = $('#datatable').DataTable();
        var rowsel = mytable.rows('.selected').ids();
        var arr = [];
        var myDict = {};
        var form = this;
        $.each(rowsel, function (index, id) {

            arr.push(id);
        });
        myDict['id'] = arr;
        console.log(myDict);
        $.ajax({
            async: true,
            method: 'POST',
            url: url + '/hotel/inventory/mass_approve_inv/',
            data: myDict,
            dataType: 'json',
        }).done((result) => {
            $('#loader').css('display', 'none');
            console.log("------done------");
            location.reload();

        }).fail((error) => {
            console.log("------fail------");
            $('#loader').css('display', 'none');
            console.log(error);
        });
    });
// {#mass active/inactive rental approve#}
    $('#myFormRentalApprove').on('submit', function (e) {
        $('#loader').css('display', 'block');
        e.preventDefault();
        var url = window.location.origin;
        var mytable = $('#datatable').DataTable();
        var rowsel = mytable.rows('.selected').ids();
        var arr = [];
        var myDict = {};
        var form = this;
        $.each(rowsel, function (index, id) {

            arr.push(id);
        });
        myDict['id'] = arr;
        console.log(myDict);
        $.ajax({
            async: true,
            method: 'POST',
            url: url + '/rental/company/mass_approve/',
            data: myDict,
            dataType: 'json',
        }).done((result) => {
            $('#loader').css('display', 'none');
            console.log("------done------");
            location.reload();

        }).fail((error) => {
            console.log("------fail------");
            $('#loader').css('display', 'none');
            console.log(error);
        });
    });
// {#mass active/inactive rental inv approve#}
    $('#myFormRentalInvApprove').on('submit', function (e) {
        $('#loader').css('display', 'block');
        e.preventDefault();
        var url = window.location.origin;
        var mytable = $('#datatable').DataTable();
        var rowsel = mytable.rows('.selected').ids();
        var arr = [];
        var myDict = {};
        var form = this;
        $.each(rowsel, function (index, id) {

            arr.push(id);
        });
        myDict['id'] = arr;
        console.log(myDict);
        $.ajax({
            async: true,
            method: 'POST',
            url: url + '/rental/vehicleInventory/mass_approve_inv/',
            data: myDict,
            dataType: 'json',
        }).done((result) => {
            $('#loader').css('display', 'none');
            console.log("------done------");
            location.reload();

        }).fail((error) => {
            console.log("------fail------");
            $('#loader').css('display', 'none');
            console.log(error);
        });
    });
// {#mass active/inactive travel approve#}
    $('#myFormTravelApprove').on('submit', function (e) {
        $('#loader').css('display', 'block');
        e.preventDefault();
        var url = window.location.origin;
        var mytable = $('#datatable').DataTable();
        var rowsel = mytable.rows('.selected').ids();
        var arr = [];
        var myDict = {};
        var form = this;
        $.each(rowsel, function (index, id) {

            arr.push(id);
        });
        myDict['id'] = arr;
        console.log(myDict);
        $.ajax({
            async: true,
            method: 'POST',
            url: url + '/travel_tour/mass_approve/',
            data: myDict,
            dataType: 'json',
        }).done((result) => {
            $('#loader').css('display', 'none');
            console.log("------done------");
            location.reload();

        }).fail((error) => {
            console.log("------fail------");
            $('#loader').css('display', 'none');
            console.log(error);
        });
    });
// {#mass active/inactive travel inv approve#}
    $('#myFormTravelInvApprove').on('submit', function (e) {
        $('#loader').css('display', 'block');
        e.preventDefault();
        var url = window.location.origin;
        var mytable = $('#datatable').DataTable();
        var rowsel = mytable.rows('.selected').ids();
        var arr = [];
        var myDict = {};
        var form = this;
        $.each(rowsel, function (index, id) {
            arr.push(id);
        });
        myDict['id'] = arr;
        console.log(myDict);
        $.ajax({
            async: true,
            method: 'POST',
            url: url + '/travel_tour/mass_approve_inv/',
            data: myDict,
            dataType: 'json',
        }).done((result) => {
            $('#loader').css('display', 'none');
            console.log("------done------");
            location.reload();

        }).fail((error) => {
            console.log("------fail------");
            $('#loader').css('display', 'none');
            console.log(error);
        });
    });
// {#mass active/inactive restaurant approve#}
    $('#myFormRestaurantApprove').on('submit', function (e) {
        $('#loader').css('display', 'block');
        e.preventDefault();
        var url = window.location.origin;
        var mytable = $('#datatable').DataTable();
        var rowsel = mytable.rows('.selected').ids();
        var arr = [];
        var myDict = {};
        var form = this;
        $.each(rowsel, function (index, id) {
            arr.push(id);
        });
        myDict['id'] = arr;
        console.log(myDict);
        $.ajax({
            async: true,
            method: 'POST',
            url: url + '/restaurant/company/mass_approve/',
            data: myDict,
            dataType: 'json',
        }).done((result) => {
            $('#loader').css('display', 'none');
            console.log("------done------");
            location.reload();

        }).fail((error) => {
            console.log("------fail------");
            $('#loader').css('display', 'none');
            console.log(error);
        });
    });
// {#mass active/inactive restaurant inv approve#}
    $('#myFormRestaurantInvApprove').on('submit', function (e) {
        $('#loader').css('display', 'block');
        e.preventDefault();
        var url = window.location.origin;
        var mytable = $('#datatable').DataTable();
        var rowsel = mytable.rows('.selected').ids();
        var arr = [];
        var myDict = {};
        var form = this;
        $.each(rowsel, function (index, id) {
            arr.push(id);
        });
        myDict['id'] = arr;
        console.log(myDict);
        $.ajax({
            async: true,
            method: 'POST',
            url: url + '/restaurant/restaurantInventory/mass_approve_inv/',
            data: myDict,
            dataType: 'json',
        }).done((result) => {
            $('#loader').css('display', 'none');
            console.log("------done------");
            location.reload();

        }).fail((error) => {
            console.log("------fail------");
            $('#loader').css('display', 'none');
            console.log(error);
        });
    });
});