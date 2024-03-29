from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_INPUT_LOCATOR = (By.XPATH, "//input[@id='username']")
    PASSWORD_INPUT_LOCATOR = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON_LOCATOR = (By.XPATH, "//input[@id='submit']")
    REG_HINT_LOCATOR = (By.XPATH, "//a[contains(@href,'/reg')]")
    INVALID_USERNAMEPASSWORD_LOCATOR = (By.XPATH, "//div[contains(text(),'Invalid username or password')]")
    SHORT_LOGIN_LOCATOR = (By.XPATH, "//div[contains(text(), 'Incorrect username length')]")

class RegistrationPageLocators:
    LOGIN_INPUT_LOCATOR = (By.XPATH, "//input[@id='username']")
    EMAIL_INPUT_LOCATOR = (By.XPATH, "//input[@id='email']")
    PASSWORD1_INPUT_LOCATOR = (By.XPATH, "//input[@id='password']")
    PASSWORD2_INPUT_LOCATOR = (By.XPATH, "//input[@id='confirm']")
    TERM_CHECKBOX_LOCATOR = (By.XPATH, "//input[@id='term']")
    LOGIN_HINT_LOCATOR = (By.XPATH, "//a[contains(@href,'/login')]")
    REG_BUTTON_LOCATOR = (By.XPATH, "//input[@id='submit']")
    MATCH_LOCATOR = (By.XPATH, "//div[contains(text(), 'Passwords must match')]")
    INVALID_EMAIL_LOCATOR = (By.XPATH, "//div[contains(text(), 'Invalid email address')]")
    SHORT_EMAIL_LOCATOR = (By.XPATH, "//div[contains(text(), 'Incorrect email length')]")
    EXISTS_LOCATOR = (By.XPATH, "//div[contains(text(), 'User already exist')]")
    EMAIL_EXISTS_LOCATOR = (By.XPATH, "//div[contains(text(), 'Internal Server Error')]")
    LONG_USERNAME_LOCATOR = (By.XPATH, "//div[contains(text(), 'Incorrect username length')]")

class WelcomePageLocators:
    LOGOUT_BUTTON_LOCATOR = (By.XPATH, "//a[contains(@href,'/logout')]")
    USERNAME_LOCATOR = (By.XPATH, "//div[@id='login-name']//li")
    RANDOM_FACT_LOCATOR = (By.XPATH, "//footer//p[last()]")
    API_PIC_LOCATOR = (By.XPATH, "//img[@src='/static/images/laptop.png']")
    PM_ARTICLE_LOCATOR = (By.XPATH, "//img[@src='/static/images/loupe.png']")
    WIKI_API_LOCATOR = (By.XPATH, "//h1[text() = 'API']")
    PM_TITLE_LOCATOR = (By.XPATH, "//h1[contains(text(), 'What Will the Internet')]")
    SMTP_PIC_LOCATOR = (By.XPATH, "//img[@src='/static/images/analytics.png']")
    WIKI_SMTP_LOCATOR = (By.XPATH, "//h1[text() = 'SMTP']")
    PY_HISTORY_LINK_LOCATOR = (By.XPATH, "//a[text() ='Python history']")
    FLASK_LINK_LOCATOR = (By.XPATH, "//a[text() ='About Flask']")
    PYHISTORY_TITLE_LOCATOR = (By.XPATH, "//h1[contains(text(), 'History of Python')]")
    PYTHON_BLOCK_LOCATOR = (By.XPATH, "//a[text() ='Python']")
    LINUX_BLOCK_LOCATOR = (By.XPATH, "//a[text() ='Linux']")
    FLASK_LOGO_LOCATOR = (By.XPATH, "//img[@src='_images/flask-logo.png']")
    CENTOS_LOCATOR = (By.XPATH, "//a[text() ='Download Centos7']")
    CENTOS_ANYWHERE_LOCATOR = (By.XPATH, "//text()[contains(translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'centos')]")
    NETWORK_LOCATOR = (By.XPATH, "//a[text() ='Network']")
    WIRE_NEWS_LOCATOR = (By.XPATH, "//a[@href='https://www.wireshark.org/news/']")
    WIRE_OK_LOCATOR = (By.XPATH, "//text()[contains(.,'Wireshark')]")
    WIRE_2OK_LOCATOR = (By.XPATH, "//img[@src='/assets/theme-2015/images/wireshark_logo.png']")
    WIREDOWN_OK_LOCATOR = (By.XPATH, "//strong[text()='Download Wireshark']")
    WIREDOWNLOAD_LOCATOR = (By.XPATH, "//a[@href='https://www.wireshark.org/#download']")
    TCP_EXAMPLES_LOCATOR = (By.XPATH, "//a[@href='https://hackertarget.com/tcpdump-examples/']")
    TCP_OK_LOCATOR = (By.XPATH, "//h1[text() = 'Tcpdump Examples']")