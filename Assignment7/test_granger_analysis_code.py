import nose
from buggy_granger_analysis_code import *

def TestGC_ContentUpperCaseString():
    assert get_gc_content('GGCCAAAA') == 50

def TestGC_ContentLowerCaseString():
    assert get_gc_content('ggccaaaa') == 50
    
def TestGC_ContentMixedCaseString():
    assert get_gc_content('GgCcAAAA') == 50
    
def TestGC_ContentMultilineString():
    multilinestring = """GGCC
    AAAA"""
    assert get_gc_content(multilinestring) == 50
    
def TestEarSizeInXLRange():
    assert get_size_class(20) == 'extralarge'

def TestEarSizeInLRange():
    assert get_size_class(14) == 'large'
    
def TestEarSizeInMRange():
    assert get_size_class(9) == 'medium'
    
def TestEarSizeInSRange():
    assert get_size_class(2) == 'small'
    
def TestEarSizeOnXLBoundary():
    assert get_size_class(15) == 'extralarge'

def TestEarSizeOnLBoundary():
    assert get_size_class(10) == 'large'
    
def TestEarSizeOnMBoundary():
    assert get_size_class(8) == 'medium'
    
def TestEarSizeString():
     nose.tools.assert_raises(AssertionError, get_size_class, 'bob')
    
