#!/usr/bin/env python3
import unittest
from unittest import mock
from io import StringIO

from main import main
from main import slugify


class TestSlugyFunction(unittest.TestCase):
    def test_happy_path(self):
        date = "2020-10-02"
        title = "This is a title"
        expected = "cfp/2020-10-02-this-is-a-title.md"
        output = slugify(date, title)
        self.assertEqual(expected, output)

    def test_single_quote(self):
        date = "2020-10-02"
        title = "It's a title"
        expected = "cfp/2020-10-02-its-a-title.md"
        output = slugify(date, title)
        self.assertEqual(expected, output)

    def test_single_quote_utf(self):
        date = "2020-10-02"
        title = "Under Deconstruction: The State of Shopify’s Monolith"
        expected = "cfp/2020-10-02-under-deconstruction-the-state-of-shopifys-monolith.md"
        output = slugify(date, title)
        self.assertEqual(expected, output)

    def test_double_quote(self):
        date = "2020-10-02"
        title = "A review of \"How Complex Systems Fail\""
        expected = "cfp/2020-10-02-a-review-of-how-complex-systems-fail.md"
        output = slugify(date, title)
        self.assertEqual(expected, output)

    def test_question_mark(self):
        date = "2020-10-02"
        title = "how they test ?"
        expected = "cfp/2020-10-02-how-they-test.md"
        output = slugify(date, title)
        self.assertEqual(expected, output)

    def test_percent_sign(self):
        date = "2020-10-02"
        title = "Why is 100% reliability the wrong target?"
        expected = "cfp/2020-10-02-why-is-100-reliability-the-wrong-target.md"
        output = slugify(date, title)
        self.assertEqual(expected, output)

    def test_em_dash_and_ellipsis(self):
        date = "2020-10-02"
        title = "SLO — From Nothing to… Production"
        expected = "cfp/2020-10-02-slo-from-nothing-to-production.md"
        output = slugify(date, title)
        self.assertEqual(expected, output)


    def test_slash_title(self):
        date = "2020-10-02"
        title = "ignition / butane: take the power back on your provisioning"
        expected = "cfp/2020-10-02-ignition-butane-take-the-power-back-on-your-provisioning.md"
        output = slugify(date, title)
        self.assertEqual(expected, output)


class TestMain(unittest.TestCase):
    @mock.patch("sys.stdout", new_callable=StringIO)
    def test_parse_issue(self, mock_stdout):
        json_data = r"""
            {
                "issue": {
                    "title": "My awesome talk",
                    "created_at": "2021-03-08T18:10:04Z",
                    "user": {
                        "login": "tormath1"
                    },
                    "body": "__author name__: My name\r\n\r\n__author bio__: My bio\r\n\r\n__expected time__ :\r\n\r\n- [x] lightning talk (~ 5 min)\r\n- [ ] 15 min\r\n\r\n__language__:\r\n\r\n- [x] :fr:\r\n- [ ] :uk:\r\n\r\n__abstract__: in this talk, we will talk about linux\r\n"
                }
            }"""
        expected = """cfp/2021-03-08-my-awesome-talk.md
---
title: "My awesome talk"
date: 2021-03-08T18:10:04Z
github_username: tormath1
twitter_username: tormath1
---
__author name__: My name\r
\r
__author bio__: My bio\r
\r
__expected time__ :\r
\r
- [x] lightning talk (~ 5 min)\r
- [ ] 15 min\r
\r
__language__:\r
\r
- [x] :fr:\r
- [ ] :uk:\r
\r
__abstract__: in this talk, we will talk about linux\r


"""
        with mock.patch("main.open", mock.mock_open(read_data=json_data)):
            main(None)
            self.assertEqual(expected, mock_stdout.getvalue())

if __name__ == "__main__":
    unittest.main()
