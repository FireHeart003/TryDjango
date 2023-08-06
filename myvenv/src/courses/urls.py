from django.urls import path
from .views import(
	CourseListView,
	CourseView,
	CourseCreateView,
	CourseUpdateView,
	CourseDeleteView
)


app_name = 'courses'
urlpatterns = [
	path('', CourseListView.as_view(), name = 'courses-list'),
	path('<int:id>/', CourseView.as_view(), name = 'courses-detail'),
	path('create/', CourseCreateView.as_view(), name = 'courses-create'),
	path('<int:id>/update/', CourseUpdateView.as_view(), name = 'courses-update'),
	path('<int:id>/delete/', CourseDeleteView.as_view(), name = 'courses-delete'),

]