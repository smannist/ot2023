import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate = Kassapaate()

    def test_luodun_kassapaatteen_rahamaara_on_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_alustuksessa_edullisia_lounaita_ei_ole_myyty(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_alustuksessa_maukkaita_lounaita_ei_ole_myyty(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_lounaan_ostaminen_kateisella_nostaa_kassan_rahamaaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_edullisen_lounaan_ostaminen_kasvataa_edullisten_lounaiden_ostomaaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisen_lounaan_ostaminen_palauttaa_oikean_maaran_vaihtorahaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)

    def test_edullisen_lounaan_ostaminen_riittamattomalla_summalla_ei_muuta_rahamaaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisen_lounaan_ostaminen_riittamattomalla_summalla_palauttaa_rahat(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(10), 10)

    def test_edullisen_lounaan_ostaminen_riittamattomalla_summalla_ei_nosta_myyntia(self):
        self.kassapaate.syo_edullisesti_kateisella(10)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaan_lounaan_ostaminen_kateisella_nostaa_kassan_rahamaaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    
    def test_maukkaan_lounaan_ostaminen_kasvataa_edullisten_lounaiden_ostomaaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaan_lounaan_ostaminen_palauttaa_oikean_maaran_vaihtorahaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(460), 60)

    def test_maukkaan_lounaan_ostaminen_riittamattomalla_summalla_ei_muuta_rahamaaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaan_lounaan_ostaminen_riittamattomalla_summalla_palauttaa_rahat(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(10), 10)

    def test_maukkaan_lounaan_ostaminen_riittamattomalla_summalla_ei_nosta_myyntia(self):
        self.kassapaate.syo_maukkaasti_kateisella(10)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kassassa_oleva_rahamaara_ei_muutu_jos_kortilla_ostetaan_edullinen_lounas(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassassa_oleva_rahamaara_ei_muutu_jos_kortilla_ostetaan_maukas_lounas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisen_lounaan_hinta_veloitetaan_kortilta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 760)

    def test_edullisen_lounaan_ostaminen_palauttaa_true_jos_rahaa_on_tarpeeksi(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))
    
    def test_edullisen_lounaan_ostaminen_kortilla_nostaa_myytyjen_maaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_edullisen_lounaan_ostaminen_kortilla_jossa_ei_ole_tarpeeksi_saldoa_ei_muuta_saldoa(self):
        maksukortti = Maksukortti(50)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 50)

    def test_edullisen_lounaan_ostaminen_kortilla_jossa_ei_ole_tarpeeksi_saldoa_ei_muuta_maaraa(self):
        maksukortti = Maksukortti(50)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_edullisen_lounaan_ostaminen_kortilla_jossa_ei_ole_tarpeeksi_saldoa_palauttaa_false(self):
        maksukortti = Maksukortti(50)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(maksukortti))
    
    def test_maukkaan_lounaan_hinta_veloitetaan_kortilta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 600)

    def test_maukkaan_lounaan_ostaminen_palauttaa_true_jos_rahaa_on_tarpeeksi(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))

    def test_maukkaan_lounaan_ostaminen_kortilla_nostaa_myytyjen_maaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaan_lounaan_ostaminen_kortilla_jossa_ei_ole_tarpeeksi_saldoa_ei_muuta_saldoa(self):
        maksukortti = Maksukortti(50)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 50)

    def test_maukkaan_lounaan_ostaminen_kortilla_jossa_ei_ole_tarpeeksi_saldoa_ei_muuta_maaraa(self):
        maksukortti = Maksukortti(50)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maukkaan_lounaan_ostaminen_kortilla_jossa_ei_ole_tarpeeksi_saldoa_palauttaa_false(self):
        maksukortti = Maksukortti(50)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(maksukortti))

    def test_kortille_rahaa_ladattaessa_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.maksukortti.saldo, 2000)

    def test_kortille_rahaa_ladatessa_kassan_rahamaara_kasvaa_ladatulla_summalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)
