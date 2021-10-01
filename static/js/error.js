$(document).ready(function () {
    reqElement = document.getElementsByClassName('errorlist');
    if (reqElement.length) {
        let errorList = document.getElementsByClassName('errorlist')[0].innerText;
        cleanErrorArray = errorList.split("\n");
        cleanErrorArray.splice(0, 0, 'tostartarrayfrom1');
        fields = [];
        msg = [];
        for (j = 1; j < cleanErrorArray.length; j++) {
            fieldName = '';
            errorMessage = '';
            if (j % 2 == 0) {
                errorMessage = cleanErrorArray[j]
                msg.push(errorMessage);
            } else if (j % 2 != 0) {
                fieldName = cleanErrorArray[j];
                fields.push(fieldName);
            }
        }
        for (k = 0; k < fields.length; k++) {
            startHtml = `<div style="background-color: white; color:red;box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.15);border:none; font-family: Proxima-Light; font-size: 15px" class="alert alert-warning alert-dismissable mt-3" role="alert">
                                            <button class="close" data-dismiss="alert">
                                                <small><sup>X</sup></small>
                                            </button>`;
            $('input[name=' + fields[k] + ']').parent().append(startHtml + msg[k] + "</div>");
            $('select[name=' + fields[k] + ']').parent().append(startHtml + msg[k] + "</div>");

        }
    }

    /*if ((document.getElementById("ep_check").checked == false) && (document.getElementById('bb_check').checked == false)) {
        console.log("checking condition");
    }*/

});