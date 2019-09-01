
from django.shortcuts import render
from .models import Post
from django.db.models import Count
from collections import Counter

def get_newest(request):
	sidebar_post_list=Post.objects.order_by('-created_on')
	return {'sidebar_post_list' :sidebar_post_list}

def get_tags(request):
	#tags_list = Post.objects.values_list('Tag', flat=True).annotate(Count('Tag'))
	 #<QuerySet ['c', 2, 'b', 6, 'a', 4, 'f', 1, 'e', 2, 'd', 1]>

	tags_list = Counter(Post.objects.values_list('Tag', flat=True)).most_common(3)

	tags_list = [tag_[0] for tag_ in tags_list]

	# Counter({'b': 6, 'a': 4, 'c': 2, 'e': 2, 'd': 1, 'f': 1})
	return {'tags_list': tags_list}
