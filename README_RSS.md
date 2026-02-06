# 코스콤 뉴스 자동 크롤러 → WordPress RSS

[![Koscom News Crawler](https://github.com/YOUR_USERNAME/koscom-news-crawler/actions/workflows/crawler.yml/badge.svg)](https://github.com/YOUR_USERNAME/koscom-news-crawler/actions/workflows/crawler.yml)

매일 아침 7시에 자동으로 코스콤 뉴스(1페이지)를 크롤링하여 **WordPress RSS 2.0 형식의 XML**로 저장하는 프로젝트입니다.

## 🎯 주요 기능

- ✅ 매일 아침 7시 자동 크롤링 (GitHub Actions)
- ✅ 코스콤 뉴스 1페이지 수집
- ✅ **WordPress RSS 2.0 XML 형식**으로 저장
- ✅ 이미지 포함 HTML 콘텐츠
- ✅ WordPress에 바로 적용 가능
- ✅ 보기 좋게 포맷팅된 XML

## 📡 RSS 피드 URL

```
https://raw.githubusercontent.com/YOUR_USERNAME/koscom-news-crawler/main/koscom_news_feed.xml
```

⚠️ **YOUR_USERNAME을 실제 GitHub 사용자명으로 변경하세요!**

## 📁 RSS XML 구조

```xml
<?xml version="1.0" ?>
<rss version="2.0" xmlns:content="..." xmlns:dc="...">
  <channel>
    <title>코스콤 뉴스</title>
    <link>https://www.koscom.co.kr/...</link>
    <description>코스콤 공식 뉴스 피드</description>
    <language>ko-KR</language>
    
    <item>
      <title>RA 시장 성장의 숨은 조력자...</title>
      <link>https://www.koscom.co.kr/...</link>
      <pubDate>Mon, 28 Jan 2026 09:00:00 +0900</pubDate>
      <dc:creator>코스콤</dc:creator>
      <category>금융IT</category>
      <description><![CDATA[
        <img src="..." />
        <p>뉴스 요약 내용...</p>
      ]]></description>
      <content:encoded><![CDATA[
        <div class="koscom-news-item">
          <img src="..." />
          <div class="news-content">...</div>
          <div class="news-meta">...</div>
        </div>
      ]]></content:encoded>
    </item>
  </channel>
</rss>
```

## 🚀 WordPress 통합 (3가지 방법)

### 방법 1: WP RSS Aggregator 플러그인 (추천 ⭐)

1. WordPress 플러그인에서 "**WP RSS Aggregator**" 설치
2. Feed Sources → Add New
3. RSS URL 입력: `https://raw.githubusercontent.com/YOUR_USERNAME/koscom-news-crawler/main/koscom_news_feed.xml`
4. 페이지에 숏코드 추가: `[wp-rss-aggregator sources="코스콤-뉴스"]`

### 방법 2: Feedzy RSS Feeds 플러그인

1. "**Feedzy RSS Feeds**" 플러그인 설치
2. 페이지/포스트에 숏코드 추가:
```
[feedzy-rss feeds="https://raw.githubusercontent.com/YOUR_USERNAME/koscom-news-crawler/main/koscom_news_feed.xml" max="10" feed_title="yes" summary="yes"]
```

### 방법 3: RSS Import 플러그인

1. "**RSS Import**" 플러그인 설치
2. 도구 → RSS Import에서 피드 추가
3. 자동 게시 설정

**자세한 WordPress 통합 가이드**: [WORDPRESS_RSS_GUIDE.md](WORDPRESS_RSS_GUIDE.md)

## 🛠️ 설치 및 실행

### 로컬 테스트

```bash
# 리포지토리 클론
git clone https://github.com/YOUR_USERNAME/koscom-news-crawler.git
cd koscom-news-crawler

# 패키지 설치
pip install -r requirements.txt

# 실행
python crawl_koscom_rss.py
```

### GitHub Actions 설정

1. 이 리포지토리를 포크하거나 클론
2. GitHub 리포지토리 Settings → Actions → General
3. "**Read and write permissions**" 선택
4. 매일 오전 7시에 자동 실행됨

**상세 설정 가이드**: [SETUP_GUIDE.md](SETUP_GUIDE.md)

## ⏰ 스케줄

- **자동 실행**: 매일 오전 7시 (한국 시간)
- **수동 실행**: GitHub Actions 탭에서 "Run workflow"

## 📊 출력 예시

### 터미널 출력
```
================================================================================
코스콤 뉴스 크롤러 - WordPress RSS XML 생성
실행 시간: 2026-02-06 07:00:15
================================================================================

뉴스 크롤링 중...
✅ 9개의 뉴스를 가져왔습니다.

최신 뉴스 3개:
--------------------------------------------------------------------------------
1. RA 시장 성장의 숨은 조력자 '코스콤 로보어드바이저 테스트베드'
   날짜: 2026-01-28
   URL: https://www.koscom.co.kr/portal/bbs/B0000064/view.do?nttId=30513...

📁 RSS 피드 저장 완료!
   파일: koscom_news_feed.xml
   형식: WordPress RSS 2.0
   항목 수: 9개
   파일 크기: 15,234 bytes
```

### XML 파일 미리보기
```xml
<?xml version="1.0" ?>
<rss version="2.0">
  <channel>
    <title>코스콤 뉴스</title>
    <lastBuildDate>Thu, 06 Feb 2026 07:00:15 +0900</lastBuildDate>
    
    <item>
      <title>RA 시장 성장의 숨은 조력자...</title>
      <pubDate>Mon, 28 Jan 2026 09:00:00 +0900</pubDate>
      <!-- 이미지 포함 HTML 콘텐츠 -->
    </item>
  </channel>
</rss>
```

## 🎨 WordPress 디자인 커스터마이징

### CSS 스타일 추가
```css
.koscom-news-item {
    background: #f9f9f9;
    border-left: 4px solid #0066cc;
    padding: 20px;
    margin-bottom: 20px;
}

.koscom-news-item img {
    max-width: 100%;
    border-radius: 8px;
}
```

더 많은 스타일링 옵션: [WORDPRESS_RSS_GUIDE.md](WORDPRESS_RSS_GUIDE.md#-디자인-커스터마이징)

## 📝 파일 구조

```
koscom-news-crawler/
├── .github/
│   └── workflows/
│       └── crawler.yml           # GitHub Actions (매일 오전 7시 실행)
├── crawl_koscom_rss.py           # RSS XML 생성 스크립트
├── koscom_news_feed.xml          # 생성된 RSS 피드 (자동 생성)
├── requirements.txt              # Python 패키지
├── SETUP_GUIDE.md                # GitHub Actions 설정 가이드
├── WORDPRESS_RSS_GUIDE.md        # WordPress 통합 가이드
└── README.md                     # 프로젝트 소개
```

## 🔧 커스터마이징

### RSS 피드 제목 변경
`crawl_koscom_rss.py` 파일에서:
```python
title = ET.SubElement(channel, 'title')
title.text = '원하는 제목'  # 여기 수정
```

### 크롤링 시간 변경
`.github/workflows/crawler.yml` 파일에서:
```yaml
schedule:
  - cron: '0 22 * * *'  # UTC 22시 = 한국시간 오전 7시
  # 0 23 * * * → 오전 8시
  # 0 0 * * * → 오전 9시
```

## 🔍 문제 해결

### RSS 피드가 업데이트되지 않을 때
1. GitHub Actions 탭에서 워크플로우 실행 확인
2. Actions 권한 확인 (Read and write)
3. XML 파일이 커밋되었는지 확인

### WordPress에 표시되지 않을 때
1. RSS URL이 올바른지 확인
2. 브라우저에서 직접 XML 열어보기
3. WordPress 캐시 삭제
4. 플러그인 재설정

자세한 문제 해결: [WORDPRESS_RSS_GUIDE.md](WORDPRESS_RSS_GUIDE.md#-문제-해결)

## 📖 가이드 문서

- 📘 [GitHub Actions 설정 가이드](SETUP_GUIDE.md)
- 🔌 [WordPress RSS 통합 가이드](WORDPRESS_RSS_GUIDE.md)
- ☁️ [Cloud Shell 테스트 가이드](CLOUD_SHELL_GUIDE.md)

## 🛡️ 사용 기술

- Python 3.11
- BeautifulSoup4 (HTML 파싱)
- Requests (HTTP 요청)
- XML ElementTree (RSS 생성)
- GitHub Actions (자동화)

## ⚠️ 주의사항

- 개인 학습 및 연구 목적으로만 사용하세요
- 웹 크롤링 시 대상 사이트의 이용 약관을 준수하세요
- 과도한 요청으로 서버에 부하를 주지 않도록 주의하세요

## 🤝 기여

이슈 제보나 개선 제안은 언제든지 환영합니다!

## 📄 라이선스

MIT License

## 📧 문의

문제가 있거나 질문이 있으면 GitHub Issues를 이용해주세요.

---

Made with ❤️ for WordPress + GitHub Actions
