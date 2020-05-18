import unittest

from collectFilesPaths import collectFilesPaths
from collectSubFolders import collectSubFolders

class RecipesTests(unittest.TestCase):

    def test_collectSubFolders(self):
        self.assertEqual(
            set(collectSubFolders('dummyFolder')),
            set(['dummyFolder/folderOne',
                 'dummyFolder/folderTwo',
                 'dummyFolder/folderThree'])
        )

    def test_collectFilesPaths(self):
        self.assertEqual(
            set(collectFilesPaths('dummyFolder')),
            set(['dummyFolder/fileOne.txt', 'dummyFolder/fileTwo.csv'])
        )

    def test_collectFilesPathsExtension(self):
        self.assertEqual(
            set(collectFilesPaths('dummyFolder', 'csv')),
            set(['dummyFolder/fileTwo.csv'])
        )


if __name__ == "__main__":
    unittest.main()