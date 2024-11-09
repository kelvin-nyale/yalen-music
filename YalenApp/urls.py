from django.urls import path
from YalenApp import views


urlpatterns=[
    path('',views.index,name='home'),
    path('panel-tabs/',views.panel,name='panel-tabs'),

    path('blank/',views.blank,name='blank'),

    path('buttons/',views.buttons,name='buttons'),

    path('component/',views.component,name='component'),
    path('error/',views.error,name='error'),
    path('forms/',views.forms,name='form'),
    path('form_advance/',views.form_advance,name='form_advance'),
    path('gallery/',views.gallery,name='gallery'),
    path('grid/',views.grid,name='grid'),
    path('icons/',views.icons,name='icons'),
    path('invoice/',views.invoice,name='invoice'),
    path('login/',views.login,name='login'),
    path('messages/',views.messages,name='messages'),
    path('notification/',views.notification,name='notification'),
    path('pricing/',views.pricing,name='pricing'),
    path('progress/',views.progress,name='progress'),
    path('social/',views.social,name='social'),
    path('table/',views.table,name='table'),
    path('typography/',views.typography,name='typography'),
    path('wizard/',views.wizard,name='wizard'),
]