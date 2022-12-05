from django.views import View
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from user.forms import UserCreationForm
from .models import Post
from django.http import HttpResponseRedirect, HttpResponseNotFound

class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)
    
    def post(self,request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') 
            password = form.cleaned_data.get('password1') 
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')

        return render(request, 'home.html', {'form': form})


def index(request):
    post = Post.objects.all()
    return render(request, 'blog/posts.html', {'dataset' : post})

def store(request):
    if request.method == "POST":
        post = Post()
        post.theme = request.POST.get("theme")
        post.description = request.POST.get("description")
        post.save()
    return HttpResponseRedirect("/post/")

def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect("/post/")

def edit(request, id):
    try:
        post = Post.objects.get(id=id)
 
        if request.method == "POST":
            post.theme = request.POST.get("theme")
            post.description = request.POST.get("description")
            post.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "blog/posts.html", {"dataset": post})
    except Person.DoesNotExist:
        return HttpResponseNotFound("Post not found")


        
# class PostView():
    # def index():
    #     posts =  Post.objects.all()
    #     return render(request, posts)


    # return Post.objects.create(theme="Заголовок нового поста", description="Текст нового поста")

    # def show(id):

    # def edit():

    # def delete():            