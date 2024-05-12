function qw(){
    $('#button').click(function(){
        $.ajax($('#button').data('url'),
        {
            'dataType': 'json',
            'type': 'POST',
            'async': true,
            'data': {'csrfmiddlewaretoken':$('input[name="csrfmiddlewaretoken"]').val()},
            'success': function(qwe){
                if ($('#button').text() == 'UnFollow'){
                    $('#button').attr('class', 'mx-3 btn btn-primary')
                }
                else{
                    $('#button').attr('class', 'mx-3 btn btn-secondary')
                }
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