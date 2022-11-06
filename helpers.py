from os.path import join, dirname, abspath
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from yaml import load, Loader

proj_root = dirname(abspath(__file__))


def get_logs_dir(): return join(proj_root, "logs")

def loadmapping() -> dict:
    data = None
    with open(join(proj_root, 'resources', 'mapping.yml'), 'r') as out_stream:
        data = load(out_stream, Loader)
    return data


def loadproperties() -> dict:
    data = None
    with open(join(proj_root, 'resources', 'properties.yml'), 'r') as out_stream:
        data = load(out_stream, Loader)
    return data


def getclientconfig() -> dict: return loadproperties()


def getwebdriver():
    chrome_options = Options()
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--headless")
    driver_path = ChromeDriverManager().install()
    driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
    driver.delete_all_cookies()
    return driver
