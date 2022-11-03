from django.shortcuts import render
from cbsa1.models import Book
from django.views.generic import ListView
from django.views.generic import DetailView

class BookList(ListView):
    model=Book
    template_name='cbsa1/books.html'
    context_object_name="list_of_books"

class BookDetails(DetailView):
    model=Book
    template_name="cbsa1/book_details.html"
    
class BookView(DetailView):
    model=Book
    

# Create your views here.
