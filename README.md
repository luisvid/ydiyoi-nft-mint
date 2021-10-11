# OpenVino Baas256 NFT minting service

A RESTful service for minting NTFs using Python and Flask_restful

### Prerequisites

Python 3.9.0

### Installing

## Clone the repo:

```sh
git clone https://github.com/luisvid/financial-scraping-service.git
```

## Install dependencies:

```sh
pip install -r requirements.txt
```

## some installed dependencies are:

    Flask

    Flask-RESTful API

    eth-brownie

    gunicorn

## Make it Heroku ready

Install gunicorn, which is a WSGI used to run python application on Heroku.

```sh
pip install gunicorn
```

Create Procfile without extension to help Heroku to understand which piece of your code to run to start the application.

```sh
web: gunicorn app:app
```

Set the python version in the runtime.txt file in the root folder.

```sh
python-3.9.0
```

## Heroku deploy

```sh
heroku login
```

```sh
heroku create — will create an app in heroku
```

```sh
heroku git:remote -a app-name — app-name is the name of the Heroku application created in the previous step
```

```sh
git push heroku main — pushes the changes to heroku
```
```sh
heroku logs --tail - check app logs from Heroku CLI
```

### Documentation 

Refer to:

[Pandas DataFrame is not JSON serializable](https://github.com/flask-restful/flask-restful/issues/269)
Flask-RESTful's json serialization isn't at fault here. If you return an object from a restful.Resource method, Flask-RESTful will call json.dumps on it. In this case, you're using a custom class that defines it's own serialization method: to_json(). To bypass Flask-RESTful's json.dumps attempt create a raw Response object.