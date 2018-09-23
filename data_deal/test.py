# encoding: utf-8
"""
对两字符串进行相似度测试
"""
import difflib
# import Levenshtein


def get_equal_rate_1(str1, str2):
    return difflib.SequenceMatcher(None, str1, str2).quick_ratio()
#
"""

SequenceMatcher is a flexible class for comparing pairs of sequences of
    any type, so long as the sequence elements are hashable.  The basic
    algorithm predates, and is a little fancier than, an algorithm
    published in the late 1980's by Ratcliff and Obershelp under the
    hyperbolic name "gestalt pattern matching".  The basic idea is to find
    the longest contiguous matching subsequence that contains no "junk"
    elements (R-O doesn't address junk).  The same idea is then applied
    recursively to the pieces of the sequences to the left and to the right
    of the matching subsequence.  This does not yield minimal edit
    sequences, but does tend to yield matches that "look right" to people.

    SequenceMatcher tries to compute a "human-friendly diff" between two
    sequences.  Unlike e.g. UNIX(tm) diff, the fundamental notion is the
    longest *contiguous* & junk-free matching subsequence.  That's what
    catches peoples' eyes.  The Windows(tm) windiff has another interesting
    notion, pairing up elements that appear uniquely in each sequence.
    That, and the method here, appear to yield more intuitive difference
    reports than does diff.  This method appears to be the least vulnerable
    to synching up on blocks of "junk lines", though (like blank lines in
    ordinary text files, or maybe "<P>" lines in HTML files).  That may be
    because this is the only method of the 3 that has a *concept* of
    "junk" <wink>.
    
    SequenceMatcher是一个灵活的类，用于比较序列对
    任何类型，只要序列元素是可清除的。基础的
    算法比算法早，并且比算法更有趣
    由Ratcliff和Obershelp于1980年代末出版
    双曲线名称“格式塔模式匹配”。基本的想法是找到
    最长的连续匹配子序列，不包含“垃圾”
    元素（R-O不解决垃圾问题）。然后应用相同的想法
    递归地向左和向右的序列片段
    匹配子序列。这不会产生最小的编辑
    序列，但确实倾向于产生对人们“看起来正确”的匹配。

    SequenceMatcher尝试计算两者之间的“人性化差异”
    序列。与...不同UNIX（tm）diff，基本概念就是
    最长*连续*和无垃圾匹配子序列。那是什么
    抓住人们的眼睛。 Windows（TM）windiff有另一个有趣的
    概念，配对在每个序列中唯一出现的元素。
    这和这里的方法似乎产生了更直观的差异
    报告比差异。这种方法似乎是最不容易受到攻击的
    然而，同步“垃圾线”块（就像在空白行中一样
    普通文本文件，或HTML文件中的“<P>”行。那可能
    因为这是具有*概念*的3的唯一方法
    “垃圾”<wink>。
Example, comparing two strings, and considering blanks to be "junk":

    >>> s = SequenceMatcher(lambda x: x == " ",
    ...                     "private Thread currentThread;",
    ...                     "private volatile Thread currentThread;")
    >>>

    .ratio() returns a float in [0, 1], measuring the "similarity" of the
    sequences.  As a rule of thumb, a .ratio() value over 0.6 means the
    sequences are close matches:

    >>> print round(s.ratio(), 3)
    0.866
    >>>
    
    If you're only interested in where the sequences match,
    .get_matching_blocks() is handy:

    >>> for block in s.get_matching_blocks():
    ...     print "a[%d] and b[%d] match for %d elements" % block
    a[0] and b[0] match for 8 elements
    a[8] and b[17] match for 21 elements
    a[29] and b[38] match for 0 elements

    Note that the last tuple returned by .get_matching_blocks() is always a
    dummy, (len(a), len(b), 0), and this is the only case in which the last
    tuple element (number of elements matched) is 0.

    If you want to know how to change the first sequence into the second,
    use .get_opcodes():

    >>> for opcode in s.get_opcodes():
    ...     print "%6s a[%d:%d] b[%d:%d]" % opcode
     equal a[0:8] b[0:8]
    insert a[8:8] b[8:17]
     equal a[8:29] b[17:38]

    See the Differ class for a fancy human-friendly file differencer, which
    uses SequenceMatcher both to compare sequences of lines, and to compare
    sequences of characters within similar (near-matching) lines.

    See also function get_close_matches() in this module, which shows how
    simple code building on SequenceMatcher can be used to do useful work.

    Timing:  Basic R-O is cubic time worst case and quadratic time expected
    case.  SequenceMatcher is quadratic time for the worst case and has
    expected-case behavior dependent in a complicated way on how many
    elements the sequences have in common; best case time is linear.

    Methods:

    __init__(isjunk=None, a='', b='')
        Construct a SequenceMatcher.

    set_seqs(a, b)
        Set the two sequences to be compared.

    set_seq1(a)
        Set the first sequence to be compared.

    set_seq2(b)
        Set the second sequence to be compared.

    find_longest_match(alo, ahi, blo, bhi)
        Find longest matching block in a[alo:ahi] and b[blo:bhi].

    get_matching_blocks()
        Return list of triples describing matching subsequences.

    get_opcodes()
        Return list of 5-tuples describing how to turn a into b.

    ratio()
        Return a measure of the sequences' similarity (float in [0,1]).

    quick_ratio()
        Return an upper bound on .ratio() relatively quickly.

    real_quick_ratio()
        Return an upper bound on ratio() very quickly.

如果您只对序列匹配的位置感兴趣，
 .get_matching_blocks（）很方便

    >>> for s.get_matching_blocks（）中的块：
    ...打印“a [％d]和b [％d]匹配％d个元素”％block
    a [0]和b [0]匹配8个元素
    a [8]和b [17]匹配21个元素
    a [29]和b [38]匹配0个元素

    请注意，.get_matching_blocks（）返回的最后一个元组始终是a
    虚拟，（len（a），len（b），0），这是最后一种情况
    元组元素（匹配的元素数）为0。

    如果您想知道如何将第一个序列更改为第二个序列，
    使用.get_opcodes（）：

    >>>对于s.get_opcodes（）中的操作码：
    ...打印“％6s a [％d：％d] b [％d：％d]”％操作码
     等于[0：8] b [0：8]
    插入[8：8] b [8:17]
     等于[8:29] b [17:38]

    请参阅Differ类，了解一个花哨的人性化文件差异器
    使用SequenceMatcher来比较行的序列，并进行比较
    类似（近匹配）线内的字符序列。

    另请参见此模块中的函数get_close_matches（），其中显示了如何操作
    在SequenceMatcher上构建简单代码可以用来做有用的工作。

    时间：基本R-O是立方时间最差情况和预期的二次时间
    案件。 SequenceMatcher是最坏情况下的二次时间，并且具有
    预期案例行为以复杂的方式依赖于多少
    序列共有的元素;最佳案例时间是线性的。

    方法：

    __init __（isjunk = None，a =''，b =''）
        构造一个SequenceMatcher。

    set_seqs（a，b）
        设置要比较的两个序列。

    set_seq1（a）中
        设置要比较的第一个序列。

    set_seq2（b）中
        设置要比较的第二个序列。

    find_longest_match（alo，ahi，blo，bhi）
        在[alo：ahi]和b [blo：bhi]中找到最长匹配块。

    get_matching_blocks（）
        返回描述匹配子序列的三元组列表。

    get_opcodes（）
        返回5元组的返回列表，描述如何将a转换为b。

    比（）
        返回序列相似性的度量（浮点数为[0,1]）。

    速动比率（）
        返回.ratio（）的上限相对较快。

    real_quick_ratio（）
        快速返回ratio（）的上限。
    “””
"""

#def get_equal_rate_2(str1, str2):
    #return Levenshtein.ratio(str1, str2)


if __name__ == '__main__':
    a = '黄石华为装饰工程有限公司'
    b = '东营华为工程项目管理有限公司'
    print(get_equal_rate_1(a, b))
    #print get_equal_rate_2(a, b)
    a = '黄石华为装饰工程有限公司'
    b = '信华为技术有限公司1信息列表×信黄石华为装饰工程有限公司信'
    print(get_equal_rate_1(a, b))
    a = '东营华为工程项目管理有限公司'
    b = '信华为技术有限公司1信息列表×信黄石华为装饰工程有限公司信'
    print(get_equal_rate_1(a, b))
    a = '山西沁州黄小米(集团)有限公司'
    b = '东营华为工程项目管理有限公司'
    print(get_equal_rate_1(a, b))
    a = '山西沁州黄小米(集团)有限公司'
    b = '东营华为工程项目管理有限公司'
    print(get_equal_rate_1(a, b))
    a = '山西沁州黄小米(集团)有限'#a = '山西沁州黄小米(集团)有限公司'
    b = '信山西州黄小米(集团)有限'
    print(get_equal_rate_1(a, b))
    a = '邢台县郁秋小米加工厂'  # a = '山西沁州黄小米(集团)有限公司'
    b = '信邢台县郁秋小米加工厂信用档'
    print(get_equal_rate_1(a, b))

#
"""
执行结果如下：
  0.717948717949
  0.923076923077
  0.928571428571
  0.506024096386
  0.506024096386
"""