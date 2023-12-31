from django.shortcuts import render
from .models import AddBook,Category,BuyBook
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect,get_object_or_404
from django.views import View
from django.contrib import messages
from . import forms
from django.utils import timezone
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

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()

        if request.method == 'POST' and comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = post  # Corrected attribute name to 'book'
            new_comment.save()

        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = forms.CommentForm()

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context




class BookBorrowView(LoginRequiredMixin,View):
    def get(self,request,id, **kwargs):
        book = get_object_or_404(AddBook, id = id)
        user = self.request.user
        if user.account.balance > book.price:
            user.account.balance -= book.price
            messages.success(request, 'book borrowed successful')
            user.account.save(update_fields=['balance'])
            BuyBook.objects.create(
                book = book,
                user = user,
                date=timezone.now(),
            )
    
            return redirect('book') 
        else:
            messages.warning(request, 'Insufficient balance to borrow the book Deposit Please')
            return redirect('book')
