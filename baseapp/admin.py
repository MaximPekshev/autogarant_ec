from django.contrib import admin
from .models import SEO_data

class SEO_dateAdmin(admin.ModelAdmin):

	list_display = (
			'page',
			'title',
		)

admin.site.register(SEO_data, SEO_dateAdmin)