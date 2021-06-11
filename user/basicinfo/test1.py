"""
检测某个文件夹中不完整的图片，并删除
"""
import os
import cv2

from PIL import Image

"""
检测图片完整性
"""


class CheckImage(object):

    def __init__(self, img):
        with open(img, "rb") as f:
            # print(f.tell(),img)
            f.seek(-2, 2)
            self.img_text = f.read()
            f.close()

    def check_jpg_jpeg(self):
        """检测jpg图片完整性，完整返回True，不完整返回False"""
        buf = self.img_text
        return buf.endswith(b'\xff\xd9')

    def check_png(self):
        """检测png图片完整性，完整返回True，不完整返回False"""

        buf = self.img_text
        return buf.endswith(b'\xaeB`\x82')


class CheckBrockImage(object):
    def __init__(self, train_dir):
        self.train_dir = train_dir
        self.completeFile = 0
        self.incompleteFile = 0

    def get_imgs(self):
        """遍历某个文件夹下的所有图片"""
        for file in os.listdir(self.train_dir):
            if os.path.splitext(file)[1].lower() == '.jpg' or os.path.splitext(file)[1].lower() == ".jpeg":

                ret1 = self.is_valid(file)
                if ret1:
                    ret2 = self.check_img(file)

                    ret = ret1 and ret2
                else:
                    ret = ret1
                # ret = self.is_valid(file)
                if ret:
                    self.completeFile += 1

                else:
                    print('{}：读取失败！'.format(file))
                    self.incompleteFile = self.incompleteFile + 1
                    # self.img_remove(file)  # 删除不完整图片

    def is_valid(self, file):
        img_origin = cv2.imread(self.train_dir + '\\' + file)
        if img_origin is None:
            print('{}：读取失败！'.format(file))
        try:
            cv2.imshow('image', img_origin)
            # cv2.waitKey(0)
        except:
            if img_origin is None:

                print('{}：读取失败！'.format(file))
                return False
            return False

        return True

    def img_remove(self, file):
        """删除图片"""
        os.remove(self.train_dir + file)

    def check_img(self, img_file):
        """检测图片完整性，图片完整返回True,图片不完整返回False"""
        return CheckImage(self.train_dir + img_file).check_jpg_jpeg()

    def run(self):
        """执行文件"""
        self.get_imgs()
        print('不完整图片 : %d个' % self.incompleteFile)
        print('完整图片 : %d个' % self.completeFile)


import os



# 遍历文件夹及其子文件夹中的文件，并存储在一个列表中
# 输入文件夹路径、空文件列表[]
# 返回 文件列表Filelist,包含文件名（完整路径）
def get_filelist(dir, Filelist,nub=0):
    newDir = dir
    if os.path.isfile(dir):
        # print(newDir)
        Filelist.append(newDir[0:len(newDir)-nub])
    if os.path.isdir(dir):
        #Filelist.append(dir)
        print(dir)
        for s in os.listdir(dir):
            # 如果需要忽略某些文件夹，使用以下代码
            #       #if s == "xxx":
            # continue
            newDir = os.path.join(dir, s)
            #print(s)
            if not os.path.isfile(newDir):

                get_filelist(newDir, Filelist,len(s))
    return list(set(Filelist))


if __name__ == '__main__':
    train_dir = 'E:\\SMONU\\user\\basicinfo\\'  # 检测文件夹
    # imgs = CheckBrockImage(train_dir)
    # imgs.run()
    lists = get_filelist('E:\\SMONU\\user\\basicinfo\\', [])
    print(len(lists),lists)
    #for e in list:
    #    print(e)
