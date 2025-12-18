# 커멘드 기록
bundle exec rails db:create db:migrate
bundle exec rails s -b 0.0.0.0

# 1. Project 생성 (이름과 메모 모두 문자열)
bundle exec rails g scaffold Project name:string memo:string

# 2. Sensor 생성 (Project에 소속됨)
bundle exec rails g scaffold Sensor project:references name:string

# 3. SensorData 생성 (Sensor에 소속됨, 데이터는 JSON 타입)
bundle exec rails g scaffold SensorData sensor:references data:json

# 4. 데이터베이스 마이그레이션 적용
bundle exec rails db:migrate

# curl
curl -X POST http://192.168.33.16:3000/projects \
  -H "Content-Type: application/json" \
  -d '{
    "project": {
      "name": "p1",
      "memo": "p1memo1"
    }
  }'

curl http://192.168.33.16:3000/projects/1


curl -X PATCH http://192.168.33.16:3000/projects/1 \
  -H "Content-Type: application/json" \
  -d '{
    "project": {
      "name": "p1edit1",
      "memo": "p1memo1edit1"
    }
  }'

curl -X DELETE http://192.168.33.16:3000/projects/1


curl -X GET http://192.168.33.16:3000/projects/2/sensors

curl -X POST http://192.168.33.16:3000/projects/2/sensors \
  -H "Content-Type: application/json" \
  -d '{
    "sensor": {
      "name": "sensor1"
    }
  }'
curl -X PATCH http://192.168.33.16:3000/projects/2/sensors/1 \
  -H "Content-Type: application/json" \
  -d '{
    "sensor": {
      "name": "sensor1edit"
    }
  }'


curl -X GET http://192.168.33.16:3000/projects/2/sensors/1/sensor_data

curl -X POST http://192.168.33.16:3000/projects/2/sensors/1/sensor_data \
  -H "Content-Type: application/json" \
  -d '{
    "sensor_datum": {
      "data": {
        "temperature": 24.5,
        "humidity": 60,
        "status": "active",
        "errors": ["e1", "e2"]
      }
    }
  }'

curl -X PATCH http://192.168.33.16:3000/projects/2/sensors/1/sensor_data/1 \
  -H "Content-Type: application/json" \
  -d '{
    "sensor_datum": {
      "data": {
        "temperature": 34.5,
        "humidity": 70,
        "status": "active",
        "errors": ["e3"]
      }
    }
  }'

curl -X DELETE http://192.168.33.16:3000/projects/2/sensors/1/sensor_data/2
