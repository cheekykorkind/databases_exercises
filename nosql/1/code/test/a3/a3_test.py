import pytest
import json
from a1 import *
from a2 import *
from a3 import *
import pprint


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
        (
            DynamodbUtil(table_name="user"),
            {
                "PK": f"u#20000",
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
                "PK": f"u#20000",
                "SK": "info",
                "name": "u20000",
                "content": "My name is u20000",
                "imageUrl": "s3://image2",
            },
            200,
        ),
        (
            DynamodbUtil(table_name="user"),
            {
                "PK": f"u#30000",
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
                "PK": f"u#30000",
                "SK": "info",
                "name": "u30000",
                "content": "My name is u30000",
                "imageUrl": "s3://image3",
            },
            200,
        ),
    ],
)
def test_three_user(d_util, serialized_item, expected):
    assert (
        new_user(d_util, serialized_item).get("ResponseMetadata").get("HTTPStatusCode")
        == expected
    )


@pytest.mark.parametrize(
    "d_util, user_id, following_user_id, expected",
    [
        (
            DynamodbUtil(table_name="user"),
            10000,
            20000,
            {
                "following": {
                    "list": [
                        {
                            "PK": "u#10000#following",
                            "SK": "u#20000",
                        }
                    ],
                    "count": 1,
                },
                "follower": {
                    "list": [
                        {
                            "PK": "u#20000#follower",
                            "SK": "u#10000",
                        }
                    ],
                    "count": 1,
                },
            },
        )
    ],
)
def test_increase_u10000s_following_count(d_util, user_id, following_user_id, expected):
    increase_following(d_util, user_id, following_user_id)

    assert (
        query_following_list_by_user_id(d_util, user_id)
        == expected["following"]["list"]
    )
    assert (
        query_user_info_by_user_id_and_sk(d_util, user_id, sk="count")[0]["following#"]
        == expected["following"]["count"]
    )
    assert (
        query_follower_list_by_user_id(d_util, following_user_id)
        == expected["follower"]["list"]
    )
    assert (
        query_user_info_by_user_id_and_sk(d_util, following_user_id, sk="count")[0][
            "follower#"
        ]
        == expected["follower"]["count"]
    )


@pytest.mark.parametrize(
    "d_util, user_id, following_user_id, expected",
    [
        (
            DynamodbUtil(table_name="user"),
            10000,
            20000,
            {
                "following": {"list": [], "count": 0},
                "follower": {"list": [], "count": 0},
            },
        )
    ],
)
def test_decrease_u10000s_following_count(d_util, user_id, following_user_id, expected):
    decrease_following(d_util, user_id, following_user_id)

    assert (
        query_following_list_by_user_id(d_util, user_id)
        == expected["following"]["list"]
    )
    assert (
        query_user_info_by_user_id_and_sk(d_util, user_id, sk="count")[0]["following#"]
        == expected["following"]["count"]
    )
    assert (
        query_follower_list_by_user_id(d_util, following_user_id)
        == expected["follower"]["list"]
    )
    assert (
        query_user_info_by_user_id_and_sk(d_util, following_user_id, sk="count")[0][
            "follower#"
        ]
        == expected["follower"]["count"]
    )
