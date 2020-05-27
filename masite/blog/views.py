import sys
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

# Create your views here.


def post_list(request):
    """ View Logic to display posts """
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)  # 3 post in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page
        posts = paginator.page(paginator.num_pages)
    print(f''"[VIEW:post list] found posts to be {posts}", file=sys.stderr)
    # if not posts:
    #     print("[*] Hmmm, found no post ?", file=sys.stderr)
    # else:
    #     print("[*] Yay, found posts")
    return render(request, 'blog/post/list.html', {'page': page,
                                                   'posts': posts})


def post_detail(request, year, month, day, post):
    """ View Logic to display posts with given filter """
    post = get_object_or_404(Post, slug=post, status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html', {'post':post})
