from django.shortcuts import render, get_object_or_404
from .models import Planet


def planet_detail(request, slug='mercury'):

    planet = get_object_or_404(
        Planet,
        slug=slug,
        status=Planet.Status.PUBLISHED
    )

    planet_detail_section = request.path.split('/').pop()
    planet_image = planet.overview_img.url
    planet_detail_context = 'overview'
    blurb = planet.overview

    if planet_detail_section == 'structure':
        planet_image = planet.internal_structure_img.url
        planet_detail_context = planet_detail_section
        blurb = planet.internal_structure

    if planet_detail_section == 'geology':
        planet_image = planet.surface_geology_img.url
        planet_detail_context = planet_detail_section
        blurb = planet.surface_geology

    return render(
        request,
        'planets/planet_detail.html',
        {
            'planet': planet,
            'planet_image': planet_image,
            'active': planet_detail_context,
            'blurb':  blurb,
        })
