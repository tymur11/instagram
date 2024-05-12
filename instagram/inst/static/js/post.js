function open(){
    $('#btn').click(function(){
        document.getElementById('img').show()
        document.getElementById('base').inert = true
        document.getElementById('quit').classList.remove('hide')

    })


}
function close(){
    $('#quit').click(function(){
        document.getElementById('img').close()
        document.getElementById('base').inert =  false
        document.getElementById('quit').classList.add('hide')
        document.getElementById('text').close()
        document.getElementById('file').value = ''

    })





}

function sendImage(){
    $('#file').change(function(){
        var data = new FormData()
        data.append('img', document.getElementById('file').files[0])
        data.append('csrfmiddlewaretoken', $('input[name="csrfmiddlewaretoken"]').val())
        
        $.ajax('/makepost/', {
            'type': 'POST',
            'dataType': 'json',
            'async': true,
            'data': data,
            'processData': false,
            'contentType': false,
            'success': function(qwe){
                document.getElementById('text').show()
                document.getElementById('img').close()
                document.getElementById('showimg').src = 'media/media/postimage/file.png'
                

            }

            
        })
    })
}

function  text(){
    $('#btnpost').click(function(){
        $.ajax('/makepost/',{
            'type': 'POST',
            'dataType': 'json',
            'async': true,
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'text': $('#text1').val()
            },
            'success': function(button){
                document.getElementById('text').close()
                document.getElementById('quit').classList.add('hide')
                document.getElementById('base').inert = false
                

            }


        })
    })

    
}




$(document).ready(function(){
    open()
    sendImage()
    $('#btnfile').click(function(){
        $('#file').trigger('click')
    })
    text()
    close()
})