from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from markdownx.models import MarkdownxField

# короче, в наглую копируем это и User
# в настройках копируем настройки Djoser и отправку почты (ну это понятно)
# и нужен View, который будет принимать get запрос активации аккаунта ActivateUser (тоже в наглую копируем)
# прикол в том, что нам на почту отправляют ссылку с uid и токеном, которые нужно отправить пост запросом
# либо бэк, либо фронт принимает гет запрос этой ссылки, извлекает uid и токен, и отправляет пост запрос
# получается я создаю юзера, но неактивированного (это значит, что я даже залогиниться не смогу)
# вся эта байда ставит у юзера галочку, что он активен
# если активация по почте не нужна, то в настройках djoser ставим false

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = User(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        assert extra_fields['is_staff']
        assert extra_fields['is_superuser']
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, null=False)
    USERNAME_FIELD = 'email'

    # дополняем к обычному джанговскому юзеру дополнительные поля
    phone = models.CharField(max_length=255, null=True, blank=True)

    # поля, с которыми мы в будущем хотим работать (кроме пароля и юзернейма)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    objects = CustomUserManager()

class Tag(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Subtag(models.Model):
    title = models.CharField(max_length=255)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class New(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Women(models.Model):
    title = models.CharField(max_length=255)
    myfield = MarkdownxField()
    content = models.TextField(blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='content/', blank=True, null=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.title
