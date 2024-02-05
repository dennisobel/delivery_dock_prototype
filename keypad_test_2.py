import time
import pins_declaration

pins_declaration.GPIO.setwarnings(False)
pins_declaration.GPIO.setmode(pins_declaration.GPIO.BCM)

# Set up buttons as inputs
for pin in pins_declaration.ROW_PINS:
    pins_declaration.GPIO.setup(pin, pins_declaration.GPIO.IN, pull_up_down=pins_declaration.GPIO.PUD_UP)  # set row pins as pulled up inputs
for pin in pins_declaration.COL_PINS:
    pins_declaration.GPIO.setup(pin, pins_declaration.GPIO.OUT)  # set column pins as outputs

if __name__=="__main__":
    # Function to read key input
    def read_key():
        for col_pin in pins_declaration.COL_PINS:
            # write all column pins high
            for all_pins in pins_declaration.COL_PINS:
                pins_declaration.GPIO.output(all_pins, pins_declaration.GPIO.HIGH)

            pins_declaration.GPIO.output(col_pin, pins_declaration.GPIO.LOW)

            for row_pin in pins_declaration.ROW_PINS:
                if not pins_declaration.GPIO.input(row_pin):
                    button_index = (col_pin, row_pin)

                    if col_pin == pins_declaration.COL_PINS[0]:
                        if row_pin == pins_declaration.ROW_PINS[0]:
                            return '1'
                        elif row_pin == pins_declaration.ROW_PINS[1]:
                            return '4'
                        elif row_pin == pins_declaration.ROW_PINS[2]:
                            return '7'
                        elif row_pin == pins_declaration.ROW_PINS[3]:
                            return '*'
                    elif col_pin == pins_declaration.COL_PINS[1]:
                        if row_pin == pins_declaration.ROW_PINS[0]:
                            return '2'
                        elif row_pin == pins_declaration.ROW_PINS[1]:
                            return '5'
                        elif row_pin == pins_declaration.ROW_PINS[2]:
                            return '8'
                        elif row_pin == pins_declaration.ROW_PINS[3]:
                            return '0'
                    elif col_pin == pins_declaration.COL_PINS[2]:
                        if row_pin == pins_declaration.ROW_PINS[0]:
                            return '3'
                        elif row_pin == pins_declaration.ROW_PINS[1]:
                            return '6'
                        elif row_pin == pins_declaration.ROW_PINS[2]:
                            return '9'
                        elif row_pin == pins_declaration.ROW_PINS[3]:
                            return '#'

        return None

    # Function to read keypad input
    def read_keypad():
        try:
            previous_time = time.time()
            debounce = 0.1
            input_buffer = []
            print("enter number ...")
            while True:
                key = read_key()
                if key is not None:
                    current_time = time.time()
                    time_elapsed = current_time - previous_time
                    previous_time = current_time
                    if time_elapsed > debounce:
                        print(f"{key}", end="")
                        if key == '#':
                            print(f"You have entered:{key}")
                            return ''.join(input_buffer)
                        input_buffer.append(key)

                time.sleep(0.2)

        except KeyboardInterrupt:
            pins_declaration.GPIO.cleanup()

    # MAIN
    try:
        while True:
            read_keypad()
    except KeyboardInterrupt:
        pins_declaration.GPIO.cleanup()
