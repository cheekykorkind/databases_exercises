from a1 import *
from a2 import *
import uuid
import pprint
from datetime import datetime, timezone


def increase_post(d_util, user_id, content, image_url):
    d_util.put_item(
        {
            "PK": f"u#{user_id}#post",
            "SK": f"p#{str(uuid.uuid4())}",
            "content": content,
            "imageUrl": image_url,
            "timestamp": int(datetime.now(timezone.utc).timestamp()),
        }
    )

    return d_util.update_item(
        {
            "PK": f"u#{user_id}",
            "SK": "count",
            "post#": len(query_post_list_by_user_id(d_util, user_id)),
        }
    )


def decrease_following(d_util, user_id, post_id):
    d_util.delete_item({"PK": f"u#{user_id}#post", "SK": f"p#{post_id}"})
    return d_util.update_item(
        {
            "PK": f"u#{user_id}",
            "SK": "count",
            "post#": len(query_post_list_by_user_id(d_util, user_id)),
        }
    )


def query_post_list_by_user_id(d_util, user_id):
    q_param = {
        "KeyConditionExpression": "PK = :PK",
        "ExpressionAttributeValues": {":PK": {"S": f"u#{user_id}#post"}},
    }
    return d_util.query(q_param)
