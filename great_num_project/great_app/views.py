from django.shortcuts import render,HttpResponse,redirect
import random


def index(request):
   if not 'random_num' in request.session:

      request.session['random_num']=random.randint(1,100)
      print(request.session['random_num'])

   return render(request,'basic.html')

def validate(request):
   if request.POST["action"] == "play_again":
      request.session.pop("status")
      request.session.pop("random_num")
      request.session.pop("num")
   else:
      if "num" in request.POST:
         num=int(request.POST["num"])
         if num < request.session['random_num']:
            status = 'Too Low'

         elif num > request.session['random_num']:
            status = 'Too High'
         
         else :
            status='Success'
            request.session['num']=num
         request.session['status']=status
      

   return redirect ('/')


