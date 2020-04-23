from django import forms

class XSearchForm(forms.Form):
    query = forms.CharField(label = 'Поиск...', min_length = 4, max_length = 255)

    query.widget.attrs.update({'class': 'form-control x-search-input'})
    query.widget.attrs.update({'autocomplete': 'off'})
