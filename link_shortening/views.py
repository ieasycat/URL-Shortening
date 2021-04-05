import string
from random import randint, choice
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from link_shortening.models import Link
from link_shortening.forms import LinkForm

# Create your views here.


def reduction():
    short_url = [choice(string.ascii_letters + str(randint(0, 9))) for x in range(6)]
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
            url=url,
            abbreviated_url=reduction()
        )
        return redirect('main')

    return render(request, 'main_page.html', context)


def redirect_original(request, short_id):
    url = Link.objects.get(id=short_id)
    url.clicked()
    return HttpResponseRedirect(url.url)
