from django.urls import include, path
from .views.your_reflex_name import YourReflexNameView

urlpatterns = [
    path('test_reflex/', YourReflexNameView.as_view(), name='your_reflex_name'),
]