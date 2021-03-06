from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('workouts/', views.workouts_index, name='workouts_index'),
    path('workouts/<int:workout_id>/', views.workouts_detail, name='workouts_detail'),
    path('workouts/create/', views.WorkoutCreate.as_view(), name='workouts_create'),
    path('workouts/<int:pk>/update/', views.WorkoutUpdate.as_view(), name='workouts_update'),
    path('workouts/<int:pk>/delete/', views.WorkoutDelete.as_view(), name='workouts_delete'),
    path('workouts/<int:workout_id>/add_didworkout/', views.add_didworkout, name='add_didworkout'),
    path('workouts/<int:pk>/update', views.DidWorkoutUpdate.as_view(), name='didworkouts_update'),
    path('workouts/<int:pk>/delete', views.DidWorkoutDelete.as_view(), name='didworkouts_delete'),
    path('workouts/<int:workout_id>/assoc_exercise/<int:exercise_id>/', views.assoc_exercise, name='assoc_exercise'),
    path('exercises/create/', views.ExerciseCreate.as_view(), name='exercises_create'),
    path('exercises/<int:pk>/', views.ExerciseDetail.as_view(), name='exercises_detail'),
    path('exercises/', views.ExerciseList.as_view(), name='exercises_index'),
    path('exercises/<int:pk>/update', views.ExerciseUpdate.as_view(), name='exercises_update'),
    path('exercises/<int:pk>/delete/', views.ExerciseDelete.as_view(), name='exercises_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('nutritions/create/', views.NutritionCreate.as_view(), name='nutritions_create'),
    path('nutritions/<int:pk>/', views.NutritionDetail.as_view(), name='nutritions_detail'),
    path('nutritions/', views.NutritionList.as_view(), name='nutritions_index'),
    path('nutritions/<int:pk>/update/', views.NutritionUpdate.as_view(), name='nutritions_update'),
    path('nutritions/<int:pk>/delete/', views.NutritionDelete.as_view(), name='nutritions_delete'),
]
