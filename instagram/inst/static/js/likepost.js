function like(){
    $(document).click(function(ivent){
        var q = $(ivent.target)
        if(q.attr('class') =='likepost' ){
            $.ajax('/', {
                'type': 'POST',
                'dataType' : 'json',
                'async': true,
                'data' : {
                    'csrfmiddlewaretoken':$('input[name="csrfmiddlewaretoken"]').val(),
                    'id': q.attr('id')

                },
                'success': function(qwe){
                    alert(qwe)
                    document.getElementById('likes'+q.attr('id')).innerHTML = qwe['likes']
                    if(qwe['like'] == 0){
                        document.getElementById(q.attr('id')).src = '/static/icons/a_like.png'
                    }
                    else{
                        document.getElementById(q.attr('id')).src = '/static/icons/like.png'      
                    }    
                }
                
            })
            
        }
        
    })
}

$(document).ready(function(){
        like()
})


