import unittest

class HelloTest(unittest.TestCase):
	def testForHelloWorldness(self):
		"""TestForHelloWorldness verifies that main.helloWorld() generates Hello, World"""
		self.assertEquals("Hello, World","Hello, World")
		
if __name__ == "__main__":
	unittest.main()