from buggy_granger_analysis_code import *

def TestGC_ContentUpperCaseString():
    assert get_gc_content('GGCCAAAA') == 50

def TestGC_ContentLowerCaseString():
    assert get_gc_content('ggccaaa') == 50
    
def TestGC_ContentMixedCaseString():
    assert get_gc_content('GgCcAAAA') == 50
    
def TestGC_ContentMultilineString():
    assert get_gc_content(""""GGCCAAAA
    GGCCAAAA""") == 50