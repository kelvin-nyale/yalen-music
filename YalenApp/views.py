from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def panel(request):
    return render(request,'panel-tabs.html')

def blank(request):
    return render(request,'blank.html')

def buttons(request):
    return render(request,'buttons.html')
def component(request):
    return render(request,'component.html')
def error(request):
    return render(request,'error.html')
def forms(request):
    return render(request,'form.html')
def form_advance(request):
    return render(request,'form-advance.html')
def gallery(request):
    return render(request,'gallery.html')
def grid(request):
    return render(request,'grid.html')
def icons(request):
    return render(request,'icons.html')
def invoice(request):
    return render(request,'invoice.html')
def login(request):
    return render(request,'login.html')
def messages(request):
    return render(request,'message-task.html')
def pricing(request):
    return render(request,'pricing.html')
def progress(request):
    return render(request,'progress.html')
def social(request):
    return render(request,'social.html')
def table(request):
    return render(request,'table.html')
def wizard(request):
    return render(request,'wizard.html')
def notification(request):
    return render(request,'notification.html')
def typography(request):
    return render(request,'typography.html')