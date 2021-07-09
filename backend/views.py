from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import TemplateView, ListView
from django.core.mail import send_mail
import numpy as np
from vehicle_recognition.settings import EMAIL_HOST_USER
from operator import itemgetter
from .models import User_info, feedback
from cv2 import cv2
import imutils
import pytesseract
from PIL import ImageGrab



# Create your views here.
def home1(request):
    users = User_info.objects.count()
    messages.info(request, users)
    return render(request, 'home1.html') 
                  
def upload(request):
# if request.method == 'POST':
#     uploaded_menu = request.FILES['menu_image'].file.read()
#     with open(uploaded_menu, 'rb') as f:
#         words = read_menu(f, api_key)
#         print(type(f))
#     print(words)  
#     user = User_info()

#     pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#     img = cv2.imread('skoda1.png', cv2.IMREAD_COLOR)
#     img = cv2.resize(img, (600, 400))

#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     gray = cv2.bilateralFilter(gray, 13, 15, 15)

#     edged = cv2.Canny(gray, 30, 200)
#     contours = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     contours = imutils.grab_contours(contours)
#     contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
#     screenCnt = None

#     for c in contours:

#         peri = cv2.arcLength(c, True)
#         approx = cv2.approxPolyDP(c, 0.018 * peri, True)

#         if len(approx) == 4:
#             screenCnt = approx
#             break

#     if screenCnt is None:
#         detected = 0
#         print("No contour detected")
#     else:
#         detected = 1

#     if detected == 1:
#         cv2.drawContours(img, [screenCnt], -1, (0, 0, 255), 3)

#     mask = np.zeros(gray.shape, np.uint8)
#     new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1, )
#     new_image = cv2.bitwise_and(img, img, mask=mask)

#     (x, y) = np.where(mask == 255)
#     (topx, topy) = (np.min(x), np.min(y))
#     (bottomx, bottomy) = (np.max(x), np.max(y))
#     Cropped = gray[topx:bottomx + 1, topy:bottomy + 1]

#     text = pytesseract.image_to_string(Cropped, config='--psm 11')
#     print("Detected license plate Number is:", text)
#     img = cv2.resize(img, (500, 300))
#     Cropped = cv2.resize(Cropped, (400, 200))
#     cv2.imshow('car', img)
#     cv2.imshow('Cropped', Cropped)

#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#     text
#     user = User_info.objects.get(vehicle_number=text)
#     send_mail(
#         'From_sidelagau', 'Please remove your vehicle','temp.practicecw2@gmail.com', [user.email], fail_silently = False)
#     print (text)
    return render(request, 'userfound.html') 

# def scan(request):  
#     user = User_info() 
#     pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#     vid = cv2.VideoCapture(0)
#     img_counter = 0
#     while (True):
#         #Capture the video frame by frame
#         ret, frame = vid.read()
#         if not ret:
#             print("print to grav frame")
#             break
#         #Display the resulting frame
#         cv2.imshow('scan', frame)
#         k = cv2.waitKey(1)
#         if k % 256 == 27:
#             break
#         elif k % 256 == 32:
#             img_name = "opencv_frame_{}.png".format(img_counter)
#             cv2.imwrite(img_name, frame)
#             print("taken")
#             img_counter += 1
#             img = cv2.imread(img_name, cv2.IMREAD_COLOR)
#             img = cv2.resize(img, (600, 400))

#             gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             gray = cv2.bilateralFilter(gray, 13, 15, 15)

#             edged = cv2.Canny(gray, 30, 200)
#             contours = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#             contours = imutils.grab_contours(contours)
#             contours = sorted(contours, key=cv2.contourArea, reverse=True)[:30]
#             screenCnt = None

#             for c in contours:
#                 peri = cv2.arcLength(c, True)
#                 approx = cv2.approxPolyDP(c, 0.018 * peri, True)
#                 if len(approx) == 4:
#                     screenCnt = approx
#                     break

#                 if screenCnt is None:
#                     detected = 0
#                     print("No contour detected")
#                     break
#                 else:
#                     detected = 1

#                 if detected == 1:
#                     cv2.drawContours(img, [screenCnt], -1, (0, 0, 255), 3)

#                 mask = np.zeros(gray.shape, np.uint8)
#                 new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1, )
#                 new_image = cv2.bitwise_and(img, img, mask=mask)

#                 (x, y) = np.where(mask == 255)
#                 (topx, topy) = (np.min(x), np.min(y))
#                 (bottomx, bottomy) = (np.max(x), np.max(y))
#                 Cropped = gray[topx:bottomx + 1, topy:bottomy + 1]

#                 text = pytesseract.image_to_string(Cropped, config='--psm 11')
#                 print("Detected license plate Number is:", text)
#                 img = cv2.resize(img, (500, 300))
#                 Cropped = cv2.resize(Cropped, (400, 200))
#                     # cv2.imshow('scanned', img)
#                     # cv2.imshow('Cropped', Cropped)
#                     # cv2.imshow('Gray Image', gray)
#                     # cv2.imshow("canny image", edged)
#                     # cv2.imshow("Top 30 contours",img)
#                 cv2.waitKey(0)
#                 vid.release()
#                 cv2.destroyAllWindows()                
#                 try:
#                     user = User_info.objects.get(vehicle_number=text) 
#                     send_mail(
#                         'From_sidelagau', 'Please remove your vehicle','temp.practicecw2@gmail.com', [user.email], fail_silently = False)
#                     print ("email sent")
#                     vid.release()
#                     cv2.destroyAllWindows()
#                 except:
#                     print ("User not found")
#                     return render(request, 'home1.html')   
#     return render(request, 'home1.html') 
# def scan(request):  
#     user = User_info() 
#     pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#     vid = cv2.VideoCapture(0)
#     img_counter = 0
#     while (True):   
#     #Capture the video frame by frame
#         ret, frame = vid.read()
#         if not ret:
#             print("print to grav frame")
#             break
#         #Display the resulting frame
#         cv2.imshow('scan', frame)
#         k = cv2.waitKey(1)
#         if k % 256 == 27:
#             break
#         elif k % 256 == 32:
#             img_name = "opencv_frame_{}.png".format(img_counter)
#             cv2.imwrite(img_name, frame)
#             print("taken")
#             img_counter += 1

#             img = cv2.imread(img_name,cv2.IMREAD_COLOR)
#             img = imutils.resize(img, width=500 )
#             gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grey scale
#             gray = cv2.bilateralFilter(gray, 11, 17, 17) #Blur to reduce noise
#             edged = cv2.Canny(gray, 30, 200) #Perform Edge detection
#             cnts,new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

#             img1=img.copy()
#             cv2.drawContours(img1,cnts,-1,(0,255,0),3)
#             #cv2.imshow("img1",img1)
#             cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:30]
#             screenCnt = None #will store the number plate contour
#             img2 = img.copy()
#             cv2.drawContours(img2,cnts,-1,(0,255,0),1) 
#             #cv2.imshow("img2",img2) #top 30 contours

#             count=0
#             idx=7
#             # loop over contours
#             for c in cnts:
#             # approximate the contour
#                     peri = cv2.arcLength(c, True)
#                     approx = cv2.approxPolyDP(c, 0.018 * peri, True)
#                     if len(approx) == 4: #chooses contours with 4 corners
#                             screenCnt = approx
#                             x,y,w,h = cv2.boundingRect(c) #finds co-ordinates of the plate
#                             new_img=img[y:y+h,x:x+w]
#                             cv2.imwrite('./'+str(idx)+'.png',new_img) #stores the new image
#                             idx+=1
#                             break
#                         #draws the selected contour on original image
#             cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)
#             #cv2.imshow("Final image with plate detected",new_img)

#             Cropped_loc='./7.png' #the filename of cropped image
#             #cv2.imshow("cropped",cv2.imread(Cropped_loc))
#             pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe' #exe file for using ocr

#             text=pytesseract.image_to_string(Cropped_loc,lang='eng') #converts image characters to string
#             print("Number is:" ,text)
#             cv2.waitKey(0)
#             vid.release()
#             cv2.destroyAllWindows()                
#             try:
#                 user = User_info.objects.get(vehicle_number=text) 
#                 send_mail(
#                     'From_sidelagau', 'Please remove your vehicle','temp.practicecw2@gmail.com', [user.email], fail_silently = False)
#                 print ("email sent")
#                 # vid.release()
#                 # cv2.destroyAllWindows()
#             except:
#                 print ("User not found")
#                 return render(request, 'usernotfound.html')   
#     return render(request, 'home1.html') 

def scan(request):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    img_counter = 0
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    def captureScreen(bbox=(300,300,1500,1000)):
        capScr = np.array(ImageGrab.grab(bbox))
        capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
        return capScr
    while True:
        timer = cv2.getTickCount()
        _,img_name = cap.read()
        #img = captureScreen()
        #DETECTING CHARACTERES
        hImg, wImg,_ = img_name.shape
        boxes = pytesseract.image_to_boxes(img_name)
        for b in boxes.splitlines():
            #print(b)
            b = b.split(' ')
            #print(b)
            x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
            cv2.rectangle(img_name, (x,hImg- y), (w,hImg- h), (50, 50, 255), 2)
            cv2.putText(img_name,b[0],(x,hImg- y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
        #cv2.putText(img, str(int(fps)), (75, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (20,230,20), 2);
        #print(pytesseract.image_to_string(img_name))
        while (True):
            # Capture the video frame by frame
            ret, frame = cap.read()
            if not ret:
                print("print to grav frame")
                break
            # Display the resulting frame
            cv2.imshow('scan', frame)
            #cv2.imshow("Result", img_name)
            k = cv2.waitKey(1)
            if k % 256 == 27:
                break
            elif k % 256 == 32:
                img_name = "opencv_frame_{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("taken")
                img_counter += 1
                text = pytesseract.image_to_string(img_name)
                print(text)
        cv2.waitKey(0)
        cap.release()
        cv2.destroyAllWindows()
        try:
            user = User_info.objects.get(vehicle_number=text) 
            send_mail(
                'From_sidelagau', 'Please remove your vehicle','temp.practicecw2@gmail.com', [user.email], fail_silently = False)
            print ("email sent")
            cap.release()
            cv2.destroyAllWindows()
        except:
            print ("User not found")
            return render(request, 'usernotfound.html')  
        return render(request, 'home1.html') 

def joinnow(request):
    user = User_info()
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        vehicle_number = request.POST['vehicle_number']
        vehicle_type = request.POST['vehicle_type']

        try:
            user = User_info.objects.get(vehicle_number=vehicle_number)
            messages.info(request, '*Vehicle Already Registered')
            return redirect('joinnow')
        except:    
            if password1 != password2: 
                messages.info(request, '*Please retype same password')
                return redirect('joinnow') 

            elif vehicle_number == "" or phone == "":
                messages.info(request, '*Empty text field')
                return redirect('joinnow')                              
            else:               
                user = User_info(name=name, email=email, phone=phone, vehicle_number=vehicle_number, vehicle_type=vehicle_type, username=username, password=password2)
                user.save()

        return redirect('home1')   
    else:            
         return render(request, 'joinnow.html')

def loginpage(request):
       
    return render(request, 'loginpage.html')

def trafficrules(request):
    return render(request, 'trafficrules.html')

def account(request):
    return render(request, 'account.html')

def search(request):
    user = User_info()
    if request.method == 'POST':
        names = request.POST['search']
        if names=="":
            return render (request,'search.html')           
        try:
            user = User_info.objects.get(vehicle_number=names) 
            send_mail(
                'From_sidelagau', 'Please remove your vehicle','temp.practicecw2@gmail.com', [user.email], fail_silently = False)
            return render(request, 'userfound.html')
        except:
            messages.info(request,"*User not found*") 
            return render(request, 'search.html')     
    else:
        return render (request,'search.html')
def userfound(request):
    return render(request, 'userfound.html')  
def usernotfound(request):
    return render(request, 'usernotfound.html')      