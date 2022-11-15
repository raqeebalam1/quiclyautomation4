#!/usr/bin/env python
import os
import sys
import yaml


def read_yaml_config():
    name = 'config.yaml'
    if name not in os.listdir():
        print('[{}] not found in Current Directory'.format(name))
        path = os.path.dirname(os.path.dirname(__file__))
        print(path)
        name = os.path.join(path, name)
        print(name)
    stream = open(name, 'r')
    dictionary = yaml.load(stream, Loader=yaml.FullLoader)
    return dictionary


config = read_yaml_config()


def get_config_value(*paths):
    value = config.get(paths[0])
    for p in paths[1:]:
        value = value.get(p)
    return value