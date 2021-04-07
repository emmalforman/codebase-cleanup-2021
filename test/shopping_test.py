
# TODO: import some code from the shopping file

from app.shopping import format_usd
from app.shopping import find_product
from pandas import read_csv
import os

# TODO: test the code
def test_format_usd():
   # assert 2==2
   assert format_usd(9.5) == "$9.50"

def test_find_product():
   products_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
   products_df = read_csv(products_filepath)
   products = products_df.to_dict("records")
   print(find_product(1, products))
   assert find_product(1, products) == [{'id': 1, 'name': 'Chocolate Sandwich Cookies', 'aisle': 'cookies cakes', 'department': 'snacks', 'price': 3.5}]
   
