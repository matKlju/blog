from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 8


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('blog:post_list')


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('blog:post_detail') 

    def get_success_url(self):
        # Redirect to the post's detail view after successful update
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.pk})


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')

