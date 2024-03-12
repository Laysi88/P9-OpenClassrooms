from django.contrib.auth.mixins import LoginRequiredMixin


class CustomLoginRequired(LoginRequiredMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
