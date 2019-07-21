# -*- coding: utf-8 -*-
import cssutils
import webcolors

import logging
cssutils.log.setLevel(logging.CRITICAL) #Disables warnings and errors triggered by new CSS properties and values.

# parser = cssutils.CSSParser()
# optionally
# parser.setFetcher('none') #The default fetcher emits a warning if encountering a different mimetype. Callin setFetcher('none') resets cssutils to use its default function. And is not needed?
# sheet = parser.parseFile('main.css') #New call with parser.

sheet = cssutils.parseFile('main.css') #Original call without parser.

for rule in sheet:
    if rule.type == rule.STYLE_RULE:
        for property in rule.style: # Find property
            if property.name == 'color' or property.name == 'background-color':
                if property.value[0] != '#' and 'rgb' not in property.value and 'transparent' not in property.value and 'inherit' not in property.value: #Checks if value is a named colour.
                    # print(f'This is a named value: {property.value}')
                    property.value = webcolors.name_to_hex(property.value)
                    # print(f'Replace with: {property.value}\n')
                else: #Else, property is not a named colour.
                    # print(f'This is a #, or rgb, or transparent, or inherit value: {property.value}')
                    # print('It will not be replaced.\n')
                    pass

with open('output.css', 'wb') as f:
    f.write(sheet.cssText)

print('The new CSS file is output.css.')