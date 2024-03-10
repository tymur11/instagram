function MakeChat(){
    $('#button').click(function(){
        $.ajax( $('#button').data('url'),{
            'type': 'POST',
            'dataType': 'json',
            'async': true,
            'data': {
                'csrfmiddlewaretoken':$('input[name="csrfmiddlewaretoken"]').val()
            }
        }
        
            
        )
    })
}

$(document).ready(
    function(){
        MakeChat()
    }
)