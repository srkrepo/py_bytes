# # -*- coding: utf-8 -*-
# # - - - - - - - - - - - Sri Pandi - - - - - - - - - - - - - -
#
# __author__ = 'Satheesh R'
#
# # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import argparse

import yaml


def covert_yaml_to_fstab(yml_file=None, out_file=None):
    """

    :param yml_file:
    :param out_file:
    :return:
    """

    status, output = False, ''

    try:
        if not yml_file:
            raise Exception('Not a valid yaml file')

        with open(yml_file, 'r') as f:
            parsed_inputs = yaml.load(f, Loader=yaml.FullLoader)

        if not parsed_inputs:
            raise Exception('No valid inputs found')

        lines = []
        for k, v in parsed_inputs.items():
            if type(v) is dict:
                for _k, _v in v.items():
                    _mount, _type, _export, _options, _reserve, _defaults = '', '', '', '', '', ' defaults'
                    _main = _k
                    if 'mount' in _v:
                        _mount = f" {_v['mount']}"
                    if 'type' in _v:
                        _type = f" {_v['type']}"
                    if 'export' in _v:
                        _export = f" {_v['export']}"
                    if 'root-reserve' in _v:
                        _reserve = f" {_v['root-reserve']}"
                    if 'options' in _v:
                        _options = f" {','.join(_v['options'])}"
                        _defaults = ''

                    line = f'{_main}{_mount}{_export}{_type}{_reserve}{_options}{_defaults} 0 0'
                    lines.append(line)
        if not lines:
            raise Exception('No valid lines found from input')

        with open(out_file, 'w') as _obj:
            _obj.writelines('\n'.join(lines))

        status, output = True, out_file

    except Exception as err_msg:
        print('Error occurred:', err_msg)

    status = 'SUCCESSFUL' if status else 'FAILED'
    output = output if output else 'not captured'

    return status, output


if __name__ == '__main__':
    print('How to..')

    parser = argparse.ArgumentParser(description='Convert YAML/YML to FSTAB flat file.', add_help=True)

    # Parser details
    parser.add_argument("-y", "--yml", required=True, help='YAML/YML  File')
    parser.add_argument("-o", "--out", default='output.txt', required=False, help='FSTAB  File')
    parser_args = vars(parser.parse_args())

    status, output = covert_yaml_to_fstab(parser_args['yml'], parser_args['out'])
    print(f'YAML/YML to FSTAB is {status} and the FSTAB file is {output}')
