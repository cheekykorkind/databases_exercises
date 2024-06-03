import os
import sys

# sys.pathに $REPOSITORY_ROOT/nosql/1/code 를 추가해둠
code_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(code_dir)
