from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, sex, date_of_birth, password=None):
        if not email:
            raise ValueError('Не введена электронная почта')
        if not first_name:
            raise ValueError('Не введено имя')
        if not sex:
            raise ValueError('Не выбран пол')
        if not date_of_birth:
            raise ValueError('Не введена дата рождения')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            sex=sex,
            date_of_birth=date_of_birth
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, sex, date_of_birth, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            sex=sex,
            date_of_birth=date_of_birth,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
        unique=True
    )
    first_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=1)  # 1m, 2f
    pic = models.CharField(max_length=16, default="Jessica")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

