from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from qr_code.qrcode.utils import QRCodeOptions
from .forms import CreateQRCodeForm
# Create your views here.


def create_qr_codes(request):
    my_options = QRCodeOptions(
        quiet_zone_color='red', finder_dark_color="blue", border=2, light_color='green', dark_color='yellow', finder_light_color='purple', separator_color='black', image_format='PNG')
    if request.method == 'POST':
        form = CreateQRCodeForm(
            request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            pass
    else:
        form = CreateQRCodeForm(instance=request.user)
    return render(request, 'create_qr_codes.html', {
        'my_options': my_options,
        'form': form
    })
