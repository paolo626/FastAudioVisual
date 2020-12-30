import sys
sys.path.append("..")
from Input.NameRegular import  *



def main():
    rootDir = "/home/liupeng/Documents/Liupeng/MultimodalEmotion/FastAudioVisual/FastAudioVisual/Test/DataBase/Audio_speechh_Actors_01-24"
    
    #ReplaceDirName(rootDir,50)
    #print("Test ReplaceDirName ok ")
    rootDir = "/home/liupeng/Documents/Liupeng/MultimodalEmotion/FastAudioVisual/FastAudioVisual/Test/DataBase/Audio_speechh_Actors_01-24/051"
    ReplaceFileName(rootDir,".wav","Two-",10)
		
if __name__ == '__main__':
	main()