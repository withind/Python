import glob
def get_all():
    '''获取目录[c:\\tmp]下面所有的文件'''
    return glob.glob('/Users/air/*.*')
def get_my_file():
    '''获取目录[c:\\tmp]下面文件名为4个字符的文件'''
    return glob.glob('/Users/air/????.txt')
def get_batch_file():
    '''获取目录[c:\\tmp]下面扩展名为\'.txt\'的文件'''
    return glob.glob('/Users/air/*.txt')
print (get_all())
print (get_my_file())
print (get_batch_file())
