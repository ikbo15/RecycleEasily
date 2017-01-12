#!/usr/bin/env python
# -*- coding: UTF-8 -*- 

import os
from django.conf import settings
from django.http import HttpResponse
from django.template import loader

from .models import Station
from .models import TrashStation

def index(request):
	template = loader.get_template('re_app/ymaps.html')
	point_data = Station.objects.filter(show=True)
	for st in point_data:
		w = False
		ns = ''
		for l in st.name:
			if l in ['"', u'«', u'»', "'"]:
				w = not w
			elif w:
				ns += l
		if ns:
			st.name_short = ns
		else:
			st.name_short = st.name

		if st.telephone.replace(' ','') == '':
			st.telephone = u'нет'

		st.position_x = str(st.position_x).replace(',','.')
		st.position_y = str(st.position_y).replace(',','.')

	context = {
        'point_data': point_data,
    }
	return HttpResponse(template.render(context, request))

def danger(request):
	template = loader.get_template('re_app/ymaps.html')
	point_data = Station.objects.filter(show=True)
	for st in point_data:
		ts_obj = TrashStation.objects.filter(station=st.id, trash_type=6)
		if not ts_obj:
			continue
		w = False
		ns = ''
		for l in st.name:
			if l in ['"', u'«', u'»', "'"]:
				w = not w
			elif w:
				ns += l
		if ns:
			st.name_short = ns
		else:
			st.name_short = st.name

		if st.telephone.replace(' ','') == '':
			st.telephone = u'нет'

		st.position_x = str(st.position_x).replace(',','.')
		st.position_y = str(st.position_y).replace(',','.')

	context = {
        'point_data': point_data,
    }
	return HttpResponse(template.render(context, request))

def metal(request):
	template = loader.get_template('re_app/ymaps.html')
	point_data = Station.objects.filter(show=True)
	for st in point_data:
		ts_obj = TrashStation.objects.filter(station=st.id, trash_type=5)
		if not ts_obj:
			continue
		w = False
		ns = ''
		for l in st.name:
			if l in ['"', u'«', u'»', "'"]:
				w = not w
			elif w:
				ns += l
		if ns:
			st.name_short = ns
		else:
			st.name_short = st.name

		if st.telephone.replace(' ','') == '':
			st.telephone = u'нет'

		st.position_x = str(st.position_x).replace(',','.')
		st.position_y = str(st.position_y).replace(',','.')

	context = {
        'point_data': point_data,
    }
	return HttpResponse(template.render(context, request))

def glass(request):
	template = loader.get_template('re_app/ymaps.html')
	point_data = Station.objects.filter(show=True)
	for st in point_data:
		ts_obj = TrashStation.objects.filter(station=st.id, trash_type=4)
		if not ts_obj:
			continue
		w = False
		ns = ''
		for l in st.name:
			if l in ['"', u'«', u'»', "'"]:
				w = not w
			elif w:
				ns += l
		if ns:
			st.name_short = ns
		else:
			st.name_short = st.name

		if st.telephone.replace(' ','') == '':
			st.telephone = u'нет'

		st.position_x = str(st.position_x).replace(',','.')
		st.position_y = str(st.position_y).replace(',','.')

	context = {
        'point_data': point_data,
    }
	return HttpResponse(template.render(context, request))

def plastic(request):
	template = loader.get_template('re_app/ymaps.html')
	point_data = Station.objects.filter(show=True)
	for st in point_data:
		ts_obj = TrashStation.objects.filter(station=st.id, trash_type=3)
		if not ts_obj:
			continue
		w = False
		ns = ''
		for l in st.name:
			if l in ['"', u'«', u'»', "'"]:
				w = not w
			elif w:
				ns += l
		if ns:
			st.name_short = ns
		else:
			st.name_short = st.name

		if st.telephone.replace(' ','') == '':
			st.telephone = u'нет'

		st.position_x = str(st.position_x).replace(',','.')
		st.position_y = str(st.position_y).replace(',','.')

	context = {
        'point_data': point_data,
    }
	return HttpResponse(template.render(context, request))

def paper(request):
	template = loader.get_template('re_app/ymaps.html')
	point_data = Station.objects.filter(show=True)
	for st in point_data:
		ts_obj = TrashStation.objects.filter(station=st.id, trash_type=2)
		if not ts_obj:
			continue
		w = False
		ns = ''
		for l in st.name:
			if l in ['"', u'«', u'»', "'"]:
				w = not w
			elif w:
				ns += l
		if ns:
			st.name_short = ns
		else:
			st.name_short = st.name

		if st.telephone.replace(' ','') == '':
			st.telephone = u'нет'

		st.position_x = str(st.position_x).replace(',','.')
		st.position_y = str(st.position_y).replace(',','.')

	context = {
        'point_data': point_data,
    }
	return HttpResponse(template.render(context, request))

def battery(request):
	template = loader.get_template('re_app/ymaps.html')
	point_data = Station.objects.filter(show=True)
	for st in point_data:
		ts_obj = TrashStation.objects.filter(station=st.id, trash_type=1)
		if not ts_obj:
			continue
		w = False
		ns = ''
		for l in st.name:
			if l in ['"', u'«', u'»', "'"]:
				w = not w
			elif w:
				ns += l
		if ns:
			st.name_short = ns
		else:
			st.name_short = st.name

		if st.telephone.replace(' ','') == '':
			st.telephone = u'нет'

		st.position_x = str(st.position_x).replace(',','.')
		st.position_y = str(st.position_y).replace(',','.')

	context = {
        'point_data': point_data,
    }
	return HttpResponse(template.render(context, request))
