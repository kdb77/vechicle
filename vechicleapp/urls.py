
from django.urls import path
from .import views
app_name='vechicleapp'


urlpatterns = [
    path('',views.index,name='index'),
    path('vechicle/<int:vechicle_id>/', views.detail, name='detail'),
    path('add/', views.add_vechicle, name='add_vechicle'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete')
]


