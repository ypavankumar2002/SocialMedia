from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from .models import Media
from .forms import Mediaform
from django.contrib.auth.decorators import login_required


# Create your views here.

def about(req):
    return render(req, 'about.html')

def main(req):
    return redirect('home')

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('main')

    if request.method == 'POST':
        un = request.POST.get('un')
        em = request.POST.get('email')
        p1 = request.POST.get('pass1')
        p2 = request.POST.get('pass2')

        if p1==p2 and len(p1)>1 and len(un)>1:
            
            if not User.objects.filter(username=un).exists():
                user = User.objects.create_user(
                    username = un,
                    email = em,
                    password = p1
                )
                user.save()
                    
                return redirect('login')
            else:
                return render(request, 'signup.html', {'error': 'user already exits, Try Loging in !'})
        else:
            if p1 != p2:
                return render(request, 'signup.html', {'msg': 'Passwords Do not Match !'})
            else:
                return render(request, 'signup.html', {'un': 'Enter valid name and password !'} )

    return render(request, 'signup.html')


def login_view(request):
    if request.user.is_authenticated:
        return render(request, 'user.html')
    if request.method == 'POST':
        un = request.POST.get('name')
        p1 = request.POST.get('pass')
        
        user = authenticate(request, username=un, password=p1)

        if user is not None:
            login(request, user)
            return redirect('user')
        else:
            return render(request, 'login.html', {'msg': 'Invalid Credentials !'} )
    return render(request, 'login.html')




@login_required
def user_view(request): 
    if request.method == 'POST':
        form = Mediaform(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user           
            form.save()
            return redirect('user')

    media = Media.objects.filter(user=request.user)[::-1]
    context = {
        'media': media
    }
    return render(request,'user.html', context)
    # return render(request, 'user.html')
    # return redirect('user')


def home_view(request):
    posts = Media.objects.all().order_by('-id')
    # print(posts, 'ppppppppp')
    # pos = Media.objects.all()[::-1]
    # print(pos)
    context ={
        'posts': posts,
        }
    return render(request, 'home.html', context )

@login_required
def logout_view(req):
    logout(req)
    return redirect('home')

@login_required
def profile(req):    
    return redirect('user')


def delete_media(req, id):
    media = Media.objects.get(id=id)
    media.delete()
    return redirect('user')



@login_required    
def delete_user(request):
    if request.method == 'POST':
        text = request.POST.get('remove')

        if str(text) == 'Delete':
            request.user.delete()
            return redirect('home')
        else:
            return render(request, 'delete_user.html', {'msg': "Invalid Text !!"})
    return render(request, 'delete_user.html')




def search_bar(req):
    if req.method == 'GET':
        searched = req.GET.get('q')
        post = []
        all_posts = Media.objects.all()
        for postss in all_posts:
            # print(type(postss))
            if searched.lower() in postss.title.lower():
                media = Media.objects.filter(title = postss)
                ld = media.values()
                # print(type(media), 'mmmmmmmmm')
                # print(type(ld), 'lllllllllllllll')
                # print(ld, ';;;;;;;;;;;;;;;;;;;;')
                post.append(ld[0]['title'])
  
        # print(post)
        se = []
        for pos in post:
            sp = Media.objects.get(title = pos)
            se.append(sp)
    context = {
        'searched_one':se,
        'searched': searched
    }
    return render(req, 'searched.html',context)






