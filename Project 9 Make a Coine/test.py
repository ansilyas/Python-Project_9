
# %%
import random
class Pound:
    def __init__(self):
        self.data={
        "original_value":1.00,
        "clean_colour":"gold",
        "rusty_colour":"greenish",
        "num_edges":1,
        "diameter":22.5,
        "thickness":3.15,
        "mass":9.5
        }
        
class Coin(Pound):
    def __init__(self,rare=False,clean=True,heads=True,**kwargs):
        super().__init__()
        for key,value in kwargs.items():
            setattr(self,key,value)
        self.is_rare=rare
        self.is_clean=clean
        self.heads=heads

        if self.is_rare:
            self.value=self.original_value*1.25
        else:
            self.value=self.original_value

        if self.is_clean:
            self.colour=self.clean_colour
        else:
            self.colour=self.rusty_colour

    def rust(self):
        self.colour=self.rusty_colour

    def clean(self):
        self.colour=self.clean_colour

    def __del__(self):
        print("Coin Spent!")

    def flip(self):
        heads_options=[True,False]
        choice=random.choice(heads_options)
        self.heads=choice


# %%
