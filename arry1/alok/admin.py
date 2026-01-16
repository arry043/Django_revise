from django.contrib import admin
from .models import AlokVarity, AlokReview, AlokCertificate

# Register your models here.

class AlokReviewInline(admin.TabularInline):
    model = AlokReview
    extra = 2

class AlokVarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date')
    inlines = [
        AlokReviewInline,
    ]
    
class AlokCertificateAdmin(admin.ModelAdmin):
    list_display = ('alok', 'issued_date', 'certificate_number')


admin.site.register(AlokVarity, AlokVarityAdmin)
admin.site.register(AlokCertificate, AlokCertificateAdmin) 