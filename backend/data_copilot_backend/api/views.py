from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views import View
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from api import models
import pymysql as sql
from django.views.decorators.csrf import csrf_exempt
import json
from api.search_ext.transfer import xunfeiTransfer



class sqlSearchView(APIView):
    def get(self, request):
        return Response('sqlSearchView')

    def post(self, request):
        """
        查询信息。需要数据库名称和自然查询语言。
        :param request:测试版，需包含数据库名DB，自然语言SQL
        :return:
        """
        database = request.data.get('DB')
        SQL = request.data.get('SQL')

        if not database:
            return HttpResponse("Database name not provided.", status=400)

        try:
            from api.search_ext.sqlOp import sqlOp
            op = sqlOp(db=database)
            db_info = op.getDB_INFO()

            print(SQL)

            transfer = xunfeiTransfer(db_info=db_info, SQL=SQL)
            SQL = transfer.generate()

            print(SQL)
            # 执行生成的 SQL 查询
            op.SQL = SQL
            result = op.excute()

            # return JsonResponse({"db_info": db_info, "query_result": result}, safe=False)
            return JsonResponse({"query_result": result}, safe=False)
        except Exception as e:
            return HttpResponse(str(e), status=500)