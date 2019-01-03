<img align="right" width="120" alt="rmotr.com" src="https://user-images.githubusercontent.com/7065401/45454218-80bee800-b6b9-11e8-97bb-bb5e7675f440.png">

# Django Ecommerce HTML Forms

### Setup Instruction

The structure of the whole Django project is built for you. Run the following commands in order to have your local environment up and running.  

```bash
$ mkvirtualenv -p $(which python3.5) django_ecommerce_html_forms
$ pip install -r requirements.txt
```

You can now run the development server and point the browser to the correct URL:

```bash
$ make runserver
```

You will have a superuser already created (username: `admin`, password: `admin`) that you can use when pointing to `http://localhost:8080/admin` in your browser with the server running. There you can find the Django admin site where you will be able to create, delete and modify objects from your database.

The database already contains some objects that we have created for you, but feel free to interact with it the way you want.

There's also a LIVE version of the solution so you can try it and check how everything should work:

https://wdc-ecommerce-html-forms.herokuapp.com/products/

![image](https://user-images.githubusercontent.com/1155573/49093930-ee53cc80-f243-11e8-93d1-6fb6a8f9d183.png)

### Your Tasks

Everything that you have to do for this practice will be located inside `products/views.py` file and `products.html` template.
There you'll find some hints and instructions that will guide you in your tasks. Also you can check the branch `solution` in this repo that contains the code running in the LIVE version mentioned above.

#### Task 1: Products list

For the first task, you'll focus on the `products` view inside `products/views.py` and `products.html` template. The template is kind of a static version that you'll have to write some logic in it using the Django template engine, like forloops or inserting data that came from the view.


#### Task 2: Creating a product

Second task will be focused on `create_product.html` template and `create_product` view. The idea is to complete everything that is needed in the form template, and make the proper input validations inside the view. If no errors occurs during the validation, the product object will be created (along with its images) and the user will be redirected to the products page.

If any of the validations fails, the `create_product.html` template must be re-rendered sending an `errors` dictionary containing the messages that will be displayed below each invalid input.


#### Task 3: Editing a product

This task is pretty similar to the one above, but you will be editing an already existing product in the DB instead of creating a new one.
You'll focus on `edit_product` view and `edit_product.html` template. Every particular cases are explained as comments inside the given code.


#### Task 4: Deleting a product

For this task you'll write a view that handles the deletion of a product when clicking the icon in the products table. The view `delete_product` will render a `delete_product.html` confirmation template when receives a GET request with a product_id, or will delete the product when receives a POST request.


#### Task 5: Mark a product as featured

The idea of this task is to mark products as featured in order to show them in the cards on top of products page. For this you'll have to work on `toggle_product` view that will be triggered when clicking the star icon in the products list.

This view will receive the product_id, get the product from the DB and toggle its `featured` boolean field. Then it redirects back to products page.
