from nose.tools import raises
import yaml
from unipath import Path
from layout import *

def test_layout():
    expected = '''\
qwertyuio
asdfghjklp
zxcvbnm'''
    actual = str(Layout())
    print 'Expected:\n', expected
    print '\nActual:\n', actual
    assert expected == actual

def test_metric():
    sample = yaml.safe_load(Path('test_layout.yml').read_file())
    expected = 26*25/2
    actual = Layout(freqs=sample['freqs'], weights=sample['weights']).metric
    print 'Expected:\n', expected
    print '\nActual:\n', actual
    assert expected == actual

@raises(ValueError)
def test_layout_valid_init():
    actual = Layout('a')

def test_second_metric():
    data = yaml.safe_load(Path('test_layout.yml').read_file())
    sample = {
        'value': 'qwdfkyuilastrghneopzxcvbjm'
        , 'freqs': data['second_freqs']
        , 'weights': data['second_weights']
        }
    expected = .5
    sample = Layout(**sample)
    actual = sample.metric
    print sample._freqs
    print sample._weights
    print 'Expected:\n', expected
    print '\nActual:\n', actual
    assert expected == actual

def test_freqs():
    expected = "<type 'dict'>"
    actual = str(type(Layout().freqs))
    print 'Expected:\n', expected
    print '\nActual:\n', actual
    assert expected == actual

def test_freqs_array():
    sample = yaml.safe_load(Path('test_layout.yml').read_file())
    expected = [1]*(26*25/2)
    actual = Layout(freqs=sample['freqs'])._freqs
    print 'Expected:\n', expected
    print '\nActual:\n', actual
    assert expected == actual

def test_freqs_array_sparse():
    sample = yaml.safe_load(Path('test_layout.yml').read_file())
    expected = 2.5
    actual = sum(Layout(freqs=sample['freqs_sparse'])._freqs)
    print 'Expected:\n', expected
    print '\nActual:\n', actual
    assert expected == actual

def test_weights():
    expected = "<type 'dict'>"
    actual = str(type(Layout().weights))
    print 'Expected:\n', expected
    print '\nActual:\n', actual
    assert expected == actual

def test_weights_array():
    sample = yaml.safe_load(Path('test_layout.yml').read_file())
    expected = [1]*(26*25/2)
    actual = Layout(weights=sample['weights'])._weights
    print 'Expected:\n', expected
    print '\nActual:\n', actual
    assert expected == actual

def test_weights_array_sparse():
    sample = yaml.safe_load(Path('test_layout.yml').read_file())
    expected = 3
    actual = sum(Layout(weights=sample['weights_sparse'])._weights)
    print 'Expected:\n', expected
    print '\nActual:\n', actual
    assert expected == actual

if __name__ == '__main__':
    test_second_metric()
