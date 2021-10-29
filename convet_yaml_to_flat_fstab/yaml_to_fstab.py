# # -*- coding: utf-8 -*-
# # - - - - - - - - - - - Sri Pandi - - - - - - - - - - - - - -
#
# __author__ = 'Satheesh R'
#
# # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import yaml

with open('input.yaml', 'r') as f:
    doc = yaml.load(f, Loader=yaml.FullLoader)

lines = []

for k, v in doc.items():
    if type(v) is dict:
        for k1, v1 in v.items():
            _mount, _type, _export, _options, _reserve, _defaults = '', '', '', '', '', 'defaults'
            _main = k1
            if 'mount' in v1:
                _mount = v1['mount']
            if 'type' in v1:
                _type = v1['type']
            if 'export' in v1:
                _export = v1['export']
            if 'root-reserve' in v1:
                _reserve = v1['root-reserve']
            if 'options' in v1:
                _options = ','.join(v1['options'])
                _defaults = ''

            line = f'{_main} {_mount} {_export} {_type} {_reserve} {_options} {_defaults} 0 0'
            lines.append(line)

with open('output.txt', 'w') as _obj:
    _obj.writelines('\n'.join(lines))
