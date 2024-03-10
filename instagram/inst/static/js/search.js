function search(){
    $('#input').keyup(function(){
        $.ajax('/search/',{
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data':{
                'csrfmiddlewaretoken':$('input[name="csrfmiddlewaretoken"]').val(),
                'asd': $('#input').val()

        },
        'success': function(zxc){
            document.getElementById('div').innerHTML = zxc
        }
        
                
        })
    })

}


$(document).ready(function(){
    search()


})