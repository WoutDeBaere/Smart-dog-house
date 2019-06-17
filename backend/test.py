from mcp import Mcp3008

mcp = Mcp3008()
answer_druk = mcp.read_channel(0)

answer_druk = answer_druk/1.023

print(answer_druk)

# import RPi.GPIO as GPIO
#
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(14, GPIO.IN)
# pir_pin = 14
# # pin = 14
# count = 0
# while True:
#     read = GPIO.input(pin)
#     if read == 1:
#         print(1)


# while True:
#     read_input = GPIO.input(pir_pin)
#     if read_input:
#         print("jaaaa")
#     else:
#         print("neee")
