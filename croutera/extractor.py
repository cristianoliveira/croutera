#!/usr/bin/env python
# -*- coding: utf-8 -*-


def extract_manufacturer(model_param):
    'Extract manufacturer from a given model param [model]'
    return model_param.split('-',1)[0]

def extract_model(model_param):
    'Extract model from a given model param [model]'
    return model_param.split('-',1)[1:][0]

def extract_subclasses(clazz):
    'Extract all subclasses (inclusive inherited) from a given class'
    subclasses = []
    for cls in clazz.__subclasses__():
        subclasses.extend([cls] + extract_subclasses(cls))
    return subclasses
