import unittest
from rsa import PublicKey, PrivateKey, make_key_pair
import random

class TestRSA(unittest.TestCase):
    def testRSA(self):
        public = PublicKey(n=2534665157, e=7)
        private = PrivateKey(n=2534665157, d=1810402843)

        assert public.encrypt(123) == 2463995467
        assert public.encrypt(456) == 2022084991
        assert public.encrypt(123456) == 1299565302

        assert private.decrypt(2463995467) == 123
        assert private.decrypt(2022084991) == 456
        assert private.decrypt(1299565302) == 123456

        # Test with random values.
        for length in range(4, 17):
            public, private = make_key_pair(length)

            assert public.n == private.n
            assert len(bin(public.n)) - 2 == length

            x = random.randrange(public.n - 2)
            y = public.encrypt(x)
            assert private.decrypt(y) == x

            assert public.encrypt(public.n - 1) == public.n - 1
            assert public.encrypt(public.n) == 0

            assert private.decrypt(public.n - 1) == public.n - 1
            assert private.decrypt(public.n) == 0