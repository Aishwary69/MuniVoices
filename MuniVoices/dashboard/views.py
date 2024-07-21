from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from samasya.models import Samasya

@login_required
def index(request):
    samasyas = Samasya.objects.filter(submitted_by=request.user)

    return render(request, 'dashboard/index.html', {
        'samasyas': samasyas,
    })