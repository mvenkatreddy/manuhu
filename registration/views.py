from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect,HttpResponse

from django.contrib import messages
from django.shortcuts import render

from .forms import RegistrationForm

###

from .models import Registration

###
def registrationuser(request):
    """ Creating a registration """
    user_form = RegistrationForm()
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            obj = user_form.save(commit=False)
            username = obj.name
            email = obj.email_id
            password = obj.password
            user = User.objects.create_user(email=email,
                                            username=username, password=password)
            user.save()
            user = authenticate(username=email, password=password)
            login(request, user)
            messages.success(request, 'You are successfully registered')
    context = {'user_form': user_form}
    return render(request, 'registration/user_registration.html', context)


def accounts_signin(request):
    """ Implementing Sigin In Functionality """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'You are successfully Logged In')
            else:
                messages.error(request, 'Invalid login credentials')
                return HttpResponseRedirect(reverse('accounts_login'))
    return HttpResponseRedirect(reverse('home'))


def accounts_login(request):
    """ Creating an accounts login"""
    context = {}
    return render(request, 'registration/account_login.html', context)


def accounts_logout(request):
    """ Logout the users  """
    logout(request)
    messages.success(request, 'You are successfully logout')
    return redirect('home')



##############        Reportlabs                 ###########

from reportlab.pdfgen import canvas
#from django.http import HttpResponse

def some_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=somefilename.pdf'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response


def html_view(request, as_pdf = False):
    #Get varaibles to populate the template
    obj = Registration.objects.all()
    payload = {'obj':obj}
    if as_pdf:
        return payload
    return render_to_response('registration/profile.html', payload, RequestContext(request))

from django.template.loader import render_to_string
from django.template import RequestContext
import StringIO
#### ************ To Know about ********** StringIO  ******** Read and write as a file *************** ##############
# https://www.google.co.in/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0CB4QFjAA&url=https%3A%2F%2Fdocs.python.org%2F2%2Flibrary%2Fstringio.html&ei=9vaNVKuoAoyWuAS634CwBw&usg=AFQjCNGpmVOzyfGGJv3FHZ379epgW-fCSQ&sig2=IGjnNN2EurCJZQC6c4c7ZQ&bvm=bv.81828268,d.c2E
import ho.pisa as pisa
###                 ************** Pisa meterial ************         ####
#http://xhtml2pdf.appspot.com/static/pisa-en.html


def pdf_view(request):
    payload = html_view(request, as_pdf = True)
    file_data = render_to_string('registration/profile.html', payload, RequestContext(request))
    myfile = StringIO.StringIO()
    pisa.CreatePDF(file_data, myfile)
    myfile.seek(0)
    response =  HttpResponse(myfile, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=coupon.pdf'
    return response

































