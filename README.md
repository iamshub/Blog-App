# Blog-App
The blog app is designed under Django framework. It works on a local server and you can easily signup and login into it. Update your writings and let others (readers) discover it. 
BLOG WITH STATIC PAGES AND UNIQUE URL:-

	Open the command prompt and switch in E: Drive and go inside
                DjangoDemos Folder and then

Articles App Creation:-

1)django-admin startproject BlogApp

2)cd BlogApp

3)python manage.py startapp articles

4) python manage.py migrate

5)start python manage.py runserver

6)open the browser
            http://localhost:8000
7)in settings.py within INSTALLED_APPS

                'articles',
---------------------------------------------------------------------------------------------------------------------------
ForeignKey and Many to one Relation:-

8)in models.py


class Article(models.Model):
        author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    text = models.TextField()


    def __str__(self):
         return self.title

-----------------------------------------
Adding articles in database:-

python manage.py makemigrations articles

python manage.py migrate articles

python manage.py createsuperuser

and once again start the server

python manage.py runserver

and open the admin in browser

in admin.py


# Register your models here.

from .models import Article

admin.site.register(Article)


and again open the admin in browser

and add some article

----------------------------------
Configuring URLs:-
         in Project urls.py

    path('', include('articles.urls')),


in app urls.py

from django.urls import path

from . import views

urlpatterns = [

    path('', views.ArticleListView.as_view(), name='home' ),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article_page' ),
]
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
in views.py:-

from django.views.generic import ListView, DetailView
# Create your views here.
from . models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'
    context_object_name = 'batman'

---------------------------------------------------------------------
After that Create one Folder(templates) and add some html file in that
-------------------
in settings.py

TEMPLATES

  'DIRS': [os.path.join(BASE_DIR, 'templates')],

-----------------------------------------------------------------------
and Access the Website from the Browser

-----------------------------------------------------
Adding static files for CSS:-
   
After that Create one Folder(static) and  add one css file in that
-------------------
in settings.py
and type this in very bottom

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

--------------------------------------------------------------------------------------------------------------------------------------------------------------



