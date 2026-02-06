# Cloud Shell 테스트 가이드

## 🚀 Google Cloud Shell에서 빠르게 테스트하기

### 1. Cloud Shell 열기
1. Google Cloud Console 접속
2. 우측 상단의 Cloud Shell 아이콘 클릭
3. 터미널이 열릴 때까지 대기

### 2. 프로젝트 준비

```bash
# 홈 디렉토리로 이동
cd ~

# 프로젝트 디렉토리 생성
mkdir koscom-crawler-test
cd koscom-crawler-test

# 필요한 파일들 다운로드 (GitHub에 업로드한 후)
# 방법 1: Git clone (추천)
git clone https://github.com/YOUR_USERNAME/koscom-news-crawler.git
cd koscom-news-crawler

# 방법 2: 직접 파일 업로드
# Cloud Shell의 "파일 업로드" 기능 사용
```

### 3. 패키지 설치

```bash
# Python 버전 확인
python3 --version

# 필요한 패키지 설치
pip3 install -r requirements.txt --user
```

### 4. 크롤러 실행

```bash
# 스크립트 실행
python3 crawl_koscom.py
```

### 5. 결과 확인

```bash
# JSON 파일이 생성되었는지 확인
ls -lh koscom_news.json

# 파일 내용 미리보기
head -50 koscom_news.json

# 또는 전체 내용 보기
cat koscom_news.json | python3 -m json.tool
```

## 📊 예상 출력

```
================================================================================
코스콤 뉴스 크롤러 (1페이지)
실행 시간: 2026-02-06 07:00:15
================================================================================

뉴스 크롤링 중...
✅ 9개의 뉴스를 가져왔습니다.

최신 뉴스 3개:
--------------------------------------------------------------------------------
1. RA 시장 성장의 숨은 조력자 '코스콤 로보어드바이저 테스트베드'
   날짜: 2026-01-28
   URL: https://www.koscom.co.kr/portal/bbs/B0000064/view.do?nttId=30513...

2. 코스콤, 대학생 대상 'KOSCOM AI Agent Challenge 2025' 공모전 성료
   날짜: 2026-01-05
   URL: https://www.koscom.co.kr/portal/bbs/B0000064/view.do?nttId=30489...

3. 코스콤, '코리아 핀테크 위크 2025'에서 금융 클라우드 기반 AI 서비스 소개
   날짜: 2025-11-27
   URL: https://www.koscom.co.kr/portal/bbs/B0000064/view.do?nttId=30440...

📁 파일 저장 완료!
   새로운 뉴스: 9개
   전체 저장된 뉴스: 9개

================================================================================
크롤링 완료!
================================================================================
```

## 🔍 데이터 분석 (선택사항)

### Python으로 JSON 분석

```bash
# Python 인터프리터 실행
python3
```

```python
import json

# JSON 파일 읽기
with open('koscom_news.json', 'r', encoding='utf-8') as f:
    news = json.load(f)

# 기사 개수
print(f"총 {len(news)}개의 기사")

# 최신 기사
latest = news[0]
print(f"\n최신 기사: {latest['title']}")
print(f"날짜: {latest['date']}")
print(f"URL: {latest['url']}")

# 날짜별 개수
from collections import Counter
dates = [item['date'] for item in news]
date_count = Counter(dates)
print("\n날짜별 기사 수:")
for date, count in sorted(date_count.items(), reverse=True)[:5]:
    print(f"  {date}: {count}개")
```

### jq로 JSON 분석 (jq 설치 필요)

```bash
# jq 설치
sudo apt-get update && sudo apt-get install -y jq

# 예쁘게 출력
cat koscom_news.json | jq '.'

# 제목만 추출
cat koscom_news.json | jq '.[].title'

# 최신 3개 뉴스
cat koscom_news.json | jq '.[:3]'

# 특정 날짜의 뉴스 필터링
cat koscom_news.json | jq '.[] | select(.date == "2026-01-28")'
```

## 📤 파일 다운로드

### Cloud Shell에서 로컬로 다운로드

```bash
# 방법 1: Cloud Shell 다운로드 기능 사용
# 파일 메뉴 → 다운로드 → koscom_news.json 선택

# 방법 2: gcloud 명령어로 다운로드 (로컬 터미널에서)
gcloud cloud-shell scp cloudshell:~/koscom-crawler-test/koscom_news.json ./koscom_news.json
```

## 🔄 정기 실행 테스트

### Cron으로 테스트 (Cloud Shell에서는 세션 종료 시 중단됨)

```bash
# crontab 편집
crontab -e

# 매일 오전 7시에 실행 (예시)
0 7 * * * cd ~/koscom-crawler-test && python3 crawl_koscom.py >> crawler.log 2>&1

# cron 목록 확인
crontab -l
```

**주의:** Cloud Shell은 세션 종료 시 cron이 중단되므로, **실제 정기 실행은 GitHub Actions 사용을 권장합니다.**

## 🐛 문제 해결

### 네트워크 오류

```bash
# DNS 확인
nslookup www.koscom.co.kr

# ping 테스트
ping -c 3 www.koscom.co.kr

# curl로 접근 테스트
curl -I https://www.koscom.co.kr
```

### 패키지 설치 오류

```bash
# pip 업그레이드
pip3 install --upgrade pip --user

# 개별 패키지 설치
pip3 install requests --user
pip3 install beautifulsoup4 --user
pip3 install lxml --user
```

### 권한 오류

```bash
# 실행 권한 부여
chmod +x crawl_koscom.py

# 홈 디렉토리 권한 확인
ls -la ~/koscom-crawler-test
```

## 📝 다음 단계

1. ✅ Cloud Shell에서 테스트 완료
2. ⬆️ GitHub 리포지토리에 코드 업로드
3. ⚙️ GitHub Actions 설정
4. 🕐 매일 자동 실행 확인

자세한 GitHub Actions 설정은 [SETUP_GUIDE.md](SETUP_GUIDE.md)를 참조하세요!

## 💡 팁

- Cloud Shell은 세션이 종료되면 환경이 초기화될 수 있습니다
- 영구 데이터 저장이 필요하면 GitHub에 커밋하거나 Cloud Storage 사용
- 실제 운영은 GitHub Actions를 사용하는 것이 더 안정적입니다

## 🎯 빠른 명령어 요약

```bash
# 전체 프로세스 한 번에
cd ~ && \
mkdir -p koscom-crawler-test && \
cd koscom-crawler-test && \
pip3 install requests beautifulsoup4 lxml --user && \
python3 crawl_koscom.py && \
cat koscom_news.json | python3 -m json.tool | head -50
```
