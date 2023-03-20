import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alustetaan_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_rahan_lataaminen_kortille_kasvattaa_saldo_oikein(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(self.maksukortti.saldo, 1100)

    def test_rahan_nostaminen_vahentaa_saldoa_oikein(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(self.maksukortti.saldo, 900)

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(50000000)
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_rahat_riittavat_nostoo_palauttaa_true(self):
        self.assertTrue(self.maksukortti.ota_rahaa(100))

    def test_rahat_eivat_riita_nostoon_palauttaa_false(self):
        self.assertFalse(self.maksukortti.ota_rahaa(2193210931))

    def test_saldon_tulostaminen_toimii_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
