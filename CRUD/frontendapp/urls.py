from django.urls import path
from frontendapp import views

urlpatterns = [
    # path('',views.basepage,name="basepage"),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('basepage/',views.basepage,name="basepage"),
    path('aboutpage/',views.aboutpage,name="aboutpage"),
    path('contactuspage/',views.contactuspage,name="contactuspage"),
   
    path('Cartpage/',views.Cartpage,name="Cartpage"),
    path('Checkoutpage/',views.Checkoutpage,name="Checkoutpage"),

    path('categorypages/',views.categorypages,name="categorypages"),
    path('saveCheckOut/',views.saveCheckOut,name="saveCheckOut"),
    
    path('ProductCategories/<catname>/',views.ProductCategories,name="ProductCategories"),
    
    
    
    path('productdetails/<singleprod>',views.productdetails,name="productdetails"),
    path('',views.accountlogin,name="accountlogin"),
    
    
    
    path('accountlogin/',views.accountlogin,name="accountlogin"),
    
    path('userlogin/',views.userlogin,name="userlogin"),
    
    path('loginpage/',views.loginpage,name="loginpage"),
    
    
    
    path('userlogout/',views.userlogout,name="userlogout"),
    
    
    
    path('saveregister/',views.saveregister,name="saveregister"),
    path('savecart/',views.savecart,name="savecart"),
    path('deleteproduct/<int:proid>/',views.deleteproduct,name="deleteproduct"),
    
    path('payment_page/',views.payment_page,name="payment_page"),
    path('search_result/',views.search_result,name="search_result"),
   
    
    
    
    
    
    
    
    
    
    
]
