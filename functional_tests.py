from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_list_and_retrive_it_later(self):
        # yova听说有一个很酷的todo应用
        # 他去看了这个应用的首页
        self.browser.get('http://localhost:8000')
        # 他看到这个应用的标题和头部都包含一个“todo”
        self.assertIn('todo',self.browser.title)
        self.fail('Finished the test!')
        # 应用邀请他输入一个待办事项
        # 他在一个文本框中输入“看完《测试驱动开发》”
        # 他的爱好是看书
        # 他按了一下回车后，页面更新了
        # 待办事项列表中更新了“1：看完《测试驱动开发》”
        # 页面中又显示了一个文本框，可以继续输入待办事项
        # 他输入了“明天去吃kfc”
        # 页面再次更新，待办事项列表中又显示了这两个待办
        # yova想知道这个网站是否会记住他的清单
        # 他看到网站为他生成了一个唯一的URL
        # 页面中还有一些文字解释这些功能
        # 他访问了唯一的URL
        # 发现他的待办还在
        # 他很满意，关掉浏览器，去睡觉了


if __name__ == '__main__':
    unittest.main(warnings='ignore')