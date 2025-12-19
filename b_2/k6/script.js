import http from 'k6/http';

// 테스트 설정 (가상 유저 10명이 30초 동안 테스트)
export const options = {
  vus: 10,        // Virtual Users: 동시에 접속하는 유저 수
  duration: '30s', // 테스트 지속 시간
};

export default function () {
  // 1. 요청 보낼 주소
  const url = 'http://192.168.33.16:3000/projects/2/sensors/1/sensor_data';

  // 2. 보낼 데이터 (JSON.stringify 필수)
  const payload = JSON.stringify({
    sensor_datum: {
      data: {
        temperature: 24.5,
        humidity: 60,
        status: "active",
        errors: ["e1", "e2"]
      }
    }
  });

  // 3. 헤더 설정
  const params = {
    headers: {
      'Content-Type': 'application/json',
    },
  };

  // 4. POST 요청 전송
  http.post(url, payload, params);
}