import sys
import pytest
from project import url_check

def test_url_check():
    assert url_check() == "www.google.com" # If inpuuted url where "www.google.com"
