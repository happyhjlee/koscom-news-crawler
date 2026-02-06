# 코스콤 뉴스 크롤러 - GitHub Actions 설정 가이드

## 📋 프로젝트 개요
코스콤 뉴스 페이지(1페이지)를 매일 아침 7시에 자동으로 크롤링하여 JSON 파일로 저장하는 프로젝트입니다.

## 🚀 설정 방법

### 1. GitHub 리포지토리 생성
1. GitHub에서 새 리포지토리 생성
2. 리포지토리 이름: `koscom-news-crawler` (또는 원하는 이름)
3. Public 또는 Private 선택

### 2. 파일 업로드
다음 파일들을 리포지토리에 업로드하세요:

```
koscom-news-crawler/
├── .github/
│   └── workflows/
│       └── crawler.yml          # GitHub Actions 워크플로우
├── crawl_koscom.py              # 크롤링 스크립트
├── requirements.txt             # Python 패키지 목록
├── README.md                    # 프로젝트 설명
└── koscom_news.json             # 뉴스 데이터 (자동 생성됨)
```

### 3. GitHub Actions 권한 설정
1. 리포지토리 페이지에서 **Settings** 클릭
2. 왼쪽 메뉴에서 **Actions** → **General** 선택
3. **Workflow permissions** 섹션에서:
   - ✅ **Read and write permissions** 선택
   - ✅ **Allow GitHub Actions to create and approve pull requests** 체크
4. **Save** 클릭

### 4. 초기 JSON 파일 생성 (선택사항)
빈 JSON 파일을 먼저 생성하려면:

```bash
echo "[]" > koscom_news.json
git add koscom_news.json
git commit -m "Initialize koscom_news.json"
git push
```

## ⏰ 스케줄 설정

### 현재 설정
- **매일 아침 7시 (한국 시간)** 자동 실행
- GitHub Actions는 UTC 시간으로 작동하므로 **UTC 22시**로 설정됨

### 스케줄 변경 방법
`.github/workflows/crawler.yml` 파일의 cron 부분을 수정:

```yaml
schedule:
  - cron: '0 22 * * *'  # 매일 한국시간 오전 7시
```

#### Cron 표현식 예시
```
'0 22 * * *'   # 매일 한국시간 오전 7시 (UTC 22시)
'0 23 * * *'   # 매일 한국시간 오전 8시 (UTC 23시)
'0 0 * * *'    # 매일 한국시간 오전 9시 (UTC 0시)
'0 1 * * *'    # 매일 한국시간 오전 10시 (UTC 1시)
'0 12 * * *'   # 매일 한국시간 오후 9시 (UTC 12시)
'0 0 * * 1'    # 매주 월요일 한국시간 오전 9시
'0 0 1 * *'    # 매월 1일 한국시간 오전 9시
```

## 🧪 테스트 방법

### 로컬에서 테스트
```bash
# 1. 패키지 설치
pip install -r requirements.txt

# 2. 스크립트 실행
python crawl_koscom.py
```

### Cloud Shell에서 테스트
```bash
# 1. Cloud Shell 열기 (Google Cloud Console)

# 2. 리포지토리 클론
git clone https://github.com/YOUR_USERNAME/koscom-news-crawler.git
cd koscom-news-crawler

# 3. 패키지 설치
pip install -r requirements.txt

# 4. 실행
python crawl_koscom.py
```

### GitHub Actions 수동 실행
1. 리포지토리 페이지에서 **Actions** 탭 클릭
2. 왼쪽에서 **Koscom News Crawler** 워크플로우 선택
3. **Run workflow** 버튼 클릭
4. **Run workflow** 확인

## 📁 출력 파일 구조

### koscom_news.json
```json
[
  {
    "title": "RA 시장 성장의 숨은 조력자 '코스콤 로보어드바이저 테스트베드'",
    "url": "https://www.koscom.co.kr/portal/bbs/B0000064/view.do?nttId=30513...",
    "date": "2026-01-28",
    "summary": "로보어드바이저(Robo-Advisor, RA) 기반 자산관리 시장이...",
    "image_url": "https://www.koscom.co.kr/cmm/fms/getImage.do?atchFileId=...",
    "crawled_at": "2026-02-06 07:00:15"
  },
  ...
]
```

## 🔍 실행 확인

### Actions 로그 확인
1. 리포지토리의 **Actions** 탭 클릭
2. 최근 워크플로우 실행 결과 확인
3. 세부 로그 보기:
   - 워크플로우 클릭 → **Run crawler** 단계 확인

### 데이터 확인
1. 리포지토리에서 `koscom_news.json` 파일 확인
2. 커밋 히스토리에서 업데이트 내역 확인

## 🛠️ 문제 해결

### 워크플로우가 실행되지 않는 경우
1. **Settings** → **Actions** → **General**에서 권한 확인
2. 리포지토리가 Public인 경우 Actions가 활성화되어 있는지 확인

### 크롤링 실패하는 경우
1. Actions 로그에서 에러 메시지 확인
2. 코스콤 웹사이트 접근 가능 여부 확인
3. 웹사이트 구조 변경 여부 확인

### 커밋이 푸시되지 않는 경우
1. **Workflow permissions**가 "Read and write"로 설정되었는지 확인
2. `.github/workflows/crawler.yml`의 git 설정 확인

## 📊 데이터 활용 예시

### Python으로 데이터 읽기
```python
import json

# JSON 파일 읽기
with open('koscom_news.json', 'r', encoding='utf-8') as f:
    news_data = json.load(f)

# 최신 뉴스 출력
for news in news_data[:5]:
    print(f"제목: {news['title']}")
    print(f"날짜: {news['date']}")
    print(f"URL: {news['url']}")
    print()
```

### JavaScript로 데이터 읽기
```javascript
fetch('koscom_news.json')
  .then(response => response.json())
  .then(data => {
    data.slice(0, 5).forEach(news => {
      console.log(`제목: ${news.title}`);
      console.log(`날짜: ${news.date}`);
      console.log(`URL: ${news.url}`);
      console.log('---');
    });
  });
```

## 📈 고급 설정

### 알림 설정 (선택사항)
크롤링 실패 시 이메일 알림을 받으려면:
1. **Settings** → **Notifications** 설정
2. 또는 워크플로우에 Slack/Discord 알림 추가

### 데이터 백업
정기적으로 데이터를 백업하려면:
- GitHub Releases 사용
- 외부 스토리지로 업로드 (S3, Google Drive 등)

## 🔐 보안 고려사항
- API 키나 비밀번호가 필요한 경우 GitHub Secrets 사용
- Public 리포지토리의 경우 민감한 정보 포함 금지

## 📝 라이선스
개인적인 학습 및 연구 목적으로만 사용하세요.

## 📧 문의
이슈가 있는 경우 GitHub Issues에 등록해주세요.
