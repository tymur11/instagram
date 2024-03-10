function like(){
    $('#Like').click(function(){
        $.ajax($('#Button').data('url'),{
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken':$('input[name="csrfmiddlewaretoken"]').val()
            },
            'success': function(zxc){   
                if (document.getElementById('Like').innerHTML == 'Dislike'){
                    document.getElementById('Like').innerHTML = 'Like'
                }
                else{
                    document.getElementById('Like').innerHTML = 'Dislike'
                }
                document.getElementById('Nlike').innerHTML = zxc[1]


            }
        

            
        })
    })

}

function LikeComent(){
    $(document).click(function(ivent){
        var a = $(ivent.target)
        if(a.attr('class') == 'LikeCom'){
            $.ajax($('#Button').data('url'),{
                'type': 'POST',
                'async': true,
                'dataType': 'json',
                'data':{
                    'csrfmiddlewaretoken':$('input[name="csrfmiddlewaretoken"]').val(),
                    'id': a.attr('id')
                    
                },
                'success': function(qw){
                    if(a.text == 'Dislike'){
                        a.text('Like')
                    }
                    else{
                        a.text('Dislike')
                    }
                    $(`#likes${a.attr('id')}`).text(qw[1])

                }
            })
        }

    })
}

$(document).ready(function(){
    like()
    LikeComent()


})