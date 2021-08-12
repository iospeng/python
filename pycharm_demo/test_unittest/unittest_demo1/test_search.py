import unittest


class Search:
    def search_fun(self):
        print("search")
        return True


class TestSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.search = Search()
        print("setUpClass_类级别")

    @classmethod
    def tearDown(cls) -> None:
        print("setUpClass_类级别")

    def test_search1(self):
        print("test_search1")
        # search = Search()
        # 断言
        assert True == self.search.search_fun()

    def test_search2(self):
        print("test_search2")
        # search = Search()
        assert True == self.search.search_fun()

    def test_search3(self):
        print("test_search3")
        # search = Search()
        assert True == self.search.search_fun()


class TestSearch1(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.search = Search()
        print("class1 setUpClass_类级别")

    @classmethod
    def tearDownClass(cls) -> None:
        print("class1 dearDownClass_类级别")

    def test_search1(self):
        print("class1 test_search1")
        # search = Search()
        assert True == self.search.search_fun()

    def test_search2(self):
        print("class1 test_search2")
        # search = Search()
        assert True == self.search.search_fun()

    def test_search3(self):
        print("class1 test_search3")
        # search = Search()
        assert True == self.search.search_fun()

    def test_equal(self):
        print("断言想等")
        self.assertEqual(1, 1, '判断1==1')

    def test_notequal(self):
        print("断言不相等")
        self.assertNotEqual(1, 2, "判断1！=2")
        # 判断条件
        # self.assertTrue(1 == 2, "verify")


class TestSearch2(unittest.TestCase):
    def test_search2(self):
        print("class3 test_search2")


# if __name__ == '__main__':
    # 方法一：执行当前文件所有的unittest测试用例
    # unittest.main()
    # 方法二：执行指定的测试用例，将要执行的测试用例添加到测试套件中，批量执行测试方法
    # 创建一个测试套件，testsuite
    # suite = unittest.TestSuite()
    # suite.addTest(TestSearch("test_search1"))
    # suite.addTest(TestSearch("test_search3"))
    # unittest.TextTestRunner().run(suite)

    # 方法三：执行某个测试类,将测试类添加到测试套件中，批量执行测试类
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSearch1)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSearch)
    # suite = unittest.TestSuite([suite1, suite2])
    # unittest.TextTestRunner(verbosity=2).run(suite)
