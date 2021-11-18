# Import <
''' keep
from backEnd.API.Utility import application
from frontEnd.Layout.Login import loginLayout
'''

# remove <
from time import sleep
from selenium import webdriver
from backEnd.API.Utility import scrapeUser
from webdriver_manager.chrome import ChromeDriverManager

# >


# >


# Main <
if (__name__ == '__main__'):

    # remove <
    username = '' # < input
    password = '' # < input

    # >

    # remove <
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://umkc.umsystem.edu/psp/csprdk/?cmd=login')
    driver.find_element_by_xpath('/html/body/table/tbody/tr/td/div[2]/div[1]/div[2]/div[1]/form/input[6]').send_keys(username), sleep(0.25)
    driver.find_element_by_xpath('/html/body/table/tbody/tr/td/div[2]/div[1]/div[2]/div[1]/form/p[2]/input').send_keys(password), sleep(0.25)
    driver.find_element_by_xpath('/html/body/table/tbody/tr/td/div[2]/div[1]/div[2]/div[1]/form/input[7]').click(), sleep(1)

    # >

    # remove <
    print(scrapeUser(driver))

    # >

    ''' keep
    application.layout = loginLayout
    application.run_server(debug = True)
    '''

# >
