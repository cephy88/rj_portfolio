from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import HttpResponse
from pathlib import Path
import pdftables_api
import pandas as pd 
import requests 
import csv , os
from wsgiref.util import FileWrapper
import tweepy
from tweepy import OAuthHandler
from .forms import MyForm
from pdf2image import convert_from_path
import gzip


# Variable
url = "https://www.pds.com.ph/index.html%3Fpage_id=1389.html"


def base(request):
	return render(request, 'base/home.html')

def resume(request):
	return render(request, 'base/resume.html')

def datascience(request):
	return render(request, 'base/datascience.html')

def webscraping(request):
	return render(request, 'base/datascience/webscraping.html')
	
def twitter_scrape(request):
	filename = 'static/datascience/webscraping/twitter.csv'
	download_name ="twitter.csv"
	wrapper      = FileWrapper(open(filename, "rb"))
	response     = HttpResponse(wrapper,content_type='text/csv')
	response['Content-Disposition'] = "attachment; filename=%s"%download_name
	return response
	

def convertpdf(request):
	return render(request, 'base/datascience/convertpdf.html')


def convertpdf_docx(request):
	pythoncom.CoInitialize()

	word=win32com.client.Dispatch("word.Application")
	word.Visible = 0
	doc_pdf="./static/pdf/test_pdf.pdf"

	input_file=os.path.abspath(doc_pdf)
	wb=word.Documents.Open(input_file)

	filename=os.path.abspath('./static/datascience/convertpdf/PDFdata_docx.docx')

	wb.SaveAs2(filename,FileFormat=16)
	print("pdf to Doc is complete")
	wb.Close()
	word.Quit()
	
	download_name ="PDFdata_docx.docx"
	wrapper      = FileWrapper(open(filename, 'rb'))
	response     = HttpResponse(wrapper,content_type='application/vnd')
	response['Content-Disposition'] = "attachment; filename=%s"%download_name
	return response



def convertpdf_csv(request):
	df = "./static/pdf/pdf.pdf"
	filename = 'static/datascience/convertpdf/PDFdata_csv.csv'
	c = pdftables_api.Client('sx112tn9r25e')
	c.csv(df, filename)
	download_name ="PDFdata_csv.csv"
	wrapper      = FileWrapper(open(filename))
	response     = HttpResponse(wrapper,content_type='text/csv')
	response['Content-Disposition'] = "attachment; filename=%s"%download_name
	return response


def convertpdf_xml(request):
	df = "./static/pdf/pdf.pdf"
	filename = 'static/datascience/convertpdf/PDFdata_docx.xml'
	c = pdftables_api.Client('sx112tn9r25e')
	c.xml(df, filename)
	download_name ="PDFdata_docx.xml"
	wrapper = FileWrapper(open(filename))
	response = HttpResponse(wrapper,content_type="text/xml; charset=utf-8")
	response['Content-Disposition'] = "attachment; filename=%s"%download_name
	return response

def convertpdf_html(request):
	df = "./static/pdf/pdf.pdf"
	filename = 'static/datascience/convertpdf/PDFdata_docx.html'
	c = pdftables_api.Client('sx112tn9r25e')
	c.html(df, filename)
	download_name ="PDFdata_docx.html"
	wrapper = FileWrapper(open(filename))
	response = HttpResponse(wrapper,content_type="application/liquid; charset=utf-8")
	response['Content-Disposition'] = "attachment; filename=%s"%download_name
	return response


@xframe_options_exempt
def converthtml(request):
	return render(request, 'base/datascience/converthtml.html')


def converthtml_csv(request):
	table = pd.read_html(url)[0] 
	table.to_csv('static/datascience/converthtml/data.csv')  
	filename = 'static/datascience/converthtml/data.csv'
	download_name ="data.csv"
	wrapper      = FileWrapper(open(filename))
	response     = HttpResponse(wrapper,content_type='text/csv')
	response['Content-Disposition'] = "attachment; filename=%s"%download_name
	return response

def converthtml_excel(request):
	table = pd.read_html(url)[0] 
	table.to_excel('static/datascience/converthtml/data.xlsx')  
	filename = 'static/datascience/converthtml/data.xlsx'
	download_name ="data_xlsx.xlsx"
	wrapper      = FileWrapper(open(filename, "rb"))
	response     = HttpResponse(wrapper,content_type='application/ms-excel')
	response['Content-Disposition'] = "attachment; filename=%s"%download_name
	return response

def certificates(request):
	return render(request, 'base/certificates.html')


def get_frame():
	camera =cv2.VideoCapture(0)
	while True:
		_, img = camera.read()
		imgencode=cv2.imencode('.jpg',img)[1]
		stringData=imgencode.tostring()
		yield (b'--frame\r\n'b'Content-Type: text/plain\r\n\r\n'+stringData+b'\r\n')
	del(camera)

def indexscreen(request):
    try:
        template = "rj_base\rj_portfolio\templates\base\screens.html"
        return render(request,template)
    except HttpResponseServerError:
        print("error")

def dynamic_stream(request,stream_path="video"):
    try :
        return StreamingHttpResponse(get_frame(),content_type="multipart/x-mixed-replace;boundary=frame")
    except :
        return "error"