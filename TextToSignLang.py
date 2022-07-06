from time import sleep
import time
from PIL import Image
from matplotlib import pyplot as plt
import matplotlib.image as image
from numpy import array
import loading as ld

st = time.time()

class BSTNode:
    
    def __init__(self, val=None, img=None):
        self.left = None
        self.right = None
        self.val = val
        self.img = img

    def insert(self, val, img):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return
        
        if val < self.val:
            if self.left:
                self.left.insert(val, img)
                return
            self.left = BSTNode(val, img)
            return
        
        if self.right:
            self.right.insert(val, img)
            return
        self.right = BSTNode(val, img)

    def textToImg(self, val):
        if val == self.val:
            return self.img
        
        if val < self.val:
            if self.left == None:
                return False
            return self.left.textToImg(val)
        
        if self.right == None:
            return False
        
        return self.right.textToImg(val)

if __name__ == '__main__':

    print("\n\nLoading image data into the Tree...")
    print("Please wait... ")
    
    nums = [96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]

    signList = []
    signList.append(array(Image.open(r"res\0.jpg")))
    signList.append(array(Image.open(r"res\1.jpg")))
    signList.append(array(Image.open(r"res\2.jpg")))
    signList.append(array(Image.open(r"res\3.jpg")))
    signList.append(array(Image.open(r"res\4.jpg")))
    signList.append(array(Image.open(r"res\5.jpg")))
    signList.append(array(Image.open(r"res\6.jpg")))
    signList.append(array(Image.open(r"res\7.jpg")))
    signList.append(array(Image.open(r"res\8.jpg")))
    signList.append(array(Image.open(r"res\9.jpg")))
    signList.append(array(Image.open(r"res\10.jpg")))
    signList.append(array(Image.open(r"res\11.jpg")))
    signList.append(array(Image.open(r"res\12.jpg")))
    signList.append(array(Image.open(r"res\13.jpg")))
    signList.append(array(Image.open(r"res\14.jpg")))
    signList.append(array(Image.open(r"res\15.jpg")))
    signList.append(array(Image.open(r"res\16.jpg")))
    signList.append(array(Image.open(r"res\17.jpg")))
    signList.append(array(Image.open(r"res\18.jpg")))
    signList.append(array(Image.open(r"res\19.jpg")))
    signList.append(array(Image.open(r"res\20.jpg")))
    signList.append(array(Image.open(r"res\21.jpg")))
    signList.append(array(Image.open(r"res\22.jpg")))
    signList.append(array(Image.open(r"res\23.jpg")))
    signList.append(array(Image.open(r"res\24.jpg")))
    signList.append(array(Image.open(r"res\25.jpg")))
    signList.append(array(Image.open(r"res\26.jpg")))

    bst = BSTNode()
    i = 0
    for num in nums:
        bst.insert(num, signList[i])
        i += 1

    ld.animate

    nospaces = input("Enter the sentence: ")
    #nospaces = sentence.replace(" ", "")

    for i in nospaces:
        if i == " ":
            sleep(2.5)
        else:
            plt.imshow(bst.textToImg(ord(i)))
            plt.pause(1)
            plt.close()
    
    et = time.time()

    print("\n\nEND---------------------------------END\n")

    print("Time taken: ", et - st, "seconds\n\n\n")