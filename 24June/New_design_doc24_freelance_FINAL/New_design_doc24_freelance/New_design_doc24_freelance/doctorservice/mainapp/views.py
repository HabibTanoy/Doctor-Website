from django.forms import model_to_dict
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.utils.text import slugify
from django.db.models import Q
from . models import Service_type
from doctors.models import Domain, LocationDoctor, Doctor

from doctors.models import Doctor
from serviceapp.models import Service, LocationCompany, DomainService
# from .models import Slider, Faq, Gallery, Service
from django.views.generic import ListView, DetailView, TemplateView

domain_doctor = ['Acupunctor','Alergolog','Androlog','Cardiochirurg','Cardiolog','Cardiolog intervenţionist','Chirurg','Chirurg estetician','Chirurg plastician',
'Cosmetolog',
'Dermatolog',
'Dietolog',
'Nutriționist',
'Ecografist',
'Endocrinolog',
'Endoscopist',
'Fitoterapeut',
'Fizioterapeut',
'Flebolog',
'Gastroenterolog',
'Ginecolog',
'Hematolog',
'Hepatolog',
'Homeopat',
'Imagist',
'Infecționist',
'Internist',
'Kinetoterapeut',
'Logoped',
'Mamolog',
'Medic de familie',
'Narcolog',
'Nefrolog',
'Neurochirurg',
'Neurolog',
'Obstetrician-ginecolog',
'Oftalmolog',
'Oncolog',
'Ortoped-traumatolog',
'Otorinolaringolog (ORL)',
'Pediatru',
'Pneumolog',
'Proctolog',
'Psihiatru',
'Psiholog',
'Psihoterapeut',
'Reabilitolog',
'Reanimatolog-neonatolog',
'Reflexoterapeut',
'Reumatolog',
'Sexolog',
'Specialist în masaj',
'Stomatolog',
'Terapeut manual',
'Triholog',
'Urolog',
'Venerolog',
'Vertebrolog']

servicii = ['ULTRASONOGRAFIE',
'neurosonografia prin fontanelă',
'ecografie glanda tiroidă',
'ecografie glanda tiroidă 2D+Doppler',
'ecografie glanda tiroidă+ganglioni limfatici',
'ecografia glandele mamare',
'ecografia glandele mamare 2D+Doppler',
'ecografia glandele mamare+ganglioni limfatici',
'ecografie țesuturile moi',
'țesuturile moi și ganglionii limfatici',
'ECOGRAFIE ABDOMINALA',
'ecografia unui organ în dinamică',
'aprecierea colecțiilor libere în una din cavități',
'ecografie [ficat și vezica biliară]',
'ecografie [pancreas și splină]',
'ecografie pancreas 2D în scară gri',
'ecografia organelor abdominale [ficat, vez.biliară, splină, pancreas]',
'ECOGRAFIE SISTEMULUI URINAR',
'organele sistemului urinar [rinichi, glandele suprarenale, vezica urinară]',
'ecografia sistemului urogenital femei/barbați [gland. suprarenale, rinichi, vezica urinară, căile urinare,org. genitale interne] transabdominal',
'ecografia sistemului urogenital femei [glandele suprarenale, rinichi, vezica urinară, căile urinare, uter, ovare] transvaginal',
'ecografia sistemului urogenital bărbați [glandele suprarenale, rinichi, vezica urinară, căile urinare, veziculele seminale, prostata] transrectal',
'ECOGRAFIA BAZINULUI MIC',
'ecografia organelor bazinul mic femei [vezica urinara, uter, ovare] transabdominal',
'ecografia organelor bazinul mic femei [uterul, trompele uterine, ovarele, colul uterin, vaginul] transvaginal',
'ecografia organelor bazinul mic barbati [vezica urinara, prostata, veziculele seminale] transabdominal',
'ecografia organelor bazinul mic barbati [vezica urinara, prostata, veziculele seminale] transrectal',
'foliculometria transvaginală',
'foliculometria transabdominală',
'ecografia prostatei transabdominal',
'ecografia prostatei transrectal',
'ecografie prostată și vezica urinară',
'ecografie prostată și veziculile seminale',
'ecografia prostatei, veziculele seminale, scrotului 2D+Doppler',
'ecografia scrotului [testiculele, epididimul, plexul panpiniform]',
'ecografia scrotului [testiculele]+Doppler',
'ecografia scrotului copii [testiculele]+Doppler',
'ecografia penisului',
'ECOGRAFIE COMPLEXA',
'ecografie glanda tiroidă, glandele mamare, organele bazinului mic',
'ecografie organele abdominale, sistemul urinar',
'ecografie organele abdominale, sistemul urinar copii',
'ecografie organele abdominale, organele sistemului urogenital',
'ecografie femei: organele abdominale, glanda tiroidă, glandele mamare, organele sistemului urogenital transvaginal',
'ecografie bărbați: organele abdominale, glanda tiroidă, organele sistemului urogenital transrectal',
'ecografie femei: glanda tiroidă/paratiroidă, organele abdominale, organele sistemului urogenital transvaginal',
'ecografie bărbați / femei: glanda tiroidă/paratiroidă, organele abdominale, organele sistemului urogenital transabdominal',
'ecografie copii pînă la 12 ani',
'ULTRASONOGRAFIE OBSTETRICĂ',
'examen ecografic sarcină unică, trimestrul I',
'examen ecografic ginecologic transabdominal [până la 10 săpt. sarcină]',
'examen ecografic ginecologic endovaginal [până la 10 săpt. sarcini]',
'examen ecografic sarcină multiplă, trimestrul I',
'examen ecografic în sarcină unică, trim.1, screening pentru 11-14 săptămâni, transabdominal',
'examen ecografic în sarcină multiplă, trim.1, screening pentru 11-14 săptămâni, transabdominal',
'examen ecografic transabdominal în trim.1 sarcină',
'examen ecografic endovaginal în trim.1 sarcină',
'examen ecografic în trim.2-3 sarcină',
'examen ecografic în trim.2-3 sarcină multiplă',
'examen ecografic în trim.2 sarcină',
'ECOCARDIOGRAFIA CORDULUI FĂTULUI',
'examen ecografic în trim.2 sarcină+Doppler',
'Ecocardiografia cordul fătului',
'examen ecografic în trim.3 sarcină+Doppler',
'examen ecografic în sarcină unică, trim.2-3, vizualizare 4D, poze, înreg. CD',
'examen ecografic în sarcină multiplă, trim.2-3, vizualizare 4D, poze, înreg. CD',
'ULTRASONOGRAFIA MUSCULOSCHELETOASĂ',
'articulația șoldului la nou-născuți după metoda Graf',
'nervul median și ulnar în sindrom de canal carpian/cubital/Guyon - 1 mână',
'nervul median și ulnar în sindrom de canal carpian/cubital/Guyon - 2 mâini',
'articulațiile palmei sau plantei',
'articulațiile palmelor sau plantelor',
'unei articulații',
'două articulații simetrice',
'două articulații diferite',
'unei zone anatomice',
'intervenție ecoghidată a unei articulații',
'intervenție ecoghidată a două articulații simetrice sau diferite',
'intervenție ecoghidată a articulației coxofemurale sau sacroiliace',
'intervenție ecoghidată a articulațiilor coxofemurale sau sacroiliace',
'MAMOGRAFIE',
'mamografia ambelor glandelor mamare în regim digital, 4 filme',
'mamografia ambelor glandelor mamare în regim digital, 2 filme',
'mamografia unei glande mamare în regim digital, 1 film',
'dublarea rezultatului mamografiei pe film digital, 2 filme',
'dublarea rezultatului mamografiei digitale pe CD',
'RADIOGRAFIE',
'craniu',
'orbitelor',
'sinusurile paranazale',
'oasele nazale',
'șelei turcești',
'vertebra cervicală C1',
'coloana vertebrală cervicală',
'coloana vertebrală toracală',
'coloana vertebrală lombară',
'osul sacral și coccis',
'articulația sacro-iliacă',
'osul pubian',
'oasele bazinului',
'claviculă',
'omoplat',
'articulația humerală',
'oasele brațului',
'plantei sau mână',
'articulația radio-carpiană',
'articulația cotului',
'organelor cutiei toracice',
'cavitatea abdominală',
'sistemul urinar',
'articulația șoldului',
'femur',
'gambă',
'articulația genunchiului',
'articulația talocrurală',
'rotula',
'calcaneu',
'oasele temporale',
'rino-laringe',
'Tomografie computerizată',
'cerebrală fără contrast',
'cerebrală cu contrast',
'șelei turcești și a creierului fără contrast',
'șelei turcești și a creierului cu contrast',
'oasele temporale',
'sinusurile paranazale',
'sinusurile paranazale și creierul',
'sinusurile paranazale și creierul cu contrast',
'nazofaringele',
'nazofaringele cu contrast',
'coloana vertebrală cervicală',
'coloana vertebrală toracală',
'coloana vertebrală lombo-sacrală',
'vertebrelor, coloanei vertebrale',
'toracelui și mediastinului',
'toracelui și mediastinului cu contrast',
'toracelui și mediastinului cu bronhoscopie virtuală',
'abdomen fără contrast',
'abdomen cu contrast',
'abdomen fără contrast',
'abdomen cu contrast',
'organele bazinului mic fără contrast',
'organele bazinului mic cu contrast',
'Colonoscopie virtuală',
'Colonoscopie virtuală cu contrast',
'o regiune a membrului',
'articulații',
'țesuturile moi cu contrast',
'bilanț oncologic fără contrast',
'bilanţ oncologic cu contrast',
'ECG',
'Electrocardiograma',
'Electrocardiografia de repaus',
'Electrocardiografia de efort fizic',
'Electrocardiografia de efort fizic',
'Funcția ventilației pulmonare',
'ECOCARDIOGRAFIE',
'ecocardiografie fetală',
'ecocardiografia copii 0-12 ani',
'ecocardiografia',
'ecocardiografia',
'MONOTORIZARE CARDIOLOGICĂ HOLTER',
'monitorizare ECG 7 derivații, 24 ore',
'monitorizare ECG 12 derivații, 24 ore',
'monitorizare ECG 7 derivații, 48 ore',
'monitorizare ECG 12 derivații, 48 ore',
'monitorizare ECG 7 derivații, 72 ore',
'monitorizare ECG 12 derivate, 72 ore',
'monitorizare ECG 12 derivate, 7 zile',
'Monitorizarea tensiunii arteriale - 24 ore',
'ELASTOGRAFIE',
'un organ sau o zonă anatomică [glanda tiroidă, glanda mamară, ficat, rinichi, uter, ovar, prostată, scrotul, țesuturi moi sau ganglioni limfatici]',
'elastografia + Shear Wave [glanda tir,oidă, glanda mamară, ficat, rinichi, uter, ovar, prostată, scrotul, țesuturi moi sau ganglioni limfatici]',
'EEG',
'VEEG-monitoring cu înreg. de noapte',
'VEEG-monitoring cu înregistrare de 24 ore',
'Electroneuromiografia',
'VEEG-monitoring cu probele funcționale',
'VEEG-monitoring cu înreg. de zi',
'Encefalografie',
'SONODOPPLERPGRAFIA',
'Examen Duplex/Triplex al vaselor sanguine [2D+Doppler color+Doppler spectral]',
'vasele brahiocefalice, porțiunile extracraniene',
'arterele sau venele membrelor superioare',
'arterele sau venele membrului superior',
'vasele brahiocefalice, porțiunile extra și intracraniene',
'vasele [artere și vene] membrului superior sau inferior',
'vasele [artere și vene] membrelor superioare sau inferioare',
'arterele sau venele membrului inferior',
'arterele sau venele membrelor inferioare',
'arterele sau venele membrelor inferioare-cu segmentul abdominal',
'vasele unui sistem de organe',
'sistemul porto-caval',
'arterele renale',
'aorta abdominală',
'aorta abdominală + ramurile viscerale',
'Dupplex scanare a vaselor extra / intracraniene',
'Dupplex scanare a aortei abdominale 2D+Doppler',
'Dupplex scanarea vaselor abdominale [aorta, vena cava inferior]',
'Dupplex scanare a sistemului Venos Port 2D+Doppler',
'Dupplex scanare a arterelor renale bilateral',
'INVESTIGAȚII ENDOSCOPIE DE DIAGNOSTIC',
'Cromoendoscopie cu colorant',
'Biopsie endoscopică cu ansă',
'Biopsie endoscopică cu forcepsul',
'Videocolonoscopie avansată de control după intervenție endoscopică',
'Videorectosigmoidoscopie complexă avansată',
'Videoesofagogastroduodenoscopie + determ. germ. Helicocacter Pylori',
'Videoesofagogastroduodenoscopie',
'Duodenoscopie ca suplimentare a VEGDS SD',
'VEGDS HD de control după intervenția endoscopică',
'Videocolonoscopie complexă avansată',
'recoltarea materialului pentru Helicobacter Pylori',
'test Helicobacter Pylori',
'DENSITOMETRIA OSOASĂ',
'osteodensitometria - antebraț',
'osteodensitometria - antebraț bilateral',
'osteodensitometria - col femural',
'osteodensitometria - col femural bilateral',
'osteodensitometria - coloana lombară',
'osteodensitometria - coloana lombară + consult. medicului',
'osteodensitometria - coloana lombară+col femural',
'osteodensitometria - coloana lombară+col femural + consult. medicului',
'osteodensitometria generală copii',
'osteodensitometria generală maturi',
'osteodensitometria generală maturi + consult. medicului',
'ANGIOGRAFIE PRIN TC',
'Angiografia cerebrală',
'Angiografia carotidiană și cerebrală',
'Angiografia arterelor cerebrale intra-extra-craniene',
'Angiografia aortei',
'Angiografia toracală sau abdominală',
'Angiografia cordului - CA-scoring',
'Angiografia arterelor carotide',
'Angiografia arterelor pulmonare',
'Angiografia arterelor renale',
'Angiografia arterelor hepatice, pancreatice',
'Arteriografia renală, inclusiv urografia',
'Angiografia arterelor bazinului mic',
'Angiografia arterelor membrelor superioare sau inferioare',
'BRONHOSCOPIE VIRTUALĂ',
'DIAGNOSTIC DE LABORATOR',
'ÎNREGISTRAREA INVESTIGAȚIEI PE FOTOGRAFIE',
'ÎNREGISTRAREA INVESTIGAȚIEI PE CD']

serviciu_domen = [
'Ultrasonografie',
'Ultrasonografie obstetrică',
'Ultrasonografia musculoscheletară',
'Mamografie',
'Radiografie',
'Tomografie computerizată',
'Electrocardiografie (ECG)',
'Ecocardiografie',
'Monitorizare cardiologică Holter',
'Elastografia',
'Electroencefalografia (EEG)',
'Sonodopplerografia',
'Investigații endoscopie de diagnostic',
'Densitometria osoasă',
'Angiografie prin TC',
'Bronhoscopie virtuală',
'Diagnostic de laborator',
'Înregistrarea investigației pe fotografie',
'Înregistrarea investigației pe CD',]

servicii1 = ["sub1", "sub12", "sub13", "sub5", "sub331"]
servicii2 = ["sub1", "sub1dsdsds dsdsds dsdsdsd2", "sub1 dsdsdsd dsdsds 3", "sub5", "sub33 dsdsdsd1", "dasdas"]
servicii3 = ["sub1", "sub1dsdsds dsdsds dsdsdsd2", "sub1 dsdsdsd dsdsds 3", "sub5", "sub33 dsdsfdfdsd1", "dsada", "afa"]
load_more1 = ["sub1", "sub12", "sub13", "sub5", "sub331"]
load_more2 = ["sub1", "sub1dsdsds dsdsds dsdsdsd2", "sub1 dsdsdsd dsdsds 3", "sub5", "sub33 dsdsdsd1", "dasdas"]
load_more3 = ["sub1", "sub1dsdsds dsdsds dsdsdsd2", "sub1 dsdsdsd dsdsds 3", "sub5", "sub33 dsdsfdfdsd1", "dsada", "afa"]
context = {"service_type": ["Doctor", "Serviciu"], "service_doc": domain_doctor,
           "service_serv": servicii, "service_domain": serviciu_domen, "location": ['Chișinău', 'Botanica', 'Buiucani', 'Centru', 'Ciocana', 'Sculeanca', 'Rîșcani', 'Telecentru'],
           "el1": {"title1": "First Column", "subcategories": servicii1 },
            "el2": {"title1": "Second Column", "subcategories": servicii2 },
            "el3": {"title1": "Fird Column", "subcategories": servicii3 },
            "el4": {"title1": "Fird Column load more", "subcategories": load_more1 },
            "el5": {"title1": "Second Column load more", "subcategories": load_more2 },
            "el6": {"title1": "Fird Column load more", "subcategories": load_more3 }
           }


def homeview(request):
    # context = {"service_type":["doctor","service"], "service_doc":["brodeaga", "ibati"], "service_serv":["glea", "iomaio"], "location":["glea", "iomaio"]}
    return render(request, 'mainapp/base_new.html', context)


def choose_city(request):
    # print(request.POST['service_type'])
    # print(request.POST['service_type'])
    # print(request.POST.get('service_doc'))
    # print(request.POST['service_serv'])

    if request.POST.get('service_doc'):
        service_type = slugify(request.POST['service_type'])
        service_doc = slugify(request.POST['service_doc'])
        location = slugify(request.POST['location'])
        return redirect('deals_by_city', permanent=True, service_type=service_type, service_doc=service_doc, location=location)
    else:
        service_type = slugify(request.POST['service_type'])
        service_serv = slugify(request.POST['service_serv'])
        print(service_serv)
        print("ds")
        location = slugify(request.POST['location'])
        return redirect('deals_by_city_serv', permanent=True, service_type=service_type, service_serv=service_serv, location=location)


def deals_by_city(request, service_type=None, location=None, service_serv=None, service_doc=None):
    print(service_serv)
    print(service_type)
    if service_type == 'doctor':
        print(service_serv)
        print(location)
        print(service_doc)
        # city = get_object_or_404(City, pk=city_id)
        # deals = Deal.objects.filter(city=city)
        page_obj = Doctor.objects.filter(service_type__slug=service_type, domain__slug=service_doc, location__slug=location)
        print(page_obj)
        # print(dir(request.environ))
        # full_context = context
        # full_context.update(page_obj)


        # print(page_obj)
        return render(request, 'doctors/doctor_list_freelance.html', context={'page_obj':page_obj, "service_type": ["Doctor", "Serviciu"], "service_doc": domain_doctor,
               "service_serv": servicii, "location": ['Chișinău', 'Botanica', 'Buiucani', 'Centru', 'Ciocana', 'Sculeanca', 'Rîșcani', 'Telecentru']})
    else:
        print(request.POST)
        print(service_type)
        print(service_serv)
        # service_type = None
        # service_serv = None
        # location = None
        # page_obj = Service.objects.filter(name="service_2")
        # second = DomainService.objects.prefeth_related()
        # page_obj = LocationCompany.objects.filter(service_type__slug=service_type, domain__slug=service_serv)
                                         # city__slug=location)
                                         # city__slug=location, sector__slug=location)
        print(service_serv)
        page_obj = LocationCompany.objects.filter(
            Q(slug_city=location) | Q(sector='some sector'),
            domain__slug_domain=service_serv,
            # or query for city or sector
        ).distinct()
        print(page_obj)
        return render(request, 'serviceapp/service_list_freelance.html',
                      context={'page_obj': page_obj, "service_type": ["Doctor", "Serviciu"],
                               "service_doc": domain_doctor,
                               "service_serv": servicii,
                               "location": ['Chișinău', 'Botanica', 'Buiucani', 'Centru', 'Ciocana', 'Sculeanca',
                                            'Rîșcani', 'Telecentru']})



def deals_by_city_serv(request, service_type=None, location=None, service_serv=None, service_doc=None):
    print(service_serv)
    if service_type == 'doctor':
        print(service_serv)
        # city = get_object_or_404(City, pk=city_id)
        # deals = Deal.objects.filter(city=city)
        page_obj = Doctor.objects.filter(service_type__slug=service_type,domain__slug=service_doc,location__slug=location).values()
        # print(dir(request.environ))
        # full_context = context
        # full_context.update(page_obj)
        # print(page_obj)

        return render(request, 'doctors/doctor_list_freelance.html', context={'page_obj':page_obj, "service_type": ["Doctor", "Serviciu"], "service_doc": domain_doctor,
               "service_serv": servicii, "location": ['Chișinău', 'Botanica', 'Buiucani', 'Centru', 'Ciocana', 'Sculeanca', 'Rîșcani', 'Telecentru']})
    else:
        print(request.POST)
        print(service_type)
        print(service_serv)
        print(location)
        # service_type = None
        # service_serv = None
        # location = None
        # page_obj = Service.objects.filter(name="service_2")
        # second = DomainService.objects.prefeth_related()
        # page_obj = LocationCompany.objects.filter(service_type__slug=service_type, domain__slug=service_serv)
                                         # city__slug=location)
                                         # city__slug=location, sector__slug=location)
        sectoare = ['botanica', 'telecentru', 'buiucani', 'centru', 'ciocana', 'rascani']
        domenii = ['ultrasonografie']

        if location in sectoare:
            if service_serv in domenii:
                page_obj = LocationCompany.objects.filter(
                    Q(slug_sector=location) | Q(slug_city=location),
                    domain__slug_domain=service_serv,
                ).distinct()
            else:
                page_obj = LocationCompany.objects.filter(
                    Q(slug_sector=location) | Q(slug_city=location),
                    services__name=service_serv,
                ).distinct()
        else:
            if service_serv in domenii:
                page_obj = LocationCompany.objects.filter(
                    Q(slug_city=location) | Q(sector='some sector'),
                    domain__slug_domain=service_serv,
                    # or query for city or sector
                ).distinct()
            else:
                page_obj = LocationCompany.objects.filter(
                    Q(slug_city=location) | Q(sector='some sector'),
                    services__name=service_serv,
                    # or query for city or sector
                ).distinct()

        data = context
        data['page_obj'] = page_obj
        return render(request, 'serviceapp/service_list_freelance.html', context=context)
                      # {'page_obj': page_obj, "service_type": ["Doctor", "Serviciu"],
                      #          "service_doc": domain_doctor,
                      #          "service_serv": servicii,
                      #          "location": ['Chișinău', 'Botanica', 'Buiucani', 'Centru', 'Ciocana', 'Sculeanca',
                      #                       'Rîșcani', 'Telecentru']})






# class HomeView(ListView):
#     template_name = 'base_list.html'
#     queryset = Service.objects.all()
#     context_object_name = 'serviceapp'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['sliders'] = Slider.objects.all()
#         context['experts'] = Doctor.objects.all()
#         return context
#
# #
# class ServiceListView(ListView):
#     queryset = Service.objects.all()
#     template_name = "serviceapp/serviceapp.html"
#
#
# class ServiceDetailView(DetailView):
#     queryset = Service.objects.all()
#     template_name = "serviceapp/service_details.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["serviceapp"] = Service.objects.all()
#         return context


# class DoctorListView(ListView):
#     template_name = 'serviceapp/team.html'
#     queryset = Doctor.objects.all()
#     paginate_by = 8


# class DoctorDetailView(DetailView):
#     template_name = 'serviceapp/team-details.html'
#     queryset = Doctor.objects.all()
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["doctors"] = Doctor.objects.all()
#         return context


# class FaqListView(ListView):
#     template_name = 'serviceapp/faqs.html'
#     queryset = Faq.objects.all()
#
#
# class GalleryListView(ListView):
#     template_name = 'serviceapp/gallery.html'
#     queryset = Gallery.objects.all()
#     paginate_by = 9
#
#
# class ContactView(TemplateView):
#     template_name = "serviceapp/contact.html"
#
#     def post(self, request, *args, **kwargs):
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
#
#         if subject == '':
#             subject = "Heartcare Contact"
#
#         if name and message and email and phone:
#             send_mail(
#                 subject+"-"+phone,
#                 message,
#                 email,
#                 ['expelmahmud@gmail.com'],
#                 fail_silently=False,
#             )
#             messages.success(request, " Email hasbeen sent successfully...")
#
#         return redirect('contact')
