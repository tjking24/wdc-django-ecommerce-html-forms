<img align="right" width="120" alt="rmotr.com" src="https://user-images.githubusercontent.com/7065401/45454218-80bee800-b6b9-11e8-97bb-bb5e7675f440.png">

# Django Ecommerce HTML Forms

### Setup Instruction

The structure of the whole Django project is built for you. Run the following commands in order to have your local environment up and running.  

```bash
$ mkvirtualenv -p $(which python3) django_ecommerce_html_forms
$ pip install -r requirements.txt
```

You can now run the development server and point the browser to the correct URL:

```bash
$ make runserver
```

You will have a superuser already created (username: `admin`, password: `admin`) that you can use when pointing to `http://localhost:8080/admin` in your browser with the server running. There you can find the Django admin site where you will be able to create, delete and modify objects from your database.

The database already contains some objects that we have created for you, but feel free to interact with it the way you want.
