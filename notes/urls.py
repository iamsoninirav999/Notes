from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.index,name="index"),
   path('register/',views.register,name="register"),
   path('logout/',views.logout_view,name="logout"),
   path('login/',views.login_view,name="login"),
   path('create/',views.create_note,name="create_note"),
   path('delete/<id>',views.delete_note,name="delete_note"),
   path('archive/<id>',views.archive_note,name="archive_note"),
   path('archived_notes',views.my_archived_notes,name="my_archived_notes"),
   path('unarchive/<id>',views.unarchive_note,name="unarchive_note"),
   path('labled_notes/<label>',views.labled_notes,name="labled_notes"),
   path('create_label/',views.create_label,name="create_label"),
   path('delete_label/',views.delete_label,name="delete_label"),
]