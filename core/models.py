from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
from phonenumbers import parse, geocoder

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    nascimento = models.DateField(help_text='Data de nascimento para saber os aniversariantes da semana', null=True, blank=True)
    slug = models.SlugField(unique=True, help_text="Preenchido automaticamente para facilitar a sua vida. Por favor não altere")
    telefone = PhoneNumberField(blank=False, null=False)
    cidade = models.CharField(max_length=40)
    estado = models.CharField(max_length=20, blank=True, null=True, editable=False)
    email = models.EmailField(blank=True, null=True)
    app = models.CharField(max_length=20, choices=(
        ("Whatsapp", "Whatsapp"),
        ("Telegram", "Telegram"),
        ("Signal", "Signal"),
    ))
    grupo = models.CharField(max_length=30)

    class Meta:
        ordering = ("nome", "cidade",)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("core.detail", kwargs={"slug": self.slug})

    def save(self):
        if self.telefone:
            tel = parse(self.telefone.__str__(), 'BR')
            self.estado = geocoder.description_for_number(tel, 'br')

        return super(Pessoa, self).save()