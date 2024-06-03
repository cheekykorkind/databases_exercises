import os
import json
import uuid
from dynamodb_util import *

import pprint


def new_user(d_util, user_id):
    return d_util.put_item(
        {
            "PK": f"u#{user_id}",
            "SK": "count",
            "follower#": 0,
            "following#": 0,
            "post#": 0,
        }
    )


def update_user(d_util, deserialized_item):
    return d_util.update_item(deserialized_item)


def delete_user(d_util, deserialized_pk_sk):
    return d_util.delete_item(deserialized_pk_sk)
