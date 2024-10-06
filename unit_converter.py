def main_menu():
    while True:
        print("[CONVERSOR PROGRAM]")
        print(" - [1] Go to conversor measure unit menu")
        print(" - [2] Go to conversor temperature menu")
        print(" - [3] Go to conversor weight menu")
        print(" - [4] Exit")

        select_option = input("\n - Select a option: ")

##### CONDITIONS #####

        if select_option == '1':
            sub_menu1()
        elif select_option == '2':
            sub_menu2()
        elif select_option == '3':
            sub_menu3()
        elif select_option == '4':
            print("Exiting")
            break
        else:
            print("Error, invalid Option, try again!")

def sub_menu1():
    while True:
        print("\n[CONVERSOR MEASURE UNIT MENU]")
        print(" - [1] Transform Kilometer to Meter")
        print(" - [2] Transform Meter to Kilometer")
        print(" - [3] Return")

        option_menus = input("\n - Select a option: ")

        if option_menus == '1':
            km_m = float(input("\nEnter the value you want to convert from Kilometers to Meters: "))
            def conversion_km_m(valor):
                return float(valor * 1000)
            print(f"{km_m} Kilometers equal to {conversion_km_m(km_m)} Meters")

        elif option_menus == '2': # METROS PARA KM
            m_km = float(input("\nEnter the value you want to convert from Meters to Kilometers: "))
            def conversion_m_km(valor):
                return float(valor / 1000)
            print(f"{m_km} Meters equal to {conversion_m_km(m_km)} Kilometers")

        elif option_menus == '3': # Retorna ao menu principal
            return  
        else:
            print("Invalid option. Try again")

def sub_menu2():
    while True:
        print("\n[CONVERSOR TEMPERATURE MENU]")
        print(" - [1] Celsius to Fahrenheit")
        print(" - [2] Fahrenheit to Celsius")
        print(" - [3] Return")
        
        option_menus_t = input("\n - Select a option: ")

        if option_menus_t == '1': ## Celsius to fahrenhait
            cel_fah = float(input("\nEnter the degrees celsius to convert a fahrenhait: "))
            def conversion_c_f(valor): 
                return float(valor * 9/5) + 32
            print(f"{cel_fah} Celsius converted's to {conversion_c_f(cel_fah):.2f} Fahrenheit")

        elif option_menus_t == '2': ## Fahrenhait to celsius
            fah_cel = float(input("\nEnter the degrees fahrenhait to convert to celsius"))
            def conversion_f_c(valor): 
                return float(valor - 32) * 5/9
            print(f"{fah_cel} Fahrenheit converted's to {conversion_f_c(fah_cel):.2f} Celsius")
            
        elif option_menus_t == '3': ## Return
            return
        else: 
            print("Invalid option. Try again")

def sub_menu3():
    while True:
        print("\n[CONVERSOR WEIGHT MENU]")
        print(" - [1] Kilos to Libras")
        print(" - [2] Libras to Kilos")
        print(" - [3] Return")
        
        option_menus_w = input("\n - Select a option: ")

        if option_menus_w == '1':
            kg_lb = float(input("\nEnter Kilograma to convert to Libras: "))
            def conversion_k_l(valor):
                return float(valor * 2.205)
            print(f"{kg_lb} Kilos converted's to {conversion_k_l(kg_lb):.2f}")
        
        elif option_menus_w == '2':
            lb_kg = float(input("\nEnter Libra to convert to Kilograma: "))
            def conversion_l_k(valor):
                return float(valor / 2.205)
            print(f"{lb_kg} Libra converted's to {conversion_l_k(lb_kg):.2f}")

        elif option_menus_w == '3':
            return
        else:
            print("Invalid option. Try again")
main_menu() # close the main menu