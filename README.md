# Attendance Using QR Code on Flask Python 3

This project will create attendance using QR Code.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Make sure you have installed Python 3 on your device

### How To Run
1. Install requirement
```
pip install -r requirements.txt
```
2. Install ZBar Third Party App
```
MacOS > brew install zbar
Linux > apt-get install libzbar-dev libzbar0
```
3. Change `Camera.py` file on IP Address of RSTP with port for your device
4. Migrate database
```
flask db init
flask db migrate
flask db upgrade
```
5. Install [RSTP Camera Server](https://play.google.com/store/apps/details?id=com.miv.rtspcamera) on your android, then start camera server
6. Run the application
```
python run.py
```

## Built With

* [Python 3](https://www.python.org/download/releases/3.0/) - The language programming used
* [Flask](http://flask.pocoo.org/) - The web framework used
* [Flask-Migrate](https://pypi.org/project/Flask-Migrate/) - The database migration
* [Virtualenv](https://virtualenv.pypa.io/en/latest/) - The virtual environment used
* [SQL Alchemy](https://www.sqlalchemy.org/) - The database library
* [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) - Flask and SQL Alchemy connector
* [OpenCV-Python](https://pypi.org/project/opencv-python/) - Open CV for Python
* [PyQRCode](https://pypi.org/project/PyQRCode/) - QR Code Generator

## Clone or Download

You can clone or download this project
```
> Clone : git clone https://github.com/piinalpin/absent-qrcode-python.git
```

## Authors

* **Alvinditya Saputra** - [LinkedIn](https://linkedin.com/in/piinalpin) [Instagram](https://www.instagram.com/piinalpin) [Twitter](https://www.twitter.com/piinalpin)
