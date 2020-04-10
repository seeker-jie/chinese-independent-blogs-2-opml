# coding=utf-8
import requests
import logging
from lxml import etree


logger = logging.getLogger()


class Spider:

    def __init__(self):
        self.url = "https://github.com/timqian/chinese-independent-blogs"
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X \
            10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
        self.tag_set = set()
        self.name_list = ['xmlUrl', 'text', 'htmlUrl']
        self.count = 0

    def parse_url(self):
        response = requests.get(self.url, self.headers).content.decode()
        return response

    @staticmethod
    def get_str(list):
        if len(list):
            return list.pop()
        else:
            return None

    def get_content(self, html_str):
        html = etree.HTML(html_str)
        tr_list = html.xpath("//*[@id='readme']/div[3]/article/table/tbody/tr")
        content_list = []
        for tr in tr_list:
            content = {}
            rule_list = ['./td[1]/a/@href', './td[2]/text()', './td[3]/a/@href']
            for i in range(len(self.name_list)-1):
                str = self.get_str(tr.xpath(rule_list[i]))
                if str:
                    content[self.name_list[i]] = str
            tags = tr.xpath("./td[4]/text()")[0].split(";")
            content["tags"] = []
            for tag in tags:
                tag = tag.lstrip()
                if len(tag) == 0:
                    continue
                content["tags"].append(tag)
                self.tag_set.add(tag)
            content_list.append(content)
        return content_list

    def run(self):
        html_str = self.parse_url()
        return self.get_content(html_str)
