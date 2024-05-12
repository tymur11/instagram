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
                if (zxc['like'] == 0){
                    document.getElementById('Like').src = '/static/icons/a_like.png'
                }
                else{
                    document.getElementById('Like').src = '/static/icons/like.png'
                }
                document.getElementById('Nlike').innerHTML = zxc[1]


            }
        

            
        })
    })

}

function LikeComent(){
    $(document).click(function(ivent){
        var a = $(ivent.target)
        if(a.attr('class') == 'LikeCom likecoment'){
            $.ajax($('#Button').data('url'),{
                'type': 'POST',
                'async': true,
                'dataType': 'json',
                'data':{
                    'csrfmiddlewaretoken':$('input[name="csrfmiddlewaretoken"]').val(),
                    'id': a.attr('id')
                    
                },
                'success': function(qw){
                    if(qw['like'] == 0){
                        document.getElementById(a.attr('id')).src = '/static/icons/a_like.png'
                    }
                    else{
                        document.getElementById(a.attr('id')).src = '/static/icons/like.png'
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