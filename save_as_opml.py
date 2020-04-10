def get_rss(content_list, tag_set, name_list):
    rss = ""
    for tag in tag_set:
        rss += '<outline title="%s" text="%s">\n' % (tag, tag)
        for content in content_list:
            if tag in content.get('tags'):
                rss += '<outline type="rss" '
                for i in range(3):
                    key = name_list[i]
                    value = content.get(key)
                    if value:
                        rss += '%s="%s" ' % (key, value)
                rss += 'title="%s" ' % content["text"]
                rss += "/>\n"
        rss += '</outline>\n'
    return rss


def save_to_opml(content_list, *args):
    rss_start = """<?xml version="1.0" encoding="UTF-8"?>\n<opml version="2.0">\n<head>\n<title>RSS</title>\n</head>\n<body>"""
    rss_endswith = """</body>\n</opml>\n"""
    rss = get_rss(content_list, *args)
    rss = rss.join([rss_start, rss_endswith])
    with open("rss.opml", mode='w', encoding='utf-8') as f:
        f.write(rss)
