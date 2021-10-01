$(".imgAdd").click(function () {
    $(this).closest(".row").find('.imgAdd').before('<div class="col-sm-2 imgUp"><div class="imagePreview"></div><label class="btn btn-primary imageclass">Upload<input type="file" class="uploadFile img" value="Upload Photo" style="width:0px;height:0px;overflow:hidden;"></label><i class="fa fa-times del"></i></div>');
});

$(function () {
    $(document).on("change", ".uploadFile", function () {
        // var numFiles = $(this).get(0).files.length
        // document.getElementById("demo").innerHTML = numFiles;

        var uploadFile = $(this);
        var files = !!this.files ? this.files : [];
        if (!files.length || !window.FileReader) return; // no file selected, or no FileReader support
        if (/^image/.test(files[0].type)) { // only image file
            var reader = new FileReader(); // instance of the FileReader
            reader.readAsDataURL(files[0]); // read the local file
            reader.onloadend = function () { // set image data as background of div
                //alert(uploadFile.closest(".upimage").find('.imagePreview').length);
                uploadFile.closest(".imgUp").find('.imagePreview').css("background-image", "url(" + this.result + ")");
                uploadFile.closest(".imgUp").find('.oldimagestatus').val('changed');
                uploadFile.closest(".imgUp").find('.newimagestatus').val('changed');
                uploadFile.closest(".imgUp").find('.statusMy').val('changed');
            }
        }
    });
});

$('.imageresetclass').on('click', function() {
    $(this).parent().children().eq(1).val('unchanged');
    $(this).parent().children().eq(2).children().eq(0).val('');
    $(this).parent().children().eq(0).css('background-image','')
});

let mainTitle = function (uploadFile) {
    let temp1 = [];
    let presentTile = uploadFile.closest(".imgUp").find('.ind-title').val();
    let mainTile = $(".main-title");
    if (mainTile.val() != "") {
        let temp2 = (mainTile.val()).split(',');
        temp1 = $.merge(temp1, temp2);
    }
    let idx = $.inArray(presentTile, temp1);
    if (idx == -1) {
        temp1.push(presentTile);
    }
    mainTile.val(temp1);
};



