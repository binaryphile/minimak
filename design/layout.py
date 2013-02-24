import string as str_
import random as rand
import numpy as num
import yaml
from unipath import Path
from bunch import bunchify

rand.seed()
cfg = bunchify(yaml.safe_load(Path('layout.yml').read_file()))

class Layout(object):
    def __init__(self, value='qwertyuioasdfghjklpzxcvbnm', freqs=None, weights=None):
        if not all([letter in value for letter in 'qwertyuioasdfghjklpzxcvbnm']) or len(value) != 26:
            raise ValueError
        self._value = value
        self._order = cfg.order
        self._freqs = freqs if freqs else cfg.freqs
        self._array_freqs = self._freqs_array()
        self._weights = weights if weights else cfg.weights
        self._array_weights = self._weights_array()

    def __str__(self):
        breaks = [9, 19]
        return '\n'.join([self._value[:breaks[0]], self._value[breaks[0]:breaks[1]], self._value[breaks[1]:]])

    def __repr__(self):
        return self._value

    @property
    def metric(self):
        return num.dot(self._array_freqs, self._array_weights)

    @property
    def freqs(self):
        return dict([(order, freq) for order, freq in zip(self._order, self._array_freqs) if freq])

    def _freqs_array(self):
        return [self._freqs[item] if item in self._freqs else 0 for item in self._order]

    @property
    def weights(self):
        return dict([(order, weight) for order, weight in zip(self._order, self._array_weights) if weight])

    def _weights_array(self):
        result = []
        for item in self._order:
            item = [str_.ascii_lowercase[self._value.index(item[0])], str_.ascii_lowercase[self._value.index(item[1])]]
            item.sort()
            item = ''.join(item)
            if item in self._weights:
                result += [self._weights[item]]
            else: 
                result += [0]
        return result

    def shuffle(self):
        val_list = list(self._value)
        rand.shuffle(val_list)
        self._value = ''.join(val_list)
        self._array_weights = self._weights_array()
