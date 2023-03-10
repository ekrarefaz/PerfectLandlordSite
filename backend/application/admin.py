from django.contrib import admin

from .models import *

admin.site.register(Application)
admin.site.register(Identity)
admin.site.register(Residential)
admin.site.register(Employment)
admin.site.register(Income)
admin.site.register(ApplicationIdentity)
admin.site.register(ApplicationResidential)
admin.site.register(ApplicationEmployment)
admin.site.register(ApplicationIncome)