# -*- coding: utf-8 -*-
import cssutils
import webcolors

import logging
cssutils.log.setLevel(logging.CRITICAL)


# print(webcolors.name_to_hex(u'goldenrod'))




parser = cssutils.CSSParser()
# optionally
parser.setFetcher('none')
sheet = parser.parseFile('main.css', 'ascii')
print(sheet.cssText)