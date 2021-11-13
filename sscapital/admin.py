from django.contrib import admin
from .models import Investors, Financials, Ledger, Prometheus

admin.site.register(Investors)
admin.site.register(Financials)
admin.site.register(Ledger)
admin.site.register(Prometheus)

