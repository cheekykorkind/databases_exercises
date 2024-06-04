import os
import json
import uuid
from dynamodb_util import *

import pprint


def new_user(d_util, deserialized_item):
    return d_util.put_item(deserialized_item)


def update_user(d_util, deserialized_item):
    return d_util.update_item(deserialized_item)


def delete_user(d_util, deserialized_pk_sk):
    return d_util.delete_item(deserialized_pk_sk)


def query_user_info_by_user_id(d_util, user_id):
    q_param = {
        "KeyConditionExpression": "PK = :PK",
        "ExpressionAttributeValues": {":PK": {"S": f"u#{user_id}"}},
    }
    return d_util.query(q_param)


def query_user_info_by_user_id_and_sk(d_util, user_id, sk):
    q_param = {
        "KeyConditionExpression": "PK = :PK AND SK = :SK",
        "ExpressionAttributeValues": {":PK": {"S": f"u#{user_id}"}, ":SK": {"S": sk}},
    }
    return d_util.query(q_param)
