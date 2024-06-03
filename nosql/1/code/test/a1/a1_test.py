import pytest
import json
from a1 import *
import pprint

module_name = "a1"


@pytest.mark.parametrize(
    "d_util, user_id, expected",
    [
        (
            DynamodbUtil(table_name="user"),
            1,
            200,
        )
    ],
)
def test_new_user(d_util, user_id, expected):
    assert (
        new_user(d_util, user_id).get("ResponseMetadata").get("HTTPStatusCode")
        == expected
    )


@pytest.mark.parametrize(
    "d_util, expected",
    [
        (
            DynamodbUtil(table_name="user"),
            [
                {
                    "PK": "u#1",
                    "SK": "count",
                    "follower#": Decimal("0"),
                    "following#": Decimal("0"),
                    "post#": Decimal("0"),
                }
            ],
        )
    ],
)
def test_scan_user(d_util, expected):
    assert d_util.scan() == expected


@pytest.mark.parametrize(
    "d_util, deserialized_item, expected",
    [
        (
            DynamodbUtil(table_name="user"),
            {
                "PK": "u#1",
                "SK": "count",
                "follower#": Decimal("12"),
                "following#": Decimal("34"),
                "post#": Decimal("56"),
            },
            [
                {
                    "PK": "u#1",
                    "SK": "count",
                    "follower#": Decimal("12"),
                    "following#": Decimal("34"),
                    "post#": Decimal("56"),
                }
            ],
        )
    ],
)
def test_update_item(d_util, deserialized_item, expected):
    update_user(d_util, deserialized_item)
    assert d_util.scan() == expected
