import datetime

def dghis_mde_tsevri(agdgoma: str):
    dabadeba = datetime.datetime.strptime(agdgoma, "%Y-%m-%d")
    dabadebis_tviseburi = dabadeba.month
    dabadebis_dge = dabadeba.day
    dghes = datetime.date.today()
    dghes_tviseburi = dghes.month
    dghes_dge = dghes.day
    shemdegi_tsevri = datetime.date(dghes.year, dabadebis_tviseburi, dabadebis_dge)
    if shemdegi_tsevri < dghes:
        shemdegi_tsevri = datetime.date(dghes.year + 1, dabadebis_tviseburi, dabadebis_dge)

    dgheebi_darchenili = (shemdegi_tsevri - dghes).days
    return dgheebi_darchenili

agdgoma_shemosavali = '2005-09-22'
print(f"Dghis mde tsevri: {dghis_mde_tsevri(agdgoma_shemosavali)}")

def ori_nashti_gamotana(func):
    def shemcveli(*args, **kwargs):
        shedegi = func(*args, **kwargs)
        return shedegi * 2
    return shemcveli

@ori_nashti_gamotana
def jamshi_chertva(a, b):
    return a + b

@ori_nashti_gamotana
def mititebuli_tqma(saxeli, momalsheni="Gamarjoba"):
    return f"{momalsheni}, {saxeli}!"

print(jamshi_chertva(3, 4))
print(mititebuli_tqma("Tengo"))
print(mititebuli_tqma("Tengo", momalsheni="Dila mshvidobis"))

import datetime
def logireba_gankhilvani(func):
    def shemcveli(*args, **kwargs):
        dgelobiti_didi = datetime.datetime.now()
        shedegi = func(*args, **kwargs)

        print(f"Funqcia: {func.__name__}")
        print(f"Gankhilia: {dgelobiti_didi}")
        print(f"Shedegi: {shedegi}")
        return shedegi

    return shemcveli

@logireba_gankhilvani
def jamshi_chertva(a, b):
    return a + b

@logireba_gankhilvani
def gamravleba(a, b):
    return a * b

print(jamshi_chertva(3, 4))
print(gamravleba(2, 5))

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class Mopoveba(QWidget):
    def __init__(self):
        super().__init__()

        self.gadawyvetileba()

    def gadawyvetileba(self):
        self.setGeometry(100, 100, 300, 150)

        ganevirveba = QVBoxLayout()

        self.teksti_veli = QLineEdit(self)
        self.teksti_veli.setPlaceholderText("Sheiyvanet tekst")

        self.sheqmnis_gunduli = QPushButton("Sheiyvane", self)

        self.shedegi_etiqueti = QLabel("Ar gaqvs sheiyvanili tekst", self)

        self.sheqmnis_gunduli.clicked.connect(self.mogeba_shedegi)

        ganevirveba.addWidget(self.teksti_veli)
        ganevirveba.addWidget(self.sheqmnis_gunduli)
        ganevirveba.addWidget(self.shedegi_etiqueti)

        self.setLayout(ganevirveba)

    def mogeba_shedegi(self):
        sheyvanili_teksti = self.teksti_veli.text()
        self.shedegi_etiqueti.setText(f"Sheyvanili tekstia: {sheyvanili_teksti}")

aplikacia = QApplication(sys.argv)
fereastra = Mopoveba()
fereastra.show()

sys.exit(aplikacia.exec_())