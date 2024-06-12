import boto3
from boto3.dynamodb.types import TypeSerializer, TypeDeserializer
import datetime
from decimal import *


class DynamodbUtil:
    def __init__(self, table_name):
        self.client = boto3.client(
            "dynamodb",
            region_name="us-east-1",
            endpoint_url="http://nosql-localstack:4566",
        )
        self.table_name = table_name
        self.serializer = TypeSerializer()
        self.deserializer = TypeDeserializer()

    def serialize_item(self, item):
        return {k: self.serializer.serialize(v) for k, v in item.items()}

    # item = {
    #     "PK": "u#12345",
    #     "SK": "count",
    #     "follower#": 3000000000,
    #     "following#": 971,
    #     "post#": 4945,
    # }
    def put_item(self, item):
        payload = {
            "TableName": self.table_name,
            "Item": self.serialize_item(item),
        }
        return self.client.put_item(**payload)

    def update_item(self, deserialized_item):
        s_item = self.serialize_item(deserialized_item)

        # 업데이트할 테이블과 항목의 키 정의
        pk_sk = {"PK": s_item["PK"], "SK": s_item["SK"]}
        del s_item["PK"]
        del s_item["SK"]

        expression_attribute_names = {}
        expression_attribute_values = {}
        update_expression_pairs = []
        i = 0
        for s_k, s_v in s_item.items():
            attr_name = f"#attr{i}"
            val_name = f":val{i}"
            update_expression_pairs.append(f"{attr_name} = {val_name}")
            expression_attribute_names[attr_name] = s_k
            expression_attribute_values[val_name] = s_v
            i += 1

        return self.client.update_item(
            TableName=self.table_name,
            Key=pk_sk,
            UpdateExpression=f"SET {','.join(update_expression_pairs)}",
            ExpressionAttributeNames=expression_attribute_names,
            ExpressionAttributeValues=expression_attribute_values,
            ReturnValues="UPDATED_NEW",
        )

    def delete_item(self, deserialized_pk_sk):
        pk_sk = self.serialize_item(deserialized_pk_sk)

        return self.client.delete_item(TableName=self.table_name, Key=pk_sk)

    def get_item(self, deserialized_pk_sk):
        pk_sk = self.serialize_item(deserialized_pk_sk)
        raw_item = self.client.get_item(TableName=self.table_name, Key=pk_sk).get(
            "Item", {}
        )

        return {k: self.deserializer.deserialize(v) for k, v in raw_item.items()}

    def query(self, q_param):
        full_param = {"TableName": self.table_name, "ScanIndexForward": False}
        full_param.update(q_param)

        return [
            {k: self.deserializer.deserialize(v) for k, v in item.items()}
            for item in self.client.query(**full_param)["Items"]
        ]

    def scan(self):
        paginator = self.client.get_paginator("scan")
        items = []
        for page in paginator.paginate(**{"TableName": self.table_name}):
            items += [
                {k: self.deserializer.deserialize(v) for k, v in item.items()}
                for item in page["Items"]
            ]
        return items

    # https://docs.aws.amazon.com/ja_jp/amazondynamodb/latest/developerguide/Expressions.OperatorsAndFunctions.html
    def scan_with_sk_filter(self, sk):
        paginator = self.client.get_paginator("scan")
        items = []
        paginator_args = {
            "TableName": self.table_name,
            "FilterExpression": "contains (SK, :value)",
            "ExpressionAttributeValues": {":value": {"S": sk}},
        }
        for page in paginator.paginate(**paginator_args):
            items += [
                {k: self.deserializer.deserialize(v) for k, v in item.items()}
                for item in page["Items"]
            ]
        return items
