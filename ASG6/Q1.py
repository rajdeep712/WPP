class Password_manager:
    passwords = ["hello@123","iuah9hh*&33","LLigaOL#pP@123"]
    
    def get_password(self):
        return Password_manager.passwords[len(Password_manager.passwords)-1]

    
    def set_password(self,newpass):
        for password in Password_manager.passwords:
            if(password == newpass):
                print("Please enter a password different from your past passwords.")
                return
        Password_manager.passwords.append(newpass)
        return
    
    def is_correct(self,curr_pass):
        return Password_manager.passwords[len(Password_manager.passwords)-1] == curr_pass
    

Pm_1 = Password_manager()
print(Pm_1.get_password())
Pm_1.set_password("LYoyO11=@#*&001")
print(Pm_1.is_correct("LLigaOL#pP@123"))