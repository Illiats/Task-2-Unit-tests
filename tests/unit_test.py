from unittest import TestCase, main
from anagrams.anagrams import reverse_string


class Test_reverse(TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string('abcd efgh'), 'dcba hgfe')
        self.assertEqual(reverse_string('a1bcd efg!h'), 'd1cba hgf!e')



if __name__ == '__main__':
    main()
