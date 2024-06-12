from dynamodb_util import *
from datetime import datetime, timezone
import uuid
import pprint


def increase_post(d_util, user_id, content, image_url):
    post_id = str(uuid.uuid4())
    d_util.put_item(
        {
            "PK": f"u#{user_id}#post",
            "SK": f"p#{post_id}",
            "content": content,
            "imageUrl": image_url,
            "timestamp": int(datetime.now(timezone.utc).timestamp()),
        }
    )
    d_util.update_item(
        {
            "PK": f"u#{user_id}",
            "SK": "count",
            "post#": len(query_post_list_by_user_id(d_util, user_id)),
        }
    )

    return increase_timeline_for_followers(d_util, user_id, post_id)


def increase_timeline_for_followers(d_util, user_id, post_id):
    retention_in_days = 30
    ttl = int(datetime.now(timezone.utc).timestamp()) + (
        retention_in_days * 24 * 60 * 60
    )
    for follower in query_follower_list_by_user_id(d_util, user_id):
        follower_id = follower["SK"]
        d_util.put_item(
            {
                "PK": f"{follower_id}#timeline",
                "SK": f"p#{post_id}u#{user_id}",
                "ttl": ttl,
            }
        )


def query_timeline_by_user_id(d_util, user_id):
    q_param = {
        "KeyConditionExpression": "PK = :PK",
        "ExpressionAttributeValues": {":PK": {"S": str(f"u#{user_id}#timeline")}},
    }
    return d_util.query(q_param)


# a2
def query_follower_list_by_user_id(d_util, user_id):
    q_param = {
        "KeyConditionExpression": "PK = :PK",
        "ExpressionAttributeValues": {":PK": {"S": str(f"u#{user_id}#follower")}},
    }
    return d_util.query(q_param)


# a4
def query_post_list_by_user_id(d_util, user_id):
    q_param = {
        "KeyConditionExpression": "PK = :PK",
        "ExpressionAttributeValues": {":PK": {"S": f"u#{user_id}#post"}},
    }
    return d_util.query(q_param)
