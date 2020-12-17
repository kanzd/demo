from django.shortcuts import render
import subprocess as sb
import django.http
from . import serializers
from . import models
from rest_framework.views import APIView
from rest_framework.response import *
from rest_framework import status


def code(code,input):
  
    file = open("Codingapp/codingfiles/code3.py",'w')
    code = """
import sys 
codeinput = []
for i in sys.argv:
    codeinput.append(i)
"""+code
    print(code)
    file.write(code)
    file.close()
    output = sb.check_output("python Codingapp/codingfiles/code3.py "+input)
    print(input)
    print(output)
    return output

class CodeAPIview(APIView):
    def post(self,req,):
        file = open('a.txt','a');
        file.write(str(req.data))
        print(req.data['code'])
        output = code(req.data['code'],req.data['input'])
        codedb = models.CodeModel()
        codedb.code=req.data ['code']
        codedb.inputs=req.data['input']
        
        codedb.output=output
        
        codedb.save()

        codeser = serializers.CodeSerializers(codedb,many=False)

        return Response(codeser.data)
