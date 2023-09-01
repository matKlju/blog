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


class PostSearchView(ListView):
    model = Post
    template_name = 'blog/post_search_results.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')  # Get the search query from the URL parameter
        if query:
            return Post.objects.filter(title__icontains=query)
        return Post.objects.none()


class PostSearchView(ListView):
    model = Post
    template_name = 'blog/post_search.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')  # Get the search query from the URL parameter
        if query:
            return Post.objects.filter(title__icontains=query)
        return Post.objects.none()  # R
