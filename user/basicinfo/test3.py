# 下载图片
# 下载
import queue
import threading
import urllib.request

import os

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
                    self.img_remove(file)  # 删除不完整图片

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


def downloadJpeg(downloadurl, rename, detail):
    # f = urllib2.urlopen(downloadurl)
    # with open(rename, "wb") as code:
    #     code.write(f.read())
    print(detail, ":downloading ", downloadurl + " with urllib")
    urllib.request.urlretrieve(downloadurl, filename=(rename + ".jpeg"))
    print(detail, rename + " already download")


def cut_Str(strs):
    str1 = strs[0:3]
    # print("str1:",str1)
    # 第几张图
    if str1 is not '':
        no = int(str1)

    # htpp的链接
    # str2 = strs.split('-001-')[1]
    # http是还需要拼接的s
    # http://www.archiviodistatovenezia.it/fast/iipsrv2.fcgi?FIF=/mnt/links/siasve/./00/30/30616 + .tif&jtl= + x,y
    http_before = 'http://www.archiviodistatovenezia.it/fast/iipsrv2.fcgi?FIF=/mnt/links/siasve/./'
    str3 = strs.split('.tif&credit=')[0]
    str4 = str3.split('=/mnt/links/siasve/./')[1]
    http = http_before + str4
    return no, http


# 'http://www.archiviodistatovenezia.it/fast/iipsrv2.fcgi?FIF=/mnt/links/siasve/./00/30/30893.tif&jtl=5,0'
# 001-http://www.archiviodistatovenezia.it/ic/iipbaldo/iipmooviewer.html?fif=/mnt/links/siasve/./00/30/30616.tif&credit=Archivio%20di%20Stato%20di%20Venezia&server=http://www.archiviodistatovenezia.it/fast/iipsrv2.fcgi&imgIdx=0&idUa=103&ctx=/divenire&imgIndexer=false


def manage_line(data, detail, file_no):
    # txt = '/Users/feizhang/PycharmProjects/photo_crawler_for_Ally/data2/' + str(file_no) + '.txt'
    downloadPath1 = 'H:\\photopic\\xiufu\\'
    http2 = '.tif&jtl=4,'
    # line = open(txt)
    print(detail, " :data:", data)
    if data is not '\n':
        no, http = cut_Str(data)
        if os.path.exists(downloadPath1 + str(file_no)) is not True:
            os.mkdir(downloadPath1 + str(file_no))
            if os.path.exists(downloadPath1 + str(file_no) + '/' + str(no)) is not True:
                os.mkdir(downloadPath1 + str(file_no) + '/' + str(no))

                for j in range(0, 90):
                    downloadurl = http + http2 + str(j)
                    rename_str = downloadPath1 + str(file_no) + '/' + str(no) + '/' + str(no) + '_' + str(j)
                    print(detail, downloadurl)
                    print(detail, rename_str)
                    try:
                        downloadJpeg(downloadurl, rename_str, detail)
                    except:
                        print(detail, '没有了')
                    finally:
                        pass

            else:
                files = os.listdir(downloadPath1 + str(file_no) + '/' + str(no))
                imgs = CheckBrockImage(files)
                imgs.run()
                for j in range(0, 90):

                    if str(no) + "_" + str(j) + '.jpeg' not in files:
                        downloadurl = http + http2 + str(j)
                        rename_str = downloadPath1 + str(file_no) + '/' + str(no) + '/' + str(no) + '_' + str(j)
                        print(detail, downloadurl)
                        print(detail, rename_str)
                        try:
                            downloadJpeg(downloadurl, rename_str, detail)
                        except:
                            print(detail, '没有了')
                        finally:
                            pass


        # else:
        #     pass
        else:
            if os.path.exists(downloadPath1 + str(file_no) + '/' + str(no)) is not True:
                os.mkdir(downloadPath1 + str(file_no) + '/' + str(no))
                for j in range(0, 90):
                    downloadurl = http + http2 + str(j)
                    rename_str = downloadPath1 + str(file_no) + '/' + str(no) + '/' + str(no) + '_' + str(j)
                    print(detail, downloadurl)
                    print(detail, rename_str)
                    try:
                        downloadJpeg(downloadurl, rename_str, detail)
                    except:
                        print(detail, '没有了')
                    finally:
                        pass
            else:
                files = os.listdir(downloadPath1 + str(file_no) + '/' + str(no))
                imgs = CheckBrockImage(files)
                imgs.run()
                for j in range(0, 90):
                    if str(no) + "_" + str(j) + '.jpeg' not in files:
                        downloadurl = http + http2 + str(j)
                        rename_str = downloadPath1 + str(file_no) + '/' + str(no) + '/' + str(no) + '_' + str(j)
                        print(detail, downloadurl)
                        print(detail, rename_str)
                        try:
                            downloadJpeg(downloadurl, rename_str, detail)
                        except:
                            print(detail, '没有了')
                        finally:
                            pass


q = queue.Queue(maxsize=10)


def producer(f_lines):
    for i in range(0, len(f_lines)):
        q.put(f_lines[i])
        # print(f_lines)


def customer(detail, file_no):
    while q.empty() is not True:
        lines = q.get()
        print("{}:消费产品:{}".format(detail, q.get()))
        manage_line(lines, detail, file_no)
        print()


def main(file_no):
    # file_no = 103
    txt = 'H:\\新建文件夹\\' + str(file_no) + '.txt'

    # downloadPath1 = '/Volumes/ZHANGFEI/project/'
    # http2 = '.tif&jtl=5,'
    f_line = []
    f_lines = open(txt).readlines()
    file_LIST = [file_no] * len(f_lines)
    print(file_LIST)

    for i in range(len(f_lines)):
        # print(i%2)
        # if i % 2 != 0:
        f_line.append(f_lines[i])
        f_line.append(f_lines[i])

    pthread_list = []
    # 建立一个生产者线程，
    thread_pro = threading.Thread(target=producer, args=(f_line,))
    pthread_list.append(thread_pro)
    # 建立5个消费者线程
    for i in range(10):
        thread_cus = threading.Thread(target=customer, args=("消费线程{}".format(i + 1), file_no,))
        pthread_list.append(thread_cus)

    # thread_pro.start()
    for i in pthread_list:
        i.start()
    # thread_pro.join()
    for j in pthread_list:
        j.join()


if __name__ == '__main__':
    main(50)
    # main(46)
    # main(47)
    # main(50)
    # main(51)
    # main(52)
    # main(55)
    # main(56)
    # main(57)
    # main(58)
    # main(59)
    # main(60)
    # main(61)
    # txt = '/Users/feizhang/PycharmProjects/photo_crawler_for_Ally/data2/' + str(file_no) + '.txt'
    # # downloadPath1 = '/Volumes/ZHANGFEI/project/'
    # # http2 = '.tif&jtl=5,'
    # f_line = []
    # f_lines = open(txt).readlines()
    # for i in range(len(f_lines)):
    #     if i % 2 != 0:
    #         f_line.append(f_lines[i])
    # pthread_list = []
    # # 建立一个生产者线程，
    # thread_pro = threading.Thread(target=producer, args=(f_line,))
    # pthread_list.append(thread_pro)
    # # 建立5个消费者线程
    # for i in range(20):
    #     thread_cus = threading.Thread(target=customer, args=("消费线程{}".format(i + 1),))
    #     pthread_list.append(thread_cus)
    #
    # # thread_pro.start()
    # for i in pthread_list:
    #     i.start()
    # thread_pro.join()
    # for j in pthread_list:
    #     j.join()

    # for data in line.readlines():

# 下载1-400的编号的图片

'http://www.archiviodistatovenezia.it/fast/iipsrv2.fcgi?FIF=/mnt/links/siasve/./00/30/30893.tif&jtl=5,0'

# 输入我的邀请码 YHZ2J2X 来获得三个月的蓝灯专业版！立即下载 https://github.com/getlantern/forum
