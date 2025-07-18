import requests
import time
from requests.exceptions import RequestException, Timeout, HTTPError

# 1. 요청할 URL과 헤더 설정
url = "https://namu.wiki/w/%EB%82%98%EB%AC%B4%EC%9C%84%ED%82%A4:%EB%8C%80%EB%AC%B8"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Connection": "keep-alive"
}

# 2. 요청 함수 정의 (예외 처리 포함)
def fetch_html(url, headers, retries=3, timeout=10):
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()  # 4xx, 5xx 에러 시 예외 발생
            print("✅ 요청 성공:", response.status_code)
            return response.text  # 혹은 response.content
        except Timeout:
            print(f"⏰ 타임아웃 발생, 재시도 ({attempt + 1}/{retries})")
        except HTTPError as e:
            print(f"❌ HTTP 오류 발생: {e}")
            break
        except RequestException as e:
            print(f"⚠️ 기타 요청 오류: {e}")
            time.sleep(2)  # 잠시 대기 후 재시도
    print("🚫 최종 실패: 요청에 실패했습니다.")
    return None

# 3. 실행
html_text = fetch_html(url, headers)

# 요청 결과 확인 (파싱 없이 출력만)
if html_text:
    print(html_text[:500])  # 처음 500자만 출력해보기
