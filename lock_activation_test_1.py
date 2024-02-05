import authentication_test_1
import pins_declaration
import keypad_test_2

pins_declaration.GPIO.setwarnings(False)
pins_declaration.GPIO.setmode(pins_declaration.GPIO.BCM)

#set solenoid locks as outputs
pins_declaration.GPIO.setup(pins_declaration.DOCS_LOCK, pins_declaration.GPIO.OUT) #dock1
pins_declaration.GPIO.setup(pins_declaration.COLD_LOCK, pins_declaration.GPIO.OUT) #dock2
pins_declaration.GPIO.setup(pins_declaration.HOT_LOCK, pins_declaration.GPIO.OUT) #dock3
pins_declaration.GPIO.setup(pins_declaration.REFILLABLES_LOCK, pins_declaration.GPIO.OUT) #dock4

if __name__=="__main__":
    def solenoid_unlock(dock_number,correct_password):
        authenticate=authentication_test_1.authenticate(correct_password)
        if authenticate:
            #open lock
            if dock_number==1:
                pins_declaration.GPIO.output(pins_declaration.DOCS_LOCK, pins_declaration.GPIO.HIGH)
            elif dock_number==2:
                pins_declaration.GPIO.output(pins_declaration.COLD_LOCK_LOCK, pins_declaration.GPIO.HIGH)
            elif dock_number==3:
                pins_declaration.GPIO.output(pins_declaration.HOT_LOCK, pins_declaration.GPIO.HIGH)
            elif dock_number==4:
                pins_declaration.GPIO.output(pins_declaration.REFILLABLES_LOCK_LOCK, pins_declaration.GPIO.HIGH)            
            else:
                print("The entered lock number doesn't exist")
            
            return True
        else:
            return False
        

    try:
        while True:
            print("Enter lock number and press #")
            lock_number=int(keypad_test_2.read_keypad())
            if solenoid_unlock(lock_number,authentication_test_1.admin_password):
                print(f"lock number {lock_number} unlocked successfully")
            else:
                print(f"Lock {lock_number} unlocking failed! recheck password or enter a valid lock number _")

    except KeyboardInterrupt:
        pins_declaration.GPIO.cleanup()