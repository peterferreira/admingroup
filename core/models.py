from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
import requests

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    nascimento = models.DateField(help_text='Data de nascimento para saber os aniversariantes da semana', null=True, blank=True)
    slug = models.SlugField(unique=True, help_text="Preenchido automaticamente para facilitar a sua vida. Por favor não altere")
    telefone = PhoneNumberField(blank=False, null=False)
    np_masp = models.CharField(max_length=20, verbose_name='Número de Polícia ou MASP', null=True, blank=True, help_text='Preenchimento opcional')
    cep = models.CharField(max_length=9, blank=True, null=True, help_text='Se preencher o cep, o endereço será preenchido automaticamente', verbose_name='CEP')
    endereco = models.CharField(max_length=100, null=True, blank=True, verbose_name='Endereço', help_text='Deverá ser preenchido automaticamente pelo cep.')
    Numero = models.CharField(max_length=5, null=True, blank=True, verbose_name='Número')
    bairro = models.CharField(max_length=100, null=True, blank=True, verbose_name='Bairro', help_text='Deverá ser preenchido automaticamente pelo cep.')
    cidade = models.CharField(max_length=40, null=True, blank=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    app = models.CharField(max_length=20, null=True, blank=True, choices=(
        ("Whatsapp", "Whatsapp"),
        ("Telegram", "Telegram"),
        ("Signal", "Signal"),
    ))
    grupo = models.CharField(max_length=30, null=True, blank=True,)

    class Meta:
        ordering = ("nome", "cidade",)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("core.detail", kwargs={"slug": self.slug})

    def getcep(self, cep):
        try:
            j = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep.replace('-', '')))
            r = j.json()
            endereco = r['logradouro']
            bairro = r['bairro']
            cidade = r['localidade']
            estado = r['uf']
            return (endereco, cidade, estado, bairro)
        except:
            j = requests.get('https://geocode.xyz/{}?json=1'.format(cep[5:] + '-' + cep[-3:]))
            r = j.json()['standard']
            end = ''
            en = r['addresst'].split()
            for t in range(1, len(en)):
                end += en[t]
                end += ' '
            endereco = end.strip()
            cidade = r['city']
            estado = r['region']
            return (endereco, cidade, estado, '')


    def save(self):
        if self.cep:
            resposta = self.getcep(self.cep)
            self.endereco = resposta[0]
            self.cidade = resposta[1]
            self.estado = resposta[2]
            self.bairro = resposta[3]
        return super(Pessoa, self).save()

