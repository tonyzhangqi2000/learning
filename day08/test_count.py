import unittest

from day08.calculator import Count


class TestCount(unittest.TestCase):

    def setUp(self):
        print("===测试开始===")

    def test_add1(self):
        print("test_add1")
        count = Count(10, 30)
        res1 = count.add()
        self.assertEqual(res1, 40)

    def test_add2(self):
        print("test_add2")
        count = Count(1.2, 3.5)
        res1 = count.add()
        self.assertAlmostEqual(res1, 4.7)

    def tearDown(self) -> None:
        print("===测试结束===")


if __name__ == '__main__':
    unittest.main()
