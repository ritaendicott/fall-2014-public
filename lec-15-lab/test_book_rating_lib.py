import unittest
import book_rating_lib as br

class TestBookRating(unittest.TestCase):
    def test_check_isbn(self):
        self.assertTrue(br.check_isbn("034545104X"))
        self.assertTrue(br.check_isbn("0425176428"))
        self.assertTrue(not br.check_isbn("28"))

    def test_parsing_record(self):
        r1 = "1;nyc, new york, usa;NULL"
        out1 = br.parsing_record(r1)
        self.assertEqual(out1, {"record_type": "user", "user":"1",\
                "location": "nyc, new york, usa", "age": "NULL"})
if __name__ == "__main__":
    unittest.main()
