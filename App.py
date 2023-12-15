# Dilraj Bola, Student # 991736047
class Application:
    
    def showMainMenu():
        exit = False
        while exit != True:
            userChoice = int(input("Please Pick A Option"))
            print(f"1 : View All\n2 : View By Type\n3 : Display Total Reveune\n4 : Add Product\n5 : Exit")

            if userChoice == 1:
                print("CSV File Will Be Printed")
            
            elif userChoice == 2:
                productType = input("Enter The Type Of Product You Want To Search For:\n")
                
                if productType.lower() == "computer":
                    print("Showing all Computers")
                    
                elif productType.lower() == "phone":
                    print("Show all Phones")
            
            elif userChoice == 3:
                print(f"Total Value of Computer:\nTotal Value of Phones\nTotal Value of All Products")
            
            elif userChoice == 4:
                print(f"New producted Added")
            
            elif userChoice == 5:
                exit = True
    
    def run():
       Application.showMainMenu()