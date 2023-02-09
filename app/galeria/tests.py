from django.test import TestCase
from .util import _Skip

# Create your tests here.

x = _Skip(1, 2, 3)
print(x.next)
