"""大模型转换"""
from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage
import re

class xunfeiTransfer():
    """讯飞星火大模型"""
    def __init__(self, db_info, SQL,
                 SPARKAI_URL = 'wss://spark-api.xf-yun.com/v3.5/chat',
                 SPARKAI_APP_ID = 'ce14f035',
                 SPARKAI_API_SECRET='NjgwMDUwNTM2MmM2ZDY3ZjhmNzY2YzBj',
                 SPARKAI_API_KEY='307768922183cfeb82d06f416a2a72f7',
                 SPARKAI_DOMAIN='generalv3.5'
                 ):
        """
        初始化函数
        :param db_info: 数据库的表结构
        :param SQL: 自然语言查询语句
        :param SPARKAI_URL: 星火认知大模型v3.5的URL值
        :param SPARKAI_APP_ID: 星火认知大模型调用秘钥信息
        :param SPARKAI_API_SECRET: 星火认知大模型API_SECRET
        :param SPARKAI_API_KEY:星火认知大模型API_KEY
        :param SPARKAI_DOMAIN:星火认知大模型v3.5的domain值
        """
        self.db_info = db_info
        self.SQL = SQL
        self.SPARKAI_URL = SPARKAI_URL
        self.SPARKAI_APP_ID = SPARKAI_APP_ID
        self.SPARKAI_API_SECRET = SPARKAI_API_SECRET
        self.SPARKAI_API_KEY = SPARKAI_API_KEY
        self.SPARKAI_DOMAIN = SPARKAI_DOMAIN

    def generate(self):
        spark = ChatSparkLLM(
                        spark_api_url=self.SPARKAI_URL,
                        spark_app_id=self.SPARKAI_APP_ID,
                        spark_api_key=self.SPARKAI_API_KEY,
                        spark_api_secret=self.SPARKAI_API_SECRET,
                        spark_llm_domain=self.SPARKAI_DOMAIN,
                        streaming=False,
                    )
        # prompt 提示词。待优化。目前对于简单的语句执行压力不大
        msg = f"我的数据库的结构为{self.db_info}，请根据这个数据库，给出查询‘{self.SQL}’问题的SQL语句。回复中请仅提供SQL语句，回复中请仅提供SQL语句,不要夹杂任何无关信息。"
         # 借助讯飞星火大模型，生成SQL语句
        messages = [ChatMessage(role="user", content=msg)]
        handler = ChunkPrintHandler()
        a = spark.generate([messages], callbacks=[handler])
        # SQL语句清洗
        SQL = a.generations[0][0].text.strip()  # 从返回结果得到回复内容
        pattern = r"SELECT.*?;"
        SQL = re.findall(pattern, SQL, re.IGNORECASE)[0]  # 提取SQL语句。同时也可避免发生对数据的操纵
        SQL = SQL.replace('，', ',')  # 回复中可能会混淆全角半角符号，目前仅发现对于','的混淆
        return SQL
