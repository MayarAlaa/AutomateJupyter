from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# create a new Firefox session
driver = webdriver.Edge()
driver.implicitly_wait(300)
driver.maximize_window()

# navigate to the Jupyter notebook server
driver.get("https://dqelearn.trainings.dlabanalytics.com/msaleh/")

# enter the password
elem = driver.find_element("id","password_input")
elem.send_keys("YOUR_JUPYTER_NOTEBOOK_PASSWORD")
elem.send_keys(Keys.RETURN)

# click on the notebook you want to run
elem = driver.find_element("name","Task2_DQ_Python.ipynb")
elem.click()

# wait for the notebook to load
# elem = driver.find_element("id","assignment_pandas")

# run the notebook
driver.execute_script("Jupyter.notebook.execute_all_cells();")

# close the browser
driver.quit()