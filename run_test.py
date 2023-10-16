"""
===================================
Author:商汤科技-刘孜煜
Time：2023/7/17
E-mail:liuziyu1@senseauto.com
Company:商汤科技
===================================
"""
import os

import pytest

if __name__ == '__main__':
    pytest.main(['-s', '-q', './test_cases', '--clean-alluredir', '--alluredir=./allure-results'])
    os.system(r"allure serve ./allure-results")

