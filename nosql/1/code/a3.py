from a1 import *
from a2 import *
import pprint


def increase_following(d_util, user_id, following_user_id):
    new_user(d_util, {"PK": f"u#{user_id}#following", "SK": f"u#{following_user_id}"})
    d_util.update_item(
        {
            "PK": f"u#{user_id}",
            "SK": "count",
            "following#": len(query_following_list_by_user_id(d_util, user_id)),
        }
    )

    # increase_follower
    new_user(d_util, {"PK": f"u#{following_user_id}#follower", "SK": f"u#{user_id}"})
    return d_util.update_item(
        {
            "PK": f"u#{following_user_id}",
            "SK": "count",
            "follower#": len(query_follower_list_by_user_id(d_util, following_user_id)),
        }
    )


def decrease_following(d_util, user_id, following_user_id):
    delete_user(
        d_util, {"PK": f"u#{user_id}#following", "SK": f"u#{following_user_id}"}
    )
    d_util.update_item(
        {
            "PK": f"u#{user_id}",
            "SK": "count",
            "following#": len(query_following_list_by_user_id(d_util, user_id)),
        }
    )

    # decrease_follower
    delete_user(d_util, {"PK": f"u#{following_user_id}#follower", "SK": f"u#{user_id}"})
    return d_util.update_item(
        {
            "PK": f"u#{following_user_id}",
            "SK": "count",
            "follower#": len(query_follower_list_by_user_id(d_util, following_user_id)),
        }
    )


def query_following_list_by_user_id(d_util, user_id):
    q_param = {
        "KeyConditionExpression": "PK = :PK",
        "ExpressionAttributeValues": {":PK": {"S": f"u#{user_id}#following"}},
    }
    return d_util.query(q_param)
