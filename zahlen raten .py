import random

while True:
    try:
        user: int = int( input( "bis welchem zahl willst du spielen :" ) )
        random_zahl = random.randint( 1, user )
        user_raten = int( input( f"1 bis {user} :>" ) )

        while random_zahl != user_raten:
            print( "Falsch" )
            user_raten = int( input( f"1 bis {user} :>" ) )

        while user_raten > user:
            print( "Der Zahl muss kleiner als angegebene Zahl" )
            user_raten = int( input( f"1 bis {user} :>" ) )

        if user_raten == random_zahl:
            print( "gewohnnen :" )
            salamon = input( "Nocheinmal spielen ss (y/n) ?" )
            while salamon != "y" and salamon != "n":
                salamon = input( "Nocheinmal spielen ss (y/n) ?" )

        if salamon != "y":
            break
            subprocess.run()
    except Exception:
        continue
if salamon == "n":
    print( "God bay" )


