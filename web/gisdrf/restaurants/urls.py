# Django
from django.urls import path

# Views
from .views import HomeView, get_csv_file, stream
from .views import StatusDetail, StatusList


app_name = "restaurants"


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('nearby/@<str:x>/<str:y>/', HomeView.as_view(), name='nearby'),
    path('nearby/csv_file/@<str:x>/<str:y>/', get_csv_file, name='csv_file'),

    path('stream/', stream, name='stream'),
    path('status-list/', StatusList.as_view(), name='status_list'),
    path('status-detail/<int:pk>', StatusDetail.as_view(), name='status_detail'),

] 