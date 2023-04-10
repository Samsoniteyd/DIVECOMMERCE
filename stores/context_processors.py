from . models import Category


def categorys(request):
    cats = Category.objects.filter()

    return{
        'catloops': cats
    }