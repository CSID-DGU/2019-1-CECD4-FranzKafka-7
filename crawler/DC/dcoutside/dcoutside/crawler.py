from datetime import datetime
from .parser import *
import requests

COMMENTS_PER_PAGE = 40

class DCInsideCrawler:

    def __init__(self, include_comments=False):
        
        
        self._view_url = 'http://gall.dcinside.com/board/view'


    def get_post(self, gall_id, post_no):
        try:
            header = {
                "User-Agent" : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
            }
            r = requests.get('%s/?id=%s&no=%d' % (self._view_url, gall_id, post_no), headers=header)
            post = parse_post(r.text)

            post['gall_id'] = gall_id
            post['post_no'] = post_no
            post['crawled_at'] = datetime.now().isoformat()

            return post
            # if self._include_comments and post.get('comment_cnt'):
                # post['comments'] = self.get_all_comments(gall_id, post_no, int(soup.find(id='comment_total_'+str(post_no)).text))
            # return post

        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout):
            # if timeout occurs, retry
            return self.get_post(gall_id, post_no)

        except NoSuchGalleryError:
            return self.get_post(gall_id, post_no)


    def get_all_comments(self, gall_id, post_no, comment_cnt):
        comment_page_cnt = (comment_cnt - 1) // COMMENTS_PER_PAGE + 1
        comments = []
        headers = {'X-Requested-With': 'XMLHttpRequest'}
        data = {'ci_t': self._session.cookies['ci_c'], 'id': gall_id, 'no': post_no}

        for i in range(comment_page_cnt):
            data['comment_page'] = i + 1

            r = self._session.post('http://gall.dcinside.com/comment/view', headers=headers, data=data)
            batch = parse_comments(r.text)
            if not batch:
                break
            comments = batch + comments

        return comments


