# 인천광역시 미추홀구_어린이보호구역 무인교통단속장비 설치현황
- 공공데이터포털
  - https://www.data.go.kr/data/15071214/fileData.do
- CSV에 제시된 애트리뷰트
  - 관리기관명, 시설명, 설치위치, 단속방향, 설치목적, 카메라대수, 설치연도, 관할경찰청, 관할경찰서, 위도, 경도

## 테이블(1차 정리)
```mermaid
erDiagram
    ManagementAgencies ||--|{ Facilities: has_many
    NationalPoliceAgencies ||--|{ ManagementAgencies: has_many
    PoliceStations ||--|{ ManagementAgencies: has_many
    Facilities ||--|{ CameraLocations: has_many
    NationalPoliceAgencies ||--|{ PoliceStations: has_many
``` 

### 관리기관(ManagementAgencies)
- 종속성
  - 관리기관명 -> 경찰청id, 경찰서id
- 관계
  - 관리기관 ||--{| 시설
  - 관리기관 |}--|| 경찰청
  - 관리기관 |}--|| 경찰서
  - 관리기관 |직접관계없음| 카메라설치위치
  
### 시설(Facilities)
- 종속성
  - 시설명 -> 관리기관id, 설치목적, 카메라대수
- 관계
  - 시설 |}--|| 관리기관
  - 시설 ||--{| 카메라설치위치
  - 시설 |직접관계없음| 경찰청
  - 시설 |직접관계없음| 경찰서

### 카메라설치위치(CameraLocations)
- 종속성
  - 설치위치 -> 시설id, 단속방향, 설치연도, 위도, 경도
- 관계
  - 카메라설치위치 |직접관계없음| 관리기관
  - 카메라설치위치 |}--|| 시설
  - 카메라설치위치 |직접관계없음| 경찰청
  - 카메라설치위치 |직접관계없음| 경찰서

### 경찰청(NationalPoliceAgencies)
- 종속성
  - 경찰청이름
- 관계
  - CSV에는 관리기관이 한군데만 나왔지만, 경찰청이 더 많이 관리할지도 모른다고 생각했다.
  - 경찰청 ||--{| 관리기관
  - 경찰청 |직접관계없음| 시설
  - 경찰청 |직접관계없음| 카메라설치위치
  - 경찰청 ||--{| 경찰서

### 경찰서(PoliceStations)
- 종속성
  - 경찰서이름 -> 경찰청id
- 관계
  - CSV에는 관리기관이 한군데만 나왔지만, 경찰서가 더 많이 관리할지도 모른다고 생각했다.
  - 경찰서 ||--{| 관리기관
  - 경찰서 |직접관계없음| 시설
  - 경찰서 |직접관계없음| 카메라설치위치
  - 경찰서 |}--|| 경찰청


## 1차 정리의 이상현상 검토
- `테이블(1차 정리)` 형태에서 `관리기관명, 시설명, 설치위치, 단속방향, 설치목적, 카메라대수, 설치연도, 관할경찰청, 관할경찰서, 위도, 경도` 항목들을 검토한다.
- 수정이상과 삭제이상이 발생하였다. 수정이 필요하다.

### 삽입이상
- 없음
  - 관리기관명을 추가할때, 경찰청id, 경찰서id를 추가해야 한다. 나머지 2항목은 종속된 항목이라 필요한 추가이다.
  - 시설명을 추가할때, 관리기관id, 설치목적, 카메라대수를 추가해야 한다. 나머지 3항목은 종속된 항목이라 필요한 추가이다.
  - 설치위치를 추가할때, 시설id, 단속방향, 설치연도, 위도, 경도를 추가해야한다. 나머지 5항목은 종속된 항목이라 필요한 추가이다.
  - 시설id, 단속방향, 설치연도, 위도, 경도,을 추가할때, 설치위치를 추가해야한다. 설치위치는 종속의 주체라 필요한 추가이다.
  - 관할경찰청은 이름 항목 하나라 이상이 발생하지 않는다
  - 관할경찰서를 추가할때, 이름, 경찰청id를 추가해야한다. 나머지 1항목은 종속된 항목이라 필요한 추가이다.
### 수정이상
- 없음
  - 관리기관명을 수정할때, 여러 레코드를 수정하지 않아도 된다.
  - 시설명을 수정할때, 여러 레코드를 수정하지 않아도 된다.
  - 설치위치를 수정할때, 여러 레코드를 수정하지 않아도 된다.
  - 카메라대수를 수정할때, 여러 레코드를 수정하지 않아도 된다.
    - 2대 같이 레코드에 같은값이 여러번 나타날수있다. 하지만 카메라대수는 해당 레코드만의 값이기 때문에 수정이상이라고 보기 어렵다.
  - 설치연도를 수정할때, 여러 레코드를 수정하지 않아도 된다.
    - 2020같이 레코드에 같은값이 여러번 나타날수있다. 하지만 설치연도 수정은 해당 레코드만의 값이기 때문에 수정이상이라고 보기 어렵다.
  - 관할경찰청를 수정할때, 여러 레코드를 수정하지 않아도 된다.
  - 관할경찰서를 수정할때, 여러 레코드를 수정하지 않아도 된다.
  - 위도를 수정할때, 여러 레코드를 수정하지 않아도 된다.
    - 37.222같이 같이 레코드에 같은값이 여러번 나타날수있다. 하지만 위도는 해당 레코드만의 값이기 때문에 수정이상이라고 보기 어렵다. 
  - 경도를 수정할때, 여러 레코드를 수정하지 않아도 된다.
    - 126.666같이 같이 레코드에 같은값이 여러번 나타날수있다. 하지만 경도는 해당 레코드만의 값이기 때문에 수정이상이라고 보기 어렵다. 
- 있음
  - 단속방향을 수정할때, 여러 레코드를 수정해야한다. 도로1의 왼쪽은 초등학교A이고 오른쪽이 초등학교B일 경우 같은 단속방향인 레코드가 여러개 생긴다.
  - 설치목적을 수정할때, 여러 레코드를 수정해야한다. `신호·과속단속` 이 여러번 나타나는데 이걸 `신호 and 과속단속` 으로 바꾸면 전부 일일이 수정해야한다.

### 삭제이상
- 없음
  - 관리기관 테이블의 레코드를 삭제하면, 관리기관명만 삭제된다. 이상없다
  - 경찰청 테이블의 레코드를 삭제하면, 이름만 삭제된다. 이상없다.
  - 경찰서 테이블의 레코드를 삭제하면, 이름만 삭제된다. 이상없다.
- 있음
  - 시설 테이블의 레코드를 삭제하면, 시설명, 관리기관id, 설치목적, 카메라대수가 삭제된다. 시설명, 관리기관id, 카메라대수은 레코드 고유값이기 때문에 문제가 없지만, 설치목적은 이상이 발생한다.
    - 레코드1에 설치목적 `신호단속` 이 유일하게 존재했다면, 시설명만 삭제하려고 했는데 의도치않게 설치목적의 유일한 값을 지우게 된다.
  - 카메라설치위치 테이블의 레코드를 삭제하면, 설치위치 ,시설id, 단속방향, 설치연도, 위도, 경도가 삭제된다. 설치위치 ,시설id, 설치연도, 위도, 경도는 레코드 고유값이기 때문에 문제가 없지만, 단속방향은 이상이 발생한다.
    - 레코드1에 단속방향 `도화IC→도화사거리` 이 유일하게 존재했다면, 설치위치만 삭제하려고 했는데 의도치않게 단속방향의 유일한 값을 지우게 된다.

## 테이블(2차 정리)
```mermaid
erDiagram
    ManagementAgencies ||--|{ Facilities: has_many
    NationalPoliceAgencies ||--|{ ManagementAgencies: has_many
    PoliceStations ||--|{ ManagementAgencies: has_many
    ManagementAgencies ||--|{ Facilities: has_many
    Facilities ||--|{ CameraLocations: has_many
    PurposeOfCameraInstallations ||--|{ Facilities: has_many
    NationalPoliceAgencies ||--|{ PoliceStations: has_many
    WhichDirections ||--|{ CameraLocations: has_many
``` 

### 관리기관(ManagementAgencies)
- 종속성
  - 관리기관명 -> 경찰청id, 경찰서id
- 관계
  - 관리기관 ||--{| 시설
  - 관리기관 |직접관계없음| 카메라설치목적
  - 관리기관 |직접관계없음| 카메라설치위치
  - 관리기관 |직접관계없음| 카메라단속방향
  - 관리기관 |}--|| 경찰청
  - 관리기관 |}--|| 경찰서

### 시설(Facilities)
- 종속성
  - 시설명 -> 관리기관id, 카메라설치목적id, 카메라대수
- 관계
  - 시설 |}--|| 관리기관
  - 시설 |}--|| 카메라설치목적
  - 시설 ||--{| 카메라설치위치
  - 시설 |직접관계없음| 카메라단속방향
  - 시설 |직접관계없음| 경찰청
  - 시설 |직접관계없음| 경찰서

### 카메라설치목적(PurposeOfCameraInstallations)
- 종속성
  - 설치목적
- 관계
  - 카메라설치목적 |직접관계없음| 관리기관
  - 카메라설치목적 ||--{| 시설
  - 카메라설치목적 |직접관계없음| 카메라설치위치
  - 카메라설치목적 |직접관계없음| 카메라단속방향
  - 카메라설치목적 |직접관계없음| 경찰청
  - 카메라설치목적 |직접관계없음| 경찰서

### 카메라설치위치(CameraLocations)
- 종속성
  - 설치위치 -> 시설id, 카메라단속방향id, 설치연도, 위도, 경도
- 관계
  - 카메라설치위치 |직접관계없음| 관리기관
  - 카메라설치위치 |}--|| 시설
  - 카메라설치위치 |직접관계없음| 카메라설치목적
  - 카메라설치위치 |}--|| 카메라단속방향
  - 카메라설치위치 |직접관계없음| 경찰청
  - 카메라설치위치 |직접관계없음| 경찰서

### 카메라단속방향(WhichDirections)
- 종속성
  - 단속방향
- 관계
  - 카메라단속방향 |직접관계없음| 관리기관
  - 카메라단속방향 |직접관계없음| 시설
  - 카메라단속방향 |직접관계없음| 카메라설치목적
  - 카메라단속방향 ||--{| 카메라설치위치
  - 카메라단속방향 |직접관계없음| 경찰청
  - 카메라단속방향 |직접관계없음| 경찰서

### 경찰청(NationalPoliceAgencies)
- 종속성
  - 경찰청이름
- 관계
  - CSV에는 관리기관이 한군데만 나왔지만, 경찰청이 더 많이 관리할지도 모른다고 생각했다.
  - 경찰청 ||--{| 관리기관
  - 경찰청 |직접관계없음| 시설
  - 경찰청 |직접관계없음| 카메라설치목적
  - 경찰청 |직접관계없음| 카메라설치위치
  - 경찰청 |직접관계없음| 카메라단속방향
  - 경찰청 ||--{| 경찰서

### 경찰서(PoliceStations)
- 종속성
  - 경찰서이름 -> 경찰청id
- 관계
  - CSV에는 관리기관이 한군데만 나왔지만, 경찰서가 더 많이 관리할지도 모른다고 생각했다.
  - 경찰서 ||--{| 관리기관
  - 경찰서 |직접관계없음| 시설
  - 경찰서 |직접관계없음| 카메라설치목적
  - 경찰서 |직접관계없음| 카메라설치위치
  - 경찰서 |직접관계없음| 카메라단속방향
  - 경찰서 |}--|| 경찰청

## 2차 정리의 이상현상 검토
### 삽입이상
- 생략
### 수정이상
- 있음
  - 카메라설치위치 테이블의 단속방향 항목을 카메라단속방향 테이블로 분리해서 해소했다.
  - 시설 테이블의 설치목적 항목을 카메라설치목적 테이블로 분리해서 해소했다.

## Rails 명령어
### 초기 설정에 사용했던 명령어
```
cd $REPOSITORY_ROOT/r_15071214
rails new . -d postgresql
# Gemfile에 gem 'rspec-rails', '~> 6.0.0' 추가
bundle config set --local path './vendor'
bundle install
bundle exec rails generate rspec:install
bundle exec rails db:create db:migrate
```

### model과 migration파일 작성할때 사용했던 명령어
```
cd $REPOSITORY_ROOT/r_15071214
# 경찰청(NationalPoliceAgencies)
bundle exec rails generate model NationalPoliceAgency name:string
# 경찰서(PoliceStations)
bundle exec rails generate model PoliceStation name:string national_police_agency:belongs_to
# 관리기관(ManagementAgencies)
bundle exec rails generate model ManagementAgency name:string national_police_agency:belongs_to:uniq police_station:belongs_to:uniq
# 카메라설치목적(PurposeOfCameraInstallations)
bundle exec rails generate model PurposeOfCameraInstallation purpose:string
# 시설(Facilities)
bundle exec rails generate model Facility name:string management_agency:belongs_to purpose_of_camera_installation:belongs_to number_of_cameras:integer
# 카메라단속방향(WhichDirections)
bundle exec rails generate model WhichDirection direction:string
# 카메라설치위치(CameraLocations)
bundle exec rails generate model CameraLocation location:string facility:belongs_to which_direction:belongs_to installation_year:integer latitude:float longitude:float
```

### rspec 실행 명령어
```
cd $REPOSITORY_ROOT/r_15071214
bundle exec rspec --format documentation
```