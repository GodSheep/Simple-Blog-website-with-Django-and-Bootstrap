from django.views import generic
from .models import Post, allcategory
from django.shortcuts import render
import markdown
from django.http import Http404



# class PostList(generic.ListView):
#     #queryset = Post.objects.filter(status=1).order_by('-created_on')
#     ct_name=kwargs.get('ct_name')

#     queryset = Post.objects.filter(status=1, Category=ct_name).order_by('-created_on')
#     template_name = 'index.html'

def PostList(request, ct_name):

	if ct_name.lower() == 'home':
		post_list = Post.objects.filter(status=1).order_by('-created_on')

	else:

		#这里还要判断一下，category是不是那四个类之中

		post_list = Post.objects.filter(status=1, Category=ct_name).order_by('-created_on')
		if not post_list and ct_name not in allcategory:
			post_list = Post.objects.filter(status=1, Tag=ct_name).order_by('-created_on')



	post_list_dict = {
        'post_list': post_list
    }

	return render(request, 'index.html', post_list_dict)


# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'

def PostDetail(request, id):
	post = Post.objects.get(id=str(id))
	post.content = markdown.markdown(post.content.replace("\r\n", '  \n'),
                        extensions=['markdown.extensions.extra',
                        			 'markdown.extensions.fenced_code',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',],safe_mode=True,enable_attributes=False)

	return render(request, 'post_detail.html', {'post' : post})



def about(request):
    #categories, new_blogs, date_archive_list = get_aside_init()
    return render(request, 'about.html')


# def newest(request):
# 	sidebar_post_list=Post.objects.order_by('-created_on')
# 	return render(request, 'sidebar.html', {'sidebar_post_list' :sidebar_post_list})




