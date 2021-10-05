from django.urls import path, register_converter
from datetime import datetime
from . import views
from django.conf import settings
from django.conf.urls.static import static

# class DateConverter:
#     regex = '\d{4}-\d{2}-\d{2}'

#     def to_python(self, value):
#         return datetime.strptime(value, '%Y-%m-%d')

#     def to_url(self, value):
#         return value

# register_converter(DateConverter, 'yyyy')

urlpatterns = [
    path('', views.news_of_day,name='newsToday'),
    path('archives/<past_date>/',views.past_days_news ,name = 'pastNews'),
    path('search/', views.search_results, name='search_results'),
    path('article/<int:article_id>/', views.article,name ='article')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)