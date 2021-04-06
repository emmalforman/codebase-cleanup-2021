
# TODO: import some code from the shopping file

from app.shopping import format_usd
from app.shopping import find_product

# TODO: test the code
def test_format_usd():
   # assert 2==2
   assert format_usd(9.5) == "$9.50"

def test_find_product():
   assert find_product(1) == 'Chocolate Sandwich Cookies'

