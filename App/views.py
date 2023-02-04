from django.shortcuts import render, get_object_or_404, redirect
from .models import Book


# Create
def book_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_date = request.POST.get('publication_date')
        Book.objects.create(title=title, author=author, publication_date=publication_date)
        return redirect('book_list')
    return render(request, 'book_create.html')



# Read
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})



def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})


# Update
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.publication_date = request.POST.get('publication_date')
        book.save()
        return redirect('book_detail', pk=book.pk)
    return render(request, 'book_update.html', {'book': book})


# Delete
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')
