from django.urls import path
from . import views

# urlpatterns = [
#     path("", views.pets, name="all_pets"),
#     path("<int:pet_id>", views.pet_detail, name="pet_detail"),
#     path("pet", views.pet_add, name="add")
# ]

urlpatterns = [
    path("", views.PetsView.as_view(), name="all_pets"),
    path("<int:pk>", views.PetDetailView.as_view(), name="pet_detail"),
    path("pet", views.PetCreateView.as_view(), name="add")
]
app_name = "pets"