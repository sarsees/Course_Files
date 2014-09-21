#Write a function that takes an array/Series of tree diameters 
#as an argument and returns an array/Series of tree masses.
def matter_to_mass(diameters):
    mass = []
    for trees in diameters:
        mass.append(0.124*trees**(2.53))
    return(mass)


    