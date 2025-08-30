from django import forms
from cars.models import Car

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 20000:
            self.add_error('price', "Valor do veículo não pode ser menor que R$ 20.000 !")
        return price

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1959:
            self.add_error('factory_year', 'Ano de fabricação do veículo não pode ser menor do que 1959')
        return factory_year
