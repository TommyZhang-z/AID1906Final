"""
多进程爬取图片
"""
import requests
import re


# Constants
pic_pattern = re.compile('img id="img".*?src="(.*?)"')


class MyRequest:
    def __init__(self, links, headers, directory, page):
        """
        :param links: 主页面解析出的所有副页面链接
        :param headers: 请求头
        :param directory: 保存路径
        :param page: 当前是主页面中的第几页
        """
        self.links = links
        self.headers = headers
        self.directory = directory
        self.page = page
        super().__init__()

    def main(self, picNo) -> None:
        """
        注：每个主页有40个副页面，每个副页面有一个图片
        :param picNo:  图片索引 0->39
        :return:
        """
        # 0->39+(40*page) = 当前总图片进度
        # print出来可以直观的看到 执行到哪张图片了
        print(picNo+(40*self.page))
        imgURL = self.parsingPicPage(picNo)
        picture = self.downloadPic(imgURL)
        self.writePic(picture, picNo+(40*self.page))

    def parsingPicPage(self, picNo) -> str:
        """
        解析副页面里包含的图片URL
        :param picNo: 图片索引 0->39
        :return: 图片下载地址(str)
        """
        picPageUrl = self.links[picNo]
        response = requests.get(picPageUrl, headers=self.headers).text
        imgURL = re.findall(pic_pattern, response)[0]
        if imgURL == "":
            raise Exception("解析失败")
        return imgURL

    def downloadPic(self, imgURL) -> requests.models.Response:
        """
        通过imgURL下载图片
        :param imgURL: 图片下载地址
        :return: 返回图片数据
        """
        picture = requests.get(imgURL, headers=self.headers)
        return picture

    def writePic(self, picture, picName) -> None:
        """
        图片写入本地
        :param picture: 图片数据
        :param picName:   图片名称(前缀)
        :return:
        """
        with open("{}{}.jpg".format(self.directory, picName), 'wb') as fd:
            fd.write(picture.content)
