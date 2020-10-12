
while True:
    try:
        calc = input("Calcular:")
        print("\tResultado:" + str(float(eval(calc))))
    except Exception:
        print("\tErro de cálculo")
        
