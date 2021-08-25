from django.shortcuts import render
from .models import *
import datetime


def index(requset):
	film = Film.objects.all().order_by('id')
	db_seance = Seance.objects.all().order_by('SeanceTime')
	seance = []
	for set_seance in db_seance:
		seance.append(
			dict(
					FilmName = str(set_seance.FilmName),
					SeanceDate = set_seance.SeanceDate.strftime('%d.%m.%Y'),
					SeanceTime = set_seance.SeanceTime.strftime('%H:%M'),
					Hall = set_seance.Hall,
					Price = set_seance.Price
				)
			)
	today = datetime.date.today()
	tomorrow = today + datetime.timedelta(days=1)
	day3 = today + datetime.timedelta(days=2)
	day4 = today + datetime.timedelta(days=3)
	day5 = today + datetime.timedelta(days=4)
	day6 = today + datetime.timedelta(days=5)
	day7 = today + datetime.timedelta(days=6)
	day8 = today + datetime.timedelta(days=7)



	calendar = []
	for days in [today, tomorrow, day3, day4, day5, day6, day7, day8]:
		if days == today:
			day_of_week = "Сегодня"
		elif days == tomorrow:
			day_of_week = "Завтра"
		else:
			if days.weekday() == 0:
				day_of_week = "Понедельник"
			elif days.weekday() == 1:
				day_of_week = "Вторник"
			elif days.weekday() == 2:
				day_of_week = "Среда"
			elif days.weekday() == 3:
				day_of_week = "Четверг"
			elif days.weekday() == 4:
				day_of_week = "Пятница"
			elif days.weekday() == 5:
				day_of_week = "Суббота"
			elif days.weekday() == 6:
				day_of_week = "Воскресенье" 
		calendar.append(
			dict(
					Day = days.strftime('%d.%m'),
					Day_of_week = day_of_week,
					Link = "/date/"+days.strftime('%Y/%m/%d')
				)
			)
	
	data = {
		'film': film,
		'seance': seance,
		'calendar': calendar
	}
	return render(requset, 'page/index.html', data)
