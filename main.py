from math import e
import matplotlib.pyplot as plt
problemler = {
    1: {'a degeri': 836.7, 'b degeri': 418.35, 'kesit alani': 110, 'giris debisi': 380, 'baslangic yuksekligi': 3.2},
    2: {'a degeri': 792.6, 'b degeri': 396.3, 'kesit alani': 110, 'giris debisi': 360, 'baslangic yuksekligi': 3.0},
    3: {'a degeri': 792.6, 'b degeri': 396.3, 'kesit alani': 120, 'giris debisi': 360, 'baslangic yuksekligi': 3.6},
    4: {'a degeri': 704.4, 'b degeri': 352.2, 'kesit alani': 140, 'giris debisi': 320, 'baslangic yuksekligi': 3.2},
    5: {'a degeri': 704.4, 'b degeri': 352.2, 'kesit alani': 140, 'giris debisi': 320, 'baslangic yuksekligi': 3.6},
    6: {'a degeri': 836.7, 'b degeri': 418.35, 'kesit alani': 130, 'giris debisi': 380, 'baslangic yuksekligi': 3.6},
    7: {'a degeri': 660.4, 'b degeri': 330.2, 'kesit alani': 100, 'giris debisi': 300, 'baslangic yuksekligi': 3.4},
    8: {'a degeri': 836.7, 'b degeri': 418.35, 'kesit alani': 130, 'giris debisi': 380, 'baslangic yuksekligi': 3.2},
    9: {'a degeri': 836.7, 'b degeri': 418.35, 'kesit alani': 150, 'giris debisi': 380, 'baslangic yuksekligi': 3.0},
    10: {'a degeri': 660.4, 'b degeri': 330.2, 'kesit alani': 110, 'giris debisi': 300, 'baslangic yuksekligi': 3.4},
    11: {'a degeri': 748.5, 'b degeri': 374.25, 'kesit alani': 120, 'giris debisi': 340, 'baslangic yuksekligi': 3.6},
    12: {'a degeri': 880.8, 'b degeri': 440.4, 'kesit alani': 100, 'giris debisi': 400, 'baslangic yuksekligi': 3.6},
    13: {'a degeri': 836.7, 'b degeri': 418.35, 'kesit alani': 140, 'giris debisi': 380, 'baslangic yuksekligi': 3.2},
    14: {'a degeri': 748.5, 'b degeri': 374.25, 'kesit alani': 110, 'giris debisi': 340, 'baslangic yuksekligi': 3.2},
    15: {'a degeri': 880.8, 'b degeri': 440.4, 'kesit alani': 140, 'giris debisi': 400, 'baslangic yuksekligi': 3.4},
    16: {'a degeri': 880.8, 'b degeri': 440.4, 'kesit alani': 110, 'giris debisi': 400, 'baslangic yuksekligi': 3.2},
    17: {'a degeri': 660.4, 'b degeri': 330.2, 'kesit alani': 120, 'giris debisi': 300, 'baslangic yuksekligi': 3.0},
    18: {'a degeri': 880.8, 'b degeri': 440.4, 'kesit alani': 140, 'giris debisi': 400, 'baslangic yuksekligi': 3.0},
    19: {'a degeri': 748.5, 'b degeri': 374.25, 'kesit alani': 110, 'giris debisi': 340, 'baslangic yuksekligi': 3.0},
    20: {'a degeri': 792.6, 'b degeri': 396.3, 'kesit alani': 100, 'giris debisi': 360, 'baslangic yuksekligi': 3.6},
    21: {'a degeri': 836.7, 'b degeri': 418.35, 'kesit alani': 130, 'giris debisi': 380, 'baslangic yuksekligi': 3.4},
    22: {'a degeri': 792.6, 'b degeri': 396.3, 'kesit alani': 130, 'giris debisi': 360, 'baslangic yuksekligi': 3.2},
    23: {'a degeri': 748.5, 'b degeri': 374.25, 'kesit alani': 140, 'giris debisi': 340, 'baslangic yuksekligi': 3.6},
    24: {'a degeri': 792.6, 'b degeri': 396.3, 'kesit alani': 140, 'giris debisi': 360, 'baslangic yuksekligi': 3.2},
    25: {'a degeri': 792.6, 'b degeri': 396.3, 'kesit alani': 150, 'giris debisi': 360, 'baslangic yuksekligi': 3.2},
    26: {'a degeri': 704.4, 'b degeri': 352.2, 'kesit alani': 130, 'giris debisi': 320, 'baslangic yuksekligi': 3.4},
    27: {'a degeri': 704.4, 'b degeri': 352.2, 'kesit alani': 140, 'giris debisi': 320, 'baslangic yuksekligi': 3.0},
    28: {'a degeri': 836.7, 'b degeri': 418.35, 'kesit alani': 150, 'giris debisi': 380, 'baslangic yuksekligi': 3.6},
    29: {'a degeri': 836.7, 'b degeri': 418.35, 'kesit alani': 150, 'giris debisi': 380, 'baslangic yuksekligi': 3.4},
    30: {'a degeri': 792.6, 'b degeri': 396.3, 'kesit alani': 130, 'giris debisi': 360, 'baslangic yuksekligi': 3.0},
    31: {'a degeri': 880.8, 'b degeri': 440.4, 'kesit alani': 150, 'giris debisi': 400, 'baslangic yuksekligi': 3.2},
    32: {'a degeri': 880.8, 'b degeri': 440.4, 'kesit alani': 120, 'giris debisi': 400, 'baslangic yuksekligi': 3.4},
    33: {'a degeri': 704.4, 'b degeri': 352.2, 'kesit alani': 120, 'giris debisi': 320, 'baslangic yuksekligi': 3.0},
    34: {'a degeri': 836.7, 'b degeri': 418.35, 'kesit alani': 100, 'giris debisi': 380, 'baslangic yuksekligi': 3.6},
    35: {'a degeri': 880.8, 'b degeri': 440.4, 'kesit alani': 150, 'giris debisi': 400, 'baslangic yuksekligi': 3.0},
    36: {'a degeri': 704.4, 'b degeri': 352.2, 'kesit alani': 120, 'giris debisi': 320, 'baslangic yuksekligi': 3.6},
    37: {'a degeri': 660.4, 'b degeri': 330.2, 'kesit alani': 130, 'giris debisi': 300, 'baslangic yuksekligi': 3.6},
    38: {'a degeri': 880.8, 'b degeri': 440.4, 'kesit alani': 150, 'giris debisi': 400, 'baslangic yuksekligi': 3.6},
    39: {'a degeri': 836.7, 'b degeri': 418.35, 'kesit alani': 100, 'giris debisi': 380, 'baslangic yuksekligi': 3.2},
    40: {'a degeri': 792.6, 'b degeri': 396.3, 'kesit alani': 120, 'giris debisi': 360, 'baslangic yuksekligi': 3.4},
    41: {'a degeri': 660.4, 'b degeri': 330.2, 'kesit alani': 130, 'giris debisi': 300, 'baslangic yuksekligi': 3.4},
    42: {'a degeri': 836.7, 'b degeri': 418.35, 'kesit alani': 140, 'giris debisi': 380, 'baslangic yuksekligi': 3.4},
    43: {'a degeri': 660.4, 'b degeri': 330.2, 'kesit alani': 110, 'giris debisi': 300, 'baslangic yuksekligi': 3.6},
    44: {'a degeri': 704.4, 'b degeri': 352.2, 'kesit alani': 140, 'giris debisi': 320, 'baslangic yuksekligi': 3.4},
    45: {'a degeri': 748.5, 'b degeri': 374.25, 'kesit alani': 110, 'giris debisi': 340, 'baslangic yuksekligi': 3.6},
    46: {'a degeri': 748.5, 'b degeri': 374.25, 'kesit alani': 120, 'giris debisi': 340, 'baslangic yuksekligi': 3.2},
    47: {'a degeri': 660.4, 'b degeri': 330.2, 'kesit alani': 150, 'giris debisi': 300, 'baslangic yuksekligi': 3.6},
    48: {'a degeri': 792.6, 'b degeri': 396.3, 'kesit alani': 150, 'giris debisi': 360, 'baslangic yuksekligi': 3.0},
    49: {'a degeri': 836.7, 'b degeri': 418.35, 'kesit alani': 110, 'giris debisi': 380, 'baslangic yuksekligi': 3.4},
    50: {'a degeri': 704.4, 'b degeri': 352.2, 'kesit alani': 150, 'giris debisi': 320, 'baslangic yuksekligi': 3.6},
    51: {'a degeri': 792.6, 'b degeri': 396.3, 'kesit alani': 140, 'giris debisi': 360, 'baslangic yuksekligi': 3.6},
    52: {'a degeri': 704.4, 'b degeri': 352.2, 'kesit alani': 110, 'giris debisi': 320, 'baslangic yuksekligi': 3.4},
    53: {'a degeri': 704.4, 'b degeri': 352.2, 'kesit alani': 100, 'giris debisi': 320, 'baslangic yuksekligi': 3.6},
    54: {'a degeri': 660.4, 'b degeri': 330.2, 'kesit alani': 130, 'giris debisi': 300, 'baslangic yuksekligi': 3.0},
    55: {'a degeri': 748.5, 'b degeri': 374.25, 'kesit alani': 140, 'giris debisi': 340, 'baslangic yuksekligi': 3.2},
    56: {'a degeri': 704.4, 'b degeri': 352.2, 'kesit alani': 130, 'giris debisi': 320, 'baslangic yuksekligi': 3.2},
    57: {'a degeri': 836.7, 'b degeri': 418.35, 'kesit alani': 140, 'giris debisi': 380, 'baslangic yuksekligi': 3.0},
    58: {'a degeri': 748.5, 'b degeri': 374.25, 'kesit alani': 110, 'giris debisi': 340, 'baslangic yuksekligi': 3.4},
    59: {'a degeri': 880.8, 'b degeri': 440.4, 'kesit alani': 120, 'giris debisi': 400, 'baslangic yuksekligi': 3.6},
    60: {'a degeri': 792.6, 'b degeri': 396.3, 'kesit alani': 140, 'giris debisi': 360, 'baslangic yuksekligi': 3.4},
    61: {'a degeri': 748.5, 'b degeri': 374.25, 'kesit alani': 130, 'giris debisi': 340, 'baslangic yuksekligi': 3.2},
    62: {'a degeri': 792.6, 'b degeri': 396.3, 'kesit alani': 120, 'giris debisi': 360, 'baslangic yuksekligi': 3.0},
    63: {'a degeri': 660.4, 'b degeri': 330.2, 'kesit alani': 100, 'giris debisi': 300, 'baslangic yuksekligi': 3.6},
    64: {'a degeri': 792.6, 'b degeri': 396.3, 'kesit alani': 110, 'giris debisi': 360, 'baslangic yuksekligi': 3.4},
    65: {'a degeri': 748.5, 'b degeri': 374.25, 'kesit alani': 130, 'giris debisi': 340, 'baslangic yuksekligi': 3.4},
    66: {'a degeri': 792.6, 'b degeri': 396.3, 'kesit alani': 100, 'giris debisi': 360, 'baslangic yuksekligi': 3.0},
    67: {'a degeri': 792.6, 'b degeri': 396.3, 'kesit alani': 100, 'giris debisi': 360, 'baslangic yuksekligi': 3.2},
    68: {'a degeri': 748.5, 'b degeri': 374.25, 'kesit alani': 140, 'giris debisi': 340, 'baslangic yuksekligi': 3.4},
    69: {'a degeri': 748.5, 'b degeri': 374.25, 'kesit alani': 100, 'giris debisi': 340, 'baslangic yuksekligi': 3.6},
    70: {'a degeri': 748.5, 'b degeri': 374.25, 'kesit alani': 120, 'giris debisi': 340, 'baslangic yuksekligi': 3.4},
    71: {'a degeri': 704.4, 'b degeri': 352.2, 'kesit alani': 130, 'giris debisi': 320, 'baslangic yuksekligi': 3.6},
    72: {'a degeri': 660.4, 'b degeri': 330.2, 'kesit alani': 120, 'giris debisi': 300, 'baslangic yuksekligi': 3.2},
    73: {'a degeri': 748.5, 'b degeri': 374.25, 'kesit alani': 120, 'giris debisi': 340, 'baslangic yuksekligi': 3.0},
    74: {'a degeri': 748.5, 'b degeri': 374.25, 'kesit alani': 150, 'giris debisi': 340, 'baslangic yuksekligi': 3.4},
    75: {'a degeri': 660.4, 'b degeri': 330.2, 'kesit alani': 150, 'giris debisi': 300, 'baslangic yuksekligi': 3.4},
    76: {'a degeri': 748.5, 'b degeri': 374.25, 'kesit alani': 150, 'giris debisi': 340, 'baslangic yuksekligi': 3.0},
    77: {'a degeri': 880.8, 'b degeri': 440.4, 'kesit alani': 130, 'giris debisi': 400, 'baslangic yuksekligi': 3.4},
    78: {'a degeri': 792.6, 'b degeri': 396.3, 'kesit alani': 150, 'giris debisi': 360, 'baslangic yuksekligi': 3.4},
    79: {'a degeri': 836.7, 'b degeri': 418.35, 'kesit alani': 130, 'giris debisi': 380, 'baslangic yuksekligi': 3.0},
    80: {'a degeri': 660.4, 'b degeri': 330.2, 'kesit alani': 120, 'giris debisi': 300, 'baslangic yuksekligi': 3.6},
    81: {'a degeri': 660.4, 'b degeri': 330.2, 'kesit alani': 140, 'giris debisi': 300, 'baslangic yuksekligi': 3.4},
    82: {'a degeri': 660.4, 'b degeri': 330.2, 'kesit alani': 100, 'giris debisi': 300, 'baslangic yuksekligi': 3.0},
    83: {'a degeri': 792.6, 'b degeri': 396.3, 'kesit alani': 110, 'giris debisi': 360, 'baslangic yuksekligi': 3.2},
    84: {'a degeri': 660.4, 'b degeri': 330.2, 'kesit alani': 150, 'giris debisi': 300, 'baslangic yuksekligi': 3.2},
    85: {'a degeri': 880.8, 'b degeri': 440.4, 'kesit alani': 130, 'giris debisi': 400, 'baslangic yuksekligi': 3.2},
    86: {'a degeri': 660.4, 'b degeri': 330.2, 'kesit alani': 130, 'giris debisi': 300, 'baslangic yuksekligi': 3.2},
    87: {'a degeri': 704.4, 'b degeri': 352.2, 'kesit alani': 100, 'giris debisi': 320, 'baslangic yuksekligi': 3.0},
    88: {'a degeri': 748.5, 'b degeri': 374.25, 'kesit alani': 130, 'giris debisi': 340, 'baslangic yuksekligi': 3.6},
    89: {'a degeri': 836.7, 'b degeri': 418.35, 'kesit alani': 120, 'giris debisi': 380, 'baslangic yuksekligi': 3.6},
    90: {'a degeri': 836.7, 'b degeri': 418.35, 'kesit alani': 100, 'giris debisi': 380, 'baslangic yuksekligi': 3.0},
    91: {'a degeri': 660.4, 'b degeri': 330.2, 'kesit alani': 110, 'giris debisi': 300, 'baslangic yuksekligi': 3.0},
    92: {'a degeri': 704.4, 'b degeri': 352.2, 'kesit alani': 150, 'giris debisi': 320, 'baslangic yuksekligi': 3.4},
    93: {'a degeri': 704.4, 'b degeri': 352.2, 'kesit alani': 120, 'giris debisi': 320, 'baslangic yuksekligi': 3.4},
    94: {'a degeri': 748.5, 'b degeri': 374.25, 'kesit alani': 150, 'giris debisi': 340, 'baslangic yuksekligi': 3.2},
    95: {'a degeri': 704.4, 'b degeri': 352.2, 'kesit alani': 130, 'giris debisi': 320, 'baslangic yuksekligi': 3.0},
    96: {'a degeri': 748.5, 'b degeri': 374.25, 'kesit alani': 100, 'giris debisi': 340, 'baslangic yuksekligi': 3.2},
    97: {'a degeri': 704.4, 'b degeri': 352.2, 'kesit alani': 110, 'giris debisi': 320, 'baslangic yuksekligi': 3.2},
    98: {'a degeri': 880.8, 'b degeri': 440.4, 'kesit alani': 110, 'giris debisi': 400, 'baslangic yuksekligi': 3.0},
    99: {'a degeri': 880.8, 'b degeri': 440.4, 'kesit alani': 140, 'giris debisi': 400, 'baslangic yuksekligi': 3.2},
    100: {'a degeri': 660.4, 'b degeri': 330.2, 'kesit alani': 140, 'giris debisi': 300, 'baslangic yuksekligi': 3.0},
    101: {'a degeri': 880.8, 'b degeri': 440.4, 'kesit alani': 130, 'giris debisi': 400, 'baslangic yuksekligi': 3.0},
    102: {'a degeri': 748.5, 'b degeri': 374.25, 'kesit alani': 100, 'giris debisi': 340, 'baslangic yuksekligi': 3.4},
    103: {'a degeri': 704.4, 'b degeri': 352.2, 'kesit alani': 110, 'giris debisi': 320, 'baslangic yuksekligi': 3.6},
    104: {'a degeri': 880.8, 'b degeri': 440.4, 'kesit alani': 150, 'giris debisi': 400, 'baslangic yuksekligi': 3.4},
    105: {'a degeri': 660.4, 'b degeri': 330.2, 'kesit alani': 140, 'giris debisi': 300, 'baslangic yuksekligi': 3.6},
    106: {'a degeri': 880.8, 'b degeri': 440.4, 'kesit alani': 100, 'giris debisi': 400, 'baslangic yuksekligi': 3.2},
    107: {'a degeri': 836.7, 'b degeri': 418.35, 'kesit alani': 110, 'giris debisi': 380, 'baslangic yuksekligi': 3.6},
    108: {'a degeri': 748.5, 'b degeri': 374.25, 'kesit alani': 150, 'giris debisi': 340, 'baslangic yuksekligi': 3.6},
    109: {'a degeri': 704.4, 'b degeri': 352.2, 'kesit alani': 100, 'giris debisi': 320, 'baslangic yuksekligi': 3.4},
    110: {'a degeri': 748.5, 'b degeri': 374.25, 'kesit alani': 130, 'giris debisi': 340, 'baslangic yuksekligi': 3.0},
    111: {'a degeri': 704.4, 'b degeri': 352.2, 'kesit alani': 120, 'giris debisi': 320, 'baslangic yuksekligi': 3.2},
    112: {'a degeri': 880.8, 'b degeri': 440.4, 'kesit alani': 110, 'giris debisi': 400, 'baslangic yuksekligi': 3.6},
    113: {'a degeri': 836.7, 'b degeri': 418.35, 'kesit alani': 100, 'giris debisi': 380, 'baslangic yuksekligi': 3.4},
    114: {'a degeri': 792.6, 'b degeri': 396.3, 'kesit alani': 140, 'giris debisi': 360, 'baslangic yuksekligi': 3.0},
    115: {'a degeri': 660.4, 'b degeri': 330.2, 'kesit alani': 140, 'giris debisi': 300, 'baslangic yuksekligi': 3.2},
    116: {'a degeri': 704.4, 'b degeri': 352.2, 'kesit alani': 100, 'giris debisi': 320, 'baslangic yuksekligi': 3.2},
    117: {'a degeri': 880.8, 'b degeri': 440.4, 'kesit alani': 120, 'giris debisi': 400, 'baslangic yuksekligi': 3.2},
    118: {'a degeri': 836.7, 'b degeri': 418.35, 'kesit alani': 140, 'giris debisi': 380, 'baslangic yuksekligi': 3.6},
    119: {'a degeri': 836.7, 'b degeri': 418.35, 'kesit alani': 110, 'giris debisi': 380, 'baslangic yuksekligi': 3.0},
    120: {'a degeri': 836.7, 'b degeri': 418.35, 'kesit alani': 120, 'giris debisi': 380, 'baslangic yuksekligi': 3.2},
    121: {'a degeri': 880.8, 'b degeri': 440.4, 'kesit alani': 130, 'giris debisi': 400, 'baslangic yuksekligi': 3.6},
    122: {'a degeri': 880.8, 'b degeri': 440.4, 'kesit alani': 140, 'giris debisi': 400, 'baslangic yuksekligi': 3.6},
    123: {'a degeri': 660.4, 'b degeri': 330.2, 'kesit alani': 150, 'giris debisi': 300, 'baslangic yuksekligi': 3.0},
    124: {'a degeri': 792.6, 'b degeri': 396.3, 'kesit alani': 100, 'giris debisi': 360, 'baslangic yuksekligi': 3.4},
    125: {'a degeri': 880.8, 'b degeri': 440.4, 'kesit alani': 120, 'giris debisi': 400, 'baslangic yuksekligi': 3.0},
    126: {'a degeri': 748.5, 'b degeri': 374.25, 'kesit alani': 140, 'giris debisi': 340, 'baslangic yuksekligi': 3.0},
    127: {'a degeri': 880.8, 'b degeri': 440.4, 'kesit alani': 110, 'giris debisi': 400, 'baslangic yuksekligi': 3.4},
    128: {'a degeri': 792.6, 'b degeri': 396.3, 'kesit alani': 130, 'giris debisi': 360, 'baslangic yuksekligi': 3.6},
    129: {'a degeri': 836.7, 'b degeri': 418.35, 'kesit alani': 120, 'giris debisi': 380, 'baslangic yuksekligi': 3.4},
    130: {'a degeri': 880.8, 'b degeri': 440.4, 'kesit alani': 100, 'giris debisi': 400, 'baslangic yuksekligi': 3.0},
    131: {'a degeri': 704.4, 'b degeri': 352.2, 'kesit alani': 150, 'giris debisi': 320, 'baslangic yuksekligi': 3.2},
    132: {'a degeri': 792.6, 'b degeri': 396.3, 'kesit alani': 130, 'giris debisi': 360, 'baslangic yuksekligi': 3.4},
    133: {'a degeri': 704.4, 'b degeri': 352.2, 'kesit alani': 110, 'giris debisi': 320, 'baslangic yuksekligi': 3.0},
    134: {'a degeri': 660.4, 'b degeri': 330.2, 'kesit alani': 100, 'giris debisi': 300, 'baslangic yuksekligi': 3.2},
    135: {'a degeri': 836.7, 'b degeri': 418.35, 'kesit alani': 120, 'giris debisi': 380, 'baslangic yuksekligi': 3.0},
    136: {'a degeri': 748.5, 'b degeri': 374.25, 'kesit alani': 100, 'giris debisi': 340, 'baslangic yuksekligi': 3.0},
    137: {'a degeri': 792.6, 'b degeri': 396.3, 'kesit alani': 110, 'giris debisi': 360, 'baslangic yuksekligi': 3.6},
    138: {'a degeri': 792.6, 'b degeri': 396.3, 'kesit alani': 120, 'giris debisi': 360, 'baslangic yuksekligi': 3.2},
    139: {'a degeri': 704.4, 'b degeri': 352.2, 'kesit alani': 150, 'giris debisi': 320, 'baslangic yuksekligi': 3.0},
    140: {'a degeri': 792.6, 'b degeri': 396.3, 'kesit alani': 150, 'giris debisi': 360, 'baslangic yuksekligi': 3.6},
    141: {'a degeri': 660.4, 'b degeri': 330.2, 'kesit alani': 120, 'giris debisi': 300, 'baslangic yuksekligi': 3.4},
    142: {'a degeri': 660.4, 'b degeri': 330.2, 'kesit alani': 110, 'giris debisi': 300, 'baslangic yuksekligi': 3.2},
    143: {'a degeri': 836.7, 'b degeri': 418.35, 'kesit alani': 150, 'giris debisi': 380, 'baslangic yuksekligi': 3.2},
    144: {'a degeri': 880.8, 'b degeri': 440.4, 'kesit alani': 100, 'giris debisi': 400, 'baslangic yuksekligi': 3.4}}
problem_input = int(input("Problem numaranizi giriniz: "))
Y_max = float(input("Ymax giriniz"))
a = (problemler[problem_input]['a degeri'])
b = (problemler[problem_input]['b degeri'])
cross_sec = (problemler[problem_input]['kesit alani'])
Y_inital = (problemler[problem_input]['baslangic yuksekligi'])
Q_input = (problemler[problem_input]['giris debisi'])
dt = 2
i = list(range(0,24,2))
y_degerleri = []
for t in i:
    x = t + 2
    yx = Y_inital + ((Q_input - (a - (b*(e**((t%24-12)**2/(24**2))))))/cross_sec)*dt
    if (yx > Y_max):
        print("Depo tastı yukseklik",yx)
        yx = Y_max
    else:
        yx = Y_inital + ((Q_input - (a - (b*(e**((t%24-12)**2/(24**2))))))/cross_sec)*dt
    print("t = ",t)
    print("y(",x,")",yx)
    Y_inital = yx
    y_degerleri.append(yx)
ortanca_degerler = []
y_degerleri_yumusak = []
ortanca_degerler = []
y_degerleri_yumusak = []
y_degerleri.insert(0,(problemler[problem_input]['baslangic yuksekligi']))
def yumusak_grafik(y_degerleri): #grafigi 24 saate cevirmek icin ara degerleri ortalama aliyor
    for i in range(len(y_degerleri)):
        try:
            mid = ( y_degerleri[i] + y_degerleri[i+1]) / 2
            ortanca_degerler.append(mid)
        except:
            print("basarili")
    for i in range(len(y_degerleri)):
        try:
            y_degerleri_yumusak.append(y_degerleri[i])
            y_degerleri_yumusak.append(ortanca_degerler[i])
        except:
            print("basarili")
yumusak_grafik(y_degerleri)
y_degerleri = y_degerleri_yumusak
plt.plot(y_degerleri)
plt.ylabel('yukseklik(m)')
plt.xlabel('saat')
plt.show()