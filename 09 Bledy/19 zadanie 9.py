import webbrowser

class URLError(Exception):
    """ custom error for URL"""
    pass


def check_url(url):
    prefixes = ('http://', 'https://', 'www')
    suffixes = ('.pl', '.com')

    if not url.startswith(prefixes):
        raise URLError("Błąd prefixu")

    if not url.endswith(suffixes):
        raise URLError("Błąd sufixu")

    return url

def open_url(url_address):
    try:
        url = check_url(url_address)
        webbrowser.open(url)
    except URLError as err:
        print("błędny URL", err)
    else:
        print("status ok")

def main():
  url = input("podaj adres www:")
  open_url(url)

if __name__ == '__main__':
        main()

