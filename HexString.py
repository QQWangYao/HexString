#coding:gbk
import os, random

"""

"""
#���ѡ��
FLAG_OUTPUT_REVERSE    = 1  # �������
FLAG_OUTPUT_RAW        = 1  # ���δ��ʽ��������


#��ʽ�����
FORMAT_OUTPUT_PREFIX    = "0X" #�����ǰ׺
FORMAT_OUTPUT_separator    = "," #�ָ��

FORMAT_OUTPUT_PADDING   = "00"

FORMAT_OUTPUT_LENGTH    = 256

FORMAT_OUTPUT_NUMBER_PER_LINE = 16


#��ʽ������
IGNORE_LIST     = ["(byte)", "0X", "0x", '(', ')', '-', '.', ',', '\r', '\n', ' '] # �ÿո�������з�16�����ַ������ɾ�����пո�



def RandomHexString(len):
    """
    �������ָ�����ȵ��ֽڴ�������16���Ƶ��ַ�����
    """
    strArr = u""
    for i in range(len):
        RDByte = random.sample(u'0123456789ABCDEF',2)
        strByte = string.join(RDByte).replace(u' ', u'')
        strArr = string.join([strArr,strByte])

    return strArr + u" "


def extract(s="", ignore_list=[]):
    """
    ��ȡ�ַ�����������ģ���еĴ��ÿո���棬���ɾ���ո�
    """
    r = str(s)
    #ɾ����Ч�ַ�
    for v in ignore_list:
        r = r.replace(v, '')

    #תΪ��д
    return r.upper()


def zero_padding(s="", len = 0):
    """
    ����ַ���0��������Ϊlen
    """
    return (s + '0' * len)


def segment(s="", szblock = 1):
    """
    �ָ��ַ���, ����һ���б�
    """
    t = []
    l = len(s)
    i = 0
    while i < l:
        t.append(s[i:i+szblock])
        i += szblock

    return t

def format(s=[], prefix = "0X", suffix = ","):
    """
    ��ʽ��һ�����У����ǰ׺�ͺ�׺������һ���µ�����
    """
    t = []
    for v in s:
        t.append(prefix + v + suffix)

    return t;

def display(s=[], number_per_line = 16):
    i = 0
    t = ""
    while i < len(s):
        if 0 == i % number_per_line:
            t += "\n"
        t += s[i]
        i += 1
    print t
    pass


def ExchEndian(s=[]):
    """
    �����б��е�Ԫ�ء�
    format: 0XAA, 0XBB... -> ..., 0XBB, 0XAA
    """
    b = a[::-1]
    #print b
    for i in range(len(b)):
        if (i % nBytesPerLine) == 0:
            print " "
        print "0X%02X," % b[i]


def ExhangeSTR( a="", nLenPerLine=16 ):
    "format: AABB... -> ...BBAA"
    b = ""
    nLen = len(a)
    while  nLen > 0:
        if (nLen%nLenPerLine) == 0:
            print b.upper()
            b=""
        b += a[nLen-2:nLen]
        nLen -= 2
    print b.upper()

def str2byte(s="", prefix = "0X", suffix = ",", max_bytes=256, bytes_per_line = 16):
    """
    format: AABB... -> ...0XAA, 0XBB
    """
    es = extract(s, IGNORE_LIST)
    es = '0'*(max_bytes*2 - len(es)) + es
    ss = segment(es, 2)
    fs = format(ss, prefix, suffix)

    #display
    display(ss, 2*len(ss))
    display(fs, bytes_per_line)
    print '-'*80
    ss.reverse()
    fs.reverse()
    display(ss, 2*len(ss))
    display(fs, bytes_per_line)

    pass


def str2word(s="", prefix = "0X", suffix = ",", max_bytes=256, bytes_per_line = 16):
    """
    format: AABB... -> ...0XAA, 0XBB
    """
    es = extract(s, IGNORE_LIST)
    es = '0'*(max_bytes*2 - len(es)) + es
    ss = segment(es, 4)
    fs = format(ss, prefix, suffix)

    #display
    display(ss, 2*len(ss))
    display(fs, bytes_per_line)
    print '-'*80
    ss.reverse()
    fs.reverse()
    display(ss, 2*len(ss))
    display(fs, bytes_per_line)

    pass

def str2dword(s="", prefix = "0X", suffix = ",", max_bytes=256, bytes_per_line = 16):
    """
    format: AABB... -> ...0XAA, 0XBB
    """
    es = extract(s, IGNORE_LIST)
    es = '0'*(max_bytes*2 - len(es)) + es
    ss = segment(es, 8)
    fs = format(ss, prefix, suffix)

    #display
    display(ss, 2*len(ss))
    display(fs, bytes_per_line)
    print '-'*80
    ss.reverse()
    fs.reverse()
    display(ss, 2*len(ss))
    display(fs, bytes_per_line)

    pass



if __name__ == "__main__":
    import string, os

    nWordPerLine = 16
    nBytes = 256
    s = '''
FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFF7203DF6B21C6052B53BBF40939D54123
  '''
    #a = HexFormat(a)

    #nZero = nBytes * 2 - len(a)
    #a = "0" * nZero + a
    #a="00"*nBytes
    #a += "00010001"
    #a = [0X68, 0X51, 0X72, 0XA4, 0XB4, 0X9F, 0XFE, 0X3D]
    #a = RandomHexString(128)
    #a = "";
    #for i in range(256):
    #    a += "%02x" % i

    #s = "FF" * 16

    #str2byte(s, "(byte)0X", ", ", 256, 16)
    str2word(s, "0X", ", ", 256, 8)
    #str2dword(s, "0X", ", ", 256, 4)



