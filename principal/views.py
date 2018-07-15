from django.views import generic, View
# Generic Views
from django.views.generic.edit import SingleObjectMixin, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.urls import reverse
from django.shortcuts import render
from principal.models import Post
from .forms import CreatePost



class PostListView(ListView):

    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # yes i know this shouldnt be done
        context['form'] = CreatePost()
        return context


class ListFormView(FormView):
    template_name = "principal/post_list.html"
    form_class = CreatePost

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('index')

    def form_valid(self, form):
        print(form.cleaned_data['image'])
        postRow = Post(image=form.cleaned_data['image'],
                             postText=form.cleaned_data['message'])
        postRow.save()
        print("form is valid")
        return super().form_valid(form)


class Index(View):

    def get(self, request, *args, **kwargs):
        view = PostListView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ListFormView.as_view()
        return view(request, *args, **kwargs)

class PostDetailView(DetailView):

    model = Post