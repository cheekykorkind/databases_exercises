import pytest
import json
from a1 import *
from a2 import *
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
                "name": "hyuklee",
                "content": "My name is Hyuk Lee",
                "imageUrl": "s3://image1",
            },
            200,
        ),
    ],
)
def test_new_user1(d_util, serialized_item, expected):
    assert (
        new_user(d_util, serialized_item).get("ResponseMetadata").get("HTTPStatusCode")
        == expected
    )


@pytest.mark.parametrize(
    "d_util, user_id, expected",
    [
        (
            DynamodbUtil(table_name="user"),
            10000,
            [],
        ),
    ],
)
def test_query_follower_list_by_user_id(d_util, user_id, expected):
    assert query_follower_list_by_user_id(d_util, user_id) == expected


@pytest.mark.parametrize(
    "d_util, user_id, follower_user_id, expected",
    [
        (
            DynamodbUtil(table_name="user"),
            10000,
            20000,
            {
                "new_pks": [
                    {
                        "PK": "u#10000#follower",
                        "SK": "u#20000",
                    },
                ],
                "updated_follower#": 1,
            },
        ),
        (
            DynamodbUtil(table_name="user"),
            10000,
            20001,
            {
                "new_pks": [
                    {
                        "PK": "u#10000#follower",
                        "SK": "u#20001",
                    },
                    {
                        "PK": "u#10000#follower",
                        "SK": "u#20000",
                    },
                ],
                "updated_follower#": 2,
            },
        ),
    ],
)
def test_query_follower_list_by_user_id(d_util, user_id, follower_user_id, expected):
    update_follower(d_util, user_id, follower_user_id)
    assert query_follower_list_by_user_id(d_util, user_id) == expected.get("new_pks")
    assert query_user_info_by_user_id_and_sk(d_util, user_id, sk="count")[0].get(
        "follower#"
    ) == expected.get("updated_follower#")
