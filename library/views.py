from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

def home_index(request):
    return render(request=request, template_name='library/index.html')

def book_list(request):
    context = {'all_books': Book.objects.all()}
    return render(request=request, template_name='library/book/list.html', context=context)

def book_description(request, book_id):
    one_book = get_object_or_404(Book, pk=book_id)
    return render(request=request, template_name='library/book/info.html', context={'one_book': one_book})




def add_book(request):
    global form
    if request.method=='POST':
        form=BookForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Book.objects.create(** form.cleaned_data) #** для распаковки словаря, чтобы не писать title=title

    else:
        form = BookForm()
    return render(request, 'library/book/add_book.html', {'form':form})

def logout_view(request):
    # Ваш код для выхода из системы
    return render(request, 'logout.html')

def profile(request):
    # Ваш код для отображения профиля
    return render(request, 'profile.html')
