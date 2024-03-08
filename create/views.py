from django.views.generic import FormView
from django.urls import reverse_lazy
from blogauth.models import IonUser
from posts.models import Post
from .models import PostForm


class CreatePost(FormView):
    form_class = PostForm
    template_name = "create.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.session.get('pk', None) is None:
            return context
        context['username'] = IonUser.objects.get(  # type: ignore
            id=self.request.session['pk']
        ).ion_username

        return context

    def form_valid(self, form: PostForm):
        new_post = Post(
            title=form.cleaned_data['title'],
            body=form.cleaned_data['body']
        )
        new_post.save()
        print(f"Saved {form.cleaned_data['title']}")
        return super().form_valid(form)
