from django.shortcuts import render
from django.shortcuts import redirect
from .models import SEO_data
from .forms import ContactForm
from django.contrib	import messages
from decouple import config
from bitrix24 import Bitrix24, BitrixError

import datetime

def show_index(request):
	try:
		seo_information = SEO_data.objects.get(page="ГЛАВНАЯ")
	except:
		seo_information = None

	context = {
		'seo_information': seo_information,
		'actual_year': datetime.datetime.now().strftime("%Y"),
	}
	return render(request, 'baseapp/index.html', context)

def show_dvs_page(request):

	try:
		seo_information = SEO_data.objects.get(page="ДВС")
	except:
		seo_information = None

	context = {
		'seo_information': seo_information,
		'actual_year': datetime.datetime.now().strftime("%Y"),
	}

	return render(request, 'baseapp/dvs.html', context)

def show_kpp_page(request):

	try:
		seo_information = SEO_data.objects.get(page="КПП")
	except:
		seo_information = None

	context = {
		'seo_information': seo_information,
		'actual_year': datetime.datetime.now().strftime("%Y"),
	}

	return render(request, 'baseapp/kpp.html', context)

def show_reductor_page(request):

	try:
		seo_information = SEO_data.objects.get(page="РЕДУКТОРЫ")
	except:
		seo_information = None

	context = {
		'seo_information': seo_information,
		'actual_year': datetime.datetime.now().strftime("%Y"),
	}

	return render(request, 'baseapp/reductor.html', context)

def show_tnvd_page(request):

	try:
		seo_information = SEO_data.objects.get(page="ТНВД")
	except:
		seo_information = None

	context = {
		'seo_information': seo_information,
		'actual_year': datetime.datetime.now().strftime("%Y"),
	}

	return render(request, 'baseapp/tnvd.html', context)	

def show_forsunki_page(request):

	try:
		seo_information = SEO_data.objects.get(page="ФОРСУНКИ")
	except:
		seo_information = None

	context = {
		'seo_information': seo_information,
		'actual_year': datetime.datetime.now().strftime("%Y"),
	}

	return render(request, 'baseapp/forsunki.html', context)	

def show_tachograph_page(request):

	try:
		seo_information = SEO_data.objects.get(page="ТАХОГРАФЫ")
	except:
		seo_information = None

	context = {
		'seo_information': seo_information,
		'actual_year': datetime.datetime.now().strftime("%Y"),
	}

	return render(request, 'baseapp/tachograph.html', context)

def show_other_page(request):

	try:
		seo_information = SEO_data.objects.get(page="ПРОЧЕЕ")
	except:
		seo_information = None

	context = {
		'seo_information': seo_information,
		'actual_year': datetime.datetime.now().strftime("%Y"),
	}

	return render(request, 'baseapp/other.html', context)

def show_contact_page(request):

	try:
		seo_information = SEO_data.objects.get(page="КОНТАКТЫ")
	except:
		seo_information = None

	context = {
		'seo_information': seo_information,
		'contact_form' : ContactForm(),
		'actual_year': datetime.datetime.now().strftime("%Y"),
	}

	return render(request, 'baseapp/contact.html', context)

def send_contact_form(request):

	if request.method == 'POST':

		contactForm = ContactForm(request.POST)

		if contactForm.is_valid():

			contactName = contactForm.cleaned_data['contactName']
			contactPhone = contactForm.cleaned_data['contactPhone']
			contactComment = contactForm.cleaned_data['contactComment']

			bx24 = Bitrix24(config('BITRIX_WEBHOOK'))

			try:
				bx24.callMethod('crm.lead.add', fields={
					'TITLE': 'Лид с сайта',
					'NAME' : contactName,
					'COMMENTS' : contactComment + ' --- ' + contactPhone,
					'OPENED' : "Y",
				})
			except BitrixError as message:
				pass
				# print(message)

			message = 'Форма обратной связи успешно отправлена.'
			messages.info(request, 'Форма обратной связи успешно отправлена.')

		else:

			message = 'Форма обратной связи заполнена некорректно. Попробуйте еще раз.'
			messages.info(request, 'Форма обратной связи заполнена некорректно. Попробуйте еще раз.')


	context = {
		'message' : message,
		'contact_form':contactForm,
 	}
	return redirect('show_contact_page')