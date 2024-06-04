import pytest
import json
from a1 import *
import pprint


@pytest.mark.parametrize(
    "d_util, deserialized_item, expected",
    [
        (
            DynamodbUtil(table_name="user"),
            {
                "PK": f"u#1",
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
                "PK": f"u#1",
                "SK": "info",
                "name": "hyuklee",
                "content": "My name is Hyuk Lee",
                "imageUrl": "s3://image1",
            },
            200,
        ),
    ],
)
def test_new_user(d_util, deserialized_item, expected):
    assert (
        new_user(d_util, deserialized_item)
        .get("ResponseMetadata")
        .get("HTTPStatusCode")
        == expected
    )


@pytest.mark.parametrize(
    "d_util, user_id, expected",
    [
        (
            DynamodbUtil(table_name="user"),
            1,
            [
                {
                    "PK": "u#1",
                    "SK": "info",
                    "content": "My name is Hyuk Lee",
                    "imageUrl": "s3://image1",
                    "name": "hyuklee",
                },
                {
                    "PK": "u#1",
                    "SK": "count",
                    "follower#": Decimal("0"),
                    "following#": Decimal("0"),
                    "post#": Decimal("0"),
                },
            ],
        )
    ],
)
def test_query_user_info_by_user_id(d_util, user_id, expected):
    assert query_user_info_by_user_id(d_util, user_id) == expected


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
                },
                {
                    "PK": "u#1",
                    "SK": "info",
                    "content": "My name is Hyuk Lee",
                    "imageUrl": "s3://image1",
                    "name": "hyuklee",
                },
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
                },
                {
                    "PK": "u#1",
                    "SK": "info",
                    "content": "My name is Hyuk Lee",
                    "imageUrl": "s3://image1",
                    "name": "hyuklee",
                },
            ],
        )
    ],
)
def test_update_item(d_util, deserialized_item, expected):
    update_user(d_util, deserialized_item)
    assert d_util.scan() == expected


@pytest.mark.parametrize(
    "d_util, deserialized_pk_sk, expected",
    [
        (
            DynamodbUtil(table_name="user"),
            {"PK": "u#1", "SK": "count"},
            [
                {
                    "PK": "u#1",
                    "SK": "info",
                    "content": "My name is Hyuk Lee",
                    "imageUrl": "s3://image1",
                    "name": "hyuklee",
                }
            ],
        ),
        (
            DynamodbUtil(table_name="user"),
            {"PK": "u#1", "SK": "info"},
            [],
        ),
    ],
)
def test_delete_user(d_util, deserialized_pk_sk, expected):
    delete_user(d_util, deserialized_pk_sk)
    assert d_util.scan() == expected
