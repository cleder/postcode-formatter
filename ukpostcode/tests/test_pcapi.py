# -*- coding: utf-8 -*-
"""Test UK postcodes API."""

import os, csv
import pytest

from ukpostcode.pcapi import PostCode

def test_regex():
    pc = PostCode()
    assert pc.is_valid('NG24 1JT')
    assert not pc.is_valid('N245 1JT')

def test_validate_all_codepoint_open():
    """Validate the regex with all postcodes from pointcode open."""
    pc = PostCode()
    for filename in os.listdir('CSV'):
        if filename.endswith('.csv'):
            path = os.path.join('CSV', filename)
            with open(path) as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    assert pc.is_valid(row[0])
                    assert pc.format_codepoint(row[0]) == row[0]

def test_parts():
    """Split a postcode into district, sector and unit."""
    pc = PostCode()
    assert pc.postcode_parts('NG24 1JT') == ('NG24', '1', 'JT')
    assert pc.postcode_parts('NG24 \t1JT') == ('NG24', '1', 'JT')


def test_format():
    """Format a human readable postcode."""
    pc = PostCode()
    assert pc.format_postcode('Ng24 \t1Jt') == 'NG24 1JT'
    with pytest.raises(ValueError):
        pc.format_postcode('Ng24 \t1Jt3')


def test_format_codepoint():
    """Format the postcode in Code-Point Open format."""
    pc = PostCode()
    assert pc.format_codepoint('Ng24 1Jt') == 'NG241JT'
