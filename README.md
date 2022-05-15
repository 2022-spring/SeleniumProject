# Selenium WebDriver with Python

-----------
## Working with Git as Version Control System

### Local git actions
- git init >> pycharm initialize VCS> Git

- git add files that needed to have versioning
  - harm select files 
- git commit "comments that summarizes the changes"
  - pycharm enter comment and click Commit 

### Remote
```git
git pull : get updates from the origin (github repo)
git push : share updates to the origin (to github repo)
```  

### Branching 
- having the multiple copies of the same repository on the same server
- Pull request, Merging to master 
- Create PR and get Approval > merg PR and close your Request

-----------------------------------

## Selenium setup
1.  download selenium
go to the Terminal (pycharm)
```python
pip install selenium # library, code written by developers, open source
pip freeze # to check the selenium is in the list
```
2. download chromedriver 
   - check the version of your chrome browser (if you dont have chrome browser, donwload and install it)
   - download the chromedriver from this location: [driver website](https://chromedriver.chromium.org/downloads)
    - select chromedriver_win32.zip if you have windows
    - Extract the downloaded folder and copy the chromedriver file

3. save in the Python main location  
   - Go to  python main folder: "C:\Program Files\Python39"
   - paste the copied chromedriver file here
    
4. import selenium, run sample code

```python
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.thelevelupsolutions.com/")
driver.maximize_window()
driver.quit() # close all tabs
```

----------------------------------

## MD document type
```
create and save file with .md extention
# - title1
## - title2

*italics text*
**bold text**

- item1
- item2

* item1
* item2

 use 3 ` to display the code snippet 
  
  [text for the link](url here)
  ![text for image](location of the image)
  [![Watch the video](https://i.imgur.com/vKb2F1B.png)](https://youtu.be/vt5fpE0bzSY)

```
Example: 
```shell
ls -l Documents
```
------------------------------

## 1. HTML DOM 

## HTML Introduction
HTML is the standard markup language for creating Web pages. Document Object Model - html document (DOM)

## What is HTML?
- HTML stands for Hyper Text Markup Language
- HTML is the standard markup language for creating Web pages
- HTML describes the structure of a Web page 
- HTML consists of a series of elements
- HTML elements tell the browser how to display the content
- HTML elements label pieces of content such as "this is a heading", "this is a paragraph", "this is a link", etc.

HTML DOM - html document object model
    this is where you find the web page elements and their 'description'.
```html
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>

</body>
</html>
```  

### Elements of HTML forms
![HTML forms](data/html-dom.svg)

--------

***NOTE: Find out more about http messages and popular status codes [here](https://www.w3schools.com/tags/ref_httpmessages.asp)***

#### Homework: 
Read and try out 
- https://www.w3schools.com/html/html_intro.asp
- https://www.w3schools.com/html/html_elements.asp
- https://www.w3schools.com/html/html_attributes.asp
- https://www.w3schools.com/html/html_links.asp
- https://www.w3schools.com/html/html_forms.asp (all other pages for html forms)



### What type of Elements we can see on the web page?
Element types are defined by tags in the HTML document (DOM)
- images 
```html
<img src="img_girl.jpg" alt="Girl in a jacket" width="500" height="600">
```

- buttons 
```html
<button name="submit" id="login" type="button">Login</button>

```  
- links 
```html
<a href="https://www.w3schools.com">Visit W3Schools.com!</a>
```  
- text box, checkbox, radio button, password etc.
The ```<input>``` tag specifies an input field where the user can enter data.
  
The different input types are as follows:
```html
<input type="button">
<input type="checkbox">
<input type="color">
<input type="date">
<input type="datetime-local">
<input type="email">
<input type="file">
<input type="hidden">
<input type="image">
<input type="month">
<input type="number">
<input type="password">
<input type="radio">
<input type="range">
<input type="reset">
<input type="search">
<input type="submit">
```  
Sample:
```html
<form action="/action_page.php">
  <label for="fname">First name:</label>
  <input type="text" id="fname" name="fname"><br><br>
  <label for="lname">Last name:</label>
  <input type="text" id="lname" name="lname"><br><br>
  <input type="submit" value="Submit">
</form>
```  
- drop down 
```html
<select><option>NY</option>State</select>

```  
- checkbox
- radio buttons
- videos 

Find out about different tags used in the html document [here](https://www.w3schools.com/tags/tag_span.asp)

### Attributes
Each element consist of attributes 
```html
<div class="myDiv" id="my-div">
  <h2>This is a heading in a div element</h2>
  <p>This is some text in a div element.</p>
</div>
```
here 'div' is a tag and 'class' is an attribute.
type

### Using chrome developers tools options to inspect web elements
-  <h4 style=color:purple>Tags are purple</h4>
- <h4 style=color:red>Attributes are in red</h4>
- <h4 style=color:blue>Values of the attributes will be in blue</h4>
- <h4 style=color:black>text in the elements, that are in the tags, will be in black</h4>

-----------------

## Selenium WebDriver: Finding Elements (locating) on the Web page.

We need to tell Selenium how to find an element so that it can simulate a desired user action, or look at the attributes or state of an element so that we can perform a check. For example, if we want to search for a product, we need to find the search text field and search button visually. We enter the search term by pressing various keys on the keyboard and click on the search button to submit our search request.

We can automate the same actions using Selenium. However, Selenium does  not understand these fields or buttons visually as we do. It needs to find the search textbox and search button to simulate keyboard entry and mouse click programmatically.

Selenium provides various find_element methods to find elements on a web page. These methods search for an element based on the criteria supplied to them. If a matching element is found, an instance of WebElement is returned or the NoSuchElementException exception is thrown if Selenium is not able to find any element matching the search criteria.

### Locator (finding the elements)
Available locators in selenium (find_element(By.locator, 'value')):
- ID
- NAME
- XPATH
- CLASS_NAME
- CSS_SELECTOR
- LINK_TEXT
- PARTIAL_LINK_TEXT

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("myapp.com")
driver.find_element(By.ID, 'search')
driver.find_element(By.NAME, 'q')
driver.find_element(By.CLASS_NAME, 'input-text')
driver.find_element(By.TAG_NAME, 'input')
driver.find_element(By.XPATH, '//form[0]/div[0]/input[0]')
driver.find_element(By.CSS_SELECTOR, '#search')
driver.find_element(By.LINK_TEXT, 'Log In')
driver.find_element(By.PARTIAL_LINK_TEXT, 'Log')
```

Selenium also provides various find_elements_by methods to locate multiple elements. These methods search and return a list of elements that match the supplied values.
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("myapp.com")
driver.find_elements(By.ID, 'products')
driver.find_elements(By.NAME, 'products')
driver.find_elements(By.CLASS_NAME, 'input-text')
driver.find_elements(By.TAG_NAME, 'a')
driver.find_elements(By.XPATH, '//div[contains(@class, "lists")]')
driver.find_elements(By.CSS_SELECTOR, '.input-class')
driver.find_elements(By.LINK_TEXT, 'Log In')
driver.find_elements(By.PARTIAL_LINK_TEXT, 'Add to')
```

Demo website: https://www.seleniumeasy.com/test/basic-first-form-demo.html

Example of Locating the element uniquely
1. xpath 
```python
msg_xpath = '//form/div/input[@id="user-message" and @class="form-control"]'
```
This is the xpath for the below element.
```html
<input type="text" class="form-control" name="input-message" placeholder="Please enter your Message" id="user-message">
Some text here
</input>
```

  
  **Tags to know:**
```html
links, images, forms (textbox, radio, checkbox, submit, fileupload, <input>, <label>, <select>, <textarea>, <button>)
    div - container to holds the styled elements
CSS - styling document, goes along with html document 
```

**NOTE: read about html click [here](https://www.w3schools.com/w3css/default.asp)**


## 2. WebDriver class 
simulates browser action 
- properties: 	current_url, current_window_handle, window_handles, name,
				title, 
- methods: 		find_element(), send_keys(), switch_to.window(), back(), 	
				refresh() ....

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.back()
driver.forward()
driver.find_element(By.XPATH, 'somexpath')
driver.refresh()
driver.get()
driver.implicitly_wait(10)
driver.maximize_window()
```

-----------
## API - application programming interface
SOAP - xml, older api type
REST API - json, xml (http messages and responses)

add.resources('/query')
def query(function, symbol, apikey):
	# verify apikey
	# find global quote for symbol

```commandline
https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey=OZ8SJC8A5DGNC

https://dog.ceo/api/breed/hound/english/images/random

```

** Homework**
Read about different message types, this will help you to understand the API and messages used in an API as a connection between server and webpage(local on the browser)
Method: GET, POST, PUT, DELETE
Note: remember status codes: 200, 401, 404, 500, 300, 201

-------------------------

## 3. WebElement class
simulates element actions 
Done topics: 
- Working with find_elements() - returns list of elements
- Webelement properties (text, size, tag_name) 
- Webelement methods: clear(), click(), send_keys(), is_displayed(), is_enabled(), get_attribute()
- Working with alerts and pop-up windows (from previous session, from webdriver class) 
- Working with forms, textboxes, checkboxes, and radio buttons
- Working with dropdowns and lists


```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

element = driver.find_element(By.XPATH, 'somexpath')
element.is_displayed()
element.is_enabled()
element.is_checked()
element.click()
element.send_keys("your message here ")
element.send_keys(Keys.RETURN)  # hitting the enter key 
element.send_keys(Keys.ESCAPE) 
element.send_keys(Keys.UP) 
element.text   # property - you must not use parenthesis
```

Assertion: 
- from python to verify something
- it generates pass/fail status in unittests

```python
Xpath="//tagname[@attribute='value']"
msg_xpah = "//input[@name = 'input-message']"

```

---------------

## Agenda for next classes on Selenium:

## 4. Synchronizing Tests
Difference between implicit and explicit waits
What is explicit wait?
How to build explicit wait with different conditions?


Synchronization methods: explicit wait : WebDriverWait class, expected_conditions class
 *practice here: https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver *

WebDriver provides the WebDriverWait and
expected_conditions classes to implement an explicit wait.
  [practice website](https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver)

## 5. Chapter 9. Advanced Techniques of Selenium WebDriver 

*practice here: https://jqueryui.com/droppable/*

In this chapter, you will learn more about:
- Creating tests that simulate keyboard or mouse events using the Actions class
- Simulating mouse operations such as drag-and-drop and double-click
- Running JavaScript code:  execute js >> alternative of button.click()
    (we have seen how to scroll down on the page)
- Capturing screenshots and movies of test runs


## 6. Chapter 8. Framework in Test Automation
The way of engineering your project, put your code in structured way: 

- Pytest - unit testing framework 
    - to generate test reports with pass and fail status.
    - hooks(fixtures)
    this will help you to better manager your execution
    - how to run regression suites
    
- Page Object Modeling (designing pattern)
    - handle locators and page functions of each page 
    - this is good when you work with complex project.
    - helps you to maintain changing web elements
    - Classes, Inheritance, encapsulation,  polymorphism
 
### General Understanding about Test Automation Frameworks


#### 1. Data Driven Framework:
Driver Script per scenario -> Data File -> input/output file
Driver script per scenario >> Data file >> execution >> compare with expected results

#### 2. Keyword Driven Framework:
Driver Script > Keyword(steps consist of function names and inputs) >> data file


#### 3. Behavior Driven Framework (from Test Automation perspective) 

**Components of BDD Test Automation Framework

1. src: 
    a. Feature file: Gherkin scenarios (plain english using Given, When, Then keywords) 
        Given I am in login page.
		
    b. Steps definition
        @Given("I am in login page.")
        def login():
            # steps to login, code

    c. pages: Page Object Modeling Design Pattern, The way of designing your selenium scripts 
        - Object oriented programming concepts (class, object, Inheritance, encapsulation, polymorphism, abstraction)
		
    d. utilities.py | helper.py | generic_helper.py  >> functions to use to handle data file, reports, general python functions
	
    e. Fixture files (in pytest it is confest.py ), some framework config files
	
	
2. Data 
    - config.yml
    - stocks_buy.yml

3. Logs
    - 05152022.log

4. Reports 
    - 051520221110052_stockbuy_report.html
	



--------
 
### PYTEST

running tests : 
```python
pytest -s -v test_scenarios.py
pytest -s -v test_scenarios.py::test_sample_pytst

# if you have marks for the functions
pytest -s -v -m sample1

$ pytest -s -v -m regression --disable-pytest-warnings >> reports/20211123_919_regression

```
Pytest Fixtures

- SetUp : steps to execute before session/file/functions (scope)
- TearDown : steps to execute after session/file/functions (scope)
 
---------------------------------------------------------		

## Must-know for Automation Testing: 
- Web UI Functionality (python, selenium WebDriver, Yes)

- API Automation
	- manual (Yes) : Postman tool, study API testing and webservices 
		(Akmal to send a video about this)
	- Automation (maybe, REQUESTS library) (Akmal to send links for quick courses)
    ***NOTE: Find out more about http messages and popular status codes [here](https://www.w3schools.com/tags/ref_httpmessages.asp)***


- Backend Automation 
    (NO, sql connection with python, server side automation with python)

- Performance testing (NO - jmeter, LoadRunner etc.)
- Security Testing (i.e.Penetration testing, NO)

### Self Study Materials: Chapter 10 Integration with Other Tools and Frameworks

Videos to watch: 
- [Bdd Framework Overview](https://drive.google.com/drive/folders/1dTlgpj4hBUGba-W-eyLr5JRTeBAVlJB-?usp=sharing)
- [CI/CD pipelines and working with Jenkins and AWS](https://drive.google.com/drive/folders/1GEP_Bw_mQVpc2RDdZS3AIUk_UygyzwPA?usp=sharing)
- [All Mock interviews to watch](https://drive.google.com/drive/folders/1oxyinen_o7BWBTrUSNzhhcvsrVXbUpI3?usp=sharing)


----- 
**Automation practice websites:**
- https://courses.letskodeit.com/practice
- https://jqueryui.com/droppable/
- https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver


## Useful links and References: 
1. [HTTP messages used in API calls](https://www.w3schools.com/tags/ref_httpmessages.asp)
2. [HTML document and tags](https://www.w3schools.com/tags/tag_span.asp)
3. [Learning Selenium Testing Tools with Python (book)](data/Learning_Selenium.pdf)
4. [What is xpath and how to build them.](https://www.guru99.com/xpath-selenium.html)
5. [Socratica playlist in youtube](https://youtu.be/bY6m6_IIN94)












