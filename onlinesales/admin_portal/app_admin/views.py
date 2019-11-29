from django.shortcuts import render
from django.utils.crypto import random
from .models import MerchantModel


def admin_Login_Verification(request):
    email = request.POST.get("email")
    print(email)
    password = request.POST.get("pass")
    print(password)
    if email == "admin@gmail.com" and password == "admin":
        return render(request, "admin_welcome_page.html")
    else:
        return render(request, "admin_login.html", {"message": "Wrong Entry"})


def admin_home_button_action(request):
    button_action = request.POST.get("btn")
    print(button_action)

    if button_action == "merchant":
        return render(request,"merchant.html")
    if button_action == "sales":
        return render(request,"sales.html")
    if button_action == "complaint":
        return render(request,"complaint.html")
    if button_action == "logout":
        return render(request,"index.html")


def merchant_actions(request):
    button = request.POST.get("btn")

    if button == "add_merchant":
        return render(request,"add_merchant.html")
    if button == "view_merchant":
        data = MerchantModel.objects.all()
        return render(request,"view_merchant.html",{"data":data})
    if button == "update_merchant":
        return render(request,"update_merchant.html")
    if button == "delete_merchant":
        return render(request,"delete_merchant.html")
    if button == "logout":
        return render(request,"index.html")

def gen_idno():
    qs = MerchantModel.objects.all()
    if qs:
        return qs[len(qs)-1].Merchant_Id+1

    else:
        return 101



def save_merchant(request):
    Name = request.POST.get("name")
    CONTACT = request.POST.get("contact")
    EMAIL = request.POST.get("email")
    Password = random.randint(10000000,99999999)
    IdNo = gen_idno()


    MerchantModel(Merchant_Name=Name,Merchant_Contact=CONTACT,Merchant_Email=EMAIL,Merchant_Password=Password,Merchant_Id=IdNo).save()

    return render(request,"merchant.html",{"message":"merchant saved successfully"})