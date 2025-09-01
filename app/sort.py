BULKY_VOLUMEN = 1000000
BULKY_DIMENSION = 150
HEAVY = 20
def sort(width:int, height:int, length:int, mass:int)->str:
    """
    Description:
    Dispatch a package to the correct stack based on dimensions (cm) and mass (kg).

    Input :
        width(cm), height(cm), length  (cm) , mass (kg)
    Output:
        Dispatch label
    """
    is_bulky = False
    is_heavy = False
    package = ""

    if any(d <= 0 for d in (width, height, length)):
        raise ValueError("All dimensions must be > 0 centimeters.")
    if mass < 0:
        raise ValueError("Mass must be >= 0 kilograms.")

    volume = width*height*length

    if max(width, height, length) >= BULKY_DIMENSION or volume >= BULKY_VOLUMEN :
        is_bulky = True

    if mass >= HEAVY:
        is_heavy = True

    if is_bulky and is_heavy :
        return  "REJECTED"

    if is_bulky or is_heavy :
        return  "SPECIAL"

    return  "STANDARD"


if __name__ == "__main__" :

    # STANDARD
    print(sort(10, 10, 10, 19))

    # SPECIAL (heavy only)
    print(sort(10, 10, 10, 20))     # mass boundary
    print(sort(149, 1, 1, 20))       # just below dimension boundary
    print(sort(100, 100, 99, 20))    # just below volume boundary

    # SPECIAL (bulky only)
    print(sort(150, 1, 1, 19))      # dimension boundary
    print(sort(100, 100, 100, 19))   # volume boundary

    # REJECTED (both)
    print(sort(150, 1, 1, 20))
    print(sort(100, 100, 100, 20))