# -*- coding: utf-8 -*-
# Copyright (C) 2010 Bastian Kleineidam
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import unittest
from patoolib import baker


class TestBaker (unittest.TestCase):

    def test_func_args (self):
        @baker.command
        def func(a, b, c):
            return (a, b, c)
        res = baker.run(argv=[__file__, 'func', '1', '2', '3'])
        self.assertEqual(res, ('1', '2', '3'))

    def test_func_noargs (self):
        @baker.command
        def func():
            return 42
        res = baker.run(argv=[__file__, 'func'])
        self.assertEqual(res, 42)

    def test_func_kwargs (self):
        @baker.command
        def func(arg1, arg2, *args, **kwargs):
            return arg1, arg2, kwargs['verbose']
        res = baker.run(argv=[__file__, 'func', 'argvalue1', 'argvalue2', '--verbose'])
        self.assertEqual(res, ('argvalue1', 'argvalue2', True))

    def test_func_kwargs_revorder (self):
        @baker.command
        def func(arg1, arg2, *args, **kwargs):
            return arg1, arg2, kwargs['verbose']
        res = baker.run(argv=[__file__, 'func', 'argvalue1', '--verbose', 'argvalue2'])
        self.assertEqual(res, ('argvalue1', 'argvalue2', True))

    def test_func_kwargs_params (self):
        @baker.command(params={"verbose": "Be verbose"})
        def func(*args, **kwargs):
            return kwargs['verbose']
        res = baker.run(argv=[__file__, 'func', '--verbose'])
        self.assertEqual(res, True)
