from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
from .models import Tag, Blog
from .serializers import BlogSerializer, TagSerializer


class BlogView(View):
    """
    博客
    """
    def get(self, request):
        blogs = Blog.objects.all()
        data = BlogSerializer(blogs, many=True).data
        # return JsonResponse({'data': data})
        return render(request, 'blog.html', {'data': data})


class BlogDetailView(View):
    """
    博客
    """
    def get(self, request, question_id):
        blog = get_object_or_404(Blog, pk=question_id)
        data = BlogSerializer(blog).data
        try:
            int('hh')
        except Exception as e:
            raise Http404()
        # return JsonResponse({'data': data})
        return render(request, 'blog_detail.html', {'data': data})
    
    
# class TagDetailView(View):
#     """
#     博客
#     """
#     def get(self, request, tag_id):
#         tag = get_object_or_404(Tag, pk=tag_id)
#         data = TagSerializer(tag).data
#         return JsonResponse({'data': data})
