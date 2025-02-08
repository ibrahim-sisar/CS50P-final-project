import pytest
from main import FileSorter

def test_get_file_category():
    file_sort = FileSorter()
    assert file_sort.get_file_category("png") == "image"
    assert file_sort.get_file_category("pdf") == "documents"
    assert file_sort.get_file_category("exe") == "run"
    assert file_sort.get_file_category("test") == "other"
def test_get_file_ex():
    file_sort = FileSorter()
    assert file_sort.get_file_ex("image.png") == 'png'
    assert file_sort.get_file_ex("doc.docx") == 'docx'
    assert file_sort.get_file_ex('6.00.1x.pdf') == 'pdf'
    assert file_sort.get_file_ex("....jpg") == 'jpg'
    assert file_sort.get_file_ex("CS50P.PNG") == 'png'
def test_get_file_category_f():
    file_sort = FileSorter()
    assert file_sort.get_file_category_f("image.png") == "image"
    assert file_sort.get_file_category_f("image.jpg") == "image"
    assert file_sort.get_file_category_f("image.jpeg") == "image"
    assert file_sort.get_file_category_f("image.PNG") == "image"
    assert file_sort.get_file_category_f("image.JPG") == "image"
    assert file_sort.get_file_category_f("doc.docx") == "documents"
    assert file_sort.get_file_category_f("doc.pdf") == "documents"
    assert file_sort.get_file_category_f("doc.txt") == "documents"