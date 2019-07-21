# -*- coding: utf-8 -*-
import cssutils
import webcolors

import logging
cssutils.log.setLevel(logging.CRITICAL)


# print(webcolors.name_to_hex(u'goldenrod'))



parser = cssutils.CSSParser()
# optionally
parser.setFetcher('none')


sheet = parser.parseFile('other.css', 'ascii')
# sheet = parser.parseFile('other.css', 'ascii')

for rule in sheet:
    if rule.type == rule.STYLE_RULE:
        # find property
        for property in rule.style:
            if property.name == 'color' or property.name == 'background-color':
                # print(f'Hey {property.value[0]}')

                # if property.value.startswith( '#' ):
                #     pass
                    # print('This is a #FFF')

                if property.value[0] != '#' and 'rgb' not in property.value and 'transparent' not in property.value and 'inherit' not in property.value:
                    print(f'This is a named value # - {property.value}\n')
                    property.value = webcolors.name_to_hex(property.value)
                    pass
                else:
                    print(f'This is a #, or rgb, or transparent, or inherit - {property.value}\n')


                # elif property.value.startswith( 'rgba' ):
                #     pass
                #     # print(f'This is a rgba {property.value}')
                #     # property.value = webcolors.rgb_to_hex(property.value)
                # elif property.value.startswith ('transparent') or property.value.startswith ('inherit'):
                #     pass
                # else:
                #     # print('This is a color name')
                #     # property.value = webcolors.name_to_hex(property.value)
                #     pass




print(sheet.cssText)