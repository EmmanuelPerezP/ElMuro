from django.views import generic, View
# Generic Views
from django.views.generic.edit import SingleObjectMixin, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.urls import reverse
from django.shortcuts import render
from principal.models import Post, Comment
from .forms import CreatePost, CreateComment
from .serializers import PostVotingSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PostVote(APIView):
    """
    Vote on a post
    """

    def post(self, request, format=None):

        serializer = PostVotingSerializer(data=request.data)
        if serializer.is_valid():
            # updating objects
            # https://docs.djangoproject.com/en/2.0/ref/models/instances/#updating-attributes-based-on-existing-fields
            post = Post.objects.get(pk=serializer.validated_data["postId"])
            if serializer.validated_data["action"] == 1:
                post.likes += 1
            elif serializer.validated_data["action"] == -1:
                post.likes -= 1
            elif serializer.validated_data["action"] == 0:
                post.likes -= 1
            post.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostListView(ListView):

    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # we create the form and pass it to the rendering html
        context['form'] = CreatePost()
        return context


class ListFormView(FormView):
    #  we have to remember to set template_name to ensure that form errors
    #  will render the same template as PostListView is using on GET
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


# Post Detail View with comment form
class CommentFormView(SingleObjectMixin, FormView):

    template_name = "principal/post_detail.html"
    form_class = CreateComment
    model = Post

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('post-detail', args=[self.object.pk])

    def form_valid(self, form):
        self.object = self.get_object()
        commentRow = Comment(commentText=form.cleaned_data['message'],
                                post=self.object)
        commentRow.save()
        return super().form_valid(form)


class PostDetailView(DetailView):

    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # we create the form and pass it to the rendering html
        # self.object = self.get_object()
        context['comment_list'] = Comment.objects.filter(post=self.object.pk)
        context['form'] = CreateComment()
        return context


class PostDetailForm(View):

    def get(self, request, *args, **kwargs):
        view = PostDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentFormView.as_view()
        return view(request, *args, **kwargs)