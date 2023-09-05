
from django.urls import path
from crudapp import views


urlpatterns = [
    path('indexpage/',views.indexpage,name="indexpage"),
    path('categorypage/',views.categorypage,name="categorypage"),
    path('categorydata/',views.categorydata,name="categorydata"),    
    path('displaycategory/',views.displaycategory,name="displaycategory"),
    path('updatecategorydata/<int:dataid>/',views.updatecategorydata,name="updatecategorydata"),
    path('editcategorydata/<int:dataid>/',views.editcategorydata,name="editcategorydata"),
    path('deleteCategoryData/<int:dataid>/',views.deleteCategoryData,name="deleteCategoryData"),

    path('poductpage/',views.poductpage,name="poductpage"),
    path('getproductdata/',views.getproductdata,name="getproductdata"),
    path('displayproduct/',views.displayproduct,name="displayproduct"),
    path('updateproductdata/<int:dataid>/',views.updateproductdata,name="updateproductdata"),
    path('editproductdata/<int:dataid>/',views.editproductdata,name="editproductdata"),
    path('deleteproductData/<int:dataid>/',views.deleteproductData,name="deleteproductData"),

    path('',views.loginpage,name="loginpage"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),

    # path('displayConatct/',views.displayConatct,name="displayConatct"),
    path('deletecheckoutData/<int:dataid>/',views.deletecheckoutData,name="deletecheckoutData"),
     path('checkoutform/',views.checkoutform,name="checkoutform"),

    


  
]