from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify

from post.models import Post, Comment, Category


# Create your views here.



def index(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    ctx = {'posts':posts, 'categories':categories}
    return render(request, 'post/index.html', context=ctx)



def post_info(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.all()
    print(type(comments))
    return render(request, 'post/post_info.html', {'post':post, 'comments':comments})



def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        if request.POST['comment_name'] != None and request.POST['comment_name'] != '' and request.POST['comment_author'] != None and  request.POST['comment_author'] != '':
            comment = Comment()
            comment.content=request.POST['comment_name']
            comment.comment_author=request.POST['comment_author']
            comment.post=post
            comment.save()
    return redirect('post_info', post_id=post_id)


def delete_comment(request, post_id, comment_id):
    post = get_object_or_404(Post, pk=post_id)
    post.comments.get(id=comment_id).delete()
    return redirect('post_info', post_id=post_id)



def add_post(request):
    post = Post()
    if request.method == 'POST':
        post.title = request.POST['post_title']
        post.description = request.POST['post_description']
        post.author = request.POST['post_author']
        post.category = Category.objects.get(name=request.POST['post_cat'])
        post.slug = slugify(post.title)
        post.save()
    return redirect('index')


def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('index')


