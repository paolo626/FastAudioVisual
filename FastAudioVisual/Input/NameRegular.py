import os
import re



def ReplaceFileName(picPath,fileSuffix=".jpg", regularName="One-",startNumber=0):
    """Modify the file name under the pic_path path.
    This function just change your file name , it is not your suffix. Suffix needs to some tools not this code.  
    # Arguments:
      picPath : The filedir  in your computer.
      fileSuffix: The fileSuxffix you want to select.If none, default = .jpg 
      regularName :  The name you want  every file have.
      startNumber: The fileName you want  start( we set file name into number sequnce.) .If none, default = 0 
    # Returns
      Not,but printing change detail.
    """
    
    picList=os.listdir(picPath)
    total_num=len(picList)
   
    i=1
    for pic in picList:
        if pic.endswith(fileSuffix):#修改成你自己想要重命名的文件格式
            oldPath=os.path.join(os.path.abspath(picPath),pic)
            newPath=os.path.join(os.path.abspath(picPath),regularName+str(1000+(int(i)))+fileSuffix)#修改成了1000+N这种格式
 
            os.renames(oldPath,newPath)
            print ("Change orignial File："+oldPath+u" to："+newPath)
            i=i+1

def ReplaceDirName(rootDir,startNumber=0):
    """Modify the folder name under the rootDir path.
    This function just change your Dir name in one loop.
      rootDir : The dir  in your computer.
      startNumber: The DirName you want  start( we set file name into number sequnce.) .If none, default = 0 
    # Returns
      Not,but printing change detail.
    """
    num = startNumber
    dirs = os.listdir(rootDir)
    for dir in dirs:
        print('Old name is:' + dir)                # 输出老的名字
      
        num = num +1
        temp = "%03d" % int(num)   #The purpose is to unify the number into 3 digits, and add 0 before the insufficient
        oldName = os.path.join(rootDir, dir)      # 老文件夹的名字
        newName = os.path.join(rootDir, temp)     # 新文件夹的名字

        os.rename(oldName, newName)        #替换


def MoveFileFromSCV(FileSVC): 
    pass









if __name__ == '__main__':
    rootDir = './data'
    ReplaceDirName(rootDir)
    ReplaceFileName(rootDir)
