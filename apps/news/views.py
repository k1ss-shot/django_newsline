from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from apps.news.models import Post
from apps.news.forms import CommentForm


class PostListView(ListView):
    model = Post
    template_name = 'news/post_list.html'
    context_object_name = 'posts'
    ordering = ['-publication_time'] 


class PostDetailView(FormView):
    template_name = 'news/post_detail.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.get_object()
        context['comments'] = context['post'].comments.all()
        return context

    def form_valid(self, form):
        post = self.get_object()
        comment = form.save(commit=False)
        comment.post = post
        comment.author = self.request.user
        comment.save()
        return redirect('post_detail.html', pk=post.pk)

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Post, pk=pk)