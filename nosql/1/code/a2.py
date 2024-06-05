from a1 import *
import pprint


def increase_follower(d_util, user_id, follower_user_id):
    new_user(d_util, {"PK": f"u#{user_id}#follower", "SK": f"u#{follower_user_id}"})
    d_util.update_item(
        {
            "PK": f"u#{user_id}",
            "SK": "count",
            "follower#": len(query_follower_list_by_user_id(d_util, user_id)),
        }
    )

    # increase_following
    from a3 import query_following_list_by_user_id

    new_user(d_util, {"PK": f"u#{follower_user_id}#following", "SK": f"u#{user_id}"})
    return d_util.update_item(
        {
            "PK": f"u#{follower_user_id}",
            "SK": "count",
            "following#": len(
                query_following_list_by_user_id(d_util, follower_user_id)
            ),
        }
    )


def decrease_follower(d_util, user_id, follower_user_id):
    delete_user(d_util, {"PK": f"u#{user_id}#follower", "SK": f"u#{follower_user_id}"})
    d_util.update_item(
        {
            "PK": f"u#{user_id}",
            "SK": "count",
            "follower#": len(query_follower_list_by_user_id(d_util, user_id)),
        }
    )

    # decrease_following
    from a3 import query_following_list_by_user_id

    delete_user(d_util, {"PK": f"u#{follower_user_id}#following", "SK": f"u#{user_id}"})
    return d_util.update_item(
        {
            "PK": f"u#{follower_user_id}",
            "SK": "count",
            "following#": len(
                query_following_list_by_user_id(d_util, follower_user_id)
            ),
        }
    )


def query_follower_list_by_user_id(d_util, user_id):
    q_param = {
        "KeyConditionExpression": "PK = :PK",
        "ExpressionAttributeValues": {":PK": {"S": str(f"u#{user_id}#follower")}},
    }
    return d_util.query(q_param)
