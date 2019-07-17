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
# sheet = parser.parseFile('other.css', 'ascii')

for rule in sheet:
    if rule.type == rule.STYLE_RULE:
        # find property
        for property in rule.style:
            if property.name == 'color' or property.name == 'background-color':

                if property.value.startswith( '#' ):
                    pass
                    # print('This is a #FFF')
                elif property.value.startswith( 'rgba' ):
                    pass
                    # print(f'This is a rgba {property.value}')
                    # property.value = webcolors.rgb_to_hex(property.value)
                elif property.value.startswith ('transparent') or property.value.startswith ('inherit'):
                    pass
                else:
                    print('This is a color name')
                    property.value = webcolors.name_to_hex(property.value)



                # print(property.value)
                # property.value = webcolors.name_to_hex(property.value)
                # break




print(sheet.cssText)