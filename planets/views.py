from django.shortcuts import render, get_object_or_404
from .models import Planet


def planet_detail(request, name='Mercury'):
    planet = get_object_or_404(
        Planet,
        name=name,
        status=Planet.Status.PUBLISHED,
    )

    return render(
        request,
        'planets/planet_detail.html',
        {
            'planet': planet
        })
