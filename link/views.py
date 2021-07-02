import requests

from django.http import JsonResponse
from django.views.generic import ListView
from django.views import View
from django.core.serializers import serialize
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Link


class LinkView(LoginRequiredMixin, ListView):
    model = Link
    template_name = 'link/index.html'
    context_object_name = 'links'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['links_json'] = serialize('json', context['links'])
        return context


class LinkCheckView(LoginRequiredMixin, View):
    http = ('get',)

    def get(self, request, *args, **kwargs):
        try:
            link = request.GET['link']
        except KeyError:
            return JsonResponse({'message': 'Need to pass link'}, status=400)
        try:
            link = link if link.startswith('http') else ('http://' + link)

            response = requests.get(link)
            status_code = response.status_code
        except Exception as e:
            status_code = 500
        return JsonResponse({'link': link, 'status_code': status_code, }, status=200)
