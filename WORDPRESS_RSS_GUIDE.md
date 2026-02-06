# WordPress RSS 피드 통합 가이드

## 📋 개요
코스콤 뉴스를 WordPress RSS 2.0 형식의 XML로 변환하여 WordPress 사이트에 자동으로 표시하는 방법입니다.

## 🎯 RSS 피드 URL
GitHub Actions가 실행되면 다음 URL에서 RSS 피드를 사용할 수 있습니다:

```
https://raw.githubusercontent.com/YOUR_USERNAME/koscom-news-crawler/main/koscom_news_feed.xml
```

⚠️ **주의**: `YOUR_USERNAME`을 실제 GitHub 사용자명으로 변경하세요!

## 📝 RSS XML 구조

생성되는 XML은 다음과 같은 구조를 가집니다:

```xml
<?xml version="1.0" ?>
<rss version="2.0" 
     xmlns:content="http://purl.org/rss/1.0/modules/content/"
     xmlns:dc="http://purl.org/dc/elements/1.1/"
     xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>코스콤 뉴스</title>
    <link>https://www.koscom.co.kr/...</link>
    <description>코스콤 공식 뉴스 피드</description>
    <language>ko-KR</language>
    
    <item>
      <title>뉴스 제목</title>
      <link>뉴스 URL</link>
      <pubDate>Mon, 28 Jan 2026 09:00:00 +0900</pubDate>
      <dc:creator>코스콤</dc:creator>
      <category>금융IT</category>
      <guid>뉴스 URL</guid>
      <description>요약 내용 (이미지 포함)</description>
      <content:encoded>전체 HTML 콘텐츠</content:encoded>
    </item>
    
  </channel>
</rss>
```

## 🔌 WordPress 통합 방법

### 방법 1: WP RSS Aggregator 플러그인 (추천)

#### 1단계: 플러그인 설치
1. WordPress 관리자 → **플러그인** → **새로 추가**
2. "**WP RSS Aggregator**" 검색
3. 설치 후 활성화

#### 2단계: 피드 소스 추가
1. **RSS Aggregator** → **Feed Sources** → **Add New**
2. 설정:
   - **Title**: 코스콤 뉴스
   - **Feed URL**: `https://raw.githubusercontent.com/YOUR_USERNAME/koscom-news-crawler/main/koscom_news_feed.xml`
   - **Update Interval**: 1 hour (또는 원하는 주기)
   - **Limit**: 10 (표시할 항목 수)
3. **게시** 클릭

#### 3단계: 페이지/포스트에 표시
숏코드 사용:
```
[wp-rss-aggregator sources="koscom-뉴스"]
```

또는 블록 에디터에서:
1. "**RSS Aggregator**" 블록 추가
2. 피드 소스 선택

### 방법 2: Feedzy RSS Feeds 플러그인

#### 1단계: 플러그인 설치
1. WordPress 관리자 → **플러그인** → **새로 추가**
2. "**Feedzy RSS Feeds**" 검색
3. 설치 후 활성화

#### 2단계: 숏코드로 표시
페이지/포스트에 다음 숏코드 추가:

```
[feedzy-rss feeds="https://raw.githubusercontent.com/YOUR_USERNAME/koscom-news-crawler/main/koscom_news_feed.xml" max="10" feed_title="yes" target="_blank" summary="yes" size="150" ]
```

**옵션 설명:**
- `max="10"`: 최대 10개 항목 표시
- `feed_title="yes"`: 피드 제목 표시
- `target="_blank"`: 새 탭에서 열기
- `summary="yes"`: 요약 표시
- `size="150"`: 요약 글자 수

#### 고급 옵션:
```
[feedzy-rss 
  feeds="https://raw.githubusercontent.com/YOUR_USERNAME/koscom-news-crawler/main/koscom_news_feed.xml" 
  max="10" 
  feed_title="yes" 
  target="_blank" 
  title="50" 
  meta="yes" 
  summary="yes" 
  summarylength="200" 
  size="150"
  keywords_title="AI, 로보어드바이저, 클라우드"
]
```

### 방법 3: RSS Import 플러그인

#### 1단계: 플러그인 설치
1. **플러그인** → **새로 추가** → "**RSS Import**" 검색
2. 설치 후 활성화

#### 2단계: 피드 가져오기
1. **도구** → **RSS Import**
2. **Add New Feed** 클릭
3. RSS URL 입력 및 설정
4. 자동 게시 설정 가능

### 방법 4: 수동 임포트 (일회성)

#### WordPress 기본 기능 사용
1. **도구** → **가져오기** → **RSS**
2. RSS Importer 설치 (처음 사용 시)
3. RSS 피드 URL 입력
4. 카테고리 및 작성자 선택
5. 가져오기 실행

⚠️ **주의**: 수동 방법은 자동 업데이트되지 않습니다.

## 🎨 디자인 커스터마이징

### CSS 스타일링
WordPress 테마의 **사용자 정의 CSS**에 추가:

```css
/* 코스콤 뉴스 피드 스타일 */
.koscom-news-item {
    background: #f9f9f9;
    border-left: 4px solid #0066cc;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 5px;
}

.koscom-news-item img {
    max-width: 100%;
    height: auto;
    border-radius: 8px;
    margin-bottom: 15px;
}

.koscom-news-item .news-content {
    line-height: 1.8;
    color: #333;
}

.koscom-news-item .news-meta {
    margin-top: 20px;
    padding-top: 20px;
    border-top: 1px solid #ddd;
    font-size: 0.9em;
    color: #666;
}

/* WP RSS Aggregator 스타일 */
.wprss-feed-item {
    padding: 15px;
    margin-bottom: 15px;
    background: white;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.wprss-feed-item-title {
    font-size: 1.2em;
    margin-bottom: 10px;
}

.wprss-feed-item-date {
    color: #888;
    font-size: 0.9em;
}
```

### PHP 템플릿 (고급)
테마 폴더에 `rss-feed-template.php` 생성:

```php
<?php
$rss_url = 'https://raw.githubusercontent.com/YOUR_USERNAME/koscom-news-crawler/main/koscom_news_feed.xml';
$rss = fetch_feed($rss_url);

if (!is_wp_error($rss)) {
    $maxitems = $rss->get_item_quantity(10);
    $rss_items = $rss->get_items(0, $maxitems);
}
?>

<div class="koscom-news-feed">
    <h2>코스콤 최신 뉴스</h2>
    
    <?php if ($maxitems > 0) : ?>
        <?php foreach ($rss_items as $item) : ?>
            <div class="news-item">
                <h3>
                    <a href="<?php echo esc_url($item->get_permalink()); ?>" target="_blank">
                        <?php echo esc_html($item->get_title()); ?>
                    </a>
                </h3>
                <p class="news-date">
                    <?php echo $item->get_date('Y-m-d'); ?>
                </p>
                <div class="news-description">
                    <?php echo $item->get_description(); ?>
                </div>
            </div>
        <?php endforeach; ?>
    <?php else : ?>
        <p>뉴스를 불러올 수 없습니다.</p>
    <?php endif; ?>
</div>
```

## 🔄 자동 업데이트 설정

### 캐시 지우기
RSS 피드가 업데이트되지 않으면:

1. **WP RSS Aggregator 사용 시:**
   - RSS Aggregator → Settings → General
   - "**Force feed update**" 체크
   - 또는 개별 피드에서 "**Fetch Items Now**" 클릭

2. **Feedzy 사용 시:**
   - Feedzy → Settings
   - Cache 시간 조정 (기본 12시간)

3. **WordPress 캐시 플러그인:**
   - WP Super Cache, W3 Total Cache 등의 캐시 삭제

### Cron 작업 확인
1. **플러그인 설치:** WP Crontrol
2. **Cron Events** 확인
3. RSS 관련 작업이 정상 실행되는지 확인

## 📱 반응형 디스플레이

### 모바일 최적화 CSS
```css
@media (max-width: 768px) {
    .koscom-news-item {
        padding: 15px;
        font-size: 0.9em;
    }
    
    .koscom-news-item img {
        max-width: 100%;
        height: auto;
    }
}
```

## 🔍 문제 해결

### RSS 피드가 표시되지 않는 경우

#### 1. URL 확인
브라우저에서 직접 XML URL 열기:
```
https://raw.githubusercontent.com/YOUR_USERNAME/koscom-news-crawler/main/koscom_news_feed.xml
```

#### 2. XML 유효성 검사
- https://validator.w3.org/feed/ 에서 검증

#### 3. WordPress 디버그 모드
`wp-config.php`에 추가:
```php
define('WP_DEBUG', true);
define('WP_DEBUG_LOG', true);
```

로그 확인: `wp-content/debug.log`

#### 4. 플러그인 충돌 확인
- 다른 플러그인 비활성화 후 테스트
- 테마를 기본 테마로 변경 후 테스트

### CORS 오류 해결
GitHub Raw 파일은 CORS를 지원하므로 일반적으로 문제없지만, 
만약 오류가 발생하면:

1. 서버에 RSS XML 파일 복사
2. 자체 도메인에서 호스팅

## 📊 사용 예시

### 사이드바 위젯
1. **외모** → **위젯**
2. "**텍스트**" 또는 "**HTML**" 위젯 추가
3. 숏코드 입력:
```
[feedzy-rss feeds="https://raw.githubusercontent.com/..." max="5"]
```

### 홈페이지 섹션
```html
<section class="koscom-news-section">
    <h2>코스콤 최신 소식</h2>
    [wp-rss-aggregator sources="koscom-뉴스" limit="5"]
</section>
```

## ⚡ 성능 최적화

### 1. 캐싱 활용
```php
// functions.php에 추가
function koscom_rss_cache_time($seconds) {
    return 3600; // 1시간 캐시
}
add_filter('wp_feed_cache_transient_lifetime', 'koscom_rss_cache_time');
```

### 2. Lazy Loading
```html
<img loading="lazy" src="...">
```

### 3. CDN 사용
이미지를 CDN을 통해 제공

## 🎁 추가 기능

### 키워드 필터링
특정 키워드가 포함된 뉴스만 표시:
```
[feedzy-rss feeds="..." keywords_title="AI, 로보어드바이저"]
```

### 카테고리별 표시
```
[feedzy-rss feeds="..." keywords_title="클라우드" categories="테크"]
```

## 📈 분석 및 추적

### Google Analytics 연동
```javascript
// 링크 클릭 추적
jQuery('.koscom-news-item a').click(function() {
    gtag('event', 'click', {
        'event_category': 'RSS Feed',
        'event_label': 'Koscom News'
    });
});
```

## 🔐 보안 고려사항

1. **신뢰할 수 있는 소스만** 사용
2. **XSS 방지**: WordPress가 자동으로 처리
3. **HTTPS 사용**: GitHub Raw는 HTTPS 제공

## 📝 체크리스트

- [ ] GitHub Actions가 정상 실행되는지 확인
- [ ] RSS XML 파일이 생성되었는지 확인
- [ ] WordPress 플러그인 설치
- [ ] RSS 피드 URL 설정
- [ ] 테스트 페이지에서 피드 확인
- [ ] 캐시 설정 확인
- [ ] CSS 스타일링 적용
- [ ] 모바일 반응형 테스트

## 🎯 최종 권장 설정

**플러그인**: WP RSS Aggregator (무료) 또는 Feedzy RSS Feeds (무료)
**업데이트 주기**: 1시간
**표시 항목**: 10개
**캐시 시간**: 1시간

이 설정으로 매일 아침 7시에 자동으로 업데이트되는 
코스콤 뉴스를 WordPress 사이트에 자동으로 표시할 수 있습니다! 🎉
