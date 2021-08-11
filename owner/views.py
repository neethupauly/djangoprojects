from django.shortcuts import render

# Create your views here.

# 8000/owner/books/add
def book_create(request):
    if request.method=='GET':
        return render(request,"book_add.html")
    elif request.method=='POST':
        print(request.POST)
        book_name=request.POST["book_name"]
        author=request.POST["author"]
        price=request.POST["price"]
        print(book_name,author,price)
        return render(request,"book_add.html")


# 8000/owner/books/change
def book_update(request,id):
    return render(request,"book_change.html")

# 8000/owner/books/remove
def book_delete(request,id):
    return render(request,"book_remove.html")
