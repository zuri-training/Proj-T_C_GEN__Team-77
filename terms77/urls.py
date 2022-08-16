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
   path('preview', views.preview, name='preview'),
   path('preview2', views.preview2, name='preview2'),
   path('logout', views.logout, name='logout'),
   path('dashboard_acct_edit', views.dashboard_acct_edit, name='dashboard_acct_edit'),
   path('faq', views.faq, name='faq'),
   path('privacypolicynt', views.privacypolicynt, name='privacypolicynt'),
   path('step2', views.step2, name='step2'),
   path('step3', views.step3, name='step3'),
   path('contactus', views.contactus, name='contactus'),
]