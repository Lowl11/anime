from django import forms

class XSearchForm(forms.Form):
    query = forms.CharField(label = 'Поиск...', max_length = 255)

    query.widget.attrs.update({'class': 'form-control x-search-input'})
