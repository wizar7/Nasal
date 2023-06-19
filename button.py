import RPi.GPIO as GPIO

# set GPIO as BCM mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin for the button
button_pin = 24

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

a=0
print(a)
# Callback function when button pressed!
def button_callback(channel):
    print("Button pressed!")
    # add your code here
    a=1
    print(a)
    
    

# Add an event detection for the button pin 为按钮引脚添加事件检测
GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=button_callback, bouncetime=200)

try:
    while True:
        #print("hello world")
        # add your code here 在这里可以继续执行其他的程序逻辑
        if(a==1):
            print(a)
            break
        

except KeyboardInterrupt:
    # clear the setup of GPIO 清理GPIO设置
    GPIO.cleanup()
