from redis import Redis
from rq import Queue

from django.shortcuts import render
from django.views.generic import TemplateView

from . import forms, tasks, rq_tasks

# Create your views here.
import time


class IndexView(TemplateView):
    template_name = 'index.html'

    def action1(self, request):
        time.sleep(10)

    def action2(self, request):
        tasks.dbt_task(request.POST.copy())

    def action3(self, request):
        import django_rq
        django_rq.enqueue(rq_tasks.rq_task, request.POST.copy())

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = forms.ContactUs()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = form = forms.ContactUs(request.POST)

        if request.POST.get('submit'):
            if request.POST.get('submit') == 'synchronous':
                self.action1(request)
            elif request.POST.get('submit') == 'django-background-tasks':
                self.action2(request)
            elif request.POST.get('submit') == 'rq':
                self.action3(request)
            else:
                form.add_errors(None, "Invalid action")

        context['message'] = 'Submitted: ' + request.POST.get('submit', '')
        return self.render_to_response(context)
