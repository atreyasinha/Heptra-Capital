from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from .models import Investors, Financials, Ledger, Prometheus
from django.contrib.auth.decorators import login_required
from .forms import AddTransactionForm, UpdatePrometheus

class LandingPage(View):
    def get(self, request):
        investors = Investors.objects.all()
        prometheus = Prometheus.objects.get(id=1)
        return render(request, 'index.html', {'investors': investors, 'prometheus': prometheus})

class Dashboard(View):
    def get(self, request, pk):
        investor = Investors.objects.get(id=pk)
        financials = Financials.objects.get(investor=investor.id)
        ledger = Ledger.objects.filter(investor=investor.id)
        prometheus = Prometheus.objects.get(id=1)

        return render(request, 'dashboard.html', {'prometheus': prometheus, 'investor': investor, 'ledger': ledger, 'financials': financials})

@method_decorator(login_required, name="dispatch")
class Admin(View):
    def get(self, request):
        ledger = Ledger.objects.all()
        prometheus = Prometheus.objects.get(id=1)
        financials = Financials.objects.all()

        form_add = AddTransactionForm()
        form_update = UpdatePrometheus()

        return render(request, 'admin.html', {'ledger': ledger, 'prometheus': prometheus, 'financials': financials, 'form_add':form_add, 'form_update':form_update})

    def post(self, request):
        form_add = AddTransactionForm(request.POST)
        form_update = UpdatePrometheus(request.POST)


        if form_add.is_valid():
            investor = form_add.cleaned_data['investor']
            money_moved = form_add.cleaned_data['money_moved']
            transaction = form_add.cleaned_data['transaction']
            ledger_data = Ledger(investor=investor, money_moved=money_moved, transaction=transaction)
            ledger_data.save()

            financial_capital = Financials.objects.get(investor=investor).capital_invested
            financial_value = Financials.objects.get(investor=investor).market_value
            prometheus_capital = Prometheus.objects.get(id=1).capital
            prometheus_value = Prometheus.objects.get(id=1).value

            if (transaction == 'Deposit'):
                financial_capital = financial_capital + float(money_moved)
                financial_value = financial_value + float(money_moved)
                prometheus_capital = prometheus_capital + float(money_moved)
                prometheus_value = prometheus_value + float(money_moved)

            else:
                financial_capital = financial_capital - float(money_moved)
                financial_value = financial_value - float(money_moved)
                prometheus_capital = prometheus_capital - float(money_moved)
                prometheus_value = prometheus_value - float(money_moved)

            # Fund
            prometheus_returns = round((((prometheus_value - prometheus_capital) / prometheus_value) * 100), 2)
            prometheus_data = Prometheus(id=1, capital=prometheus_capital, value=prometheus_value, returns=prometheus_returns)
            prometheus_data.save()

            # Investors
            financial_data = Financials.objects.get(investor=investor.id)
            financial_data.market_value = financial_value
            financial_data.capital_invested = financial_capital
            financial_data.returns = round((((financial_value - financial_capital) / financial_capital) * 100), 2)
            financial_data.shareholder = round((prometheus_value / financial_value), 2)
            financial_data.save()


        if form_update.is_valid():
            value = form_update.cleaned_data['value']
            data = Prometheus.objects.get(id=1)
            data.value = value
            difference = float(value) - data.capital
            data.returns = round((difference / data.capital) * 100, 2)
            data.save()

            for i in Financials.objects.all():
                if i.capital_invested == 0:
                    continue
                financial_value = round(i.market_value + (i.shareholder * difference) / 100, 2)
                i.market_value = financial_value
                i.returns = round(((financial_value - i.capital_invested) / i.capital_invested) * 100, 2)
                i.shareholder = round(data.value / financial_value, 2)
                i.save()

        return redirect('/administrator')

