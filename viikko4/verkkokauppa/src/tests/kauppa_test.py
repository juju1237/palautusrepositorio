import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto kutsutaan oikeilla argumenteilla
        pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 5
        )

    def test_maksettaessa_kaksi_tuotetta_pankin_metodia_tilisiirto_kutsutaan_oikeilla_tiedoilla(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        viitegeneraattori_mock.uusi.return_value = 42

        tuotteet = {
            1: Tuote(1, "maito", 5),
            2: Tuote(2, "leipa", 7),
        }
        varasto_mock = Mock()
        varasto_mock.saldo.side_effect = lambda tuote_id: 10 if tuote_id in tuotteet else 0
        varasto_mock.hae_tuote.side_effect = tuotteet.get

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

        pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 12
        )

    def test_maksettaessa_kaksi_samaa_tuotetta_tilisiirto_kutsutaan_oikeilla_tiedoilla(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        viitegeneraattori_mock.uusi.return_value = 42

        tuote = Tuote(1, "maito", 5)
        varasto_mock = Mock()
        varasto_mock.saldo.return_value = 10
        varasto_mock.hae_tuote.return_value = tuote

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 10
        )

    def test_maksettaessa_varastossa_oleva_ja_loppunut_tuote_tilisiirto_kutsutaan_oikeilla_tiedoilla(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        viitegeneraattori_mock.uusi.return_value = 42

        tuotteet = {
            1: Tuote(1, "maito", 5),
            2: Tuote(2, "leipa", 7),
        }
        varasto_mock = Mock()
        varasto_mock.saldo.side_effect = lambda tuote_id: {
            1: 10,
            2: 0,
        }.get(tuote_id, 0)
        varasto_mock.hae_tuote.side_effect = tuotteet.get

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

        pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 5
        )
