from django.shortcuts import render
# from django.views.generic import CreateView,ListView,DeleteView
from .models import Links
from django.http import HttpResponseRedirect


from bs4 import BeautifulSoup
import requests

# Create your views here.



def ScrapeView(request):

    if request.method == "POST":
        site = request.POST.get('site','')

        page = requests.get(site)
        soup = BeautifulSoup(page.text,'html.parser')

        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            Links.objects.create(address=link_address,name=link_text)

        return HttpResponseRedirect('/')
    else:
        data = Links.objects.all()

    context_object_name = 'data'

    return render(request,'scrape/scraper.html',{'data':data})



def clear(request):
    Links.objects.all().delete()
    return render(request,'scrape/scraper.html')
