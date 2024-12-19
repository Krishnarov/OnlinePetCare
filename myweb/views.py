from django.shortcuts import render,redirect,reverse,get_object_or_404
from .models import Admin,Login,ImageUpload,CardsUpload,Enquiry
from django.http import HttpResponse

from django.contrib import messages
# Create your views here.
def index(request):
    images = ImageUpload.objects.all()
    Cards= CardsUpload.objects.all()
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        enq=Enquiry(name=name,email=email,subject=subject,message=message)
        enq.save()
        messages.success(request, "enquriy successfully save")

        print("enquriy successfully save")
        return redirect(reverse('myweb:index'))
    return render(request,'index.html',{'images': images,"Cards":Cards})

def gallery(request):
    return render(request,'gallery.html')

def services(request):
    Cards= CardsUpload.objects.all()
    return render(request,'services.html',{"Cards":Cards})

def blog(request):
    return render(request,'blog.html')

def signup(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        psw=request.POST['psw']
        if not email or not psw:
            return HttpResponse("Email and password are required!", status=400)
        reg=Admin(name=name,email=email,psw=psw)
        log=Login(email=email,psw=psw)
        reg.save()
        log.save()
        return redirect(reverse('myweb:login'))
    return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        psw=request.POST['psw']
        user = Login.objects.get(email=email)
        if(psw==user.psw):
            messages.success(request, "welcome back mr...")
            return redirect(reverse('myweb:adminhome'))
        else:
            messages.error(request, "Invalid password.")
    return render(request,'login.html')

def adminhome(request):
    return render(request,'adminhome.html')

def upload_image(request):
    success = False
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        formdata=ImageUpload(title=title,image=image)
        formdata.save()
        print("data seve successfull")
        success = True
    images = ImageUpload.objects.all()
    Cards= CardsUpload.objects.all()
    # return render(request, 'image_list.html', {'images': images})
    return render(request,'upload_image.html',{'images': images,'success': success})

def delete_slider(request, id):
    # success = False
    slider = get_object_or_404(ImageUpload, id=id)
    slider.delete()
    # success = True
    messages.success(request, "Slider deleted successfully!")
    return redirect('myweb:upload_image') 
    
    
def cards(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Description = request.POST.get('Description')
        image = request.FILES.get('image')
        formdata=CardsUpload(title=title,Description=Description,image=image)
        formdata.save()
        print("titli ;=",title)
        print("desc ;=",Description)
        print("image ;=",image)

    Cards= CardsUpload.objects.all()
    return render(request,'cards.html',{'cards':Cards})

def delete_cards(request, id):
    # success = False
    cards = get_object_or_404(CardsUpload, id=id)
    cards.delete()
    # success = True
    messages.success(request, "Slider deleted successfully!")
    return redirect('myweb:cards') 


def viewenquiry(request):
    enq=Enquiry.objects.all()
    return render(request,'viewenquiry.html',{"enq":enq})