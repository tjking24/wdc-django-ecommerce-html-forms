from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound

from products.models import Product, Category, ProductImage


def products(request):
    	
    products = Product.objects.all() 
    featured_products = Product.objects.filter(featured=True)[0:4] 
 
    return render(request,'products.html',
					context={'products': products, 
							'featured_products': featured_products})

def create_product(request):
    categories = Category.objects.all()
     
    if request.method == 'GET':
		return render(request, 'create_product.html', 
					context={'categories':categories})  
	elif request.method == 'POST':
		
		fields = ['name', 'sku', 'price']
		errors = {}
        
		for field in fields:
			if not request.POST.get(field):
				errors[field] = 'Missing Field. You need to enter the {}'.format(field)
		
		if errors:
			return render(request,'create_product.html',
									context= {'errors': errors})							
							
		name = request.POST.get('name')
		if len(name) > 100:
			errors['name'] = "Name can't be longer than 100 characters."

		sku = request.POST.get('sku')
		count = [letter for letter in sku if re.search('[a-zA-Z]',letter)]
		if len(count) < 8:
			errors['sku'] = "Sku must contain 8 alphanumeric characters"
			
    
		price = float(request.POST.get('price'))
		if price <0 or price >= 10000:
			errors['price'] = "Price must be greater than $0 and less than $1000" 
      
        
		if errors:
			return render(request,'create_product.html',
									context= {'errors': errors})
		
		category = Category.objects.get(name = request.POST.get('category'))
		
		
		product = Product.objects.create(name = name,
										sku = sku,
										category = category,
										description = request.POST.get('description'),
										price = price)
		
		images = ['image_1', 'image_2', 'image_3']
		
		images_url = [request.POST.get(image) for image in images]
		
		_ = [ProductImage.objects.create( product=product, url=image_url) for image_url in images_url if len(image_url) > 1 ]
		
		return redirect('products')

def edit_product(request, product_id):
    # Get product with given product_id
	product = Product.objects.get(id=product_id)
   
	categories = Category.objects.all()
    
	product_images = [image.url for image in product.productimage_set.all()]
	
	
	if request.method == 'GET':
		
		return render(request,'edit_product.html',context={'product':product,
													'categories':categories,
													'images':product_images})	

	elif request.method == 'POST':
        
		fields = ['name', 'sku', 'price']
		errors = {}
		
		for field in fields:
			
			if not request.POST.get(field):
				errors[field] = 'Missing Field. You need to enter the {}'.format(field)
		
		if errors:
			return render(request,'create_product.html',
									context= {'errors': errors})							
			
          
		product.name = request.POST.get('name')
		product.sku = request.POST.get('sku')
		product.price = float(request.POST.get('price'))
		category = Category.objects.get(name=request.POST.get('category'))
		product.category = category
		product.save()

		images = ['image-1', 'image-2', 'image-3']
		
		images_url = [request.POST.get(image) for image in images]
		
		
		for image_object in product.productimage_set.all():
			if image_object.url not in images_url:
				image_object.delete()
		
		for url in images_url:
			if url in product_images:
				continue
			if url is not '': 
				ProductImage.objects.create(product=product, url=url)
	
		return redirect('products')



def delete_product(request, product_id):
    
    product = Product.objects.get(id=product_id)
	if request.method == 'GET':
      
		return render(request, 'delete_product.html', context={'product':product})

	elif request.method == "POST":
		product.delete()
		return redirect('products')
    
    
  


def toggle_featured(request, product_id):
    product = Product.objects.get(id=product_id)
    
    product.featured = True 
    product.save()
    
    return redirect('products')