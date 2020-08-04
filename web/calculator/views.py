from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from django.template import RequestContext

@api_view()
def api_root(request):
    return Response({
        'add': reverse('add', request=request),
    })

@api_view()
def add(request):
    try:
        first_number = int(request.GET.get('number1'))
        second_number = int(request.GET.get('number2'))
        return Response({'function': 'add','result': first_number + second_number})
    except Exception as e:
        return Response({'function': 'add','result': 'there was an error ' + str(e)})

@api_view()
def sub(request):
    try:
        first_number = int(request.GET.get('number1'))
        second_number = int(request.GET.get('number2'))
        return Response({'function': 'sub','result': first_number - second_number})
    except Exception as e:
        return Response({'function': 'sub','result': 'there was an error ' + str(e)})

@api_view()
def mul(request):
    try:
        first_number = int(request.GET.get('number1'))
        second_number = int(request.GET.get('number2'))
        return Response({'function': 'mul','result': first_number * second_number})
    except Exception as e:
        return Response({'function': 'mul','result': 'there was an error ' + str(e)})


@api_view()
def div(request):
    try:
        first_number = int(request.GET.get('number1'))
        second_number = int(request.GET.get('number2'))
        return Response({'function': 'div','result': first_number / second_number})
    except Exception as e:
        return Response({'function': 'div','result': 'there was an error ' + str(e)})

def index(request):
    return render(request,'index.html')

@api_view(('POST',))
def submitquery(request):
    operand1=int(request.POST.get('number1'))
    operand2=int(request.POST.get('number2'))
    #op=int(request.GET['op'])
    return Response({"number1 ":operand1,"number2 ":operand2,"result":operand1+operand2})
