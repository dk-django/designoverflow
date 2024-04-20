from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views import View

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from .models import DalleGeneration
from .serializers import ProductSerializer
from .pagination import DefaultPagination

import openai


class HomepageView(TemplateView):
    template_name = 'generator/dump.html'

class GeneratorView(TemplateView):
    template_name = 'generator/sidebar.html'

class DalleGenerationView(View):
    def post(self, request):
        input_text = request.Post.get('input_text', '')
        openai.api_key = 'your api key'
        response = openai.completions.create(
            engine="davinci",
            prompt=input_text,
            max_tokens=50
        )
        image_url = response.choices[0].file
        dalle_interaction = DalleGeneration.objects.create(
            user_prompt=input_text,
            dalle_response=response.choices[0].text
        )
        return redirect('interaction_detail', pk=dalle_interaction.pk)

    def get(self, request):
        return render(request, 'generator/generator_create.html')

class InteractionDetailView(TemplateView):
    def get(self, request, pk):
        interaction = DalleGeneration.objects.get(pk=pk)
        return render(request, 'generator/interaction_detail.html', {'interaction': interaction})


class ProductViewSet(ModelViewSet):
    queryset = DalleGeneration.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['owner']
    pagination_class = DefaultPagination
    search_fields = ['user_prompt', 'dalle_response']
    ordering_fields = ['user_prompt', 'dalle_response']

    def destroy(self, request, pk):
        queryset = DalleGeneration.objects.all()
        self.perform_destroy(queryset)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def delete(self, request, pk):
    #     product = get_object_or_404(DalleGeneration, pk=pk )
    #     product.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


# class ProductList(ListCreateAPIView):

    # def get_queryset(self):
    #     return DalleGeneration.objects.all()
    
    # def get_serializer_class(self):
    #     return ProductSerializer

    # def get(self, request):
    #     queryset = DalleGeneration.objects.all()
    #     serializer = ProductSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def post(self, request):
    #     serializer = ProductSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

# class ProductDetail(RetrieveUpdateDestroyAPIView):
#     queryset = DalleGeneration.objects.all()
    # serializer_class = ProductSerializer

    # def get(self, request, id):
    #     product = get_object_or_404(DalleGeneration, pk=id)
    #     serializer = ProductSerializer(product)
    #     return Response(serializer.data)

    # def put(self, request, id):
    #     product = get_object_or_404(DalleGeneration, pk=id)
    #     serializer = ProductSerializer(product, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

