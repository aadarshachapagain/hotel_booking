  $(document).ready(function () {
            // {#  To select all room Amenties/Facilities#}
            $('#select_all').on('click', function () {
                if (this.checked) {
                    $('.checkbox').each(function () {
                        this.checked = true;
                    });
                } else {
                    $('.checkbox').each(function () {
                        this.checked = false;
                    });
                }
            });

        // {#  To select all room Feature#}
             $('#select_all_room_feature').on('click', function () {
                if (this.checked) {
                    $('.checkbox_room_feature').each(function () {
                        this.checked = true;
                    });
                } else {
                    $('.checkbox_room_feature').each(function () {
                        this.checked = false;
                    });
                }
            });
        });

