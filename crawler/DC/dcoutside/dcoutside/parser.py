from bs4 import BeautifulSoup
import pdb
import re
def parse_list(markup) -> dict:
    
    soup = BeautifulSoup(markup,'html.parser')
    gall_nums = soup.find_all('td',attrs={'class':'gall_num'})

    result=[]
    for gall_num in gall_nums:
        
        num = re.findall('\d+', gall_num.text)[0] if len(re.findall('\d+', gall_num.text)) > 0 else None
        if num is not None:
            result.append(num)

    print(result)


    return result



def parse_post(markup) -> dict:
    
    soup = BeautifulSoup(markup,'html.parser')
    
    if not str(soup):
        soup = BeautifulSoup(markup, 'html.parser')

        if '/error/deleted/' in str(soup):
            return {'deleted': True}
        elif '해당 갤러리는 존재하지 않습니다' in str(soup):
            raise NoSuchGalleryError
        else:
            pass
    
    timestamp = soup.find(attrs={'class':'gall_date'})['title']

    header_info = soup.find(attrs={'class':'gallview_head'})
    user_info = header_info.find(attrs={'class':'gall_writer'})
    user_id = user_info['data-uid']
    user_ip = '' if user_id else user_info['data-ip']
    nickname = user_info['data-nick']



    title = header_info.find(attrs={'class':'title_subject'}).text

    view_info = soup.find_all(attrs={'class':'fr'})[1]

    view_cnt = view_info.find(attrs={'class':'gall_count'}).text
    view_cnt = int(view_cnt.split()[1])

    comment_cnt = view_info.find(attrs={'class':'gall_comment'}).text
    comment_cnt = int(comment_cnt.split()[1])

    view_up = int(soup.find(attrs={'class':'up_num'}).text)
    view_dn = int(soup.find(attrs={'class':'down_num'}).text)
    
    body = soup.find(attrs={'class':'writing_view_box'}).text

    post = {
        'user_id': user_id,
        'user_ip': user_ip,
        'nickname': nickname,

        'title': title,
        'written_at': timestamp,

        'view_up': view_up,
        'view_dn': view_dn,
        'view_cnt': view_cnt,
        'comment_cnt': comment_cnt,
        'body': body,
    }

    return post


def parse_comments(text: str) -> list:

    comments = []
    soup = BeautifulSoup(text, 'lxml')
    comment_elements = soup.find_all('tr', class_='reply_line')

    for element in comment_elements:
        user_layer = element.find('td', class_='user_layer')
        nickname = user_layer['user_name']
        user_id = user_layer['user_id']
        body = element.find('td', class_='reply')
        user_ip = '' if user_id else body.find('span').extract().text
        timestamp = element.find('td', class_='retime').text

        comment = {
            'user_id': user_id,
            'user_ip': user_ip,
            'nickname': nickname,
            'written_at': timestamp,
            'body': body.text.strip()
        }

        comments.append(comment)

    return comments


class NoSuchGalleryError(Exception):
    pass
