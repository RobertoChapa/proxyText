import mechanicalsoup

def main():
    url = 'https://whatismyipaddress.com/'
    hide_me_proxy = {'http':'207.157.25.44:80'}

    test_proxy(url, hide_me_proxy)

    return

def test_proxy(url, proxy):
    browser = mechanicalsoup.StatefulBrowser()
    browser.session.proxies = proxy
    browser.open(url)

    source_code = browser.get_current_page()
    
    print(source_code)

    return

main()


