from django import forms
from rango.models import Category, Page


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=124,
                            help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=123,
                            help_text="Please enter the title of the page")
    url = forms.URLField(max_length=123,
                        help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get()
        if url and url.startswitch('http://'):
            url = 'http://' + url 
            cleaned_url['url'] = url

            return cleaned_data

    class Meta:
        model = Page
        exclude = ('category',)