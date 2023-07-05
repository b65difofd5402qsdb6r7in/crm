from django.urls import path
from .views import ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView, PDFGeneratorView, UtilisateurCreateView, UtilisateurDeleteView, UtilisateurDetailView,UtilisateurListView, UtilisateurUpdateView


app_name = "clients"
   
urlpatterns = [ 
    path('', ClientListView.as_view(), name='list'),
    # path('signature/', signature_view, name='signature'),
    # path('store_signature/', store_signature_view, name='store_signature'),
    # path('retrieve_signature/', retrieve_signature_view, name='retrieve_signature'),
    path('pdf/<int:pk>/', PDFGeneratorView.as_view(), name='generate_pdf'),
    path('create/', ClientCreateView.as_view() , name='create'),
    path('<int:pk>/update/', ClientUpdateView.as_view() , name='update'),
    path('<int:pk>/delete/', ClientDeleteView.as_view() , name='delete'),
    path('<int:pk>', ClientDetailView.as_view(), name='detail'),
    path('utilisateur/', UtilisateurListView.as_view(), name='utilisateur-list'),
    path('utilisateur/create/', UtilisateurCreateView.as_view() , name='utilisateur-create'),
    path('utilisateur/<int:pk>/update/', UtilisateurUpdateView.as_view() , name='utilisateur-update'),
    path('utilisateur/<int:pk>/delete/', UtilisateurDeleteView.as_view() , name='utilisateur-delete'),
    path('utilisateur/<int:pk>', UtilisateurDetailView.as_view(), name='utilisateur-detail'),
   
    # path('<int:pk>/update', client_update)
    ]
