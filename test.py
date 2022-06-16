import Request

def scrape_webpage_text_raw(url):

    import urllib.request
    headers = {
        "User-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
    }
    request = Request(url, headers=headers)
    html = urlopen(request).read()
    soup = BeautifulSoup(html, "html.parser")
    # kill all script and style elements
    for script in soup(["script", "style", "meta", "[document]"]):
        script.extract()    # rip it out
    # get text
    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text

scrape_webpage_text_raw("http://microsoft.com/")