from django.urls import path

from . import views

app_name = "app1"
urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contacts/", views.contact, name="contact"),
    # path("blog",views.blog,name="blog"),
    # path("project",views.project,name="project"),
    path("service/", views.service, name="service"),
    path("team", views.team, name="team"),
    path("formation", views.formation, name="formation"),
    path("consieldegestion", views.consielgestion, name="consielgestion"),
    path("productionsdefilm", views.productionsdeFilms, name="productionsdefilms"),
    path("importexport", views.importExport, name="importexport")
]
