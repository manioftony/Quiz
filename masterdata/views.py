# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from masterdata.models import Question, Answer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from masterdata.forms import CustomUserCreationForm
import requests
import random


# def swap_random(seq):
#   idx = range(len(seq))
#   i1, i2 = random.sample(idx, 2)
#   seq[i1], seq[i2] = seq[i2], seq[i1]


def index(request):
    return render(request, 'index.html', locals())
# *        # import ipdb;ipdb.set_trace()
        # return HttpResponse(e)


def login_data(request):
    # import ipdb;ipdb.set_trace()
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/index')
            else:
                pass
        else:
            return render(request, 'login.html', locals())
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/index')
        else:
            form = AuthenticationForm()
            return render(request=request,
                          template_name="login.html",
                          context={"form": form})


def createuser(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')

    else:
        f = CustomUserCreationForm()

    return render(request, 'usercreation.html', {'form': f})



class QuestionAnswerView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        obj = requests.get("https://opentdb.com/api.php?amount=1000")
        data = obj.json().get('results')[0:5]
        total = []
        for i in data:
            question = i['question']
            result = []
            q_obj = i['incorrect_answers']
            for z in q_obj:
                page = {}
                page['answerText']=z
                page['correct'] = False
                result.append(page)
            mani = {"answerText":i['correct_answer'],"correct":True}
            result.append(mani)
            swap_random(result)
            total.append({'questionText':question,"answers":result})
        response_dict = {"data":total,"status":200}
        return Response(response_dict)



def logout_request(request):
    logout(request)
    # messages.info(request, "Logged out successfully!")
    return redirect("/")


def swap_random(seq):
  idx = range(len(seq))
  i1, i2 = random.sample(idx, 2)
  seq[i1], seq[i2] = seq[i2], seq[i1]


def question_answer(request):
    obj = requests.get("https://opentdb.com/api.php?amount=1000")
    data = obj.json().get('results')[0:5]
    total = []
    for i in data:
        question = i['question']
        result = []
        q_obj = i['incorrect_answers']
        for z in q_obj:
            page = {}
            page['answerText']=z
            page['correct'] = False
            result.append(page)
        mani = {"answerText":i['correct_answer'],"correct":True}
        result.append(mani)
        swap_random(result)
        total.append({'questionText':question,"answers":result})
    response_dict = {"data":total,"status":200}
    return Response(response_dict)





