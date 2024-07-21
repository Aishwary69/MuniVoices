from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404,redirect,render
from .forms import NewSamasyaForm,EditSamasyaForm
from .models import Samasya,Category


def samasyas(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    samasyas = Samasya.objects.filter(is_solved=False)

    if category_id:
        samasyas = samasyas.filter(category_id=category_id)

    if query:
        samasyas = samasyas.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'samasya/samasyas.html', {
        'samasyas': samasyas,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })

def detail(request,pk):
    samasya = get_object_or_404(Samasya,pk=pk)

    return render(request, 'samasya/detail.html',{
        'samasya': samasya

    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewSamasyaForm(request.POST, request.FILES)

        if form.is_valid():
            samasya = form.save(commit=False)
            samasya.submitted_by = request.user
            samasya.save()

            return redirect('samasya:detail', pk=samasya.id)
    else:
        form = NewSamasyaForm()

    return render(request, 'samasya/form.html', {
        'form': form,
        'title': 'New samasya',
    })

@login_required
def edit(request, pk):
    samasya = get_object_or_404(Samasya, pk=pk, submitted_by=request.user)

    if request.method == 'POST':
        form = EditSamasyaForm(request.POST, request.FILES, instance=samasya)

        if form.is_valid():
            form.save()

            return redirect('samasya:detail', pk=samasya.id)
    else:
        form = EditSamasyaForm(instance=samasya)

    return render(request, 'samasya/form.html', {
        'form': form,
        'title': 'Edit samasya',
    })

@login_required
def delete(request, pk):
    samasya = get_object_or_404(Samasya, pk=pk, submitted_by=request.user)
    samasya.delete()

    return redirect('dashboard:index')



