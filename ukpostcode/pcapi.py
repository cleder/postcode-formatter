# -*- coding: utf-8 -*-
"""UK postcodes API."""

import re

#regex modified from wikipedia to account for more than 1 whitespace character
valid_code = re.compile(r'^([A-Za-z][A-Ha-hK-Yk-y]?[0-9][A-Za-z0-9]?\s*[0-9][A-Za-z]{2}|[Gg][Ii][Rr] ?0[Aa]{2})$')

class PostCode(object):

    def is_valid(self, postcode):
        """Validate a postcode without trailing whitespace."""
        if valid_code.match(postcode) is None:
            return False
        return True

    def postcode_parts(self, postcode):
        """Return the District, sector and unit as a tuple"""
        postcode = postcode.strip()
        if self.is_valid(postcode):
            unit = postcode[-2:]
            sector = postcode[-3:-2]
            district = postcode [:-3].strip()
            return (district, sector, unit)
        raise ValueError('Not a valid postcode')

    def format_postcode(self, postcode):
        """Format a postcode to all uppercase with a single whitespace."""
        parts = self.postcode_parts(postcode)
        return parts[0].upper() + ' ' + parts[1] + parts[2].upper()

    def format_codepoint(self, postcode):
        """Format the postcode in Code-Point Open format."""
        parts = self.postcode_parts(postcode)
        return parts[0].upper().ljust(4) + parts[1] + parts[2].upper()
