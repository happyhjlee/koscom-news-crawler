"""
코스콤 뉴스 크롤러 - WordPress RSS XML 생성
GitHub Actions용 자동화 스크립트
"""

import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
from datetime import datetime
import xml.etree.ElementTree as ET
from xml.dom import minidom
import os


class KoscomNewsRSSCrawler:
    def __init__(self):
        self.base_url = "https://www.koscom.co.kr"
        self.list_url = "https://www.koscom.co.kr/portal/bbs/B0000064/list.do"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
    
    def get_news_list(self):
        """첫 페이지 뉴스 목록 가져오기"""
        params = {
            'type': 'list',
            'status': '',
            'year': '',
            'menuNo': '200629',
            'searchWrd': '',
            'searchCnd': '',
            'pageIndex': '1'
        }
        
        try:
            response = requests.get(self.list_url, params=params, headers=self.headers, timeout=30)
            response.raise_for_status()
            response.encoding = 'utf-8'
            
            soup = BeautifulSoup(response.text, 'html.parser')
            news_items = []
            
            # 뉴스 항목 찾기
            news_list = soup.select('ul > li')
            
            for item in news_list:
                try:
                    link_tag = item.find('a')
                    if not link_tag:
                        continue
                    
                    # 제목
                    title = link_tag.text.strip()
                    
                    # URL
                    detail_url = link_tag.get('href', '')
                    if detail_url and not detail_url.startswith('http'):
                        detail_url = urljoin(self.base_url, detail_url)
                    
                    # 날짜
                    date = ''
                    dd_tags = item.find_all('dd')
                    for dd in dd_tags:
                        date_match = re.search(r'\d{4}-\d{2}-\d{2}', dd.text)
                        if date_match:
                            date = date_match.group()
                            break
                    
                    # 요약
                    summary = ''
                    if len(dd_tags) > 1:
                        summary = dd_tags[1].text.strip()
                    
                    # 이미지
                    img_tag = item.find('img')
                    img_url = ''
                    if img_tag:
                        img_src = img_tag.get('src', '')
                        if img_src and not img_src.startswith('http'):
                            img_url = urljoin(self.base_url, img_src)
                        else:
                            img_url = img_src
                    
                    if title and detail_url:
                        news_items.append({
                            'title': title,
                            'url': detail_url,
                            'date': date,
                            'summary': summary,
                            'image_url': img_url
                        })
                
                except Exception as e:
                    print(f"항목 파싱 오류: {e}")
                    continue
            
            return news_items
            
        except Exception as e:
            print(f"뉴스 목록 가져오기 오류: {e}")
            return []
    
    def convert_date_to_rfc822(self, date_str):
        """날짜를 RFC 822 형식으로 변환 (RSS 표준)"""
        try:
            if not date_str:
                return datetime.now().strftime('%a, %d %b %Y %H:%M:%S +0900')
            
            # YYYY-MM-DD 형식을 파싱
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            # RFC 822 형식으로 변환 (예: Mon, 28 Jan 2026 09:00:00 +0900)
            return date_obj.strftime('%a, %d %b %Y 09:00:00 +0900')
        except:
            return datetime.now().strftime('%a, %d %b %Y %H:%M:%S +0900')
    
    def create_rss_feed(self, news_items):
        """WordPress RSS 2.0 형식의 XML 생성"""
        
        # RSS root element
        rss = ET.Element('rss')
        rss.set('version', '2.0')
        rss.set('xmlns:content', 'http://purl.org/rss/1.0/modules/content/')
        rss.set('xmlns:wfw', 'http://wellformedweb.org/CommentAPI/')
        rss.set('xmlns:dc', 'http://purl.org/dc/elements/1.1/')
        rss.set('xmlns:atom', 'http://www.w3.org/2005/Atom')
        rss.set('xmlns:sy', 'http://purl.org/rss/1.0/modules/syndication/')
        rss.set('xmlns:slash', 'http://purl.org/rss/1.0/modules/slash/')
        
        # Channel element
        channel = ET.SubElement(rss, 'channel')
        
        # Channel 메타데이터
        title = ET.SubElement(channel, 'title')
        title.text = '코스콤 뉴스'
        
        link = ET.SubElement(channel, 'link')
        link.text = 'https://www.koscom.co.kr/portal/bbs/B0000064/list.do?menuNo=200629'
        
        description = ET.SubElement(channel, 'description')
        description.text = '코스콤(KOSCOM) 공식 뉴스 피드 - 금융IT, 자본시장, 핀테크 관련 최신 소식'
        
        language = ET.SubElement(channel, 'language')
        language.text = 'ko-KR'
        
        last_build_date = ET.SubElement(channel, 'lastBuildDate')
        last_build_date.text = datetime.now().strftime('%a, %d %b %Y %H:%M:%S +0900')
        
        update_period = ET.SubElement(channel, 'sy:updatePeriod')
        update_period.text = 'daily'
        
        update_frequency = ET.SubElement(channel, 'sy:updateFrequency')
        update_frequency.text = '1'
        
        generator = ET.SubElement(channel, 'generator')
        generator.text = 'Koscom News Crawler v1.0'
        
        # Atom self link
        atom_link = ET.SubElement(channel, 'atom:link')
        atom_link.set('href', 'https://raw.githubusercontent.com/happyhjlee/koscom-news-crawler/main/koscom_news_feed.xml')
        atom_link.set('rel', 'self')
        atom_link.set('type', 'application/rss+xml')
        
        # 각 뉴스 항목 추가
        for news in news_items:
            item = ET.SubElement(channel, 'item')
            
            # 제목
            item_title = ET.SubElement(item, 'title')
            item_title.text = news['title']
            
            # 링크
            item_link = ET.SubElement(item, 'link')
            item_link.text = news['url']
            
            # 발행일
            pub_date = ET.SubElement(item, 'pubDate')
            pub_date.text = self.convert_date_to_rfc822(news['date'])
            
            # 작성자
            creator = ET.SubElement(item, 'dc:creator')
            creator.text = '코스콤'
            
            # 카테고리
            category = ET.SubElement(item, 'category')
            category.text = '금융IT'
            
            # GUID (고유 식별자)
            guid = ET.SubElement(item, 'guid')
            guid.set('isPermaLink', 'true')
            guid.text = news['url']
            
            # 설명 (요약)
            item_description = ET.SubElement(item, 'description')
            description_text = news['summary']
            if news['image_url']:
                # 이미지가 있으면 HTML 형식으로 포함
                description_text = f'<img src="{news["image_url"]}" alt="{news["title"]}" style="max-width:100%; height:auto; margin-bottom:15px;"/><p>{news["summary"]}</p>'
            item_description.text = description_text
            
            # Content (전체 내용 - description과 동일하게 설정)
            content = ET.SubElement(item, 'content:encoded')
            content_html = f'''<div class="koscom-news-item">
    {f'<img src="{news["image_url"]}" alt="{news["title"]}" style="max-width:100%; height:auto; margin-bottom:20px; border-radius:8px;"/>' if news["image_url"] else ''}
    <div class="news-content">
        {news["summary"]}
    </div>
    <div class="news-meta" style="margin-top:20px; padding-top:20px; border-top:1px solid #eee; color:#666;">
        <p><strong>출처:</strong> 코스콤 공식 뉴스</p>
        <p><strong>원문 보기:</strong> <a href="{news["url"]}" target="_blank" rel="noopener">{news["url"]}</a></p>
        <p><strong>발행일:</strong> {news["date"]}</p>
    </div>
</div>'''
            content.text = content_html
        
        return rss
    
    def prettify_xml(self, elem):
        """XML을 보기 좋게 포맷팅"""
        rough_string = ET.tostring(elem, encoding='utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ", encoding='utf-8').decode('utf-8')
    
    def save_to_xml(self, news_items, filename='koscom_news_feed.xml'):
        """RSS XML 파일로 저장"""
        try:
            # RSS 피드 생성
            rss = self.create_rss_feed(news_items)
            
            # 보기 좋게 포맷팅
            pretty_xml = self.prettify_xml(rss)
            
            # 파일로 저장
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(pretty_xml)
            
            return True
            
        except Exception as e:
            print(f"파일 저장 오류: {e}")
            return False


def main():
    print("="*80)
    print("코스콤 뉴스 크롤러 - WordPress RSS XML 생성")
    print(f"실행 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80)
    
    crawler = KoscomNewsRSSCrawler()
    
    # 뉴스 목록 가져오기
    print("\n뉴스 크롤링 중...")
    news_items = crawler.get_news_list()
    
    if news_items:
        print(f"✅ {len(news_items)}개의 뉴스를 가져왔습니다.\n")
        
        # 최신 3개 출력
        print("최신 뉴스 3개:")
        print("-"*80)
        for i, news in enumerate(news_items[:3], 1):
            print(f"{i}. {news['title']}")
            print(f"   날짜: {news['date']}")
            print(f"   URL: {news['url']}")
            print()
        
        # RSS XML 파일로 저장
        if crawler.save_to_xml(news_items):
            print(f"📁 RSS 피드 저장 완료!")
            print(f"   파일: koscom_news_feed.xml")
            print(f"   형식: WordPress RSS 2.0")
            print(f"   항목 수: {len(news_items)}개")
            
            # 파일 크기 확인
            file_size = os.path.getsize('koscom_news_feed.xml')
            print(f"   파일 크기: {file_size:,} bytes")
        
    else:
        print("❌ 뉴스를 가져오지 못했습니다.")
    
    print("\n" + "="*80)
    print("크롤링 완료!")
    print("="*80)
    
    # WordPress에서 사용하는 방법 안내
    print("\n📝 WordPress에서 사용하는 방법:")
    print("-"*80)
    print("1. GitHub에 koscom_news_feed.xml 파일이 업로드되면")
    print("2. Raw 파일 URL을 복사:")
    print("   https://raw.githubusercontent.com/YOUR_USERNAME/koscom-news-crawler/main/koscom_news_feed.xml")
    print("3. WordPress 관리자 → 도구 → 가져오기 → RSS")
    print("4. 또는 RSS 피드 플러그인 사용 (예: Feedzy, WP RSS Aggregator)")
    print("-"*80)


if __name__ == "__main__":
    main()
