from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.views import *
from django.contrib.auth import views as auth_view

app_name = ''

urlpatterns = [
    path('', home),
    path('category/<slug:val>',CategoryView.as_view(),name='category'),
    path('categorytitle/<val>',CategoryTitle.as_view(),name='categorytitle'),
    path('productdetail/<int:pk>',ProductDetail.as_view(),name='productdetail'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('profile/',ProfileView.as_view(), name="profile"),
    path('address/',address, name="address"),
    path('updateAddress/<int:pk>', updateAddress.as_view(), name='updateAddress'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('show_cart/', show_cart, name='show_cart'),
    path('checkout/', show_cart, name='checkout'),
    
    
    path('customer_registeration/', CustomerRegisterationView.as_view(), name='customer_registeration'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone'), name='passwordchange'),
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='app/changepassworddone.html'), name='passwordchangedone'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),
    
    
    
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset_done/', auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
