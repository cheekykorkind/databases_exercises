import boto3
from boto3.dynamodb.types import TypeSerializer, TypeDeserializer
import datetime
from decimal import *
import pprint

class DynamodbUtil:
    def __init__(self, table_name):
        self.client = boto3.client("dynamodb", region_name="us-east-1", endpoint_url="http://localhost:4566")
        self.table_name = table_name
        self.serializer = TypeSerializer()
        self.deserializer = TypeDeserializer()

    def serialize_item(self, item):
        return {
            k: self.serializer.serialize(v)
            for k, v in item.items()
        }

    # item = {
    #     "PK": "u#12345",
    #     "SK": "count",
    #     "follower#": 3000000000,
    #     "following#": 971,
    #     "post#": 4945,
    # }
    def put_item(self, item):
        payload = {
            'TableName': self.table_name,
            'Item': self.serialize_item(item),
        }
        self.client.put_item(**payload)

    # def update_item(self, item):
    #     # 업데이트할 테이블과 항목의 키 정의
    #     key = {'PK': {'S': item.get('PK')}}

    #     # 업데이트 표현식 정의
    #     update_expression = 'SET #attr1 = :val1, #attr2 = :val2'
    #     expression_attribute_names = {
    #         '#attr1': 'attribute1',
    #         '#attr2': 'attribute2'
    #     }
    #     expression_attribute_values = {
    #         ':val1': {'S': 'new_value1'},
    #         ':val2': {'N': '42'}
    #     }

    #     # 업데이트 요청
    #     response = dynamodb.update_item(
    #         TableName=self.table_name,
    #         Key=key,
    #         UpdateExpression=update_expression,
    #         ExpressionAttributeNames=expression_attribute_names,
    #         ExpressionAttributeValues=expression_attribute_values,
    #         ReturnValues="UPDATED_NEW"  # 업데이트된 새 값을 반환하도록 설정
    #     )


    # q_param = {
    #     "TableName": table_name,
    #     "ScanIndexForward": False,
    #     "KeyConditionExpression": "PK = :PK",
    #     "ExpressionAttributeValues": {":PK": {"S": str(f"{post_id}#likelist")}},
    # }
    def query(self, q_param):
        return [{k: self.deserializer.deserialize(v) for k, v in item.items()} for item in self.client.query(**q_param)["Items"]]


    def scan(self):
        paginator = self.client.get_paginator("scan")
        items = []
        for page in paginator.paginate(**{"TableName": self.table_name}):
            items += [{k: self.deserializer.deserialize(v) for k, v in item.items()} for item in page["Items"]]
        return items

    # # 업데이트할 테이블과 항목의 키 정의
    # key = {'PK': {'S': item.get('PK')}}
    # # 업데이트 표현식 정의
    # update_expression = 'SET #attr1 = :val1, #attr2 = :val2'
    # expression_attribute_names = {
    #     '#attr1': 'attribute1',
    #     '#attr2': 'attribute2'
    # }
    # expression_attribute_values = {
    #     ':val1': {'S': 'new_value1'},
    #     ':val2': {'N': '42'}
    # }
    def ss1(self):
        item = {
            'PK': 'u#f71076f4-68f5-4926-b52d-499b2bb16459',
            'SK': 'count',
            'follower#': Decimal('0'),
            'following#': Decimal('0'),
            'post#': Decimal('0')
        }
        # pprint.pprint(item)
        aaa1=self.serialize_item(item)



        
        