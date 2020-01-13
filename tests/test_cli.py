#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from click.testing import CliRunner
from pp import pp
from pp import cli


class TestPivotPoint(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_command_line_interface(self):
        result = self.runner.invoke(cli.main, ["34.80", "32.80", "33.40"])
        assert "35.67\n34.54\n33.67\n32.54\n31.67\n" in result.output
