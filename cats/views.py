from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404

from .models import Cat


# Create your views here.
def list(request: HttpRequest) -> JsonResponse:
    cats = Cat.objects.all()
    return JsonResponse(
        {
            "cats": [
                {
                    "name": c.name,
                    "years_exp": c.experience,
                    "breed": c.breed,
                    "salary": c.salary,
                }
                for c in cats
            ]
        }
    )


def info(request: HttpRequest, cat_id: int) -> JsonResponse:
    c = get_object_or_404(Cat, pk=cat_id)
    return JsonResponse(
        {
            "name": c.name,
            "years_exp": c.experience,
            "breed": c.breed,
            "salary": c.salary,
        }
    )
