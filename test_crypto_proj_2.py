import unittest

import crypto_proj


class TestCryptoProject(unittest.TestCase):

    def setUp(self):
        self.proj = crypto_proj.CryptoProject()

    def test_task_1(self):
        m = self.proj.task_1()
        self.assertEqual('0xd7fe8d6bde78aacbbb0649f8a22ac714', m)

    def test_task_2(self):
        password, salt = self.proj.task_2()
        self.assertEqual('friendship', password)
        self.assertEqual('bailey', salt)

    def test_task_3(self):
        d = self.proj.task_3()
        self.assertEqual('0x803370c3c0ee601', d)

    def test_task_4(self):
        d, waldo = self.proj.task_4()
        self.assertEqual('0xc742eaca941a13ada209f990340f7396f9ce53b4834df3559f0d2c13d65dcffa4732a23f929dfd798f054dc1c314a561694a7c1277421fb332c50432daa47ef189037b6b1b83f3eef6cac06425802ee004dc4e945f09abc50908ef847a7d84ce39f5ccea2363163a9b3b7e9fa05ca87a1bcc8f4aaba93d047db6ff55bca4c319', d)
        self.assertEqual('7a271af52856be0957cacfe6dfc17f90c683999213b7bb863fed7c6d', waldo)

    def test_task_5(self):
        msg = self.proj.task_5()
        self.assertEqual('I am the Lizard King, I can do anything!', msg)


if __name__ == '__main__':
    unittest.main()
