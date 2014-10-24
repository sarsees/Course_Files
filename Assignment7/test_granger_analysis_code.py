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