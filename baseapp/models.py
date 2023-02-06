from django.db import models

class SEO_data(models.Model):

	page =  models.CharField(max_length = 60, verbose_name = 'Страница')

	title = models.CharField(max_length = 70, verbose_name = 'Title, max 70 символов', null=True, blank=True, default='')
	description = models.CharField(max_length = 180, verbose_name = 'Description, max 180 символов', null=True, blank=True, default='')
	keywords = models.CharField(max_length = 512, verbose_name = 'Keywords, max 512 символов', null=True, blank=True, default='')


	def __str__(self):

		return '{0}'.format(self.page)

	class Meta:
		verbose_name = 'СЕО'
		verbose_name_plural = 'СЕО'
