# 게임 프로필 비즈니스 사용 사례

# 요구사항
- 사용자의 친구 목록 가져오기
  - a1
- 플레이어의 모든 정보 가져오기
  - a2
- 사용자의 아이템 목록 가져오기
  - a3
- 사용자의 아이템 목록에서 특정 아이템 가져오기
  - a4
- 사용자 캐릭터 업데이트
  - a5
- 사용자의 아이템 개수 업데이트
  - a6


# 메모
DynamoDB로 구현한다


# 감상
NoSQL은 AWS DynamoDB을 의미합니다.
## Query결과를 정렬하는 옵션은 ScanIndexForward
- 정렬 키의 데이터 형식이 Number이면 결과가 숫자 순서대로 반환됩니다. 그렇지 않으면 결과가 UTF-8 바이트 순서로 반환됩니다.
- 기본 정렬은 오름차순입니다. 역순으로 바꾸려면 ScanIndexForward 파라미터를 false로 설정하면 됩니다.

## Query결과가 1MB를 넘어가면?
### 1MB제한이 있습니다.
```
단일 Query 작업은 최대 1MB의 데이터를 가져올 수 있습니다. 이러한 크기 제한은 FilterExpression 또는 ProjectionExpression이 결과에 반영되기 전에 적용됩니다.
```
- https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.FilterExpression.html

### 페이지네이터를 사용해서 Query결과를 전부 취득할 수 있습니다.
- https://docs.aws.amazon.com/ko_kr/amazondynamodb/latest/developerguide/programming-with-python.html#programming-with-python-pagination

### AWS의 1MB란?
- 1MB = 1,000,000 bytes
  - https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#mebibyte

## Query의 FilterExpression vs KeyConditionExpression
### KeyConditionExpression은?
- KeyConditionExpression은 partition key와 sort key에 적용된다.
  - https://docs.aws.amazon.com/ko_kr/amazondynamodb/latest/developerguide/Query.KeyConditionExpressions.html
- expression에 사용가능한 문법들
  - https://docs.aws.amazon.com/ko_kr/amazondynamodb/latest/developerguide/Expressions.OperatorsAndFunctions.html

### FilterExpression은?
- KeyConditionExpression의 결과를 좀더 좁히고 싶을때
  - https://docs.aws.amazon.com/ko_kr/amazondynamodb/latest/developerguide/Query.FilterExpression.html
- expression에 사용가능한 문법들
  - https://docs.aws.amazon.com/ko_kr/amazondynamodb/latest/developerguide/Expressions.OperatorsAndFunctions.html
