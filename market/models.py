from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailadmin.edit_handlers import PageChooserPanel

@register_snippet
@python_2_unicode_compatible
class MarketItem(models.Model):
    '''
    An item available for trade (or free) on the market place
    '''
    UNITS_PLANTS = 1
    UNITS_KILOGRAMS = 2
    _UNIT_CHOICES = (
        (UNITS_PLANTS, "Individual plants"),
        (UNITS_KILOGRAMS, "Kilograms")
    )

    plant = models.ForeignKey('plants.Plant', related_name='market_offers')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    date_posted = models.DateTimeField(auto_now=True)

    quantity = models.FloatField(
        default=1.0,
        help_text="Quantity of plant offered for the trade",

    )

    quantity_units = models.IntegerField(
        choices=_UNIT_CHOICES,
        help_text="Quantity units for plant offered for trade"
    )

    will_post = models.BooleanField(
        default=False,
        help_text="Designates whether the user is willing to post the item(s)"
    )
    pick_your_own = models.BooleanField(
        default=False,
        help_text="Allow traders to harvest the plant(s) themselves, from your garden"
    )
    is_free = models.BooleanField(
        default=False,
        help_text="Give the item(s) away for free"
    )
    accept_offers = models.BooleanField(
        default=True,
        help_text="Accept offers of any other plant(s)"
    )

    wanted_plant = models.ForeignKey(
        'plants.Plant',
        blank=True,
        null=True,
        help_text="The plant desired in return for the offered crop",
        related_name='market_wanted'
    )

    wanted_quantity = models.FloatField(
        default=1.0,
        help_text="Quantity of plant wanted for the trade",
        blank=True,
        null=True
    )

    wanted_quantity_units = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        choices=_UNIT_CHOICES,
        help_text="The units to be used for the quantity of wanted plants"
    )

    comments = models.TextField(blank=True, null=True)

    panels = [
        PageChooserPanel('plant', 'plants.Plant'),
        FieldPanel('user'),
        FieldPanel('quantity'),
        FieldPanel('quantity_units'),
        FieldPanel('will_post'),
        FieldPanel('pick_your_own'),
        FieldPanel('is_free'),
        FieldPanel('accept_offers'),
        PageChooserPanel('wanted_plant', 'plants.Plant'),
        FieldPanel('wanted_quantity'),
        FieldPanel('wanted_quantity_units'),
        FieldPanel('comments')
    ]

    def __str__(self):
        return "{} - {} - {}".format(self.date_posted.strftime("%Y-%m-%d"), self.plant, self.user)