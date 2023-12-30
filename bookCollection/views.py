from django.shortcuts import render
from .models import AddBook,Category
from django.views import View
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