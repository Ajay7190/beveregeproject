from django.shortcuts import render, redirect
from crudapp.models import categoryDB, poductDB
from frontendapp.models import signupDB,cartdb,checkoutDb
from django.contrib import messages
from frontendapp.bizLogic import createOrder

# Create your views here.

# index page function

def basepage(request):
    
    data=categoryDB.objects.all()
    prod=poductDB.objects.all()
    return render(request,"home2.html",{'data':data, 'prod':prod})

def aboutpage(request):
    return render(request,"aboutus.html")

def contactuspage(request):
    return render(request,"contactus.html")

def deleteproduct(request,proid):
    
    data= cartdb.objects.get(id=proid)
    data.delete()

    return redirect(Cartpage)
     
def loginpage(request):

    return render(request, "loginpage.html")
def Cartpage(request):
    
    if 'Username' in request.session:
        usrn = request.session['Username']
        if usrn:
            data=categoryDB.objects.all()
            cdata=cartdb.objects.filter(username=usrn)    
            total_price = 0
            for i in cdata:
                total_price += i.tprice
            messages.success(request,"Added to Cart")
            return render(request,"cartpage.html",{'data':data,'cdata':cdata, "total_price":total_price})
        else:
            messages.error(request,"please login")
            return redirect(accountlogin)
    else:
        messages.error(request,"please login")
        return redirect(accountlogin)
    
def savecart(req):
    if req.method=="POST":
        uname=req.POST.get('username')
        pname=req.POST.get('pname')
        des=req.POST.get('pdes')
        pric=req.POST.get('pprice')
        

        tprice=req.POST.get('totalprice')
        quantity=req.POST.get('qty')
        
        

        obj=cartdb(username=uname,productname=pname,price=pric,description=des,tprice=tprice,quantity=quantity)
        obj.save()
        return redirect(Cartpage)   
    
def place_order(req):
    item = cartdb.objects.filter( username = req.session['Username'])
    total_price =0
    for i in item :
        total_price=total_price + i.tprice
    return render(req, "cartpage.html" ,{'item':item, 'total_price':total_price})
        
    
    
        
def saveCheckOut(req):
    if req.method=="POST":
        district=req.POST.get('district')
        fname=req.POST.get('fname')
        lname=req.POST.get('lname')
        address=req.POST.get('address1')
        address2=req.POST.get('address2')
        city=req.POST.get('city')
        state=req.POST.get('state')
        zip=req.POST.get('zip')
        email=req.POST.get('email')
        number=req.POST.get('number')       
        obj=checkoutDb(district=district,firstname=fname,lastname=lname,address=address,adresstwo=address2,city=city,state=state,email=email,zip=zip,mobile=number)
        obj.save()
        return redirect(Checkoutpage) 

def categorypages(request):
    categories=poductDB.objects.all()
    return render(request,"category.html",{'categories':categories})

def ProductCategories(request, catname):
    prd=categoryDB.objects.all()
    data=categoryDB.objects.filter(category_name=catname)
    product=poductDB.objects.filter(product_category=catname)
    return render(request,"productscategory.html", {'data':data, 'product':product,'prd':prd})

def productdetails(request ,singleprod): 
    single_pro= poductDB.objects.filter(product_name=singleprod)
    spro = poductDB.objects.all()
    data= categoryDB.objects.all()
    return render(request,"singleProductDetails.html",{'single_pro':single_pro, 'spro':spro, 'data':data})

def accountlogin(request):
    return render(request,"loginpage.html")

def userlogin(request):
    if request.method == "POST":
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        if signupDB.objects.filter(Username=username, password=password).exists():
            request.session['Username'] = username
            request.session['password'] = password
            
            return redirect(basepage)
        else:
            messages.error(request,"Invalid User Name or Password")
            return redirect(accountlogin)
    else:
        messages.error(request,"Invalid User Name or Password")
        return redirect(accountlogin) 

def userlogout(request):
    messages.success(request,"logout succesfully...")
    del request.session['Username']
    del request.session['password']
    return redirect(accountlogin)

def saveregister(req):
    if req.method == "POST":    
        na = req.POST.get('uName')
        em = req.POST.get('uEmail')       
        pswd = req.POST.get('uPassword')        
        obj = signupDB(Username=na, Email=em,  password=pswd, )
        obj.save()        
        return redirect(accountlogin)
    
def paymenthandler(request):
    if 'Username' in request.session:
        usrn = request.session['Username']
        if usrn:
           
            return createOrder(request)

def Checkoutpage(request):
    if 'Username' in request.session:
        usrn = request.session['Username']
        if usrn:
            cdata= cartdb.objects.all()
            data=cartdb.objects.filter(username=usrn)
            return render(request,"checkoutpage.html",{'data':data,'cdata':cdata})        
        
        
        
        
        
        
        
        
        
        
        
def payment_page(request):
    messages.success(request,"payment succesfull")
    return render(request,"paymentpage.html")



def search_result(request):
    if request.method=="GET":
        search=request.GET.get('q')
        cat=categoryDB.objects.filter(category_name__icontains=search)
        pro=poductDB.objects.filter(product_name__icontains=search) 
        return render(request,"searchpage.html",{'cat':cat, 'pro':pro})
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
