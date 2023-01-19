from django.shortcuts import render
from rest_framework import generics


from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms import model_to_dict

from .models import Hero, Element, Country
from .serializers import HeroSerializer

from rest_framework import viewsets
from rest_framework.decorators import action

# from .serializers import HeroSerializer

# class HeroAPIView(generics.ListAPIView):
#     queryset = Hero.objects.all()
#     serializer_class = HeroSerializer


# class HeroAPIView(APIView):
#     def get(self, request):
#         all_hero=Hero.objects.all().values()
#         return Response({'heroes':list(all_hero)})


# class HeroApiList(generics.ListCreateAPIView):
#     queryset = Hero.objects.all()
#     serializer_class = HeroSerializer

# class HeroApiUpdate(generics.UpdateAPIView):
#     queryset = Hero.objects.all()
#     serializer_class = HeroSerializer


# class HeroApiDetailView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Hero.objects.all()
    # serializer_class = HeroSerializer


class HeroViewSet(viewsets.ModelViewSet):
    # queryset = Hero.objects.all()
    serializer_class = HeroSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Hero.objects.all()[:]
        return Hero.objects.filter(pk=pk)

    @action(methods=['get'], detail=1)
    def category_elements(self,request, pk=None):
        cats = Element.objects.get(pk =pk)
        return Response({'cats':cats.name_element})

    @action(methods=['get'], detail=1)
    def category_country(self,request, pk=None):
        cats = Country.objects.get(pk=pk)
        return Response({'cats':cats.city})