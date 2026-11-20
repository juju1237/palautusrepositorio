import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorissa_yksi_ostos(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostos_nimi_ja_lukumaara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), maito.nimi())
        self.assertEqual(ostos.lukumaara(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), maito.hinta())

    def test_kahden_eri_tuotteen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        porkkana = Tuote("Porkkana", 67)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(porkkana)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_jalkeen_korissa_kaksi_ostosta(self):
        maito = Tuote("Maito", 3)
        porkkana = Tuote("Porkkana", 67)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(porkkana)

        self.assertEqual(len(self.kori.ostokset()), 2)

    def test_kahden_eri_tuotteen_jalkeen_korin_hinta_on_tuotteiden_hintojen_summa(self):
        maito = Tuote("Maito", 3)
        porkkana = Tuote("Porkkana", 67)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(porkkana)

        self.assertEqual(self.kori.hinta(), (maito.hinta() + porkkana.hinta()))

    def test_kahden_saman_tuotteen_jalkeen_korissa_kaksi_tavaraa(self):
        porkkana = Tuote("Porkkana", 67)
        self.kori.lisaa_tuote(porkkana)
        self.kori.lisaa_tuote(porkkana)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_jalkeen_korin_hinta_2_kertaa_tuotteen_hinta(self):
        porkkana = Tuote("Porkkana", 67)
        self.kori.lisaa_tuote(porkkana)
        self.kori.lisaa_tuote(porkkana)

        self.assertEqual(self.kori.hinta(), (porkkana.hinta()*2))

    def test_kahden_saman_tuotteen_jalkeen_ostoskorissa_yksi_ostos(self):
        porkkana = Tuote("Porkkana", 67)
        self.kori.lisaa_tuote(porkkana)
        self.kori.lisaa_tuote(porkkana)

        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_kahden_saman_tuotteen_jalkeen_ostos_nimi_ja_lukumaara(self):
        porkkana = Tuote("Porkkana", 67)
        self.kori.lisaa_tuote(porkkana)
        self.kori.lisaa_tuote(porkkana)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), porkkana.nimi())
        self.assertEqual(ostos.lukumaara(), 2)

    def test_saman_tuotteen_poistamisen_jalkeen_ostoskorissa_yksi_kappale(self):
        porkkana = Tuote("Porkkana", 67)
        self.kori.lisaa_tuote(porkkana)
        self.kori.lisaa_tuote(porkkana)

        self.kori.poista_tuote(porkkana)

        self.assertEqual(len(self.kori.ostokset()), 1)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), porkkana.nimi())
        self.assertEqual(ostos.lukumaara(), 1)

    def test_tuotteen_poistamisen_jalkeen_kori_on_tyhjennyt(self):
        porkkana = Tuote("Porkkana", 67)
        self.kori.lisaa_tuote(porkkana)

        self.kori.poista_tuote(porkkana)

        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(len(self.kori.ostokset()), 0)

    def test_tyhjenna_tyhjentaa_korin(self):
        porkkana = Tuote("Porkkana", 67)
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(porkkana)
        self.kori.lisaa_tuote(porkkana)
        self.kori.lisaa_tuote(maito)

        self.kori.tyhjenna()

        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(len(self.kori.ostokset()), 0)