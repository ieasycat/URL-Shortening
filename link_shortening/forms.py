from django import forms
from link_shortening.models import Link


class LinkForm(forms.Form):
    url = forms.URLField()
    abbreviated_urls = forms.CharField(max_length=6, required=False, error_messages={'required': 'Error'})

    def clean(self):
        abbreviated_urls = self.cleaned_data.get("abbreviated_urls")
        if abbreviated_urls:
            check = Link.objects.filter(abbreviated_url=f'http://127.0.0.1:8000/{abbreviated_urls}')

            if check:
                check = check[0].abbreviated_url.split('/')

                if abbreviated_urls == check[3]:
                    raise forms.ValidationError('This short link already exists, enter another one.')
        return self.cleaned_data
