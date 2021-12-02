# Import <
from backEnd.API.Utility import application
from frontEnd.Layout.Login import loginLayout

from frontEnd.Layout.Home import homeLayout # remove
from backEnd.API.Utility import Verify, Authenticate, scrapeUser, scrapeSchedule # remove

# >


# Main <

if (__name__ == '__main__'):

    application.layout = loginLayout
    application.run_server(debug = True)

    '''driver = Verify('', '')
    driver = Authenticate(driver)
    driver = Authenticate(driver, code = input('Code: '))
    driver, name = scrapeUser(driver)
    driver, schedule = scrapeSchedule(driver)'''

# >
