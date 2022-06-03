from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Women, Category
from django.forms.models import model_to_dict
from .serializers import WomenSerializer
from rest_framework import viewsets, routers
from rest_framework.decorators import action



# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Women.objects.all()

        return Women.objects.filter(pk=pk)


    @action(methods=['get'], detail=False)
    def get_category(self, request, pk=None):
        cats = Category.objects.all()
        return Response({'cats': [c.name for c in cats]})




router = routers.DefaultRouter()
router.register(r'women', WomenViewSet)



#
# class WomenAPIList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenAPIDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

# class WomenAPIView(APIView):
#
#     def get(self, request):
#         lst = Women.objects.all()
#         return Response({'posts': WomenSerializer(lst, many=True).data})
#
#     def post(self, request):
#         serializer =WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pks = kwargs.get("pk")
#         if not pks:
#             return Response({"error": "Method PUT not allowed 1"})
#
#         try:
#             instance = Women.objects.get(pk=pks)
#         except:
#             return Response({"error": "Object does not exists 2"})
#
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk")
#         if not pk:
#             return Response({"error": "Нет данных по этому id"})
#
#         instance = Women.objects.get(pk=pk)
#         instance.delete()
#
#         return Response({"delete": "успешно удален пост id " + str(pk)})
#






