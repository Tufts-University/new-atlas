from django.contrib import admin
from django.urls import include, path

from .views import HomePageView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomePageView.as_view(), name="home"),
    path("", include("atlas.alignments.urls")),
    path("", include("atlas.annotations.urls")),
    path("", include("atlas.ctslibrary.urls")),
    path("", include("atlas.dictionaries.urls")),
    path("", include("atlas.morphology.urls")),
    path("", include("atlas.texts.urls")),
]
