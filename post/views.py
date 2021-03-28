from django.shortcuts import render
from post.models import *
from django.db.models import Q
# Create your views here.

# SEARCHING FUNCTION

def home(request):
    if request.method == "POST":
        try:
            search_keyword = request.POST["keyword"]
            searching_result = Post.objects.filter(title__icontains=search_keyword)
            # Searching Result Store in DataBase
            SearchResultStore.objects.create(
                search_key_store=search_keyword
            )
            
            context = {
                'posts': searching_result
            }
            return render(request, 'search.html', context)
        except Exception as error:
            print(error)
    return render(request, 'search.html')



# FILTERING BY USER

def user_filtering_post(request,user_name):
    user = User.objects.get(username=user_name)
    posts = Post.objects.filter(author=user)
    context = {
        'posts': posts
    }
    return render(request, 'user_filtering_post.html', context)



# FILTERING BY CATEGORY

def category_filtering_post(request,category_name):
    category = Category.objects.get(name=category_name)
    print(category)
    posts = Post.objects.filter(category=category)
    context = {
        'posts': posts
    }
    return render(request, 'caregory_filtering_post.html', context)


# DETAILS POST

def post_details(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post': post
    }
    return render(request, 'post_details.html', context)
