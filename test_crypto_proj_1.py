import unittest

import crypto_proj


class TestCryptoProject(unittest.TestCase):

    def setUp(self):
        self.proj = crypto_proj.CryptoProject()

    def test_task_1(self):
        m = self.proj.task_1()
        self.assertEqual('0x2a1a46196caa5ef1876002db2860249b', m)

    def test_task_2(self):
        password, salt = self.proj.task_2()
        self.assertEqual('123456789', password)
        self.assertEqual('volleyball', salt)

    def test_task_3(self):
        d = self.proj.task_3()
        self.assertEqual('0x10d9dad90249bfd', d)

    def test_task_4(self):
        d, waldo = self.proj.task_4()
        self.assertEqual('0xb62338237fddc7e2e4d80cb87d3bbd6ecb5b70379b66b861f046f51fed50fc413347132bf764370cc3997ffe32ba1f5311a89d30eb338e6b8a95d14ba447777d3b19a0fd3374c69e63c3a0220629d82956311de3b6c43ddd61a7a52b28b99c3a863556d95727f1e86894163b05c1ca1771386ec1e64605d28f45c2d4c3702ba9', d)
        self.assertEqual('636df37b8d550e29c4999c5938bbdeebb72483abfda7cb28f82d43d1', waldo)

    def test_task_5(self):
        msg = self.proj.task_5()
        self.assertEqual('They are the egg men. I am the walrus. Goo goo g\'joob.', msg)


if __name__ == '__main__':
    unittest.main()
