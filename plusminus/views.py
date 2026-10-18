from django.shortcuts import render
from django.views.decorators.http import require_http_methods


def index(request):
    return render(request, 'plusminus/index.html')


@require_http_methods(['GET', 'POST'])
def results(request):
    if request.method == 'GET':
        return render(request, 'plusminus/index.html', {
            'error_message': 'Submit the form to calculate a player\'s field goal percentage.',
        })

    name = (request.POST.get('name') or '').strip()
    try:
        fgm = int(request.POST.get('fgm'))
        fga = int(request.POST.get('fga'))
    except (TypeError, ValueError):
        return render(request, 'plusminus/index.html', {
            'error_message': 'Please enter valid numbers for field goals made and attempted.',
        })

    if not name:
        return render(request, 'plusminus/index.html', {
            'error_message': 'Please provide a player name.',
        })
    if fga < 0 or fgm < 0:
        return render(request, 'plusminus/index.html', {
            'error_message': 'Field goal attempts and makes cannot be negative.',
        })
    if fga == 0:
        fgp = 0.0
    else:
        fgp = (fgm / fga) * 100

    if fgm > fga:
        return render(request, 'plusminus/index.html', {
            'error_message': 'You made more shots than your attempts. That\'s impossible. Try again.',
        })

    return render(request, 'plusminus/results.html', {
        'name': name,
        'fga': fga,
        'fgm': fgm,
        'fgp': round(fgp, 2),
    })