from django.shortcuts import render
from .models import AddBook,Category
from django.views.generic import DetailView
from django.views import View
from . import forms
# Create your views here.
class BookView(View):
    template_name = 'book.html'

    def get(self, request, category_slug=None):
        data = AddBook.objects.all()
        categories = Category.objects.all()

        if category_slug is not None:
            category = Category.objects.get(slug=category_slug)
            data = AddBook.objects.filter(category=category)

        return render(request, self.template_name, {"data": data, "categories": categories})
    

class DetailsPost(DetailView):
    model = AddBook
    pk_url_kwarg = 'id'
    template_name = 'details.html'


    def post(self,request,*args,**kwargs):
        comment_form = forms.CommentForm(data = self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = False)
            new_comment.post = post 
            new_comment.save()
        # if 'buy_car' in request.POST:
        #     if post.quantity > 0:
        #         post.quantity -=1
        #         post.save()
        #         models.BuyCar.objects.create(user=request.user, car=post)
        #     else:
        #         messages.warning(self.request, 'All Car is Sold out please look forward')
        return self.get(request, *args,**kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context