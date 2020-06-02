from selenium import webdriver
from os import system

Initials = '''
\t\t\t\t _    _      _    ______                  _____           _ 
\t\t\t\t| |  | |    | |   | ___ \                |_   _|         | |
\t\t\t\t| |  | | ___| |__ | |_/ / __ _____  ___   _| | ___   ___ | |
\t\t\t\t| |/\| |/ _ \ '_ \|  __/ '__/ _ \ \/ / | | | |/ _ \ / _ \| |
\t\t\t\t\  /\  /  __/ |_) | |  | | | (_) >  <| |_| | | (_) | (_) | |
\t\t\t\t \/  \/ \___|_.__/\_|  |_|  \___/_/\_\___, \_/\___/ \___/|_|
\t\t\t\t                                       __/ |                
\t\t\t\t                                      |___/                 
\n\t\t\t\t\t Created By : GitHub | amitray007\n
'''

if __name__ == '__main__':
    system('title AutoWebProxy Tool - By GitHub : amitray007')
    while True:
        _ = system('cls')
        print(Initials)

        siteAddress = input(' [+] Enter Website address to surf anonymously : ')

        menuKey = int(input('\n [+] Available Feature\n [1] Enter Proxy Manually\n [2] Enter Proxy Automatically\n\n [+] Enter your Choice : '))

        if menuKey == 1:
            proxy = str(input('\n [+] Enter HTTPS Proxy (IP:Port) : '))

            print(" [+] NOTE : If Website doesn't loads after sometime, it maybe because of Invalid/Inactive Proxy.")

            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--proxy-server=http://{}'.format(proxy))

            chrome = webdriver.Chrome(options=chrome_options)
            chrome.get(siteAddress)
        elif menuKey == 2:
            driver = webdriver.Chrome()
            driver.get('https://proxyscrape.com/web-proxy')

            driver.find_element_by_xpath('/html/body/main/div/div/div[2]/div/form/input').send_keys(siteAddress)
            driver.find_element_by_xpath('/html/body/main/div/div/div[2]/div/form/button').click()
        else:
            input(' [+] Wrong Input! Press Enter to get back to main menu ... ')
