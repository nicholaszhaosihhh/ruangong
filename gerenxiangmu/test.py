import unittest
from main import main
#测试类
class TestMain(unittest.TestCase):
    def test_add(self):
        print('测试add:')
        main("E:\\homework_test\\orig.txt","E:\\homework_test\\orig_0.8_add.txt")

    def test_del(self):
        print('测试del:')
        main("E:\\homework_test\\orig.txt", "E:\\homework_test\\orig_0.8_del.txt")

    def test_dis_1(self):
        print('测试dis_1:')
        main("E:\\homework_test\\orig.txt", "E:\\homework_test\\orig_0.8_dis_1.txt")

    def test_dis_10(self):
        print('测试dis_10:')
        main("E:\\homework_test\\orig.txt", "E:\\homework_test\\orig_0.8_dis_10.txt")

    def test_dis_15(self):
        print('测试dis_15:')
        main("E:\\homework_test\\orig.txt", "E:\\homework_test\\orig_0.8_dis_15.txt")

    if __name__ == '__main__':
        unittest.main()
