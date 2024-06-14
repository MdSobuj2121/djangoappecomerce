from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import loginForm, MyPasswordChangeForm
from .forms import MyPasswordResetForm, MySetPasswordForm
from django.contrib.auth import logout
from django.shortcuts import redirect


def custom_logout(request):
    logout(request)
    print("User logged out successfully.")
    return redirect('login')
urlpatterns = [
    path('', views.home),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('category/<slug:val>', views.CategoryView.as_view(), name="category"),
    path("category-title/<val>", views.CategoryTitle.as_view(), name="category-title"),
    path('product-detail/<int:pk>', views.ProductDetail.as_view(), name="product-detail"),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('updateAddress/<int:pk>', views.updateAddress.as_view(), name='updateAddress'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('checkout/', views.checkout.as_view(), name='checkout'),
    path('payment-options/', views.PaymentOptionsView.as_view(), name='payment_options'),
    path('orders/', views.home, name='orders'),
    
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
    
    # Authentication URLs
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=loginForm), name='login'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/changepassword.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    path('logout/', custom_logout, name='logout'),
    
    path('password-reset/', auth_views.PasswordResetView.as_view(
    template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
    template_name='app/password_reset_done.html'), name="password_reset_done"),
    
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
    template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
    template_name='app/password_reset_complete.html'), name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)