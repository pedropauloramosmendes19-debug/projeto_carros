from django.core.management.base import BaseCommand
from cars.models import Car
import csv
from decimal import Decimal

class Command(BaseCommand):
    help = 'Ajuda a colocar preços nos modelos da tabela de uma forma mais rápida, caso tenha que alterar.'

    def handle(self, *args, **options):

        lista_de_precos = []
        try:
            with open('preco.csv', 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    lista_de_precos.append(Decimal(row['price']))
                self.stdout.write('15 valores serão atribuídos nos carros presentes no banco de dados!')

        except FileNotFoundError:

            self.stdout.write(self.style.ERROR('Arquivo não encontrado'))
            return

        carros = Car.objects.all().order_by('id')

        if len(carros) != len(lista_de_precos):
            self.stdout.write(self.style.Error(
                'Existem mais carros do que valores na tabela de preços!!!'
            ))
            return

        self.stdout.write(self.style.SUCCESS(
            'Atualizando os valores no banco de dados!!!'
        ))
        for carro, preco in zip(carros, lista_de_precos):
            carro.price = preco
            carro.save()
            self.stdout.write(self.style.SUCCESS(f'{carro.model} teve seu preço atualizado para {carro.price}'))
            self.stdout.write(self.style.SUCCESS('Operação concluída com sucesso!'))