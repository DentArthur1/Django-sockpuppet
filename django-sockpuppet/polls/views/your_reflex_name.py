from django.views.generic.base import TemplateView


class YourReflexNameView(TemplateView):
    template_name = 'your_reflex_name.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = 0
        return context
