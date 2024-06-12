# 요구사항
- 주어진 userID의 사용자 정보 가져오기
  - a1
- 주어진 userID의 팔로워 목록 가져오기
  - a2
- 주어진 userID가 팔로우하는 사용자 목록 가져오기
  - a3
- 주어진 userID의 게시물 목록 가져오기
  - a4
- 주어진 postID의 게시물을 좋아하는 사용자 목록 가져오기
  - a5
- 주어진 postID의 좋아요 개수 가져오기
  - a6
- 주어진 userID의 타임라인 가져오기
  - a7

# 용어
## 사용자
시스템의 사용자

## 팔로워
사용자1을 팔로우하는 사용자2가 있을때 사용자2를 팔로워라고 한다

## 팔로우하는 사용자
사용자1이 사용자2를 팔로우하면, 사용자1이 팔로우하는 사용자이다

## 게시물
사용자가 등록한 글

## 게시물을 좋아하는 사용자
게시물에 대해서 좋아요를 남긴 사용자

## 좋아요
게시물이 마음에 들면 좋아요를 남길수 있다

## 타임라인
사용자의 대쉬보드에 최신순으로 게시물을 보여주는 곳

# 메모
localstack에서 작업한다
DynamoDB로 구현한다
브라우저에서 상호작용하는 내용을 python 함수로 표한한다 

# 감상
NoSQL은 AWS DynamoDB을 의미합니다.
- NoSQL로 설계할때는 RDBMS로 설계할때보다 구체적으로 설계해야한다
  - 요건정의 단계에서 RDBMS는 테이블을 만들고, 테이블 간의 관계를 정의하면 크게 문제가 없다고 생각한다. 왜냐하면, SQL을 사용하기 때문에 유연하게 데이터를 조작할 수 있기때문이다.
  - 반면에 NoSQL은 요건정의 단계에서 수집한 요건들을 테이블로 만들어보고 어떤 형태로 CRUD할지 구체적으로 확인해야 한다. 왜냐하면, 검색은 primary key, sork key, GSI, LSI만 가능하고 RDBMS의 SQL에 비해 제약이 있기때문이다
- DynamoDB의 이점으로 대규모, 고성능이라고 하지만, WCU와 RCU라는 제한이 있기때문에 요건정의에서 신중해야한다.
  - https://aws.amazon.com/ko/dynamodb/?nc1=h_ls
- RDBMS의 Transaction기능이 없는것을 기억하자
  - AWS Dynamodb는 Transaction 비슷한 기능이 있기는 하다. 다만 크기나 갯수 제한이 있다. RDBMS인 PostgreSQL과 비교하면 주의해야 한다고 생각한다.
  - https://docs.aws.amazon.com/ko_kr/amazondynamodb/latest/developerguide/transaction-apis.html
  - RDBMS인 PostgreSQL은 Transaction은 크기나 갯수 제한에 대한 언급이 없다. 
    - https://www.postgresql.org/docs/current/limits.html
    - https://www.postgresql.org/docs/current/tutorial-transactions.html
    - https://www.postgresql.org/docs/current/transactions.html