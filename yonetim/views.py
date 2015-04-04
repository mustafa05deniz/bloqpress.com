from django.shortcuts import render_to_response,get_object_or_404
from yonetim.models import *
from django.shortcuts import render
from time import gmtime, strftime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def ana_sayfa(request):
    entry=Entry.objects.all().order_by('-id')
    rapor=raporlar.objects.all().order_by('-id')
    pageCounter= PageCounter.objects.all()[0] 
    pageCounter.sayi += 1
    pageCounter.save() 
    hakkinda=PageCounter.objects.all()[1]
    iletisim=PageCounter.objects.all()[2]
    gecmis=PageCounter.objects.all()[3]
    simdi=PageCounter.objects.all()[4]
    gelecek=PageCounter.objects.all()[5]
    sol_entry=Entry.objects.all()
    katagoriler = catagory.objects.all()
    simdiki_zaman=strftime("%H:%M:%S", gmtime())
    sozler=Sozler.objects.all()
    resim1=Resim_Katalogu.objects.all()
    test_sayfalari=Testler.objects.all().order_by('-id')
    a=[]
    for i in range(1,5):
        a.append(i)
    
    return render_to_response('deneme.html',locals())
    
def hakkinda(request):
    hakkinda=PageCounter.objects.all()[1]
    hakkinda.sayi += 1
    hakkinda.save()
    pageCounter= PageCounter.objects.all()[0] 
    iletisim=PageCounter.objects.all()[2]
    gecmis=PageCounter.objects.all()[3]
    simdi=PageCounter.objects.all()[4]
    gelecek=PageCounter.objects.all()[5]
    return render_to_response('hakkinda.html',locals())

@csrf_exempt
def iletisim(request):
    iletisim=PageCounter.objects.all()[2]
    iletisim.sayi += 1
    iletisim.save()
    pageCounter= PageCounter.objects.all()[0] 
    hakkinda=PageCounter.objects.all()[1]
    gecmis=PageCounter.objects.all()[3]
    simdi=PageCounter.objects.all()[4]
    gelecek=PageCounter.objects.all()[5]
    if request.method=="POST":
        yazi=request.POST.get('yazi')
        adi=request.POST.get('adi')
        yazi_gonderme=Gelen_yazilar(gonderen_adi=adi,text=yazi)
        yazi_gonderme.save()
        return HttpResponse('<br><br><br><br><center><span class="label label-success">yazi gonderildi . 2 saniye sonra Ana Sayfaya gidiyorsun </span> <meta http-equiv="refresh" content="2; url="http://bloqpress.com/"> ')
    return render_to_response('iletisim.html',locals())


def gecmis(request):
    gecmis=PageCounter.objects.all()[3]
    gecmis.sayi += 1
    gecmis.save()
    pageCounter= PageCounter.objects.all()[0] 
    hakkinda=PageCounter.objects.all()[1]
    iletisim=PageCounter.objects.all()[2]
    simdi=PageCounter.objects.all()[4]
    gelecek=PageCounter.objects.all()[5]
    return render_to_response('gecmis.html',locals())


def simdi(request):
    simdi=PageCounter.objects.all()[4]
    simdi.sayi += 1
    simdi.save()
    pageCounter= PageCounter.objects.all()[0] 
    hakkinda=PageCounter.objects.all()[1]
    iletisim=PageCounter.objects.all()[2]
    gecmis=PageCounter.objects.all()[3]
    gelecek=PageCounter.objects.all()[5]
    return render_to_response('simdi.html',locals())

def gelecek(request):
    gelecek=PageCounter.objects.all()[5]
    gelecek.sayi += 1
    gelecek.save()
    pageCounter= PageCounter.objects.all()[0] 
    hakkinda=PageCounter.objects.all()[1]
    iletisim=PageCounter.objects.all()[2]
    gecmis=PageCounter.objects.all()[3]
    simdi=PageCounter.objects.all()[4]
    return render_to_response('gelecek.html',locals())
@csrf_exempt
def sayfa(request,soru):
    question = get_object_or_404(Entry, pk=soru)
    resim1=Resim_Katalogu.objects.all()
    pageCounter= PageCounter.objects.all()[0] 
    hakkinda=PageCounter.objects.all()[1]
    iletisim=PageCounter.objects.all()[2]
    gecmis=PageCounter.objects.all()[3]
    simdi=PageCounter.objects.all()[4]
    gelecek=PageCounter.objects.all()[5]
    sol_entry=Entry.objects.all()
    a=[]
    for i in range(1,15):
        a.append(i)
    resim=Resim_Katalogu.objects.all()
    paginator = Paginator(resim, 1) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render_to_response('yeni.html',locals())

def test(request,soru):
    question = get_object_or_404(Testler, pk=soru)
    a=[]
    for i in range(1,15):
        a.append(i)
    resim1=Resim_Katalogu.objects.all()
    pageCounter= PageCounter.objects.all()[0] 
    hakkinda=PageCounter.objects.all()[1]
    iletisim=PageCounter.objects.all()[2]
    gecmis=PageCounter.objects.all()[3]
    simdi=PageCounter.objects.all()[4]
    gelecek=PageCounter.objects.all()[5]
    sol_entry=Entry.objects.all()
    a=[]
    for i in range(1,15):
        a.append(i)
    resim=Resim_Katalogu.objects.all()
    paginator = Paginator(resim, 1) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render_to_response('yeni.html',locals())
    
