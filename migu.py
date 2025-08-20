# -*- coding: utf-8 -*-
# @Author  : Red
# @Time    : 2025/8/20

import sys
import requests
sys.path.append('..')
from base.spider import Spider


class Spider(Spider):
    def getName(self):
        return "M3ULoader"

    def init(self, extend):
        self.extend = extend

    def getDependence(self):
        return []

    def liveContent(self, url):
        m3u_url = self.extend.get("https://raw.githubusercontent.com/timelapse4/migu/refs/heads/main/sportsmigu.m3u")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Android 14; Mobile) AppleWebKit/537.36 Chrome/114.0.0.0 Safari/537.36'
        }
        response = requests.get(m3u_url, headers=headers)
        lines = response.text.splitlines()

        tv_list = ['#EXTM3U']
        current_name = ""
        for line in lines:
            if line.startswith('#EXTINF'):
                # Extract channel name
                parts = line.split(',')
                current_name = parts[-1].strip()
                group = "กีฬา" if "Sport" in current_name else "ทั่วไป"
                logo = f"https://live.fanmingming.cn/tv/{current_name}.png"
                tv_list.append(f'#EXTINF:-1 tvg-id="" tvg-name="{current_name}" tvg-logo="{logo}" group-title="{group}",{current_name}')
            elif line.startswith('http'):
                tv_list.append(line)

        return '\n'.join(tv_list)

    def homeContent(self, filter):
        return {}

    def homeVideoContent(self):
        return {}

    def categoryContent(self, cid, page, filter, ext):
        return {}

    def detailContent(self, did):
        return {}

    def searchContent(self, key, quick, page='1'):
        return {}

    def searchContentPage(self, keywords, quick, page):
        return {}

    def playerContent(self, flag, pid, vipFlags):
        return {}

    def localProxy(self, params):
        return {}

    def destroy(self):
        return "Destroying..."

if __name__ == '__main__':
    pass