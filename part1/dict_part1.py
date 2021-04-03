from PyQt5.QtCore import Qt
dict_brush_patt={
"SolidPattern":Qt.SolidPattern,
"NobBush":Qt.NoBrush,
"HorPattern":Qt.HorPattern,
"VerPattern":Qt.VerPattern,
"CrossPattern":Qt.CrossPattern,
"BDiagPattern":Qt.BDiagPattern,
"FDiagPattern":Qt.FDiagPattern,
"DiagCrossPattern":Qt.DiagCrossPattern,
"LinearPattern":Qt.LinearGradientPattern,
"RadialGradientPattern":Qt.RadialGradientPattern,
"ConicalGradientPattern":Qt.ConicalGradientPattern,
"Dense1Pattern":Qt.Dense1Pattern,
"Dense2Pattern":Qt.Dense2Pattern,
"Dense3Pattern":Qt.Dense3Pattern,
"Dense4Pattern":Qt.Dense4Pattern,
"Dense5Pattern":Qt.Dense5Pattern,
"Dense6Pattern":Qt.Dense6Pattern,
"Dense7Pattern":Qt.Dense7Pattern}

def change_brush_pattern(self,index):
    self.qbrush.setStyle(dict_brush_patt[index])