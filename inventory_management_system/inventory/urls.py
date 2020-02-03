from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),

    url(r'^display_pens$', display_pens, name='display_pens'),
    url(r'^display_notebooks$', display_notebooks, name='display_notebooks'),
    url(r'^display_pencilcases$', display_pencilcases, name='display_pencilcases'),

    url(r'^add_pen$', add_pen, name="add_pen"),
    url(r'^add_notebook$', add_notebook, name="add_notebook"),
    url(r'^add_pencilcase$', add_pencilcase, name="add_pencilcase"),

    url(r'^edit_pen/(?P<pk>\d+)$', edit_pen, name="edit_pen"),
    url(r'^edit_notebook/(?P<pk>\d+)$', edit_notebook, name="edit_notebook"),
    url(r'^edit_pencilcase/(?P<pk>\d+)$', edit_pencilcase, name="edit_pencilcase"),

    url(r'^delete_pen/(?P<pk>\d+)$', delete_pen, name="delete_pen"),
    url(r'^delete_notebook/(?P<pk>\d+)$', delete_notebook, name="delete_notebook"),
    url(r'^delete_pencilcase/(?P<pk>\d+)$', delete_pencilcase, name="delete_pencilcase"),

]
