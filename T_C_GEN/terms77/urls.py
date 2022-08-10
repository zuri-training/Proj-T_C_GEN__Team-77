from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('signup', views.signup, name='signup'),
   path('signin', views.signin, name='signin'),
   path('dashboard', views.dashboard, name='dashboard'),
   path('aboutus', views.aboutus, name='aboutus'),
   path('forgotpass', views.forgotpass, name='forgotpass'),
   path('newterms', views.newterms, name='newterms'),
   path('ourprivacypolicy', views.ourprivacypolicy, name='ourprivacypolicy'),
   path('settings', views.settings, name='settings'),
   path('termsofuse', views.termsofuse, name='termsofuse'),
   path('step2', views.settings, name='step2'),
   path('step3', views.settings, name='step3'),
   path('preview', views.settings, name='preview'),
   path('logout', views.logout, name='logout'),
   path('dashboard_acct_edit', views.dashboard_acct_edit, name='dashboard_acct_edit'),
]