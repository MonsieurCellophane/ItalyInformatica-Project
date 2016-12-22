from rest_framework.response import Response

from rest_framework import schemas
from rest_framework import renderers, response
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view
from rest_framework.decorators import api_view, renderer_classes

from renderers import SwaggerRenderer

# Schema stuff 
# TODO: remove spurious urls from schema views.
APItitle="ItalyInformatica Big Project API"
schema_view = get_schema_view(title=APItitle)
swagger_view=get_swagger_view(title=APItitle)

@api_view()
@renderer_classes([SwaggerRenderer])
def openapi_view(request):
    generator = schemas.SchemaGenerator(title=APItitle)
    return response.Response(generator.get_schema(request=request))
