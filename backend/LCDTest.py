from Classes.lcd import LCD
from subprocess import check_output

lcd = LCD()

try:
    while True:
        ips = check_output(['hostname', '--all-ip-addresses'])

        lcd.write_message("Loading IP...")
        lcd.send_instruction(lcd.second_row())

        ip = ips.decode('utf-8', errors='ignore').rstrip('\n')

        lcd.write_message(ip)
        lcd.send_instruction(lcd.first_row())

except KeyboardInterrupt as e:
    print(e)
finally:
    lcd.cleanup()
    print("Sadly this super awesome script has been interupted :(")
