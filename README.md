# assignment

Installation Requirements:

pip install grequests
pip install PySide2


The appliacion uses database to store the result and the result will also be fetched from database and save in a json file.
The application provides two different UIs (tkinter and Qt), you can decide which one you prefer (uncomment what you like and comment what you dislike)

'grequests' is used for the asynchronous requests for more details: https://pypi.org/project/grequests/

Input, you can provide the UI with a list of URLs (e.g. https://www.google.fi , https://www.yahoo.com) via UI and the output is Timestamp, the url and HTTP status code for each request

