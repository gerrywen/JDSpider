# -*- coding: utf-8 -*-
# @Time : 2019-08-02 17:33
# @Author : GerryWen
# @Contact : 15160333779
# @Email: blog@gerrywen.com
# @Site : 
# @File : es_types.py
# @Software: PyCharm

from datetime import datetime
from elasticsearch_dsl import DocType, Date, Nested, Boolean, \
    analyzer, Completion, Keyword, Text, Integer, Double, Float

from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer

from elasticsearch_dsl.connections import connections

connections.create_connection(hosts=["localhost"])


class CustomAnalyzer(_CustomAnalyzer):
    def get_analysis_definition(self):
        return {}


# filter 大小写转化
ik_analyzer = CustomAnalyzer("ik_max_word", filter=["lowercase"])


class ProductType(DocType):
    name = Text(analyzer="ik_max_word")  # 产品名称
    url = Keyword()  # 产品url
    product_id = Keyword()  # 产品id
    category = Keyword()  # 产品分类
    productInfo = Nested()  # 产品信息
    specInfo = Nested()  # 规格信息
    reallyPrice = Double()  # 产品价格
    originalPrice = Double()  # 原价
    description = Text(analyzer="ik_max_word")  # 产品描述
    shopId = Keyword()  # shop id
    venderId = Keyword()  # vender id
    commentCount = Integer()  # 评价总数
    goodComment = Integer()  # 好评数
    generalComment = Integer()  # 中评数
    poolComment = Integer()  # 差评数
    favourableDesc1 = Text(analyzer="ik_max_word")  # 优惠描述1
    favourableDesc2 = Text(analyzer="ik_max_word")  # 优惠描述2

    class Meta:
        index = "jd"
        doc_type = "products"


if __name__ == "__main__":
    ProductType.init()
