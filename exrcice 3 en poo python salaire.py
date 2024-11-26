from datetime import *
class Salarie :
    __auto = 0
    def __init__(self, nom , prenom , date_Naissance : int ,date_Embauche : int , salaire_Base : float):
        salarie__auto +=1
        self.__matricule = salarie__auto
        self.__nom = nom
        self.__prenom = prenom
        self.__date_Naissance = date_Naissance
        self.__date_Embauche = date_Embauche
        self.__salaire_Base = salaire_Base
    @property
    def matricule(self):
        return self.__matricule

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self,value):
        self.__nom = value

    @property
    def prenom(self):
        return self.__prenom

    @prenom.setter
    def prenom(self, value):
        self.__prenom = value

    @property
    def dateNaissance(self):
        return self.__date_Naissance

    @DateNaissance.setter
    def DateNaissance(self, value):
        self.__date_Naissance = value

    @property
    def dateEmbauche(self):
        return self.__date_Embauche

    @DateEmbauche.setter
    def DateEmbauche(self, value):
        if Age >=16 :
            self.__date_Embauche = value

    @property
    def salaireBase(self):
        return self.__salaire_Base

    @SalairBase.setter
    def SalaireBase(self, value):
        if  self.__salair_Base > 0 :
         self.__salair_Base = value

    @property
    def Age(self):
        return datetime.now().year - date_Naissance

    @property
    def ancienne(self):
        return self.__ancienne

    @property
    def primeAnciente(self):
        if 0 < self.__anciente < 2:
            taux_anciente = 0
        elif 2 <= self.__anciente < 5:
            taux_anciente = 5
        elif 5 <= self.__anciente < 10:
            taux_anciente = 10
        elif 10 <= self.__anciente < 15:
            taux_anciente = 15
        elif 15 <= self.__anciente < 20:
            taux_anciente = 20
        else:
            taux_anciente = 25
        return self.__salair_base * taux_anciente / 100

    @property
    def SalaireBrut(self):
        salaireBrut = self.prime_ancients + self.__salaire_Base
        return self.salaireBrut

    @property
    def mutuelle(self):
       mutuelle = (3 * self.salaireBrut) / 100
       return self.mutuelle

    @property
    def Retrait(self):
        Retrait= (6 * self.salaireBrut) / 100
        return self.Retrait

    @property
    def dateRetrait(self):
        return self.date_Naissance.replace(year=self.__date_Naissance + 60 )

    @property
    def IR(self):
        if 0 < self.__salaireBrut <= 2500:
            taux = 0
            deduction = 0
        elif 2500 <  self.__salaireBrut <= 4166:
            taux = 10
            deduction = 250
        elif 4166 <  self.__salaireBrut  <= 5000:
            taux = 20
            deduction = 666.67
        elif 5000 <  self.__salaireBrut  <= 6666:
            taux = 30
            deduction = 1166.67
        elif 6666 <  self.__salaireBrut  <= 15000:
            taux = 34
            deduction = 1433.33
        else:
            taux = 38
            deduction = 2033.33
        IR =  self.salaireBrut * taux / 100 - deduction
        return self.IR

    @property
    def salaireNet(self):
        salaire_Net = self.salairBrut - self.mutuelle - self.Retrait- self.IR
        return self.salaire_Net


    def __str__(self):
        return (f"Nom : {self.nom}\n"
                f"Prénom : {self.prenom}\n"
                f"Date de Naissance : { self.date_Naissance }\n"
                f"{'Date embauche :' + {str(self.__date_Embauche)} if self.__date_Embauche is not None else 'rien'}\n"
                f"Salaire de basee : {self.salaire_Base} ")






