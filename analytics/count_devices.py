from .models import UrlAnalytics, QRAnalytics

# URL


def url_is_mobile() -> int:
    return UrlAnalytics.objects.filter(is_mobile=True).count()


def url_is_pc() -> int:
    return UrlAnalytics.objects.filter(is_pc=True).count()


def url_is_tablet() -> int:
    return UrlAnalytics.objects.filter(is_tablet=True).count()


def url_other() -> int:
    is_touch_capable = UrlAnalytics.objects.filter(
        is_touch_capable=True).count()
    is_bot = UrlAnalytics.objects.filter(is_bot=True).count()

    return is_bot + is_touch_capable


# QR

def qr_is_mobile() -> int:
    return QRAnalytics.objects.filter(is_mobile=True).count()


def qr_is_pc() -> int:
    return QRAnalytics.objects.filter(is_pc=True).count()


def qr_is_tablet() -> int:
    return QRAnalytics.objects.filter(is_tablet=True).count()


def qr_other() -> int:
    is_touch_capable = QRAnalytics.objects.filter(
        is_touch_capable=True).count()
    is_bot = QRAnalytics.objects.filter(is_bot=True).count()

    return is_bot + is_touch_capable
