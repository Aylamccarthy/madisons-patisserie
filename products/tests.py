
"""
Product App - Tests
----------------
Tests for Product App.
"""


from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.urls import reverse
from products.models import Product, Category
from products.forms import UpdateProductForm


class TestViews(TestCase):
    """
    Unit Tests for Products App
    """

    def setUp(self):
        """Create test login"""

        # creates test user
        email = "testuser@yahoo.com"
        username = "username"
        pswd = "T12345678."
        user_model = get_user_model()
        self.user = user_model.objects.create_user(
            username=username, email=email, password=pswd
        )
        logged_in = self.client.login(email=email, password=pswd)
        self.assertTrue(logged_in)

        # creates test category object
        self.category = Category.objects.create(
            name="cakes",
            friendly_name="Cakes",
        )

        # # creates test product object
        self.product = Product.objects.create(
            category=self.category,
            sku="ca101994",
            name="Fresh Cream Cake",
            type="dessert",
            code="107901",
            price=25.00,
            image="fresh_cream_cake.jpg",
            stock=100,

        )

    def test_products_page(self):
        """ Test if products page renders correct page when user is
        authenticated as client user"""
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_products_page_neauthenticated(self):
        """ Test if products page renders correct page
        without user authentication """
        self.client.logout()
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_products_context(self):
        """ Test if context is rendered to create products page"""
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('products' in response.context)
        self.assertTrue('search_term' in response.context)
        self.assertTrue('current_category' in response.context)
        self.assertTrue('categories' in response.context)
        self.assertTrue('current_url' in response.context)
        self.assertTrue('current_url_no_filters' in response.context)
        self.assertTrue('remove_filter' in response.context)
        self.assertTrue('current_sorting' in response.context)

    def test_product_detail_page(self):
        """ Test if product detail page renders correct template when user is
        authenticated as client user"""
        response = self.client.get(
            '/products/product_details/' + str(self.product.id) + '/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_product_detail_page_neauthenticated(self):
        """ Test if product detail page renders correct template
        without user authentication """
        self.client.logout()
        response = self.client.get(
            '/products/product_details/' + str(self.product.id) + '/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_product_detail_page_context(self):
        """ Test if context is rendered to create products page"""
        response = self.client.get(
            '/products/product_details/' + str(self.product.id) + '/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('product' in response.context)
        self.assertTrue('update_product_form' in response.context)
        self.assertTrue('review_form' in response.context)
        self.assertTrue('update_review_form' in response.context)
        self.assertTrue('review_list' in response.context)
        self.assertTrue('current_review' in response.context)
        self.assertTrue('add_to_wishlist_form' in response.context)
        self.assertTrue('current_wishlist_line' in response.context)

    def test_product_add_for_user_not_superuser(self):
        """ Test if post method for add product fails
        for not admin users"""
        new_product = {
            'ADD-category': self.category.id,
            'ADD-sku': "ca101994",
            'ADD-name': "Fresh Cream Cake",
            'ADD-type': 'dessert',
            'ADD-code': "107901",
            'ADD-price': 25.00,
            'ADD-image': '"fresh_cream_cake.jpg"',
            'ADD-stock': 100
        }

        # Call post method for client use
        response = self.client.post(
            reverse('product_add'),
            new_product,)
        # Test if the user gets 403 forbidden on post
        self.assertEqual(response.status_code, 403)

        self.client.logout()
        # Call post method for neauthenticated user
        response = self.client.post(
            reverse('product_add'),
            new_product)
        # Test if the neauthenticated user is redirected to login page
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response['location'])

