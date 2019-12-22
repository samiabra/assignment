# assignment

Installation Requirements:

pip install grequests

pip install PySide2

maybe: pip install pysqlite3 

maybe: pip install db-sqlite3

maybe: sudo apt-get install python3-tk

The appliacion uses database to store the result and the result will also be fetched from database and save in a json file.
The application provides two different UIs (tkinter and Qt), you can decide which one you prefer (uncomment what you like and comment what you dislike)

'grequests' is used for the asynchronous requests for more details: https://pypi.org/project/grequests/

Input, you can provide the UI with a list of URLs (e.g. https://www.google.fi , https://www.yahoo.com) via UI and the output is Timestamp, the url and HTTP status code, and HTTP header for each request

------------------------------------------------------------Attention------------------------------------------
If you prefer Jupyter Notebook then you can try assignment.ipynb.

1. Open anaconda (Jupyter Notebook)
2. Restart and Run all
3. If you get No module ..... error , please create a new cell and the add " %pip install the_model_name " to the cell and then run the cell. Take the first cell in assignment.ipynb as an example :)
