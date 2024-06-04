from a1 import *
import pprint


def update_follower(d_util, user_id, follower_user_id):
    new_user(d_util, {"PK": f"u#{user_id}#follower", "SK": f"u#{follower_user_id}"})

    return d_util.update_item(
        {
            "PK": f"u#{user_id}",
            "SK": "count",
            "follower#": len(query_follower_list_by_user_id(d_util, user_id)),
        }
    )


def query_follower_list_by_user_id(d_util, user_id):
    q_param = {
        "KeyConditionExpression": "PK = :PK",
        "ExpressionAttributeValues": {":PK": {"S": str(f"u#{user_id}#follower")}},
    }
    return d_util.query(q_param)
