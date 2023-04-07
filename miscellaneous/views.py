from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages

from .forms import ContactForm
from .models import Contacts


def about(request):
    return render(request, 'miscellaneous/about.html')


@csrf_protect
def contact(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data.get('name')
            email = contact_form.cleaned_data.get('email')
            subject = contact_form.cleaned_data.get('subject')
            message = contact_form.cleaned_data.get('message')
            contact_info_model = Contacts(name=name, email=email, subject=subject, message=message)
            contact_info_model.save()
            messages.success(request, "Thank you for your message. We'll be in touch..!")
        else:
            messages.error(request, 'Form is Invalid..!!')
    return render(request, 'miscellaneous/contact.html', {"contact_form": ContactForm()})


def privacypolicy(request):
    return render(request, 'miscellaneous/privacypolicy.html')


def termsofuse(request):
    return render(request, 'miscellaneous/termsofuse.html')


# On commit message to mail and show notification on site.
# def user_message(subject, body, sender, recipients, password):
#     print(subject)
#     msg = MIMEText(body)
#     msg['Subject'] = subject
#     msg['From'] = sender
#     msg['To'] = ', '.join(recipients)
#     smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#     smtp_server.login(sender, password)
#     smtp_server.sendmail(sender, recipients, msg.as_string())
#     smtp_server.quit()
