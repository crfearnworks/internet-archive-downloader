import unittest
from downloader.src.utils.downloader import download_file

class TestDownloader(unittest.TestCase):
    def test_download_file(self):
        # Test downloading a file from a valid URL
        url = "https://example.com/file.txt"
        filename = "file.txt"
        download_file(url, filename)
        # Assert that the file was downloaded successfully
        self.assertTrue(os.path.exists(filename))
        # Clean up the downloaded file
        os.remove(filename)

        # Test downloading a file from an invalid URL
        url = "https://example.com/invalid"
        filename = "invalid.txt"
        with self.assertRaises(Exception):
            download_file(url, filename)

if __name__ == '__main__':
    unittest.main()