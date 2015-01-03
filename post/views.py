# -*- coding: utf-8 -*-

from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.core.urlresolvers import reverse

from post.models import Post, Comment
from post.forms import PostForm, CommentForm


class PostListView(ListView):
    model = Post
    template_name = 'post/list.html'
    

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/edit.html'

    @property
    def success_url(self):
        return reverse('posts')


class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post/edit.html'

    @property
    def success_url(self):
        return reverse('posts')


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'post/comment_form.html'

    @property
    def success_url(self):
        return reverse('add_comment', kwargs=self.kwargs)

    def get_form_kwargs(self):
        form_kwargs = super(CommentCreateView, self).get_form_kwargs()
        post = Post.objects.get(pk=self.kwargs['post_pk'])
        instance = Comment(post=post)
        form_kwargs['instance'] = instance
        return form_kwargs

    def get_context_data(self, **kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=self.kwargs['post_pk'])
        context['comments'] = Comment.objects.filter(post=context['post'])
        return context