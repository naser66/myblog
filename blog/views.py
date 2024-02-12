from .models import Post, BlogGroup
from django.views import generic
from .forms import NewPostForm, NewBlogGroupForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect


def author_post(request):
    author = request.user
    return author


class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_edit')


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


# class PostCreateView(generic.CreateView):
#     model = Post
#     form_class = NewPostForm()
#     template_name = 'blog/create_post.html'

def post_create_view(request):
    if request.method == 'POST':
        post_form = NewPostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.author = request.user
            new_post.user = request.user
            new_post.save()
            return redirect('post_list')
    else:
        post_form = NewPostForm()

    return render(request, 'blog/create_post.html', context={'form': post_form})


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = NewPostForm
    template_name = 'blog/update_post.html'


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('post_list')


class BlogGroupListView(generic.ListView):
    model = BlogGroup
    #bloggroups = BlogGroup.objects.all()
    template_name = 'blog/group_list.html'
    context_object_name = 'group_list'

    def get_queryset(self):
        return BlogGroup.objects.all()


class BlogGroupDetailView(generic.DetailView):
    model = BlogGroup
    template_name = 'blog/group_detail.html'
    context_object_name = 'group'


class BlogGroupCreateView(generic.CreateView):
    model = BlogGroup

    form_class = NewBlogGroupForm
    template_name = 'blog/create_group.html'
