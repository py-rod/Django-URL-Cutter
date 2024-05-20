from .models import UrlAnalytics, QRAnalytics

# URL


def url_is_mobile(request) -> int:
    return UrlAnalytics.objects.filter(creator=request.user.email, is_mobile=True).count()


def url_is_pc(request) -> int:
    return UrlAnalytics.objects.filter(creator=request.user.email, is_pc=True).count()


def url_is_tablet(request) -> int:
    return UrlAnalytics.objects.filter(creator=request.user.email, is_tablet=True).count()


def url_other(request) -> int:
    is_touch_capable = UrlAnalytics.objects.filter(
        is_touch_capable=True).count()
    is_bot = UrlAnalytics.objects.filter(
        creator=request.user.email, is_bot=True).count()

    return is_bot + is_touch_capable


# QR

def qr_is_mobile(request) -> int:
    return QRAnalytics.objects.filter(creator=request.user.email, is_mobile=True).count()


def qr_is_pc(request) -> int:
    return QRAnalytics.objects.filter(creator=request.user.email, is_pc=True).count()


def qr_is_tablet(request) -> int:
    return QRAnalytics.objects.filter(creator=request.user.email, is_tablet=True).count()


def qr_other(request) -> int:
    is_touch_capable = QRAnalytics.objects.filter(
        is_touch_capable=True).count()
    is_bot = QRAnalytics.objects.filter(
        creator=request.user.email, is_bot=True).count()

    return is_bot + is_touch_capable
