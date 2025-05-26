from .models import Artist

def nav_pages(request):
    return {
        'nav_pages': [
            {'title': 'Про нас', 'url_name': 'about'},
            {'title': 'Платівки які радимо', 'url_name': 'recommended'},
            {'title': 'Умови на яких працюємо', 'url_name': 'terms'},
            {'title': 'Створити свою платівку', 'url_name': 'create_vinyl'},
        ]
    }
def artist_list(request):
    return {
        'artists': Artist.objects.all()
    }
