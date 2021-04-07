import string
from random import randint, choice
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from link_shortening.models import Link
from link_shortening.forms import LinkForm

# Create your views here.


def reduction(user_short_url=None):
    if user_short_url:
        short_url = user_short_url
    else:
        short_url = ''.join([choice(string.ascii_letters + str(randint(0, 9))) for x in range(6)])
    return f"http://127.0.0.1:8000/{short_url}"


def main(request):
    urls = Link.objects.all()
    if request.POST:
        form = LinkForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            url = cd.get('url')
            user_short_url = cd.get('abbreviated_urls')

            Link.objects.create(
                url=url,
                abbreviated_url=reduction(user_short_url)
            )
            return redirect('main')
    else:
        form = LinkForm()

    context = {
        'urls': urls[::-1],
        'form': form,
    }
    return render(request, 'main_page.html', context)


def redirect_original(request, short_id):
    url = Link.objects.get(id=short_id)
    url.clicked()
    return HttpResponseRedirect(url.url)
