from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

proxy = Proxy({
    'proxyType': 'MANUAL',
    'httpProxy': '1.2.3.4:8080',
    'sslProxy': '1.2.3.4:8080',
})

capabilities = DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)

driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
    desired_capabilities=capabilities
)

driver.get('http://www.baidu.com/')
driver.find_element_by_id('kw').send_keys('ip')
driver.find_element_by_id('su').click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'nums_text'))
)

driver.close()
