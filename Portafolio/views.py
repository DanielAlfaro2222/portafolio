from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Technology
from .models import Project
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect
import threading
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.urls import reverse
from .models import Formation


class IndexTemplateView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['tecnologias'] = Technology.objects.filter(state=True)
        context['proyectos'] = Project.objects.filter(state=True)
        context['formaciones'] = Formation.objects.filter(state=True)

        return self.render_to_response(context)


def contact_send_mail(request):

    if request.method == 'POST':
        template = get_template('mail.html')
        context = {
            'nombre': request.POST.get('nombre'),
            'correo': request.POST.get('correo'),
            'mensaje': request.POST.get('mensaje')
        }
        content = template.render(context)

        email = EmailMultiAlternatives(
            subject='Nuevo mensaje de contacto',
            body='',
            from_email=settings.EMAIL_HOST_USER,
            to=['kdalfaro45@misena.edu.co'],
            cc=['danielalfaro22222@gmail.com']
        )

        email.attach_alternative(content, 'text/html')

        try:
            thread = threading.Thread(target=email.send, kwargs={
                'fail_silently': False,
            })

            thread.start()

            messages.success(
                request, 'Mensaje enviado con éxito, pronto me comunicare contigo.')
        except:
            messages.error(
                request, 'Oops, ocurrio un error por favor vuelve a intentarlo de nuevo')

    return redirect(f"{reverse('Portafolio:index')}#contacto")
