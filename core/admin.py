from django.contrib import admin

from core.models import Acompanhamento_animal, Animal, Especie, Usuario, Raça, adocao, doacao 

admin.site.register(Acompanhamento_animal)
admin.site.register(Raça)
admin.site.register(Especie)
admin.site.register(Animal)
admin.site.register(doacao)
admin.site.register(adocao)
admin.site.register(Usuario)