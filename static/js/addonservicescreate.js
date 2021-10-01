class AddonService {
    facid = 0;
    facname = '';
    facprice = 0;
    flatorpercent = '';
}

$(document).ready(function () {
    /*intially hide service module*/
    $("#avail_service").hide();
    /*show and hide service-module on click*/
    $("#adonserv").on('click', function (event) {
        $("#avail_service").toggle();
    });
    /*show and hide service-module on click*/

//    append paid facilities field
    $(".adonfacs").on('click', function (event) {
        var checked_status = $(this).prop("checked");
        console.log('checked_status:' + checked_status);
        //mutually exclusive Free Checkbox changed status
        free_checkbox = this.parentNode.parentNode.parentNode.childNodes[3].childNodes[2].childNodes[0];
        if (free_checkbox) {
            $(free_checkbox).prop('checked', !checked_status);
        }
        //mutually exclusive Free Checkbox changed status

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
//    append paid facilities field

    //obtain json of paid amenties and free amenties
    $("#save_all_serv").on('click', function (event) {
        selected_fac_id = [];
        chosen_fac_id = [];
        choosen_fac_list = [];
        choosen_fac_id_list = [];
        free_selected_fac_id = [];


        /*For Paid FAcilities*/

        $(".adonfacs").each(function () {
            fac_checked = $(this).prop("checked");
            if (fac_checked == true) {
                selected_fac_id.push(this.name);
            }
        });

        if (selected_fac_id) {
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

        }

        json_choosen_fac_list = JSON.stringify(choosen_fac_list);
        document.getElementById('paidservices').value = json_choosen_fac_list;
        console.log('json_choosen_fac_list')
        console.log(json_choosen_fac_list);
        /*For Paid FAcilities*/
        /*For Free Facilities*/

        $(".freefacs").each(function () {
            free_fac_checked = $(this).prop("checked");
            if (free_fac_checked == true) {
                free_selected_fac_id.push(this.name);
            }
        });

        json_free_fac_list = JSON.stringify(free_selected_fac_id);
        document.getElementById('freeservices').value = json_free_fac_list;
        console.log('json_free_fac_list');
        console.log(json_free_fac_list);
        /*For Free Facilities*/


    });
    //obtain json of paid amenties and free amenties

});

let makejson = function () {


}