from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect,render
from django.views.generic import ListView
from bookCollection.models import BuyBook

class BookListView(LoginRequiredMixin, ListView):
    model = BuyBook
    template_name = 'profile.html'
    context_object_name = 'borrowed_books'

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = BuyBook.objects.filter(user_id=user_id)
        return queryset


