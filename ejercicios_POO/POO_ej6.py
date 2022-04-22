class Familia():
    def __init__(self,dad,mum,sons):
        self.dad = dad
        self.mum = mum
        self.sons = sons

    def __str__(self):
        return f" Dad: {self.dad} \n Mum: {self.mum} \n Sons: {self.sons}"



familia  = Familia("Felipe", "Artemis", ["Hache","Sorrento","Oasis"] )
print(familia)