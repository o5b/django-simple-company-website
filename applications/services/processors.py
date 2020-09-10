from .models import Service


def service_list(*args, **kwargs):
    return {
        'service_list': Service.published.all() or []
    }
