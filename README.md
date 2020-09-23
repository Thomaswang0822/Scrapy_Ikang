# Scrapy_Ikang
## Project Description:
Use scrapy in python to crawl: https://mall.ikang.com/ <br />
This is an advanced web-crawling example, because the website has anti-crawler mechanism <br />
Thus, we use selenium package together with scrapy. <br />
Selenium can simulate web-browser actions like opening the browser, scrolling, clicking a button, switching back and forth among tabs, etc. <br />
The key feature to use in selenium is driver. Driver "directs" those actions mentioned above <br />

## Set up
1) Install Google Chrome browser. It's most commonly-used in selenium and probably has the best performance <br />
2) Install chromedriver from: https://chromedriver.chromium.org/downloads <br />
NOTICE: You need to check the particular version of your Chrome and download the corresponding driver.. Find it in setting->About Google Chrome. <br />
3) Unzip the file and put it into your project folder. <br />
4) Install scrapy, selenium package and make sure they can functions in your project environment <br />

## Special Notice
Make sure you put the unzipped chromedriver executable in the correct place, otherwise you get error when initializing the driver. <br />
The STARTER.py file is just for convinience. You don't need to type in the terminal, just run this file in your IDE. <br />

## Additional Feature: saving data into your database
1) I use PostgreSQL for a local database. I want to save the data into the table I created. Each item in scrapy is a row (a piece of data) in the table.
2) You can either execute simple sql commands to create a table, or manually create it in your PostgreSQL visualization software, like Navicat. (It's paid, but super powerful)
3) Remember to set the data type of each field in your table to be varchar. 
4) Most importantly, the length of field 'exams' (all medical examinations included in the product) should be long enough, 1023 for me, otherwise you get error when writing data.
5) After creating table, we need to modify pipeline.py enable data writing. Functions open_spider() and close_spider simply connect to and disconnect from your DB. Function process_item write each of your item into the DB.
6) Last step, enable pipeline feature. Just uncomment those 3 lines in settings.py

## Special Thanks
Special thanks to Harry Wang, https://github.com/harrywang <br />
for his fantastic end-to-end tutorial (it has 5 parts), https://towardsdatascience.com/a-minimalist-end-to-end-scrapy-tutorial-part-i-11e350bcdec0  <br />
and his scrapy-selenium-demo, https://github.com/harrywang/scrapy-selenium-demo <br />
