from django.core.exceptions import ValidationError
from django.shortcuts import render,redirect
from lists.models import Item,List
# Create your views here.
def home_page(request):
    return render(request,'home.html')
def view_list(request,list_id):
    temp_list = List.objects.get(id=list_id)
    if request.method == "POST":
            Item.objects.create(text=request.POST['item_text'],list = temp_list)
            return redirect(temp_list)
    return render(request,'list.html',{'list':temp_list,})
def new_list(request):
        new_list = List.objects.create()
        try:
            item=Item.objects.create(text=request.POST['item_text'],list = new_list)
            item.full_clean()
            item.save()
            return redirect(new_list)
        except ValidationError:
            new_list.delete()
            error = "You cannot have an empty list item"
            return render(request,'home.html',{"error":error})
