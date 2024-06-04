import os
import sys

# sys.pathに $REPOSITORY_ROOT/nosql/1/code 를 추가해둠
code_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(code_dir)


from a1 import *
from a2 import *

# pytest커멘드 실행이 끝나면 dynamodb의 모든 record를 삭제
def pytest_sessionfinish(session, exitstatus):
    d_util = DynamodbUtil(table_name="user")
    for record in d_util.scan():
        d_util.delete_item({"PK": record.get("PK"), "SK": record.get("SK")})