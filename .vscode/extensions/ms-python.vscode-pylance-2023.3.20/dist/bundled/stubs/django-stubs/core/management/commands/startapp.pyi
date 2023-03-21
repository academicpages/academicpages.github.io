from django.core.management.templates import TemplateCommand as TemplateCommand

class Command(TemplateCommand):
    missing_args_message: str = ...
