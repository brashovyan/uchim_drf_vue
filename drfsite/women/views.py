import requests
from django.core.files.storage import FileSystemStorage
from django.forms import model_to_dict
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from rest_framework import generics, viewsets
from rest_framework.response import Response
from .models import Women, Category, Tag, New, Subtag
from .permissions import IsManufacturer
from .serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()
from django.db.models.signals import post_save
from django.dispatch import receiver


# этот метод вызывается после регистрации юзера
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        # print(f"{instance} создан, делай чё хочешь)")
        pass


class ActivateUser(APIView):
    def get(self, request, uid, token, format = None):
        payload = {'uid': uid, 'token': token}
        url = f"http://{request.get_host()}/api/v1/auth/users/activation/"
        response = requests.post(url, data = payload)

        if response.status_code == 204:
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')


class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class NewViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer


class SubtagViewSet(viewsets.ModelViewSet):
    queryset = Subtag.objects.all()
    serializer_class = SubtagSerializer


class WomenApiList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()

    # def get_queryset(self):
    #     pk = self.kwargs.get("pk")
    #     return Women.objects.filter(cat=Category.objects.filter(title="Певицы").first())


class WomenApiListUser(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self, requset, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if pk:
            try:
                lst = Women.objects.filter(owner_id=pk)
                return Response({'posts': WomenSerializer(lst, many=True).data})
            except:
                return Response({'error': 'Ничего не найдено!'})
        else:
            return Response({"error": 'Не user id'})


class WomenApiDetail(generics.RetrieveAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = [IsAuthenticated, ]


class WomenApiUpdate(generics.UpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = [IsAuthenticated, ]





class WomenApiDelete(generics.DestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = [IsAuthenticated, ]


class CategoryApiDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, ]


class UserDetail(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self, request):
        return Response({'username': request.user.username, 'id': request.user.id, 'email': request.user.email, 'phone': request.user.phone})


class WomenApiView(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self, request):
        #id = request.data["id"]
        #print(id)

        # добавление юзера в группу (добавление роли)
        user = request.user
        group = Group.objects.get(name='Moderator')
        user.groups.add(group)

        lst = Women.objects.all()
        print(request.user.id)
        return Response({'posts': WomenSerializer(lst, many=True).data})

    def post(self, request):
        # context нужен из-за кастомного юзера
        serializer = WomenSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['owner'] = self.request.user

        serializer.save()




        # post_new = Women.objects.create(
        #     title = request.data['title'],
        #     content = request.data['content'],
        #     cat = Category.objects.get(id = int(request.data['cat'])),
        #     photo = request.FILES['photo'],
        # )
        return Response({'title': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "pk не найден"})

        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({"error": "Объект не найден"})

        serializer = WomenSerializer(data=request.data, instance=instance, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'title': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "pk не найден"})

        try:
            Women.objects.get(pk=pk).delete()
        except:
            return Response({"error": "Объект не найден"})

        return Response({'title': f"Объект {pk} удален"})


#class WomenApiView(generics.ListAPIView):
#    queryset = Women.objects.all()
#    serializer_class = WomenSerializer
