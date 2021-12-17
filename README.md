# COVID-19 Dashboard programming project

Description
------------
The aim of this programming project was to design a user interface which displayed news articles relating to COVID-19 as well as COVID data concerning Exeter and England. The news articles have been filtered so only those with the key terms "covid", "covid-19" and "coronavirus" are shown.

Prerequisites and Installation
------------------------------
This project used Python 3.9.9 so before you run the code, please ensure that the correct version of Python is being used

You will need to install some packages using pip:
- 'pip install flask'
- 'pip install newsapi-python'
- 'pip install pytest'

A news api key is required for this program which you can get from https://newsapi.org/

How to run
----------
To launch the program, you run flask_interface.py then click on http://127.0.0.1:5000/. To get to the /index page simply add 'index' to the end of the link.

Testing
-------
The pytest module is used to test the functions
This can be installed with 'pip install -U pytest'

License
-------
MIT License

Copyright (c) 2021 ksyh201

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
