from django.urls import path
from .views import BookView, BookCreateView, BookDeleteView, BookUpdateView, BookDetailView

urlpatterns = [
    path('', BookView.as_view(), name='main'),
    path('create', BookCreateView.as_view(), name='create'),
    path('delete/<int:pk>', BookDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', BookUpdateView.as_view(), name='update'),
    path('detail/<int:pk>', BookDetailView.as_view(), name='detail')
]