import unittest

ts_dir = "./"
testSuite1 = unittest.defaultTestLoader.discover(ts_dir, pattern="test*.py")

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(testSuite1)
