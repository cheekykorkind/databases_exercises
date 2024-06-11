from a1 import *
from a2 import *
from a7 import *

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
    "d_util, user_id, follower_user_id, expected",
    [
        (
            DynamodbUtil(table_name="user"),
            10000,
            20000,
            {},
        )
    ],
)
def test_one_follower(d_util, user_id, follower_user_id, expected):
    increase_follower(d_util, user_id, follower_user_id)


@pytest.mark.parametrize(
    "d_util, user_id, content, image_url, expected",
    [
        (
            DynamodbUtil(table_name="user"),
            10000,
            "content1",
            "image_url1",
            {
                "timeline": {
                    "list": [
                        {
                            "PK": "u#20000#timeline",
                            "SK": "p#t-uuid-1u#10000",
                            "ttl": Decimal("1720278000"),
                        }
                    ]
                }
            },
        )
    ],
)
def test_increase_timeline_for_followers(d_util, user_id, content, image_url, expected):
    module_name = "a7"
    with freeze_time(
        datetime(2024, 6, 6, 15, 0, 0, tzinfo=timezone.utc)
    ) as frozen_time, patch(f"{module_name}.uuid") as u1:
        u1.uuid4.return_value = "t-uuid-1"
        increase_post(d_util, user_id, content, image_url)
        follower_id = query_follower_list_by_user_id(d_util, user_id)[0]["SK"].replace(
            "u#", ""
        )
        assert (
            query_timeline_by_user_id(d_util, follower_id)
            == expected["timeline"]["list"]
        )
