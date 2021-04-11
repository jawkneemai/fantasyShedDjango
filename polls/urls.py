from django.urls import path
from . import views

urlpatterns = [
	# /polls/
	path('', views.index, name='index'),
	# /polls/69/
	path('<int:question_id>/', views.detail, name='detail'),

	# /polls/69/vote/
	path('<int:question_id>/vote/', views.votePage, name='votePage'),

	# /polls/69/results/
	path('<int:question_id>/results/', views.results, name='results'),

	#path('<int:recipe_id>/', views.recipePage, name='recipePage')
]

