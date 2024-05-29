import os
import json
import uuid
from dynamodb_util import *

import pprint

def new_user(d_util, user_id):
    d_util.put_item({
        "PK": f"u#{user_id}",
        "SK": "count",
        "follower#": 0,
        "following#": 0,
        "post#": 0,
    })

# user_id=1
# new_user(DynamodbUtil(table_name="user"), user_id)



# item = {
#     "PK": f"u#{str(uuid.uuid4())}",
#     "SK": "count",
#     "follower#": 0,
#     "following#": 0,
#     "post#": 0,
# }
# d_util.put_item(table_name, item)

# r1 = DynamodbUtil(table_name="user").scan()
# pprint.pprint(r1)

DynamodbUtil(table_name="user").ss1()
