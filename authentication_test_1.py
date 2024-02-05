import keypad_test_2

#hard coded admin password********to be replaced by a txt file read to allow password change @runtime
admin_password="5678"

if __name__=="__main__":
    def authenticate(correct_password):#password authentication function

        print("Enter password and press # to proceed _")
        value=keypad_test_2.read_keypad()
        if value==correct_password:
            print("correct password")
            return True
        else:
            print("wrong password!")
            return False
        
