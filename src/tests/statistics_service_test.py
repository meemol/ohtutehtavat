import unittest
import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    def test_etsi_pelaaja(self):
        pelaaja = self.stats.search("Lemieux").name
        self.assertAlmostEqual(pelaaja,"Lemieux" )
    
    def test_team_members(self):
        teammembers = self.stats.team("EDM")
        names = []
        for player in teammembers:
            names.append(player.name)
        self.assertAlmostEqual(names, ["Semenko", "Kurri", "Gretzky"])
    

    def test_top(self):
        players = self.stats.top(50)

        names = []
        for player in players:
            names.append(player.name)
        self.assertAlmostEqual(names , ["Lemieux","Kurri", "Yzerman", "Gretzky"])