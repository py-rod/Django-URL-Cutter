from django.shortcuts import render
from url_link.models import SaveUrlShortened
from qr_codes_link.models import QRGenerator
from django.contrib.sites.shortcuts import get_current_site

# Create your views here.


def analytics(request):
    popular_click = SaveUrlShortened.objects.all().order_by('-clicks').first()
    popular_qr_code = QRGenerator.objects.all().order_by('-scans').first()
    get_domain = get_current_site(request).domain
    return render(request, 'analytics.html', {
        'click': popular_click,
        'scan': popular_qr_code,
        'domain': get_domain,
    })
