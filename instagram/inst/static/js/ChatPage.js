function Chat(){
    $('#Button').click(function(){
        $.ajax($('#Button').data('url'),{
            'type': 'POST',
            'dataType': 'json',
            'async': true,
            'data': {'csrfmiddlewaretoken':$('input[name="csrfmiddlewaretoken"]').val(),
                    'text': $('#text').val()},
                    'success': function(qwe){
                        document.getElementById('div').innerHTML+=qwe
                        document.getElementById('text').value = ''
                    }

            
        })
    })
}

$(document).ready(
    function(){
        Chat()
    }
)