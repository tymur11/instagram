function coment(){
    $('#Button').click(function(){
        $.ajax($('#Button').data('url'),{
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken':$('input[name="csrfmiddlewaretoken"]').val(),
                'text': $('#text').val()
            },
            'success': function(zxc){
                document.getElementById('div').innerHTML += zxc

            }
            
            
        })
    })
}

$(document).ready(function(){
    coment()


})