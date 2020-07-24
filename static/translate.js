$(function() {
        $('.word').bind('click', function() {
            var id = $(this).attr('id');
            $('#myPopup'+ id).toggleClass('show');
            $.getJSON('/_translate', {
                word : $('span#' + id).text() ,
            },
            function(data) {
                      $('#myPopup' + id).text(data.result);
                    console.log($('#myPopup' + id).text(data.result)) 
            });
            return false;
        });
});
