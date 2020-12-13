import unittest
import edit_screenings_utils as esu

class test_edit_screenings_utils(unittest.TestCase):

    def test_convertToDisplayForm(self):
        #correct input
        a = esu.convertToDisplayForm("FilmName,1,01:00,02:00")
        self.assertEqual(a, "Screen 1 -  FilmName:  01:00 02:00 ")

        #one incorrect time
        b = esu.convertToDisplayForm("FilmName,1,01:a0,02:00")
        self.assertEqual(b, "Screen 1 -  FilmName:  02:00 ")

        #two incorrect times
        c = esu.convertToDisplayForm("FilmName,1,01:a0,02:a0")
        self.assertEqual(c, "Screen 1 -  FilmName:  ")

        #incorrect screen 
        d = esu.convertToDisplayForm("FilmName,a,01:00,02:00")
        self.assertEqual(d, "01:00 02:00 ")

        #no times
        e = esu.convertToDisplayForm("FilmName,1")
        self.assertEqual(e, "Screen 1 -  FilmName:  ")

        #no screen or times
        f = esu.convertToDisplayForm("FilmName")
        self.assertEqual(f, "")

    def test_convertToEditForm(self):
        #correct input
        a = esu.convertToEditForm("Screen 1 -  FilmName:  01:00 02:00 ")
        self.assertEqual(a, "FilmName,1,01:00,02:00")

        #one incorrect time
        b = esu.convertToEditForm("Screen 1 -  FilmName:  01:a0 02:00 ")
        self.assertEqual(b, "FilmName,1,01:a0,02:00")

        #two incorrect time
        c = esu.convertToEditForm("Screen 1 -  FilmName:  01:a0 02:a0 ")
        self.assertEqual(c, "FilmName,1,01:a0,02:a0")

        #incorrect screen
        d = esu.convertToEditForm("Screen a -  FilmName:  01:00 02:00 ")
        self.assertEqual(d, "FilmName,a,01:00,02:00")

        #no times
        e = esu.convertToEditForm("Screen 1 -  FilmName:  ")
        self.assertEqual(e, "FilmName,1")

        #no filename or times
        e = esu.convertToEditForm("Screen 1 -  ")
        self.assertEqual(e, ",1")

    def test_convertToSaveForm(self):
        #correct input
        a = esu.convertToSaveForm("Screen 1 -  FilmName:  01:00 02:00 ")
        self.assertEqual(a, "FilmName,1, 01:00, 02:00, ")

        #one incorrect time
        b = esu.convertToSaveForm("Screen 1 -  FilmName:  01:a0 02:00 ")
        self.assertEqual(b, "FilmName,1, 01:a0, 02:00, ")

        #two incorrect time
        c = esu.convertToSaveForm("Screen 1 -  FilmName:  01:a0 02:a0 ")
        self.assertEqual(c, "FilmName,1, 01:a0, 02:a0, ")

        #incorrect screen
        d = esu.convertToSaveForm("Screen a -  FilmName:  01:00 02:00 ")
        self.assertEqual(d, "FilmName,a, 01:00, 02:00, ")

        #no times
        e = esu.convertToSaveForm("Screen 1 -  FilmName:  ")
        self.assertEqual(e, "FilmName,1, ")

        #no filename or times
        e = esu.convertToSaveForm("Screen 1 -  ")
        self.assertEqual(e, ",1")
