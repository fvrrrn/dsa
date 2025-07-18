import unittest
from typing import cast

from monads import Just
from tasks.t12 import NativeCache, polynomial_hash


class TestNativeCache(unittest.TestCase):
    def test_cache_insert_and_retrieve(self):
        a = {"key": "string123"}

        cache = NativeCache[str, str](
            sz=8, getter=a.__getitem__, hasher=polynomial_hash
        )

        result1 = cache["key"]
        self.assertIsInstance(result1, Just)
        self.assertEqual(cast(Just, result1).value, a["key"])


if __name__ == "__main__":
    unittest.main()
