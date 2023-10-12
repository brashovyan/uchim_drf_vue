from rest_framework import serializers
from .models import Women, Category, Tag, New, Subtag
from rest_framework.renderers import JSONRenderer
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


# пример с полем Many to many
# {
#     "title": "new 1",
#     "description": "asdas das das das dasd asd",
#     "tags" : [1, 2]
# }
# tags - просто айдишники
# методотом put можно изменить список айдишников, просто отправив новый список
class NewSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    class Meta:
        model = New
        fields = "__all__"


# пример с полем ForeignKey (просто отправляем айдишник)
class SubtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtag
        fields = "__all__"


class WomenSerializer(serializers.ModelSerializer):
    # юзер будет добавляться автоматически, но хрен мы его получим
    # owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    # так юзер будет виден, но надо будет дополнительную байду писать во views
    # например serializer.validated_data['owner'] = self.request.user
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Women
        # fields = ("id", "title", "content", "photo", "cat")
        fields = "__all__"

    # def validate_НазваниеПоляСериалайзера(self, value):
    #     if условия_при_которых_значение_невалидно:
    #         raise serializers.ValidationError("Описание ошибки")
    #     return value

    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Описание ошибки")
        return value



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"



# class WomenModel():
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


# class WomenSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     content = serializers.CharField(required=False)
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     photo = serializers.ImageField()
#     cat_id = serializers.IntegerField(required=False)
#
#     def create(self, validated_data):
#         return Women.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.content = validated_data.get("content", instance.content)
#         instance.time_update = validated_data.get("time_update", instance.time_update)
#         instance.is_published = validated_data.get("is_published", instance.is_published)
#         instance.photo = validated_data.get("photo", instance.photo)
#         instance.cat_id = validated_data.get("cat_id", instance.cat_id)
#         instance.save()
#         return instance


# def encode():
#     model = WomenModel('Anjelina', "Cool actor")
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)