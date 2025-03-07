from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    """


    driver_path =ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)
    #
    # #
    # chrome_options = Options()
    # mobile_emulation = {"deviceName": "Nexus 5"}
    # #chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # #driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
    #                           #desired_capabilities=chrome_options.to_capabilities())

    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service, options=chrome_options)

    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(service=service, options=options)

    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver=webdriver.Firefox(service=service)




    # # # ---- BROWSERSTACK ----
    # bs_user = 'maralmajidli_lSNKum'
    # bs_key = 'qpfRaSgmXazBa1uqzg1f'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     "os": "OS X",
    #     "osVersion": "Sonoma",
    #     'browserName': 'Safari',
    #     'browserVersion': '17.3',
    #     'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)



    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
