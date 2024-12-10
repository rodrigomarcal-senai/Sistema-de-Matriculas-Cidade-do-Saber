from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    username = models.CharField(
        verbose_name="CPF",
        max_length=14,
        blank=False,
        unique=True,
        validators=[
            RegexValidator(
                r"^\d{3}\.\d{3}\.\d{3}-\d{2}$",
                message=_("Enter a valid CPF in the format XXX.XXX.XXX-XX"),
            )
        ],
        db_column="cpf",
    )

    REQUIRED_FIELDS = ["first_name", "last_name", "email"]

    class Meta:
        db_table = "usuario_sistema"

    def __str__(self):
        return self.username
