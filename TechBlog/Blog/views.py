from django.shortcuts import render
from django.views.generic import (TemplateView,DeleteView,UpdateView,CreateView,DetailView,ListView)
from django.utils import timezone
from Blog.models import Post,Comment
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from Blog.forms import PostForm,CommentForm
class AboutView(TemplateView):
    template_name = 'home.html'
class PostDetailView(DetailView):
    model=Post
class PostListView(ListView):
    model=Post
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
class PostCreateView(LoginRequiredMixin,CreateView):
    form_class=PostForm
    model=Post
    login_url='/login/'
    redirect_field_name='Blog/post_detail.html'
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model=Post
    success_url=reverse_lazy('post_detail')
class PostDraftListView(LoginRequiredMixin,ListView):
    model=Post
    login_url='/login/'
    redirect_field_name='Blog/post_detail.html'
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')
class PostUpdateView(LoginRequiredMixin,UpdateView):
    model=Post
    form_class=PostForm
    login_url='/login/'
    redirect_field_name='Blog/post_detail.html'
#############################FUNCTIONAL VIEWS#################################

@login_required
def add_comment_to_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=CommentForm()
    return render(request,'Blog/comment_form.html',{'form':form})
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.pk
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def post_publish(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)
