$(document).ready(function(){
    //  by id
    var container = $('#container');
    // by class
    $('.hide-btn').click(function(){
        container.hide();
    });
    $('.show-btn').click(function(){
        container.show();
    });

    $(".choice").change(function(){
        $('.user-form').hide();
        switch($(this).val()) {
            case "student":
                $('.student-form').show();
                break;
            case 'teacher':
                $('.teacher-form').show();
                break;
            case 'other':
                $('.other-form').show();
                break;
        }
    });

    $('.form-submit').click(function(event){
        // if <a> or <input>, add
        event.preventDefault();
        $('.error').html('');
        $.ajax({
            method: "POST",
            url: '/register/',
            data: $('form').serializeArray()
        }).done(function(response){
            if (response.status == 'ok') {
                alert('Success!');
            } else {
                debugger;
                for(var key in response.message) {
                    var errorDiv = $(".error." + key);
                    errorDiv.html(response.message[key][0]);
                }
            }
        }).fail(function(response){
            alert('Fail :(');
        });
    });
    //$.ajax({
    //    'method': "GET",
    //    'url': '/get_time/'
    //}).done(function(){
    //
    //});
});