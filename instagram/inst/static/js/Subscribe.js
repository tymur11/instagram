function qw(){
    $('#button').click(function(){
        $.ajax($('#button').data('url'),
        {
            'dataType': 'json',
            'type': 'POST',
            'async': true,
            'data': {'csrfmiddlewaretoken':$('input[name="csrfmiddlewaretoken"]').val()},
            'success': function(qwe){
                $('#button').text(qwe.follow)
                $('#NFollow').text(qwe.NFollow)
                $('#NFolowers').text(qwe.NFollowers)
            }
        })  
    })
}

$(document).ready(function(){
    qw()
})