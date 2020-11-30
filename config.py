#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from os.path import join, dirname, abspath, isfile, isdir
import shutil
import argparse
from urllib.parse import urlparse

dir_scr = dirname(abspath(__file__))
import helper as fn

dir_scr = dirname(abspath(__file__))

def main(_args):
    print("----- redis env setting start.")

    env_org = join(dir_scr, "_org", '.env')
    env_file = join(dir_scr, '.env')

    if _args.reset or not isfile(env_file):
        print("[info] init .env file.")
        shutil.copyfile(env_org, env_file)

    params = fn.getenv(env_file)

    fn.setparams(params, [
        'PORT_EXTERNAL',
        'MEM',
        'MEM_DB',
    ])
    fn.setenv(params, env_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='set config files')
    parser.add_argument('--reset', '-r', help="reset files", action="store_true")
    args = parser.parse_args()

    main(args)
