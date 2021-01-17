# -*- coding: utf-8 -*-
# @Time  :2020/10/27 9:03 下午
# @Author : caohe
# @File :test_calc.py
import  pytest
import yaml
import os
from pytest1.corepytest1.calc import Calc


class Testcalc:
    def setup(self):
        self.calc=Calc()
    @pytest.mark.parametrize("a,b,c",yaml.safe_load(open("/Users/caohe/PycharmProjects/hogwarts_caohe/pytest1/source/miltcorrect.yml")))
    def test_mul(self,a,b,c):
            assert self.calc.mul(a,b) == c

    @pytest.mark.parametrize("a,b,c",yaml.safe_load(open('/Users/caohe/PycharmProjects/hogwarts_caohe/pytest1/source/milterror.yml')))
    def test_mul1(self,a,b,c):
            with pytest.raises(Exception):
                assert self.calc.mul(a,b) == c
