# Copyright 2017 Virgil Dupras
#
# This software is licensed under the "GPLv3" License as described in the "LICENSE" file,
# which should be included with this package. The terms are also available at
# http://www.gnu.org/licenses/gpl-3.0.html

from argparse import ArgumentParser

from hscommon.build import setup_package_argparser, package_cocoa_app_in_dmg

def parse_args():
    parser = ArgumentParser()
    setup_package_argparser(parser)
    return parser.parse_args()

def main():
    args = parse_args()
    print("Packaging moneyGuru")
    package_cocoa_app_in_dmg('build/moneyGuru.app', '.', args)

if __name__ == '__main__':
    main()

