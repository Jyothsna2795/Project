from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
import mysql.connector
import json

mydb = mysql.connector.connect(
  host="hostname",
  user="username",
  passwd="password",
  database="database_name"
  )

class Data(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    def get(self,request):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM data WHERE id='1'")
        row_headers=[x[0] for x in mycursor.description]
        myresult = mycursor.fetchall()
        json_data=[]
        for result in myresult:
            json_data.append(dict(zip(row_headers,result)))
        json_out = json.dumps(json_data, default=str)
        return Response(json_out)
