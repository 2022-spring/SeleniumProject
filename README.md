# Working with Git 

## Local git actions
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


Selenium topics to go through:
----

## 1. HTML DOM 
- hw: https://www.w3schools.com/html/
  - <tagname>Content goes here...</tagname>
  - purple - tagname
  - red - attribute
  - blue - attribute value
  - black - Content/text of the element
  
  **Tags to know:**
```html
	links, images, forms (textbox, radio, checkbox, submit, fileupload, <input>, <label>, <select>, <textarea>, <button>)
        div - container to holds the styled elements
    CSS - styling document, goes along with html document 
```

**NOTE: read about html click [here](https://www.w3schools.com/w3css/default.asp)**

### MD document type
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


## Locator (finding the elements)
Available locators in selenium (find_element(By.locator, 'value')):
- ID
- NAME
- XPATH
- CLASS_NAME
- CSS_SELECTOR
- LINK_TEXT
- PARTIAL_LINK_TEXT

## 2. WebDriver class 
simulates browser action 
- properties: 	current_url, current_window_handle, window_handles, name,
				title, 
- methods: 		find_element(), send_keys(), switch_to.window(), back(), 	
				refresh() ....

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

Method: GET, POST, PUT, DELETE
response code: 200, 201, 300, 401, 404, 500


## 3. WebElement class
simulates element actions 
Done topics: 
- Working with find_elements() - returns list of elements
- Webelement properties (text, size, tag_name) 
- Webelement methods: clear(), click(), send_keys(), is_displayed(), is_enabled(), get_attribute()
- Working with alerts and pop-up windows (from previous session, from webdriver class)

  TODO: 
- Working with forms, textboxes, checkboxes, and radio buttons
- Working with dropdowns and lists

## 4. Synchronizing Tests
Difference between implicit and explicit waits
What is explicit wait?
How to build explicit wait with different conditions?

## 5. Advanced Techniques of Selenium WebDriver
mouse movement, Executing JavaScript
	
## 6. Framework in Test Automation
way of engineering your project, put your code in structured way: 

- Page Objects Modeling (design pattern) 
    using classes, objects, inheritence, encapsulation
- Pytest - unit testing framework 
    - to generate Pass/Fail status, generate reports 














