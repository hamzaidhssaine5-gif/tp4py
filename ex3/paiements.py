from abc import ABC, abstractmethod

def luhn_valide(numero):
    numero = numero.replace(" ", "")
    if not numero.isdigit():
        return False
    total = 0
    inverse = numero[::-1]
    for i, c in enumerate(inverse):
        n = int(c)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0

class Paiement(ABC):
    def __init__(self, montant):
        if montant <= 0:
            raise ValueError("Le montant doit être positif.")
        self._montant = montant

    @abstractmethod
    def payer(self):
        pass

class CarteBancaire(Paiement):
    def __init__(self, montant, numero, cvv):
        super().__init__(montant)
        if not luhn_valide(numero):
            raise ValueError("Numéro de carte invalide")
        if len(cvv) != 3 or not cvv.isdigit():
            raise ValueError("CVV invalide")
        self.numero = numero
        self.cvv = cvv

    def payer(self):
        return f"Paiement de {self._montant:.2f} € par Carte Bancaire (**** {self.numero[-4:]})"

class PayPal(Paiement):
    def __init__(self, montant, email, token):
        super().__init__(montant)
        if "@" not in email:
            raise ValueError("Email invalide")
        self.email = email
        self.token = token

    def payer(self):
        return f"Paiement de {self._montant:.2f} € via PayPal ({self.email})"

class Crypto(Paiement):
    def __init__(self, montant, wallet_id, reseau):
        super().__init__(montant)
        if reseau not in ("BTC", "ETH", "SOL", "BNB"):
            raise ValueError("Réseau non supporté")
        self.wallet_id = wallet_id
        self.reseau = reseau

    def payer(self):
        return f"Transaction crypto de {self._montant:.2f} € réseau {self.reseau} (wallet {self.wallet_id})"

def traiter_paiements(liste):
    for p in liste:
        print(p.payer())

if __name__ == "__main__":
    paiements = [
        CarteBancaire(50, "4539 1488 0343 6467", "123"),
        CarteBancaire(20, "4716 2455 1067 2448", "999"),
        PayPal(30, "alice@example.com", "tok123"),
        PayPal(60, "bob@example.com", "tok456"),
        Crypto(100, "0xABC", "ETH"),
        Crypto(250, "0xXYZ", "BTC")
    ]
    traiter_paiements(paiements)
