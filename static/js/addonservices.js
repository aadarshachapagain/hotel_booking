$(document).ready(function () {

    class AddonService {
        facid = 0;
        facname = '';
        facprice = 0;
        flatorpercent = '';
    }

    chosen_fac_id = new Array();
    selected_fac_id = new Array();
    choosen_fac_list = [];
    choosen_fac_id_list = [];
    url = window.location.pathname;
    var inventory_id = url.match(/update\/(\d+)/)[1];
    var base_url = window.location.origin;
    var token = getCookie('csrftoken');

    $('#dialog').dialog({
        // width: 500,
        autoOpen: false,
        minHeight: 0,
        title: 'Saved Services Successfully',
    });

    $("#avail_service").hide();
    $(".freefacs").on('click', function (event) {

    });
    $(".adonfacs").on('click', function (event) {
        var checked_status = $(this).prop("checked");
        console.log('checked_status:' + checked_status);
        //mutually exclusive Free Checkbox changed status
        free_checkbox = this.parentNode.parentNode.parentNode.childNodes[3].childNodes[2].childNodes[0];
        if (free_checkbox) {
            $(free_checkbox).prop('checked', !checked_status);
        }

        if (checked_status == true) {
            var pricename = this.name + 'price';
            var flatorpercent = this.name + 'flatorpercent';

            addfields = `<div class="form-row form-row-1" style="margin:auto; padding:6px">
                            <label style="margin:auto;">Price</label>
                            <input style="width:60%" type="text" class="input-text" name=${pricename} id=${pricename}>
                            <select style="margin:auto;" name=${flatorpercent} id=${flatorpercent}>
                            <option value="0">Flat</option>
                            <option value="1">percent</option>
                            </select>
                             </div>`;
            /* {
                 #if fields are not already appended while document isready#
             }*/

            console.log('this.parentNode.childNodes[7] when adonfacs clicked ');
            console.log(!this.parentNode.childNodes[7]);
            // if (!this.parentNode.childNodes[5]) {
            // if (!this.parentNode.childNodes[7]) {
            if (!this.parentNode.parentNode.parentNode.childNodes[7]) {
                $(this.parentNode.parentNode.parentNode).append(addfields);
            }
            /*
            {
                #if fields are not already appended while document is ready #
            }*/
        } else if (checked_status == false) {
            this.parentNode.parentNode.parentNode.lastChild.remove();
        }
    });
    $("#adonserv").on('click', function (event) {
        $("#avail_service").toggle();
    });

    $("#save_all_serv").on('click', function (event) {
        /*For Paid FAcilities*/
        $(".adonfacs").each(function () {
            fac_checked = $(this).prop("checked");
            if (fac_checked == true) {
                selected_fac_id.push(this.name);
            }
        });

        for (let name of selected_fac_id.values()) {
            fac_obj = new AddonService();
            final_price_name = name + 'price';
            flatorpercent_name = name + 'flatorpercent';
            final_price_instance = document.getElementById(final_price_name);
            if (final_price_instance) {
                final_price = final_price_instance.value;
            }
            final_flatorpercent_instance = document.getElementById(flatorpercent_name);

            if (final_price_instance) {
                final_flatorpercent = final_flatorpercent_instance.value;
            }
            facid_instance = document.getElementsByName(name);
            if (facid_instance) {
                facid = facid_instance[0].value;
            }
            fac_obj.facname = name;
            fac_obj.facid = facid;
            fac_obj.flatorpercent = final_flatorpercent;
            fac_obj.facprice = final_price;
            if (choosen_fac_id_list.indexOf(facid) == -1) {
                choosen_fac_id_list.push(facid);
                choosen_fac_list.push(fac_obj)
            }
        }
        json_choosen_fac_list = JSON.stringify(choosen_fac_list);

        /*For Paid FAcilities*/

        /*For Free Facilites*/
        free_selected_fac_id = [];
        $(".freefacs").each(function () {
            free_fac_checked = $(this).prop("checked");
            if (free_fac_checked == true) {
                free_selected_fac_id.push(this.name);
            }
        });

        json_free_fac_list = JSON.stringify(free_selected_fac_id);
        console.log('json_free_fac_list');
        console.log(json_free_fac_list);


        /*For Free Facilites*/

        /* // {
         //     #Ajax Call to Post the addon services #
         // }*/
        console.log('json_choosen_fac_list');
        console.log(json_choosen_fac_list);
        url_add_services = base_url + '/hotel/inventory/addonservices/';
        $.ajax({ // create an AJAX call...
                headers: {"X-CSRFToken": token},
                async: true,
                data: {
                    'faclist': json_choosen_fac_list,
                    'inv_id': inventory_id,
                    'freefaclist': json_free_fac_list
                }, // get the form data
                type: 'POST', // GET or POST
                url: url_add_services, // the file to call
                /*{#processData:false, // IMPORTANT: Without this, ajax will not send Data object correctly#}
                {#contentType:false, #}*/
                dataType: 'json',
                success:
                    function (response) {
                        $('#dialog').dialog('open');
                        choosen_fac_list = []
                    }
            }
        ).done((result) => {
            console.log('result:');
            console.log('--done--')

        }).fail((error) => {
            console.log(error);
            console.log("---failed---");
        });

        // {# Ajax Call to Post the addon services #}


    });

    // {#initially#}
    services_instance = document.getElementById('exist_serv');
    free_services_instance = document.getElementById('free_exist_serv');
    console.log('free_services_instance');
    console.log(free_services_instance.value);

    //to Populate free services
    if (free_services_instance) {
        free_services_instance_value = JSON.parse(free_services_instance.value);
    }

    for (i = 0; i < free_services_instance_value.length; i++) {
        free_serv_to_b_selected = free_services_instance_value[i].amenities;
        free_serv_name = 'free' + free_serv_to_b_selected;
        console.log(free_serv_name);
        itemselected = document.getElementById(free_serv_name);
        itemselected.checked = true;
    }
    //to Populate free services


    if (services_instance) {
        services_instance_value = JSON.parse(services_instance.value);
    }

    for (i = 0; i < services_instance_value.length; i++) {
        console.log('services_instance_value[i]');
        console.log(services_instance_value[i]);
        id = services_instance_value[i].amenities;
        priceid = id + 'price';
        flatorpercentid = id + 'flatorpercent';
        serv_to_b_selected = services_instance_value[i].amenities;
        itemselected = document.getElementById(serv_to_b_selected);
        oldprice = parseFloat(services_instance_value[i].price);
        console.log('oldprice:' + oldprice);
        oldflatorpercent = parseFloat(services_instance_value[i].flatorpercent);
        itemselected.checked = true;

        addfields = `<div class="form-row form-row-1" style="margin:auto; padding:6px">
                            <label style="margin:auto;">Price</label>
                            <input style="width:60%" type="text" class="input-text" name=${priceid} id=${priceid} value=${oldprice}>
                            <select style="margin:auto;" name=${flatorpercentid} id=${flatorpercentid}>
                            <option value="0">Flat</option>
                            <option value="1">percent</option>
                            </select>
                             </div>`;


        if (!itemselected.parentNode.parentNode.parentNode.childNodes[7]) {
            $(itemselected.parentNode.parentNode.parentNode).append(addfields);
        }
    }

    // {#initially#}

});