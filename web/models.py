from django.db import models

class Film(models.Model):
	class Meta:
		verbose_name = 'Фильм'
		verbose_name_plural = 'Фильм'
	Age_list = [
		("0+", "0+"),
		("6+", "6+"),
		("12+", "12+"),
		("16+", "16+"),
		("18+", "18+")
	]
	Category_list = [
		("Боевик", "Боевик"),
		("Вестерн", "Вестерн"),
		("Гангстерский фильм", "Гангстерский фильм"),
		("Детектив", "Детектив"),
		("Драма", "Драма"),
		("Исторический фильм", "Исторический фильм"),
		("Комедия", "Комедия"),
		("Мелодрама", "Мелодрама"),
		("Музыкальный фильм", "Музыкальный фильм"),
		("Нуар", "Нуар"),
		("Политический фильм", "Политический фильм"),
		("Приключенческий фильм", "Приключенческий фильм"),
		("Сказка", "Сказка"),
		("Трагедия", "Трагедия"),
		("Трагикомедия", "Трагикомедия")
	]
	Name = models.CharField(verbose_name="Название", max_length=50)
	Image = models.ImageField(verbose_name="Постер", upload_to='poster/')
	Trailer = models.FileField(upload_to='videos/', null=True, blank=True, verbose_name="Трейлер")
	Age = models.CharField(choices=Age_list, verbose_name="Возростное ограничение", max_length=50)
	Category = models.CharField(choices=Category_list, verbose_name="Жанр", max_length=50)

	def __str__(self):
		return str(self.Name)



class Seance(models.Model):
	class Meta:
		verbose_name = 'Сеанс'
		verbose_name_plural = 'Сеанс'

	Hall_list = [
		("Зал1", "Зал1"),
		("Зал2", "Зал2")
	]
	FilmName = models.ForeignKey(Film, on_delete=models.SET_NULL, null=True, blank=True)
	SeanceDate = models.DateField(verbose_name="Дата сеанса")
	SeanceTime = models.TimeField(verbose_name="Время сеанса")
	Hall = models.CharField(verbose_name="Зал", choices=Hall_list, max_length=50)
	Price = models.IntegerField(verbose_name="Цена")

	def __str__(self):
		return str(str(self.FilmName) + " " +str(self.SeanceDate) + " " + str(self.SeanceTime))
			