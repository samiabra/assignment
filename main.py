#!/usr/bin/env python3
import sys
from tkurl import URLForm1
from mydb_sqlite import *
import json
from PySide2.QtWidgets import QApplication
from gtkui import URLForm


def activate_qt():
    app = QApplication(sys.argv)
    widget = URLForm()
    widget.resize(400, 300)
    widget.show()
    sys.exit(app.exec_())


def activate_tk():
    app = URLForm1()
    app.mainloop()
    return


# a json file will be create from the data maintained in the database
def generate_json_file():
    create_table()
    with open('url_to_json.json', 'w') as outfile:
        json.dump(json.dumps({'results': get_values()}), outfile)
    return


def main():
    generate_json_file()

    # you if you prefer Tkinter
    activate_tk()

    # if you prefer Qt then you can uncomment activate_qt() and comment activate_tk()
    #activate_qt()


if __name__ == '__main__':
    main()
