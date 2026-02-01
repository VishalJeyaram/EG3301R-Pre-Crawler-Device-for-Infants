from guizero import App, Text, PushButton, Picture, Slider, Combo, Window
import time    #https://docs.python.org/fr/3/library/time.html
from adafruit_servokit import ServoKit    #https://circuitpython.readthedocs.io/projects/servokit/en/latest/
#import RPi.GPIO as GPIO
import socket 
from time import sleep, gmtime,strftime, localtime
import datetime

pca = ServoKit(channels=16)

left_arm = 0
right_arm = 6
left_thigh = 7
right_thigh = 10
left_leg = 9
right_leg = 15

#Constants
speed = "1"
stop = 2
crawling_style = "Classic Crawl"
nbPCAServo=16
current_angle = 0
port = 2788
phase = 0
bear_crawl_init = 0
start_time = 0

left_thigh_pw_min = 0
left_thigh_pw_max = 0
right_thigh_pw_min = 0
right_thigh_pw_max = 0
left_arm_pw_min = 0
left_arm_pw_max = 0
right_arm_pw_min = 0
right_arm_pw_max = 0
left_leg_pw_min = 0
right_leg_pw_max = 0

left_arm_angle = pca.servo[left_arm]
right_arm_angle = pca.servo[right_arm]
left_thigh_angle = pca.servo[left_thigh]
right_thigh_angle = pca.servo[right_thigh]
left_leg_angle = pca.servo[left_leg]
right_leg_angle = pca.servo[right_leg]


#Parameters
#min imp is 500 and max imp is 2500

#8 PARTITIONS
SPEED_1_MIN_1 = 500
SPEED_1_MAX_1 = 750
SPEED_1_MIN_2 = 750
SPEED_1_MAX_2 = 1000
SPEED_1_MIN_3 = 1000
SPEED_1_MAX_3 = 1250
SPEED_1_MIN_4 = 1250
SPEED_1_MAX_4 = 1500
SPEED_1_MIN_5 = 1500
SPEED_1_MAX_5 = 1750
SPEED_1_MIN_6 = 1750
SPEED_1_MAX_6 = 2000
SPEED_1_MIN_7 = 2000
SPEED_1_MAX_7 = 2250 
SPEED_1_MIN_8 = 2250
SPEED_1_MAX_8 = 2500

#4 PARTITIONS
SPEED_2_MIN_1 = 500
SPEED_2_MAX_1 = 1000
SPEED_2_MIN_2 = 1000
SPEED_2_MAX_2 = 1500
SPEED_2_MIN_3 = 1500
SPEED_2_MAX_3 = 2000
SPEED_2_MIN_4 = 2000
SPEED_2_MAX_4 = 2500

#3 PARTITIONS
SPEED_N_MIN_5 = 2665
SPEED_N_MAX_5 = 2998
SPEED_N_MIN_4 = 2332
SPEED_N_MAX_4 = 2665
SPEED_N_MIN_1 = 1000
SPEED_N_MAX_1 = 1333
SPEED_N_MIN_2 = 1333
SPEED_N_MAX_2 = 1666
SPEED_N_MIN_3 = 1666
SPEED_N_MAX_3 = 1999

# 2 PARTITIONS
SPEED_3_MIN_1 = 500
SPEED_3_MAX_1 = 1500
SPEED_3_MIN_2 = 1500
SPEED_3_MAX_2 = 2500

# 1 PARTITION
SPEED_4_MIN_1 = 500
SPEED_4_MAX_1 = 2500

MIN_ANG  =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
MAX_ANG  =[180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180]

#Objects

# function init 
#def init():
#    for i in range(nbPCAServo):
#        pca.servo[i].set_pulse_width_range(MIN_IMP_1[i], MAX_IMP_1[i])

# function main 
#def main():
#    classicBabyCrawlArmsSpeed1();
    #classicBabyCrawlLowerLegs()
    #test()

def checkForButtonPress():
    global stop
    global port
    global phase
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), port))
    msg = s.recv(8)
    full_msg = msg.decode("utf-8")
    if (full_msg == "yes"):
        stop = 1 

def selectAngles(left_thigh_angle, right_thigh_angle, left_arm_angle, right_arm_angle, left_leg_angle, right_leg_angle):
    global left_arm 
    global right_arm 
    global left_thigh 
    global right_thigh 
    global left_leg 
    global right_leg    
    global speed
    pca.servo[left_thigh].angle = left_thigh_angle
    pca.servo[right_thigh].angle = right_thigh_angle
    pca.servo[left_arm].angle = left_arm_angle
    pca.servo[right_arm].angle = right_arm_angle
    pca.servo[left_leg].angle = left_leg_angle
    pca.servo[right_leg].angle = right_leg_angle
    if (speed == "4"):
        time.sleep(0.0025)
    elif (speed == "3"):
        time.sleep(0.005)
    elif (speed == "2"):
        time.sleep(0.01)
    elif (speed == "1"):
        time.sleep(0.02) 

def selectCurrentAngle(j):
    global current_angle 
    current_angle = j 

def selectPulseWidths(left_thigh_pw_min, left_thigh_pw_max, right_thigh_pw_min, right_thigh_pw_max, left_arm_pw_min, left_arm_pw_max, right_arm_pw_min, right_arm_pw_max, left_leg_pw_min, left_leg_pw_max, right_leg_pw_min, right_leg_pw_max):
    global left_arm 
    global right_arm 
    global left_thigh 
    global right_thigh 
    global left_leg 
    global right_leg
    pca.servo[left_thigh].set_pulse_width_range(left_thigh_pw_min, left_thigh_pw_max)
    pca.servo[right_thigh].set_pulse_width_range(right_thigh_pw_min, right_thigh_pw_max)
    pca.servo[left_arm].set_pulse_width_range(left_arm_pw_min, left_arm_pw_max)
    pca.servo[right_arm].set_pulse_width_range(right_arm_pw_min, right_arm_pw_max)
    pca.servo[left_leg].set_pulse_width_range(left_leg_pw_min, left_leg_pw_max)
    pca.servo[right_leg].set_pulse_width_range(right_leg_pw_min, right_leg_pw_max)

def updateAngles(left_thigh_angle, right_thigh_angle, left_arm_angle, right_arm_angle, left_leg_angle, right_leg_angle):
    global start_time
    global stop
    left_arm_angle_display.value = f"Left Arm: {left_arm_angle}°"
    right_arm_angle_display.value = f"Right Arm: {right_arm_angle}°"
    left_thigh_angle_display.value = f"Left Thigh: {left_thigh_angle}°"
    right_thigh_angle_display.value = f"Right Thigh: {right_thigh_angle}°"
    left_leg_angle_display.value = f"Left Leg: {left_leg_angle}°"
    right_leg_angle_display.value = f"Right Leg: {right_leg_angle}°"
    end_time = time.time()
    timer =  (end_time - start_time) / 60
    if (timer >= 15):
        stop = 1
    time_left_display.value = f"Timer: {end_time}"
    angle_app.update()

def classicBabyCrawl():
    """Scenario to test servo"""
    angle_app.show()
    angle_app.update()
    global left_arm 
    global right_arm 
    global left_thigh 
    global right_thigh 
    global left_leg 
    global right_leg
    global start_time
    global stop 
    global phase

    global left_arm_angle

    print("start")

    selectPulseWidths(SPEED_3_MIN_2, SPEED_3_MAX_2, SPEED_3_MIN_1, SPEED_3_MAX_1, SPEED_3_MIN_1, SPEED_3_MAX_1, SPEED_3_MIN_1, SPEED_3_MAX_1, SPEED_3_MIN_1, SPEED_3_MAX_1, SPEED_3_MIN_1, SPEED_3_MAX_1)
    for j in range(90,180,1): # 45 - 0, 45 - 90, 90 - 135, 90 - 45, 90 - 135, 90 - 45 
        checkForButtonPress()
        if (stop == 1):
            return   
        selectAngles(j, j, -j + 270, -j + 270, -j + 270, -j + 270)
        updateAngles(45 - ((j-90)/2), 45 + ((j-90)/2), 90 + ((j- 90)/2), 90 - ((j-90)/2), 90 + ((j- 90)/2), 90 - ((j-90)/2))    
        phase = 1
        selectCurrentAngle(j)
    for j in range(180,0,-1): # 0 - 90, 90 - 0, 135 - 45, 45 - 135, 135 - 45, 45 - 135
        checkForButtonPress()
        if (stop == 1):
            return   
        if (j <= 90):
             selectPulseWidths(SPEED_3_MIN_2, SPEED_3_MAX_2, SPEED_3_MIN_1, SPEED_3_MAX_1, SPEED_3_MIN_2, SPEED_3_MAX_2, SPEED_3_MIN_2, SPEED_3_MAX_2, SPEED_3_MIN_2, SPEED_3_MAX_2, SPEED_3_MIN_2, SPEED_3_MAX_2) 
             selectAngles(j, j, 90-j, 90-j, 90-j, 90-j)
             phase = 2
             selectCurrentAngle(j)
        else:
             selectAngles(j, j, -j + 270, -j + 270, -j + 270, -j + 270)
             selectCurrentAngle(j)
        updateAngles(((180-j)/2), 90-((180-j)/2), 135-((180-j)/2), 45+((180-j)/2), 135-((180-j)/2), 45+((180-j)/2))    
    for j in range(0,90,1): # 90 - 45, 0 - 45, 45 - 90, 135 - 90, 45 - 90, 135 - 90
        checkForButtonPress()
        if (stop == 1):
            return   
        selectAngles(j, j, 90-j, 90-j, 90-j, 90-j)
        phase = 2
        selectCurrentAngle(j)
        updateAngles(90 - (j/2), (j/2), 45 + (j/2), 135-(j/2), 45 + (j/2), 135- (j/2))    
    phase = 0
    print("end")

def bearCrawlInitialization():
    angle_app.show()
    angle_app.update()
    """Scenario to test servo"""
    global left_leg 
    global right_leg
    global stop 
    global phase
    global bear_crawl_init
   
    print("start")

    selectPulseWidths(SPEED_3_MIN_2, SPEED_3_MAX_2, SPEED_3_MIN_1, SPEED_3_MAX_1, SPEED_3_MIN_1, SPEED_3_MAX_1, SPEED_3_MIN_1, SPEED_3_MAX_1, SPEED_3_MIN_2, SPEED_3_MAX_2, SPEED_3_MIN_1, SPEED_3_MAX_1)

    for j in range(90,180,1):
        checkForButtonPress()
        if (stop == 1):
            return   
        pca.servo[left_leg].angle = -j + 270
        pca.servo[right_leg].angle = j - 90
        angle = 90 - ((j-90)/2)
        left_leg_angle_display.value = f"Left Leg: {angle}°"
        right_leg_angle_display.value = f"Right Leg: {angle}°"
        angle_app.update()
        time.sleep(0.01)

    bear_crawl_init = 1

def bearBabyCrawl():
    """Scenario to test servo"""
    global left_arm 
    global right_arm 
    global left_thigh 
    global right_thigh 
    global left_leg 
    global right_leg

    global stop 
    global phase

    global left_arm_angle

    print("start")

    selectPulseWidths(SPEED_3_MIN_2, SPEED_3_MAX_2, SPEED_3_MIN_1, SPEED_3_MAX_1, SPEED_3_MIN_1, SPEED_3_MAX_1, SPEED_3_MIN_1, SPEED_3_MAX_1, SPEED_3_MIN_1, SPEED_3_MAX_1, SPEED_3_MIN_2, SPEED_3_MAX_2)
    for j in range(90,180,1): # 45 - 0, 0 - 45 
        checkForButtonPress()
        if (stop == 1):
            return       
        pca.servo[left_thigh].angle = j
        pca.servo[right_thigh].angle = j - 90
        angle_1 = 45 - ((j-90)/2) 
        angle_2 = (j-90)/2
        left_thigh_angle_display.value = f"Left Thigh: {angle_1}°"
        right_thigh_angle_display.value = f"Right Thigh: {angle_2}°"
        angle_app.update()
        time.sleep(0.01)
        phase = 1
        selectCurrentAngle(j)
    for j in range(180,90,-1): # 0 - 45, 45 - 0
        checkForButtonPress()
        if (stop == 1):
            return   
        pca.servo[left_thigh].angle = j
        pca.servo[right_thigh].angle = j - 90
        angle_1 = (j-90)/2 
        angle_2 = 45 - ((j-90)/2)
        left_thigh_angle_display.value = f"Left Thigh: {angle_1}°"
        right_thigh_angle_display.value = f"Right Thigh: {angle_2}°"
        angle_app.update()
        time.sleep(0.01)
        selectCurrentAngle(j)
    phase = 0
    print("end")

def neutralPosition():
    global speed
    global current_angle  
    global phase
    global crawling_style
    if (phase == 0):
        return
    if (crawling_style == "Classic Crawl"):
        if (phase == 1):
            for j in range(current_angle,90,-1):
                selectAngles(j, j, -j + 270, -j + 270, -j + 270, -j + 270)
        if (phase == 2):
            for j in range(current_angle,90,1):
                selectAngles(j, j, 90-j, 90-j, 90-j, 90-j)
    elif (crawling_style == "Bear Crawl"):
        if (phase == 1):
            for j in range(current_angle,90,-1):
                pca.servo[left_thigh].angle = j
                pca.servo[right_thigh].angle = j
                time.sleep(0.01)
        selectPulseWidths(SPEED_3_MIN_2, SPEED_3_MAX_2, SPEED_3_MIN_1, SPEED_3_MAX_1, SPEED_3_MIN_1, SPEED_3_MAX_1, SPEED_3_MIN_1, SPEED_3_MAX_1, SPEED_3_MIN_2, SPEED_3_MAX_2, SPEED_3_MIN_1, SPEED_3_MAX_1)
        for j in range(90,180,1):
            pca.servo[right_leg].angle = 180 
            time.sleep(0.015)
        for j in range(180, 0, -1):
            pca.servo[left_leg].angle = 0
            time.sleep(0.015)

def timeDisplay():
    clock.value = strftime('%B %d %A %H:%M', localtime())


app = App(title="Hello world", bg="#ffffff")
#app.full_screen = True
#filler = Text(app, text="", size=50, font="Times New Roman", color= "#000000")

welcome_message = Text(app, text="Pre-Crawler Device", size=50, font="Times New Roman", color= "#000000")
baby = Picture(app, image="baby.gif")

angle_app = Window(app, title="Angles", bg="#ffffff")
angle_app.hide()
#filler_1 = Text(app, text="", size=10, font="Times New Roman", color= "#000000")

def change_speed(slider_value):
    global speed
    speed = slider_value

def chooseCrawlingStyle(crawling_value):
    global crawling_style
    crawling_style = crawling_value

def start_classic_crawl_1():
    global stop 
    global bear_crawl_init
    global phase
    global start_time 
    stop = 0
    start_time = time.time()
    update_crawl.toggle()
    start_classic_crawl_2()
    neutralPosition()
    stop = 2
    phase = 0
    bear_crawl_init = 0
    update_crawl.toggle()
    angle_app.hide()
#   classicBabyCrawlSpeed2()


def start_classic_crawl_2():
    global stop
    global phase 
    global speed
    global crawling_style
    global bear_crawl_init
    while (stop == 0):
        #if (stop == 0):
        if (crawling_style == "Bear Crawl"):
            if (bear_crawl_init == 0):
                bearCrawlInitialization()
            bearBabyCrawl()
        elif (crawling_style == "Classic Crawl"):
            print("classic")
            classicBabyCrawl()
             

#def stop_classic_crawl():
#    global stop
#    update_crawl.toggle()
#    #stop_crawl.toggle()
#    stop = 1
#    print(stop)
#    #neutralPosition()

filler_1 = Text(app, text="", size=10, font="Times New Roman", color= "#000000")
change_speeds_text = Text(app, text="Change Speed!", size=20, font="Times New Roman", color= "#000000")
filler_2 = Text(app, text="", size=10, font="Times New Roman", color= "#000000")
change_speeds = Slider(app, command=change_speed, start=1, end=4, width = 100, height = 40 )
filler_3 = Text(app, text="", size=10, font="Times New Roman", color= "#000000")
crawling_styles_text = Text(app, text="Choose Crawling Style!", size=20, font="Times New Roman", color= "#000000")
filler_4 = Text(app, text="", size=10, font="Times New Roman", color= "#000000")
crawling_styles = Combo(app, options = ["Classic Crawl", "Bear Crawl", "Commando Crawl"], command= chooseCrawlingStyle)
filler_5 = Text(app, text="", size=10, font="Times New Roman", color= "#000000")
update_crawl = PushButton(app, command=start_classic_crawl_1, text="Start training routine")
filler_6 = Text(app, text="", size=10, font="Times New Roman", color= "#000000")
#stop_crawl = PushButton(app, command=stop_classic_crawl, text="Stop training")
#angles_display_1 = Text(app, text=f"", size=40, font="Times New Roman", color= "#ff0000")
#angles_display_1.repeat(200, start_classic_crawl_2)
left_arm_angle_display = Text(angle_app, text=f"Left Arm: 90°", size=40, font="Times New Roman", color= "#ff0000")
right_arm_angle_display = Text(angle_app, text=f"Right Arm: 90°", size=40, font="Times New Roman", color= "#ff0000")
left_thigh_angle_display = Text(angle_app, text=f"Left Thigh: 45°", size=40, font="Times New Roman", color= "#0000ff")
right_thigh_angle_display = Text(angle_app, text=f"Right Thigh: 45°", size=40, font="Times New Roman", color= "#0000ff")
left_leg_angle_display = Text(angle_app, text=f"Left Leg: 90°", size=40, font="Times New Roman", color= "#008000")
right_leg_angle_display = Text(angle_app, text=f"Right Leg: 90°", size=40, font="Times New Roman", color= "#008000")
filler_7 = Text(app, text="", size=10, font="Times New Roman", color= "#000000")
time_left_display = Text(angle_app, text=f"Time remaining: 15:00", size=40, font="Times New Roman", color= "#ffa500")
clock = Text(app, text='Hello')
clock.repeat(100, timeDisplay)

if __name__ == '__main__':
    app.display()
    #main()



