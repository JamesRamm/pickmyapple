from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel

class PlantIndex(Page):
    pass

class Plant(Page):
    '''
    Represents a plant of any kind
    '''
    common_name = models.CharField(max_length=64)
    variety = models.CharField(max_length=128)
    description = RichTextField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('common_name'),
        FieldPanel('variety'),
        FieldPanel('description', classname="full"),
    ]

