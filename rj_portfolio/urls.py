from django.urls import path
from . import views

urlpatterns = [
    #path('', views.base, name='base'),
    path('info', views.resume, name='resume'),
    path('datascience', views.datascience, name='datascience'),
    path('webscraping', views.webscraping, name='webscraping'),
    path('twitter_scrape', views.twitter_scrape, name='twitter_scrape'),
    path('convertpdf', views.convertpdf, name='convertpdf'),
    path('convertpdf_xml', views.convertpdf_xml, name='convertpdf_xml'),
    path('convertpdf_html', views.convertpdf_html, name='convertpdf_html'),
    path('convertpdf_csv', views.convertpdf_csv, name='convertpdf_csv'),
    path('convertpdf_docx', views.convertpdf_docx, name='convertpdf_docx'),
    path('converthtml', views.converthtml, name='converthtml'),
    path('converthtml_csv', views.converthtml_csv, name='converthtml_csv'),
    path('converthtml_excel', views.converthtml_excel, name='converthtml_excel'),
    path('certificates', views.certificates, name='certificates'),

]