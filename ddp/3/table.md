# 테이블
- package 테이블(객실 패키지)
  - id
  - 이름
  - 기간
  - 가격
  - 설명

- package_category 테이블(객실 패키지 검색의 '유형 구분')
  - id
  - 이름

- package_package_category
  - id
  - package_id
  - package_category_id

- package_keyword 테이블(객실 패키지 검색의 '키워드')
  - id
  - 이름

- package_package_keyword
  - id
  - package_id
  - package_keyword_id

- event 테이블
  - id
  - 이름
  - 기간
  - 가격
  - 설명

- room_info 테이블(객실의 디럭스, 코너 스위트 같은 이름)
  - id
  - 이름
  - 소개
  - 크기
  - 전망
  - 침대타입
  - 욕실

- room_category 테이블(스탠다드, 이그제큐티브, 스위트)
  - id
  - 이름

- room_info_room_category 테이블
  - id
  - room_info_id
  - room_category_id

- photo 테이블
  - id
  - 이름
  - 파일위치

- photo_room_category 테이블(photo테이블은 객실 사진말고 모든 사진이 있음)
  - id
  - photo_id
  - room_category_id

- room_category_package 테이블(객실 종류에 맞춰서 패키지를 보여준다)
  - id
  - room_category_id
  - package_id

- room 테이블(101호실 같은 객실의 번호를 관리합니다)
  - id
  - 객실 번호
  - room_info_id

- 예약 테이블
  - id
  - 예약 날짜
  - 인원
  - 신라 리워즈 id(예약한 사람)
  - room_info_id(선택한 객실 상세 정보)

- 신라 리워즈 테이블(회원)
  - id
  - 가입자 이름
  - 가입자 정보
  - 신라 리워즈 등급 id

- 신라 리워즈 등급 테이블(브라운, 실버, 골드, 다이아몬드)
  - id
  - 이름

# 요건 
- 메인 page에서 객실 패키지를 3개씩 보여준다
- 메인 page에서 이벤트를 3개씩 보여준다
- 객실 패키지 page에서 패키지를 나열해야 한다
- 객실 패키지 page에서 기간, 유형 구분, 키워드로 검색 가능해야한다
- 객실 상세 page에서 객실 종류에 따라서 객실 패키지를 보여준다
- 객실 예약이 가능해야 한다
- 이벤트 page에서 이벤트를 나열해야 한다
- 전체 객실 보기 page에서 객실 이름, 객실수, 크기, 전망, 침대타입, 욕실을 보여준다
  - 객실 개수가 있다는건 모든 호실의 정보를 관리해야 한다
- 쇼핑 -> 아케이드 page에서 매장명, 전화번호, 매장종류를 1F와 B1F로 보여준다
- 갤러리 page에서 전체, 객실, 다이닝, 라이프 스타일, 웨딩 & 연회, 기타를 필터링해서 보여줄 수 있어야 한다
- 신라리워즈 -> 회원특전 page에서 회원 등급, 등급별 혜택(서울 신라호텔, 제주 신라호텔, 신라 스테이, 신라모노그램 다낭 따로), 비고 를 보여준다