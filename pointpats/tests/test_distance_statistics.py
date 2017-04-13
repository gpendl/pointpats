import unittest
import numpy as np

from ..distance_statistics import *
from ..pointpattern import PointPattern


class TestDistanceStatistics(unittest.TestCase):
    def setUp(self):
        self.points = [[66.22, 32.54], [22.52, 22.39], [31.01, 81.21],
                       [9.47, 31.02], [30.78, 60.10], [75.21, 58.93],
                       [79.26, 7.68], [8.23, 39.93], [98.73, 77.17],
                       [89.78, 42.53], [65.19, 92.08], [54.46, 8.48]]
        self.pp = PointPattern(self.points)

    def test_distance_statistics_G(self):
        g = G(self.pp, intervals=20)
        distance_domain_sequence = [
            0.0, 1.73156208378, 3.46312416757, 5.19468625135,
            6.92624833514, 8.65781041892, 10.3893725027, 12.1209345865,
            13.8524966703, 15.5840587541, 17.3156208378, 19.0471829216,
            20.7787450054, 22.5103070892, 24.241869173, 25.9734312568,
            27.7049933406, 29.4365554243, 31.1681175081, 32.8996795919,
            34.6312416757, 36.3628037595
        ]
        envelop = [
            0.0, 0.0146894910196, 0.0574759094992, 0.124697772575,
            0.210831326089, 0.309238901911, 0.413008064625, 0.515735506438,
            0.612136108644, 0.698406273989, 0.772327023751, 0.83314205264,
            0.881278728773, 0.917991964321, 0.945004075083, 0.964194409454,
            0.977368288342, 0.986112304319, 0.991726501147, 0.995214862073,
            0.997313134422, 0.998535316975
        ]
        np.testing.assert_array_almost_equal(g.ev, envelop)
        np.testing.assert_array_almost_equal(g.d, distance_domain_sequence)

    def test_distance_statistics_F(self):
        f = F(self.pp, intervals=20)
        distance_domain_sequence = [
            0.0, 1.73156208378, 3.46312416757, 5.19468625135,
            6.92624833514, 8.65781041892, 10.3893725027, 12.1209345865,
            13.8524966703, 15.5840587541, 17.3156208378, 19.0471829216,
            20.7787450054, 22.5103070892, 24.241869173, 25.9734312568,
            27.7049933406, 29.4365554243, 31.1681175081, 32.8996795919,
            34.6312416757, 36.3628037595
        ]
        envelop = [
            0.0, 0.0146894910196, 0.0574759094992, 0.124697772575,
            0.210831326089, 0.309238901911, 0.413008064625, 0.515735506438,
            0.612136108644, 0.698406273989, 0.772327023751, 0.83314205264,
            0.881278728773, 0.917991964321, 0.945004075083, 0.964194409454,
            0.977368288342, 0.986112304319, 0.991726501147, 0.995214862073,
            0.997313134422, 0.998535316975
        ]
        np.testing.assert_array_almost_equal(f.ev, envelop)
        np.testing.assert_array_almost_equal(f.d, distance_domain_sequence)

    def test_distance_statistics_J(self):
        j = J(self.pp, intervals=20)
        distance_domain_sequence = [
            0.0, 1.73156208378, 3.46312416757, 5.19468625135,
            6.92624833514, 8.65781041892, 10.3893725027, 12.1209345865,
            13.8524966703, 15.5840587541, 17.3156208378, 19.0471829216,
            20.7787450054, 22.5103070892
        ]
        for val in j.ev:
            np.testing.assert_approx_equal(val, 1.0)
        np.testing.assert_array_almost_equal(j.d, distance_domain_sequence)

    def test_distance_statistics_K(self):
        k = K(self.pp, intervals=20)
        distance_domain_sequence = [
            0.0, 6.18740858518, 12.3748171704, 18.5622257555,
            24.7496343407, 30.9370429259, 37.1244515111, 43.3118600963,
            49.4992686815, 55.6866772666, 61.8740858518, 68.061494437,
            74.2489030222, 80.4363116074, 86.6237201926, 92.8111287777,
            98.9985373629, 105.185945948, 111.373354533, 117.560763118,
            123.748171704, 129.935580289
        ]
        envelop = [
            0.0, 120.27281169, 481.091246759, 1082.45530521,
            1924.36498704, 3006.82029225, 4329.82122083, 5893.3677728,
            7697.45994815, 9742.09774688, 12027.281169, 14553.0102145,
            17319.2848833, 20326.1051756, 23573.4710912, 27061.3826302,
            30789.8397926, 34758.8425784, 38968.3909875, 43418.48502,
            48109.1246759, 53040.3099552
        ]
        np.testing.assert_array_almost_equal(k.ev, envelop)
        np.testing.assert_array_almost_equal(k.d, distance_domain_sequence)

    def test_distance_statistics_L(self):
        l = L(self.pp, intervals=20)
        distance_domain_sequence = [
            0.0, 6.18740858518, 12.3748171704, 18.5622257555,
            24.7496343407, 30.9370429259, 37.1244515111, 43.3118600963,
            49.4992686815, 55.6866772666, 61.8740858518, 68.061494437,
            74.2489030222, 80.4363116074, 86.6237201926, 92.8111287777,
            98.9985373629, 105.185945948, 111.373354533, 117.560763118,
            123.748171704, 129.935580289
        ]
        np.testing.assert_array_almost_equal(l.d, distance_domain_sequence)
