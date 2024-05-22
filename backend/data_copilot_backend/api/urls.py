from django.urls import path, re_path
from api import views

urlpatterns = [
    # path('login/', ),

    # path('register/', ),

    path('sqlSearch/', views.sqlSearchView.as_view()),   # 查询界面

    # path('order/', views.OrderView.as_view()),

    # path('visualize/',),   # 可视化

    # path('connection/',),    # 连接

    # path('remain_count/')   # 个人主页
]

"""
1 数据查询 sql
2 图表生成 
3 后台管理
"""
