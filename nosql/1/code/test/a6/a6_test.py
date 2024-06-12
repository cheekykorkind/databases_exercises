from a4 import *
from a6 import *

import pytest
from unittest.mock import patch
from freezegun import freeze_time

import pprint
from datetime import datetime, timezone


@pytest.mark.parametrize(
    "d_util, serialized_item, expected",
    [
        (
            DynamodbUtil(table_name="user"),
            {
                "PK": f"u#10000",
                "SK": "count",
                "follower#": 0,
                "following#": 0,
                "post#": 0,
            },
            200,
        ),
        (
            DynamodbUtil(table_name="user"),
            {
                "PK": f"u#10000",
                "SK": "info",
                "name": "u10000",
                "content": "My name is u10000",
                "imageUrl": "s3://image1",
            },
            200,
        ),
    ],
)
def test_one_user(d_util, serialized_item, expected):
    assert (
        new_user(d_util, serialized_item).get("ResponseMetadata").get("HTTPStatusCode")
        == expected
    )


@pytest.mark.parametrize(
    "d_util, user_id, content, image_url, expected",
    [
        (
            DynamodbUtil(table_name="user"),
            10000,
            "content1",
            "image_url1",
            {
                "post": {
                    "list": [
                        {
                            "PK": "u#10000#post",
                            "SK": "p#t-uuid-1",
                            "content": "content1",
                            "imageUrl": "image_url1",
                            "timestamp": 1717686000,
                        }
                    ],
                    "count": 1,
                }
            },
        )
    ],
)
def test_one_post(d_util, user_id, content, image_url, expected):
    module_name = "a4"
    with freeze_time(
        datetime(2024, 6, 6, 15, 0, 0, tzinfo=timezone.utc)
    ) as frozen_time, patch(f"{module_name}.uuid") as u1:
        u1.uuid4.return_value = "t-uuid-1"
        increase_post(d_util, user_id, content, image_url)


@pytest.mark.parametrize(
    "d_util, user_id, post_id, expected",
    [
        (
            DynamodbUtil(table_name="user"),
            10000,
            "t-uuid-1",
            1,
        ),
    ],
)
def test_increase_like_count(d_util, user_id, post_id, expected):
    increase_like_count(d_util, user_id, post_id)
    assert get_like_count_by_post_id(d_util, post_id)["etc"] == expected


@pytest.mark.parametrize(
    "d_util, user_id, post_id, expected",
    [
        (
            DynamodbUtil(table_name="user"),
            10000,
            10000,
            0,
        )
    ],
)
def test_decrease_like_count(d_util, user_id, post_id, expected):
    decrease_like_count(d_util, user_id, post_id)
    assert get_like_count_by_post_id(d_util, post_id)["etc"] == expected
