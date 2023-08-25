""" File Helper Module

Returns:
    _type_: _description_
"""

import os
import time
import shutil
import validators


def get_urls(list_file_path=''):
    """ Returns a list of valid urls from the urls.txt file

    Returns:
        list
    """
    if not list_file_path:
        list_file_path = os.path.dirname(__file__) + '/../urls.txt'
    url_list = []
    with open(list_file_path, 'r') as file_handler:
        for url in file_handler.readlines():
            url = url.rstrip('\n')
            if validators.url(url):
                url_list.append(url)
    return url_list


def file_name(url):
    """_summary_

    Args:
        url (str): a valid url

    Returns:
        str: formated string for the screenshot filename
    """
    url = url.replace('//', '_').replace('/',
                                         '_').replace(':', '').replace('.', '_')
    return url + '_' + file_time() + '.png'


def dir_path():
    """ Creates if not exists and returns a directory path named with today's date
        e.g. 2023_08_23

    Returns:
        str: _description_
    """
    today_date = time.strftime('%Y_%m_%d')
    path = os.path.dirname(__file__) + '/../screenshots/' + today_date
    if not os.path.isdir(path):
        os.mkdir(path)
    return path


def file_time():
    """Is used to append the current hours_minutes_seconds to a screenshopt file name.

    Returns:
        str: _description_
    """
    return time.strftime('%H_%M_%S')


def rm_todays_screenshots():
    """Removes today screenshot folder and all it's contents

    Returns:
        _type_: _description_
    """
    return shutil.rmtree(dir_path())
