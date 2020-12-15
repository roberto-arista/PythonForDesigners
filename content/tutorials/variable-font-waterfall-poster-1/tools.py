#!/usr/bin/env python3
# coding: utf-8

def lerp(aa, bb, factor):
    return aa + (bb - aa) * factor

def getFactor(aa, bb, innerValue):
    return (innerValue-aa)/(bb-aa)
