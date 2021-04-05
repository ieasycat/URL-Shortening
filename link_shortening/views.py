from random import randint
from django.http import HttpResponseRedirect
from django.shortcuts import render
from link_shortening.models import Link
from link_shortening.forms import LinkForm

# Create your views here.


def reduction():
    short_url = [(str(randint(0, 9))) for i in range(5)]
    return f"http://127.0.0.1:8000/{''.join(short_url)}"


def main(request):
    form = LinkForm(request.POST)
    urls = Link.objects.all()
    context = {
        'urls': urls,
        'form': LinkForm(),
    }

    if form.is_valid():
        cd = form.cleaned_data
        url = cd.get('url')

        Link.objects.create(
            link=url,
            abbreviated_link=reduction()
        )
    return render(request, 'main_page.html', context)


def redirect_original(request, short_id):
    url = Link.objects.get(id=short_id)
    url.clicked()
    return HttpResponseRedirect(url.link)
