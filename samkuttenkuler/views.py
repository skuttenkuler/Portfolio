from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = "base.html"

class PortfolioPage(TemplateView):
    template_name = "portfolio.html"