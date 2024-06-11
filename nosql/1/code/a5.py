from dynamodb_util import *
from a1 import *
import pprint


def increase_like(d_util, user_id, post_id):
    def exist_post_id(d_util, post_id):
        return len(d_util.scan_with_sk_filter(f"p#{post_id}")) > 0

    def exist_user_id(d_util, user_id):
        return len(query_user_info_by_user_id(d_util, user_id)) > 0

    if not exist_post_id(d_util, post_id) or not exist_user_id(d_util, user_id):
        return None
    d_util.put_item({"PK": f"p#{post_id}#likelist", "SK": f"u#{user_id}"})

    return d_util.update_item(
        {
            "PK": f"p#{post_id}#likecount",
            "SK": "count",
            "etc": len(query_user_like_by_post_id(d_util, post_id)),
        }
    )


def decrease_like(d_util, user_id, post_id):
    d_util.delete_item({"PK": f"p#{post_id}#likelist", "SK": f"u#{user_id}"})
    return d_util.update_item(
        {
            "PK": f"p#{post_id}#likecount",
            "SK": "count",
            "etc": len(query_user_like_by_post_id(d_util, post_id)),
        }
    )


def query_user_like_by_post_id(d_util, post_id):
    q_param = {
        "KeyConditionExpression": "PK = :PK",
        "ExpressionAttributeValues": {":PK": {"S": f"p#{post_id}#likelist"}},
    }
    return d_util.query(q_param)
