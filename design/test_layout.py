from nose.tools import raises
import yaml
from unipath import Path
from layout import *

sample_layout = yaml.safe_load(Path('test_layout.yml').read_file())

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
    sample = sample_layout
    expected = 26*25/2
    actual = Layout(freqs=sample['freqs'], weights=sample['weights']).metric
    print 'Expected:\n', expected
    print '\nActual:\n', actual
    assert expected == actual

@raises(ValueError)
def test_layout_valid_init():
    actual = Layout('a')

def test_second_metric():
    data = sample_layout
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
    sample = sample_layout
    expected = [1]*(26*25/2)
    actual = Layout(freqs=sample['freqs'])._array_freqs
    print 'Expected:\n', expected
    print '\nActual:\n', actual
    assert expected == actual

def test_freqs_array_sparse():
    sample = sample_layout
    expected = 2.5
    actual = sum(Layout(freqs=sample['freqs_sparse'])._array_freqs)
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
    sample = sample_layout
    expected = [1]*(26*25/2)
    actual = Layout(weights=sample['weights'])._array_weights
    print 'Expected:\n', expected
    print '\nActual:\n', actual
    assert expected == actual

def test_weights_array_sparse():
    sample = sample_layout
    expected = 3
    actual = sum(Layout(weights=sample['weights_sparse'])._array_weights)
    print 'Expected:\n', expected
    print '\nActual:\n', actual
    assert expected == actual

def test_shuffle():
    expected = 0.67700000000000038
    l = Layout()
    l.shuffle()
    actual = l.metric
    print 'Expected:\n', expected
    print '\nActual:\n', actual
    assert expected != actual

if __name__ == '__main__':
    test_second_metric()
