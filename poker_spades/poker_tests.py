import poker_spades
import unittest


class TestSequenceFunctions(unittest.TestCase):
    """ This is one of potentially many TestCases """

    def test_check_straight_true(self):
        print(self.assertEqual(poker_spades.check_straight('S4', 'S3', 'S2'), 4))
        print(self.assertEqual(poker_spades.check_straight('SQ', 'SJ', 'S10'), 12))
        print(self.assertEqual(poker_spades.check_straight('S8', 'S7', 'S9'), 9))

    def test_check_straight_false(self):
        print(self.assertEqual(poker_spades.check_straight('S4', 'S8', 'S2'), 0))
        print(self.assertEqual(poker_spades.check_straight('SA', 'S3', 'S2'), 0))
        print(self.assertEqual(poker_spades.check_straight('SK', 'SK', 'S2'), 0))

    def test_check_3ofkind_true(self):
        print(self.assertEqual(poker_spades.check_3ofa_kind('S4', 'S4', 'S4'), 4))
        print(self.assertEqual(poker_spades.check_3ofa_kind('SA', 'SA', 'SA'), 14))
        print(self.assertEqual(poker_spades.check_3ofa_kind('S2', 'S2', 'S2'), 2))

    def test_check_3ofkind_false(self):
        print(self.assertEqual(poker_spades.check_3ofa_kind('S5', 'S5', 'S2'), 0))
        print(self.assertEqual(poker_spades.check_3ofa_kind('SK', 'SQ', 'SJ'), 0))
        print(self.assertEqual(poker_spades.check_3ofa_kind('SA', 'S3', 'S10'), 0))

    def test_check_royal_true(self):
        print(self.assertEqual(poker_spades.check_royal_flush('SA', 'SK', 'SQ'), 14))
        print(self.assertEqual(poker_spades.check_royal_flush('SK', 'SQ', 'SA'), 14))

    def test_check_royal_false(self):
        print(self.assertEqual(poker_spades.check_royal_flush('S10', 'SJ', 'SK'), 0))
        print(self.assertEqual(poker_spades.check_royal_flush('SK', 'SQ', 'SJ'), 0))
        print(self.assertEqual(poker_spades.check_royal_flush('S7', 'S8', 'S9'), 0))

    def test_check_draw(self):
        print(self.assertEqual(poker_spades.play_cards('SA', 'SK', 'SQ', 'SA', 'SQ', 'SK'), 0))
        print(self.assertEqual(poker_spades.play_cards('S7', 'S8', 'S9', 'S7', 'S8', 'S9'), 0))
        print(self.assertEqual(poker_spades.play_cards('SK', 'SK', 'SK', 'SK', 'SK', 'SK'), 0))
        print(self.assertEqual(poker_spades.play_cards('S9', 'S10', 'SJ', 'SJ', 'S9', 'S10'), 0))
        print(self.assertEqual(poker_spades.play_cards('S4', 'S4', 'S4', 'S4', 'S4', 'S4'), 0))

    def test_check_left_wins(self):
        print(self.assertEqual(poker_spades.play_cards('SA', 'SK', 'SQ', 'SJ', 'SQ', 'SK'), -1))
        print(self.assertEqual(poker_spades.play_cards('S10', 'S9', 'SJ', 'S4', 'S6', 'S5'), -1))
        print(self.assertEqual(poker_spades.play_cards('S6', 'S6', 'S6', 'S2', 'S2', 'S2'), -1))

    def test_check_right_wins(self):
        print(self.assertEqual(poker_spades.play_cards('SA', 'S7', 'SQ', 'SA', 'SQ', 'SK'), 1))
        print(self.assertEqual(poker_spades.play_cards('SK', 'SK', 'SK', 'SA', 'SA', 'SA'), 1))
        print(self.assertEqual(poker_spades.play_cards('S7', 'S6', 'S5', 'S7', 'S9', 'S8'), 1))

    def check_both_players_no_hand(self):
        print(self.assertEqual(poker_spades.play_cards('S4', 'S2', 'S10', 'SJ', 'SQ', 'S4'), 0))
        print(self.assertEqual(poker_spades.play_cards('S4', 'S5', 'S4', 'S7', 'S4', 'S2'), 0))
        print(self.assertEqual(poker_spades.play_cards('SA', 'SK', 'S2', 'S8', 'S3', 'SQ'), 0))

if __name__ == '__main__':
    unittest.main()