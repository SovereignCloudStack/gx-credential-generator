import unittest
from generator.wallet.filesystem_wallet import FileSystemWallet

class FilesytemWalletTestCase(unittest.TestCase):
    def test_get_graph_of_subject(self):
        wallet = FileSystemWallet("/home/anja-strunk/Playground/gaia-x/wallet")
        wallet.get_graph_of_subject("test")


if __name__ == '__main__':
    unittest.main()
