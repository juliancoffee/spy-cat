from django.http import HttpRequest, JsonResponse


# Create your views here.
def list(request: HttpRequest) -> JsonResponse:
    raise NotImplementedError
    return JsonResponse([])


def info(request: HttpRequest) -> JsonResponse:
    raise NotImplementedError
