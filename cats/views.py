import json

import requests
from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_POST

from .models import Cat


def get_json(request) -> dict:
    # ok, now I understand the value of DRF, lol
    data = json.loads(request.body)

    return data


# Create your views here.
def list(request: HttpRequest) -> JsonResponse:
    cats = Cat.objects.all()
    return JsonResponse(
        {
            "cats": [
                {
                    "id": c.id,
                    "name": c.name,
                    "years_exp": c.experience,
                    "breed": c.breed,
                    "salary": c.salary,
                }
                for c in cats
            ]
        }
    )


@require_http_methods(["GET", "DELETE"])
@csrf_exempt
def cat(request: HttpRequest, cat_id: int) -> JsonResponse:
    if request.method == "GET":
        c = get_object_or_404(Cat, pk=cat_id)
        return JsonResponse(
            {
                "name": c.name,
                "years_exp": c.experience,
                "breed": c.breed,
                "salary": c.salary,
            }
        )
    elif request.method == "DELETE":
        Cat.objects.get(pk=cat_id).delete()
        return JsonResponse({"ok": cat_id})


def is_valid_breed(breed: str) -> bool:
    # TODO: we should probably cache this somehow
    r = requests.get("https://api.thecatapi.com/v1/breeds")
    breed_data = r.json()
    return breed in map(lambda data: data["name"], breed_data)


@require_POST
@csrf_exempt
# TODO: I guess this could be a PUT method?
# but then PUT should be idempotent and we create a new cat each time...
#
# this wouldn't be a problem if we had uniqueness constraint on name, I think
#
# or maybe I'm just overthinking
def create_cat(request: HttpRequest) -> JsonResponse:
    data = get_json(request)

    name = data["name"]
    experience = int(data["years_exp"])
    breed = data["breed"]
    if not is_valid_breed(breed):
        return JsonResponse(
            {
                "err": "bad breed",
            },
            status=400,
        )

    salary = int(data["salary"])
    cat = Cat(name=name, experience=experience, breed=breed, salary=salary)
    cat.save()

    return JsonResponse({"id": cat.id})
