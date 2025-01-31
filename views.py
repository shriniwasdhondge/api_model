from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response as APIResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from .models import Response as ResponseModel
from .serializers import ResponseSerializer


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class ResponseListCreateAPI(APIView):
    @ratelimit(key='ip', rate='5/m', method='ALL')
    def get(self, request):
        cached_responses = cache.get('responses')
        if cached_responses is None:
            responses = ResponseModel.objects.all()
            paginator = CustomPagination()
            paginated_responses = paginator.paginate_queryset(responses, request)
            serializer = ResponseSerializer(paginated_responses, many=True)
            cache.set('responses', serializer.data, timeout=60*15)
        else:
            return APIResponse(cached_responses)

        return paginator.get_paginated_response(serializer.data)

    @ratelimit(key='ip', rate='5/m', method='ALL')
    def post(self, request):
        serializer = ResponseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return APIResponse(serializer.data, status=status.HTTP_201_CREATED)
        return APIResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve Single Response
class ResponseDetailAPI(APIView):
    def get(self, request, id):
        try:
            response = ResponseModel.objects.get(id=id)
            serializer = ResponseSerializer(response)
            return APIResponse(serializer.data)
        except ResponseModel.DoesNotExist:
            return APIResponse({'error': 'Response not found'}, status=status.HTTP_404_NOT_FOUND)



from django_ratelimit.decorators import ratelimit

# List and Create Endpoint with Rate Limiting
from django_ratelimit.decorators import ratelimit

class ResponseListCreateAPI(APIView):
    @ratelimit(key='ip', rate='5/m', method='ALL')  # Removed burst argument
    def get(self, request):
        paginator = CustomPagination()
        responses = ResponseModel.objects.all()
        paginated_responses = paginator.paginate_queryset(responses, request)
        serializer = ResponseSerializer(paginated_responses, many=True)
        return paginator.get_paginated_response(serializer.data)

    @ratelimit(key='ip', rate='5/m', method='ALL')  # Removed burst argument
    def post(self, request):
        serializer = ResponseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return APIResponse(serializer.data, status=status.HTTP_201_CREATED)
        return APIResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    from rest_framework import filters
from django.db.models import Q
from rest_framework.decorators import action

class ResponseListCreateAPI(APIView):
    def get(self, request):
        model_used = request.query_params.get('model_used', None)
        start_date = request.query_params.get('start_date', None)
        end_date = request.query_params.get('end_date', None)
        
        responses = ResponseModel.objects.all()

        if model_used:
            responses = responses.filter(model_used=model_used)
        
        if start_date and end_date:
            responses = responses.filter(timestamp__range=[start_date, end_date])

        paginator = CustomPagination()
        paginated_responses = paginator.paginate_queryset(responses, request)
        serializer = ResponseSerializer(paginated_responses, many=True)
        return paginator.get_paginated_response(serializer.data)

from django.core.cache import cache

class ResponseListCreateAPI(APIView):
    def get(self, request):
        cached_responses = cache.get('responses')
        
        if cached_responses is None:
            paginator = CustomPagination()
            responses = ResponseModel.objects.all()
            paginated_responses = paginator.paginate_queryset(responses, request)
            serializer = ResponseSerializer(paginated_responses, many=True)
            cache.set('responses', serializer.data, timeout=60*15)  # Cache for 15 minutes
        else:
            return APIResponse(cached_responses)
        
        return paginator.get_paginated_response(serializer.data)



