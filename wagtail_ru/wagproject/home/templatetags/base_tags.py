from django import template
from wagtail.core.models import Site
from home.models import Footer

register = template.Library()

@register.inclusion_tag('home/tags/footer.html', takes_context=True)
def footer_tag(context):
    return {
        'request': context['request'],
        'footer': Footer.objects.first()
    }

@register.simple_tag(takes_context=True)
def get_site_root(context):
    # This returns a core.Page. The main menu needs to have the site.root_page
    # defined else will return an object attribute error ('str' object has no
    # attribute 'get_children')
    return Site.find_for_request(context['request']).root_page

# def has_menu_children(page):
#     # This is used by the top_menu property
#     # get_children is a Treebeard API thing
#     # https://tabo.pe/projects/django-treebeard/docs/4.0.1/api.html
#     return page.get_children().live().in_menu().exists()



@register.inclusion_tag('tags/top_menu.html', takes_context=True)
def top_menu(context, parent, calling_page=None):
    menuitems = parent.get_children().live().in_menu()
    # for menuitem in menuitems:
    #     menuitem.show_dropdown = has_menu_children(menuitem)
    #     # We don't directly check if calling_page is None since the template
    #     # engine can pass an empty string to calling_page
    #     # if the variable passed as calling_page does not exist.
    #     menuitem.active = (calling_page.url_path.startswith(menuitem.url_path)
    #                        if calling_page else False)
    return {
        # 'calling_page': calling_page,
        'menuitems': menuitems,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }