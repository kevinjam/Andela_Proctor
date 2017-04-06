
import unittest

class ShoppingCartTestCases(unittest.TestCase):
  def setUp(self):
    self.cart = ShoppingCart()
    self.shop = Shop()
    
  def test_cart_property_initialization(self):
    self.assertEqual(self.cart.total, 0, msg='Initial value of total not correct')
    self.assertIsInstance(self.cart.items, dict, msg='Items is not a dictionary')
    
  def test_add_item(self):
    self.cart.add_item('Mango', 3, 10)
    
    self.assertEqual(self.cart.total, 30, msg='Cart total not correct after adding items')
    self.assertEqual(self.cart.items['Mango'], 3, msg='Quantity of items not correct after adding item')
    
  def test_remove_item(self):
    self.cart.add_item('Mango', 3, 10)
    self.cart.remove_item('Mango', 2, 10)
    
    self.assertEqual(self.cart.total, 10, msg='Cart total not correct after removing item')
    self.assertEqual(self.cart.items['Mango'], 1, msg='Quantity of items not correct after removing item')
    
  def test_checkout_returns_correct_balance(self):
    self.cart.add_item('Mango', 3, 10)
    self.cart.add_item('Orange', 16, 10)
    
    self.assertEqual(self.cart.checkout(265), 75, msg='Balance of checkout not correct')
    self.assertEqual(self.cart.checkout(25), 'Cash paid not enough', msg='Balance of checkout not correct')
    
  def test_shop_is_instance_of_shopping_cart(self):
    self.assertTrue(isinstance(self.shop, ShoppingCart), msg='Shop is not a subclass of ShoppingCart')

  def test_shop_remove_item_method(self):
    for i in range(15):
      self.shop.remove_item()

    self.assertEqual(self.shop.quantity, 85)
