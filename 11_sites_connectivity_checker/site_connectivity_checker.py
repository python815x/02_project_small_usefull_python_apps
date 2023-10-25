import urllib.request as urllib_request


def connection_check(url):
    print('Checking connection to ' + url)

    response = urllib_request.urlopen(url)

    print(f'Got response: {response.getcode()}')


print('This is a connection checker for URLs')
input_url = input('Input the url of the site you want to check: ')

connection_check(input_url)
