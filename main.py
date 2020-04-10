from Spider import Spider
from save_as_opml import save_to_opml


if __name__ == "__main__":
    spider = Spider()
    content_list = spider.run()
    save_to_opml(content_list, spider.tag_set, spider.name_list)
