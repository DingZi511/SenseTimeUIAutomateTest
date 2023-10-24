
import os

import pytest
#这是执行文件
if __name__ == '__main__':
    pytest.main(['-s', '-q', './test_cases', '--clean-alluredir', '--alluredir=./allure-results'])
    # pytest.main(['-s', '-q', './test_cases/test_healthOnlinelnQuiry.py', '--clean-alluredir', '--alluredir=./allure-results'])
    os.system(r"allure serve ./allure-results")


