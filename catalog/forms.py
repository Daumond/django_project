from django import forms

from catalog.models import Product, Version


class StyleFormMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_active':
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('date_of_creation', 'last_modified_date')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        list_word = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар', ]

        for word in list_word:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Это запрещенный продукт, нельзя добавить!')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        list_word = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар', ]

        for word in list_word:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Это запрещенный продукт, нельзя добавить!')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
