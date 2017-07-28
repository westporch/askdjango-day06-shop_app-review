from django.shortcuts import render
from .models import Item
from django.shortcuts import render, redirect
from .forms import ItemForm
from django.db.models import Q


def item_list(request):
    qs = Item.objects.all()
    query = request.GET.get('query', '')
    if query:
        condition = Q(name__icontains=query) | Q(desc__icontains=query)
        qs = qs.filter(condition)

    return render(request, 'shop/item_list.html', {
        'item_list': qs,
        'query': query,
    })


def item_detail(request, pk):
    item = Item.objects.get(pk=pk)
    return render(request, 'shop/item_detail.html', {
        'item': item,
    })


# def item_new(request):


def item_edit(request, pk):
    item = Item.objects.get(pk=pk)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect('shop:item_detail', item.id)
    else:
        form = ItemForm(instance=item)

    return render(request, 'shop/item_form.html', {
        'form': form,
    })


def item_delete(request, pk):
    item = Item.objects.get(pk=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('shop:item_list')
    return render(request, 'shop/item_confirm_delete.html', {
        'item': item,
    })


def item_new(request):
    if request.method == 'POST':

        form = ItemForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
        form = ItemForm()
    return render(request, 'shop/item_form.html', {
        'form': form
    })
