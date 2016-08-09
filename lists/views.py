from django.core.exceptions import ValidationError
from django.shortcuts import render,redirect
from lists.models import Item,List
# Create your views here.
def home_page(request):
    return render(request,'home.html')
def view_list(request,list_id):
    temp_list = List.objects.get(id=list_id)
    item = Item.objects.filter(list=temp_list) 
    return render(request,'list.html',{'list':temp_list,'items':item})
def new_list(request):
        new_list = List.objects.create()
        item=Item.objects.create(text=request.POST['item_text'],list = new_list)
        error = "You cannot have an empty list item"
        #item.full_clean()
        #return render(request,'home.html',{"error":error})
        try:
            item.full_clean()
        except ValidationError:
            error = "You cannot have an empty list item"
            return render(request,'home.html',{"error":error})
def add_item(request,list_id):
    new_list = List.objects.get(id=list_id)
    Item.objects.create(text = request.POST['item_text'],list=new_list)
    return redirect('/lists/%d/'%(new_list.id))
