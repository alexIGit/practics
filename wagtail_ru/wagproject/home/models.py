from tabnanny import verbose
from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField, StreamField

from wagtail.core.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.snippets.models import register_snippet

from .blocks import FigCaptionBlock

@register_snippet
class Footer(models.Model):
    bodytext = RichTextField(
        blank=True,
        null=True,
    )

    panels = [
        FieldPanel('bodytext'),
    ]

    class Meta:
        verbose_name = 'Футер'
        verbose_name_plural = 'Футеры'

    def __str__(self):
        return 'Футер'

class NewsPage(Page):
    max_count = 3
    # template = 'home/news_page.html'


class HomePage(Page):

    # subpage_types = ['home.NewsPage']
    parent_page_types = []


    subtitle = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Подзаголовок"
    )

    rtfbody = RichTextField(
        blank=True,
        null=True,
    )

    body = StreamField([
            ('figcaptionblock', FigCaptionBlock()),
            ('rtfblock', RichTextBlock(
                features=['h1', 'h6', 'hr', 'bold', 'italic'],
                label='Текст',
                help_text='Введите описание'
            )),
            ('imgblock', ImageChooserBlock(
                template='blocks/imagblock.html'
            )),
            ('youtubeblock', EmbedBlock())
        ], 
        block_counts={
            'rtfblock': {'min_num': 0},
            'imgblock': {'max_num': 1},
        },
        blank=True
    )

    bg_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    ) 

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('rtfbody'),
        ImageChooserPanel('bg_image'),
        StreamFieldPanel('body'),
    ] 

    # promote_panels = Page.promote_panels
    # settings_panels = Page.promote_panels
