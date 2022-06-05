from django.shortcuts import render
from Lab1.forms import prescriptionForm
from django.views.generic import TemplateView
from Lab1.models import prescription

# Create your views here.

#def prescription(request):
#    return render(request, 'Lab1/prescription.html')

class prescriptionView(TemplateView):
    template_name = 'Lab1/prescription.html'

    def get(self, request):
        form = prescriptionForm()
        args = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        form = prescriptionForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            firstname = form.cleaned_data['firstname']
            surname = form.cleaned_data['surname']
        if number:
            prescriptions = prescription.objects.filter(number=number)
        if not number and firstname and surname:
            prescriptions = prescription.objects.filter(firstname=firstname, surname=surname, VIP=True)
        args = {'form': form, 'number': number, 'prescriptions': prescriptions}
        return render(request, self.template_name, args)