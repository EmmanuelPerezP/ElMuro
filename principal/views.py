from django.views.generic.list import ListView
from django.views import generic, View
from django.views.generic.edit import SingleObjectMixin, FormView
from django.shortcuts import render
from principal.models import Comment
from .forms import CreatePost
from django.urls import reverse


class CommentListView(ListView):

    model = Comment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # yes i know this shouldnt be done
        context['form'] = CreatePost()
        return context


class CommentForm(FormView):
    template_name = "principal/comment_list.html"
    form_class = CreatePost

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('index')

    def form_valid(self, form):
        commentRow = Comment()
        # commentRow.image = form.cleaned_data['image']
        # commentRow.commentText = form.cleaned_data['message']
        commentRow = Comment(image=form.cleaned_data['image'],
                             commentText=form.cleaned_data['message'])
        commentRow.save()
        # reviewMo = Review(textReview=form.cleaned_data['message'],
                          # titleReview="temp",
                          # ratingReview=form.cleaned_data['rating'])
        # reviewMo.save()
        # self.object.reviews.add(reviewMo)
        print("form is valid")
        return super().form_valid(form)


class Index(View):

    def get(self, request, *args, **kwargs):
        view = CommentListView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentForm.as_view()
        return view(request, *args, **kwargs)
