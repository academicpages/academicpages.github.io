from notebook import i18n

def test_parse_accept_lang_header():
    palh = i18n.parse_accept_lang_header
    assert palh('') == []
    assert palh('zh-CN,en-GB;q=0.7,en;q=0.3') == ['en', 'en_GB', 'zh', 'zh_CN']
    assert palh('nl,fr;q=0') == ['nl']
