from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.blocks import ImageChooserBlock


class MyBlockItem(blocks.StructBlock):
    label = blocks.CharBlock()
    value = blocks.IntegerBlock()


class MyBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=100)
    item = MyBlockItem()
    items = blocks.ListBlock(MyBlockItem)
    image = ImageChooserBlock()


class MyTestPage(Page):
    app_label = 'test'
    body = StreamField([
        ('char_array', blocks.ListBlock(blocks.CharBlock())),
        ('int_array', blocks.ListBlock(blocks.IntegerBlock())),
        ('struct', MyBlock()),
        ('image', ImageChooserBlock()),
    ])
