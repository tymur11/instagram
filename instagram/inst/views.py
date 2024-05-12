from typing import Any
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, RedirectView
from .models import Post , User, Coment, Like, Chat, Mesege, Subscribe
from django.views.generic.edit import CreateView
from .form import Register, Login
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.http import JsonResponse
from django.core.files import File
from pathlib import Path
from django.template.loader import render_to_string








class Main(TemplateView):
    template_name = 'mein.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['currentuser'] = self.request.user
        posts = Post.objects.all()
        result = []
        for a in posts:
            like = Like.objects.filter(post=a)
            for q in like:
                if q.user == self.request.user:
                    result.append([a, 1, len(like)])
                    break
            else:
                result.append([a,0, len(like)])
        context['post'] = result
        return context 
    def post(self,request):
        post = request.POST
        q = Post.objects.get(id= post['id'])
        like = Like.objects.filter(post=q)
        for a in like:
            if a.user == self.request.user:
                a.delete()
                return JsonResponse({"like": 1,'likes': len(like)-1 })
        else:
            w = Like(post=q, user=self.request.user)
            w.save()
            return JsonResponse({'like': 0, 'likes': len(like)+1})
    
            
            
        

    

class RegisterPage(CreateView):
    form_class = Register
    template_name = 'register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    def get_success_url(self):
        asd = Subscribe(user=self.object)
        asd.save()
        return '/login'
    


class LoginPage(LoginView):
    template_name = 'login.html'
    form_class = Login
    redirect_authenticated_user = True


class LogoutPage(LogoutView):
    pass

class MakePost(TemplateView):
    def post(self, request):
        data = request.POST
        if len(data.keys()) == 1:
            with open('media/media/postimagefile.png', 'wb') as openfile:
                openfile.write(request.FILES['img'].read())
        else:
            path = Path('media/media/postimagefile.png')
            with path.open(mode='rb') as openpath:
                file = File(openpath, name=openpath.name)
                p = Post(text=data['text'], imege=file, user=self.request.user)
                p.save()
            
    
        return JsonResponse('1', safe=False)
    

class UserPage(TemplateView):
     template_name = 'userPage.html'
    
     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['currentuser'] = self.request.user
        user = User.objects.get(id=self.kwargs['id'])
        subscribe = Subscribe.objects.get(user=user)
        context['NFolowers'] = len(subscribe.subscribers.all())
        context['NFollow'] = len(subscribe.subscribe.all())
        context['Post'] = len(Post.objects.filter(user=user))
        if self.request.user in subscribe.subscribers.all():
            context['subscribe'] = True
        else:
            context['subscribe'] = False
        context['post'] = Post.objects.filter(user=user)
        context['user'] = user 
        return context 
     
     def post(self, request, **kwargs):
         user = User.objects.get(id=self.kwargs['id'])
         user2 = self.request.user
         subscribe = Subscribe.objects.get(user=user)
         subscribe2 = Subscribe.objects.get(user=user2)
         if user in subscribe2.subscribe.all():
             subscribe.subscribers.remove(user2)
             subscribe.save()
             subscribe2.subscribe.remove(user)
             subscribe2.save()
             return JsonResponse({'follow':'Follow','NFollowers':len(subscribe.subscribers.all()),'NFollow': len(subscribe.subscribe.all())})
         else:
             subscribe.subscribers.add(user2)
             subscribe.save()
             subscribe2.subscribe.add(user)
             subscribe2.save()
             return JsonResponse({'follow':'UnFollow','NFollowers': len(subscribe.subscribers.all()),'NFollow': len(subscribe.subscribe.all())})
 
class PostPage(TemplateView):
    template_name = 'PostPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['currentuser'] = self.request.user
        post = Post.objects.get(id=self.kwargs['id'])
        context['post'] = post 
        like = Like.objects.filter(post=post)
        context['NLike'] = len(like)
        coment = Coment.objects.filter(post=post)
        qwe = []
        for q in coment:
            L = Like.objects.filter(coment=q)
            for c in L:
                if c.user == self.request.user:
                    qwe.append([q, 1,len(L)])
                    break
            else:
                qwe.append([q, 0,len(L)])
        

                


        context['coment'] = qwe
        for l in like:
            if l.user == self.request.user:
                context['Liked'] = 1
                break 
        else:
            context['Liked'] = 0

        return context 
    
    def post(self, request, **kwargs):
        q = request.POST 
        post = Post.objects.get(id=self.kwargs['id'])
        user = self.request.user 
        if 'text' in q.keys():        
            coment = Coment(text=q['text'], post=post, user=user)
            coment.save()
            html = render_to_string('coment.html', context={'q': coment} )
            
            return JsonResponse( html, safe=False )
        elif len(q.keys()) == 1:
            like = Like.objects.filter(post=post)
            for l in like:
                if l.user == self.request.user:
                    l.delete()
                    return JsonResponse({1:len(like)-1, 'like': 1})
            else:
                context = Like(post=post,user=user)
                context.save()
                return JsonResponse({1:len(like)+1, 'like': 0})
        elif 'id' in q.keys():
            com = Coment.objects.get(id=int(q['id']))
            likeCom = Like.objects.filter(coment=com)
            for q in likeCom:
                if q.user == self.request.user:
                    q.delete()
                    return JsonResponse({1:len(likeCom)-1, 'like':1})
            else:
                context = Like(coment=com, user=user)
                context.save()
                return JsonResponse({1:len(likeCom)+1, 'like':0})
                
    
            

class ProfilPage(TemplateView):
    template_name = 'profilPage.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['currentuser'] = self.request.user
        context['User'] = self.request.user
        context['Subscribe'] = len(Subscribe.objects.get(user=self.request.user).subscribe.all())
        context['Subscribers'] = len(Subscribe.objects.get(user=self.request.user).subscribers.all())
        context['post'] = len(Post.objects.filter(user=self.request.user))
        context['Post'] = Post.objects.filter(user=self.request.user)
        return context



class SearchPage(TemplateView):
    template_name = 'searchPage.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['currentuser'] = self.request.user
        return context
    def post(self, request):
        a = request.POST
        if a['asd']:
            b = User.objects.filter(username__contains=a['asd'])
        else:
            b = []
        x = render_to_string('asd.html', {'users': b})
        return JsonResponse(x, safe=False)
    


class ChatPage(TemplateView):
    template_name = 'ChatPage.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['currentuser'] = self.request.user
        chat = Chat.objects.get(id=self.kwargs['id'])
        context['chat'] = chat 
        mesege = Mesege.objects.filter(chat=chat)
        context['mesege'] = mesege
        return context

    def post(self, request, **kwargs):
        a = request.POST
        chat = Chat.objects.get(id=self.kwargs['id'])
        b = Mesege(text=a['text'], user=self.request.user, chat=chat)
        b.save()
        x = render_to_string('qwe.html', {'mesege': b})
        return JsonResponse(x, safe=False)


class ChatCreate(RedirectView):
    def get_redirect_url(self,*args, **kwargs):
        user = User.objects.get(id=self.kwargs['id'])
        user2 = self.request.user
        chat = Chat.objects.filter(user=user,user2=user2)
        chat2 = Chat.objects.filter(user=user2,user2=user)
        if len(chat) == 1:
            self.url= f'/chat/{chat[0].id}'
        elif len(chat2) == 1:
                self.url= f'/chat/{chat2[0].id}'
        else:
            new_chat = Chat(user=user, user2=user2)
            new_chat.save()
            self.url= f'/chat/{new_chat.id}'
        return super().get_redirect_url(*args, **kwargs)
    
        




            
    



          

    