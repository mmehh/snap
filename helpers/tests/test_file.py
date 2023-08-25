""" Tests for the file helper
"""
import os
import time
import helpers.file as f


def test_get_urls():
    url_list = f.get_urls(os.path.dirname(__file__) + '/test_urls.txt')
    assert len(url_list) == 3


def test_file_name():
    """Test that the filename is generated correctly
    """
    assert f.file_name(
        'https://example.com') == 'https_example_com_' + time.strftime('%H_%M_%S') + '.png'
