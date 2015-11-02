## AUTHOR: Kieran Owen Wand (14yrs)
## ASSISTANT: Christopher John Butcher (DAD, 35yrs), Tsena Maria Wand (MUM, 34yrs), Kristian Peter Butcher (BROTHER, 9yrs)


## CREATED JUNE 2015


# 1 #   CREDITS                                                     [165 - 168]
# 2 #   IMPORT MODULES                                              [171 - 180]
# 3 #   SETTING UP PROGRAM                                          [183 - 206]
        #    SETS ASTROPI MODULES AS FRIENDLY NAME                  [185 - 187]
        #    SETTING UP RASPBERRYPI FOR FLIGHT BUTTONS TO USE GPIO PINS         [189 - 192]
        #    ASSIGNING FRIENDLY NAMES FOR GPIO PINS                 [195 - 202]
        #    FORCING PROGRAM TO RUN PROGRAM WITHIN WHILE LOOP       [204 - 206]
# 4 #   CREATE TIMESTAMP                                            [209 - 214] {UPDATED - AUG 2015}
# 5 #   ASSIGNING LEVELS TO LEDS AND COLOURS                        [217 - 226]
        #    ADJUSTABLE LED LIGHT LEVELS                            [219 - 221]
        #    ASSIGNING LEVELS TO COLOURS                            [223 - 226]
# 6 #   DEFAULT VALUES                                              [229 - 248]
        #    ASSIGNING DEFAULTS TO TEMPERATURE + HUMIDITY OR PRESSURE PAGES     [231 - 234]
        #    ASSIGNING DEFAULT VALUES TO ALARM TRIGGERS             [237 - 241]
        #    ASSIGNING DEFAULTS TO WARNING PAGES (MUTE / SHOW)      [244 - 248]
# 7 #   CREATES A LOG FILE                                          [251 - 257]
# 8 #   TEMPERATURE LED MATRIX INCLUDING WARNINGS                   [260 - 718]
        #    TEMPERATURE NUMBERS MATRIX BELOW                       [262 - 646]
        #    NUMBER 0_top_left  - TEMPERATURE                       [267 - 283]
        #    NUMBER 1_top_left  - TEMPERATURE                       [286 - 302]
        #    NUMBER 2_top_left  - TEMPERATURE                       [305 - 321]
        #    NUMBER 3_top_left  - TEMPERATURE                       [324 - 340]
        #    NUMBER 4_top_left  - TEMPERATURE                       [343 - 359]
        #    NUMBER 5_top_left  - TEMPERATURE                       [362 - 378]
        #    NUMBER 6_top_left  - TEMPERATURE                       [381 - 397]
        #    NUMBER 7_top_left  - TEMPERATURE                       [400 - 416]
        #    NUMBER 8_top_left  - TEMPERATURE                       [419 - 435]
        #    NUMBER 9_top_left  - TEMPERATURE                       [438 - 454]
        #    NUMBER 0_top_right  - TEMPERATURE                      [459 - 475]
        #    NUMBER 1_top_right  - TEMPERATURE                      [478 - 494]
        #    NUMBER 2_top_right  - TEMPERATURE                      [497 - 513]
        #    NUMBER 3_top_right  - TEMPERATURE                      [516 - 532]
        #    NUMBER 4_top_right  - TEMPERATURE                      [535 - 551]
        #    NUMBER 5_top_right  - TEMPERATURE                      [554 - 570]
        #    NUMBER 6_top_right  - TEMPERATURE                      [573 - 589]
        #    NUMBER 7_top_right  - TEMPERATURE                      [592 - 608]
        #    NUMBER 8_top_right  - TEMPERATURE                      [611 - 627]
        #    NUMBER 9_top_right  - TEMPERATURE                      [630 - 646]
        #    TEMPERATURE ERROR STATES                               [648 - 718]
        #    ERROR STATE WARNING FOR - HIGH TEMPERATURE             [651 - 683]
        #    ERROR STATE WARNING FOR - LOW TEMPERATURE              [681 - 718]
# 9 #   HUMIDITY LED MATRIX INCLUDING WARNINGS                      [721 - 1179]
        #    HUMIDITY NUMBERS MATRIX BELOW                          [723 - 1107]
        #    NUMBER 0_bot_left  - HUMIDITY                          [727 - 744]
        #    NUMBER 1_bot_left  - HUMIDITY                          [746 - 763]
        #    NUMBER 2_bot_left  - HUMIDITY                          [765 - 782]
        #    NUMBER 3_bot_left  - HUMIDITY                          [784 - 801]
        #    NUMBER 4_bot_left  - HUMIDITY                          [803 - 820]
        #    NUMBER 5_bot_left  - HUMIDITY                          [822 - 839]
        #    NUMBER 6_bot_left  - HUMIDITY                          [841 - 858]
        #    NUMBER 7_bot_left  - HUMIDITY                          [860 - 877]
        #    NUMBER 8_bot_left  - HUMIDITY                          [879 - 896]
        #    NUMBER 9_bot_left  - HUMIDITY                          [898 - 915]
        #    NUMBER 0_bot_right  - HUMIDITY                         [919 - 936]
        #    NUMBER 1_bot_right  - HUMIDITY                         [938 - 955]
        #    NUMBER 2_bot_right  - HUMIDITY                         [957 - 974]
        #    NUMBER 3_bot_right  - HUMIDITY                         [976 - 993]
        #    NUMBER 4_bot_right  - HUMIDITY                         [995 - 1012]
        #    NUMBER 5_bot_right  - HUMIDITY                         [1014 - 1031]
        #    NUMBER 6_bot_right  - HUMIDITY                         [1033 - 1050]
        #    NUMBER 7_bot_right  - HUMIDITY                         [1052 - 1069]
        #    NUMBER 8_bot_right  - HUMIDITY                         [1071 - 1088]
        #    NUMBER 9_bot_right  - HUMIDITY                         [1090 - 1107]
        #    HUMIDITY ERROR STATES                                  [1109 - 1179]
        #    ERROR STATE WARNING FOR - HIGH HUMIDITY                [1112 - 1144]
        #    ERROR STATE WARNING FOR - LOW HUMIDITY                 [1146 - 1179]
# 10 #  PRESSURE LED MATRIX INCLUDING WARNINGS                      [1182 - 2088]
        #    PRESSURE NUMBERS MATRIX BELOW                          [1182 - 1952]
        #    NUMBER 0_top_left  - PRESSURE                          [1188 - 1205]
        #    NUMBER 1_top_left  - PRESSURE                          [1207 - 1224]
        #    NUMBER 2_top_left  - PRESSURE                          [1226 - 1243]
        #    NUMBER 3_top_left  - PRESSURE                          [1245 - 1262]
        #    NUMBER 4_top_left  - PRESSURE                          [1264 - 1281]
        #    NUMBER 5_top_left  - PRESSURE                          [1283 - 1300]
        #    NUMBER 6_top_left  - PRESSURE                          [1302 - 1319]
        #    NUMBER 7_top_left  - PRESSURE                          [1321 - 1338]
        #    NUMBER 8_top_left  - PRESSURE                          [1340 - 1357]
        #    NUMBER 9_top_left  - PRESSURE                          [1359 - 1376]
        #    NUMBER 0_top_right  - PRESSURE                         [1380 - 1397]
        #    NUMBER 1_top_right  - PRESSURE                         [1399 - 1416]
        #    NUMBER 2_top_right  - PRESSURE                         [1418 - 1435]
        #    NUMBER 3_top_right  - PRESSURE                         [1437 - 1454]
        #    NUMBER 4_top_right  - PRESSURE                         [1456 - 1473]
        #    NUMBER 5_top_right  - PRESSURE                         [1475 - 1492]
        #    NUMBER 6_top_ right  - PRESSURE                        [1494 - 1511]
        #    NUMBER 7_top_right  - PRESSURE                         [1513 - 1530]
        #    NUMBER 8_top_right  - PRESSURE                         [1532 - 1550]
        #    NUMBER 9_top_right  - PRESSURE                         [1551 - 1568]
        #    NUMBER 0_bot_left  - PRESSURE                          [1572 - 1589]
        #    NUMBER 1_bot_left  - PRESSURE                          [1591 - 1608]
        #    NUMBER 2_bot_left  - PRESSURE                          [1610 - 1627]
        #    NUMBER 3_bot_left  - PRESSURE                          [1629 - 1646]
        #    NUMBER 4_bot_left  - PRESSURE                          [1648 - 1665]
        #    NUMBER 5_bot_left  - PRESSURE                          [1667 - 1684]
        #    NUMBER 6_bot_left  - PRESSURE                          [1686 - 1703]
        #    NUMBER 7_bot_left  - PRESSURE                          [1705 - 1722]
        #    NUMBER 8_bot_left  - PRESSURE                          [1724 - 1741]
        #    NUMBER 9_bot_left  - PRESSURE                          [1743 - 1760]
        #    NUMBER 0_bot_right  - PRESSURE                         [1764 - 1781]
        #    NUMBER 1_bot_right  - PRESSURE                         [1783 - 1800]
        #    NUMBER 2_bot_right  - PRESSURE                         [1802 - 1819]
        #    NUMBER 3_bot_right  - PRESSURE                         [1821 - 1838]
        #    NUMBER 4_bot_right  - PRESSURE                         [1840 - 1857]
        #    NUMBER 5_bot_right  - PRESSURE                         [1859 - 1876]
        #    NUMBER 6_bot_right  - PRESSURE                         [1878 - 1895]
        #    NUMBER 7_bot_right  - PRESSURE                         [1897 - 1914]
        #    NUMBER 8_bot_right  - PRESSURE                         [1916 - 1933]
        #    NUMBER 9_bot_right  - PRESSURE                         [1935 - 1952]
        #    PRESSURE ERROR STATES                                  [1954 - 2088]
        #    ERROR STATE WARNING FOR - HIGH PRESSURE                [1956 - 2021]
        #    ERROR STATE WARNING FOR - LOW PRESSURE                 [2023 - 2088]
# 11 #  SETTING UP FLIGHT BUTTONS FOR USE AND ASSIGNING COMMANDS    [2091 - 2158]
        #    LOOKING FOR BUTTON PRESSES FROM FLIGHT BUTTONS         [2093 - 2158]
        #    UP BUTTON (BRIGHTNESS INCREASES)                       [2105 - 2107]
        #    DOWN BUTTON (BRIGHTNESS DECREASES)                     [2109 - 2111]
        #    LEFT BUTTON (TEMPERATURE & HUMIDITY PAGE ON)           [2113 - 2127]
        #    RIGHT BUTTON (PRESSURE PAGE ON)                        [2129 - 2140]
        #    A BUTTON (MUTES ALARMS)                                [2142 - 2147]
        #    B BUTTON (UN-MUTES ALARMS)                             [2149 - 2154]
# 12 #  RESETTING PREVIOUS READINGS TO START CLEAN                  [2161 - 2178]
        #    SET PREVIOUS TEMPERATURE, HUMIDITY & PRESSURE VALUES TO ZERO           [2163 - 2178]
# 13 #  NEW ASTROPI CLASS FILE TO ENSURE ORIENTATION READING IS CORRECT             [2181 - 2240] {NOT COMPATIBLE WITH RASPBERRYPI B+ - AUG 2015}
# 14 #  NEW CLASS FILE TO ALLOW CPU_TEMPERATURE TO BE RECALLEDAS NEEDED             [2243 - 2277]
# 15 #  CAMERA SYSTEM FOR SNAPSHOTS                                 [2280 - 2295]   {UPDATED - NEW ADD-ON TO PROGRAM - AUG 2015}
# 16 #  MAIN PROGRAM LOOP                                           [2298 - 2665]
        #    SETUP INITIAL MODULES FOR PROGRAM LOOP                 [2302 - 2310]
        #    ALLOWS THE LOG SECTION TO RECALL INFORMATION FROM SECTIONS             [2313 - 2325]
        #    SET VALUES FOR LOGGING INFO                            [2330 - 2332] {UPDATED - AUG 2015}
        #    ENSURES THAT SNAPSHOT AND LOG INPUT HAVE THE SAME TIME [2335 - 2337] {UPDATED - AUG 2015}
        #    REMOVE DAY LABEL FROM ASCTIME TO ALLOW WINDOWS TO SORT IMAGES AND LOG CORRECTLY        [2340 - 2341]
        #    TAKE SNAPSHOT IF THE ASTROPI IS IN AN ERROR STATE - TEMPERATURE / HUMIDITY / PRESSURE  [2344 - 2372]   {UPDATED - NEW ADD-ON TO PROGRAM - AUG 2015}
        #    LOG ALL INFORMATION REQUIRED FOR ASTROPI               [2375 - 2383]
        #    COUNTER TO RE-ENABLE ALARMS FOR THE TEMPERATURE, HUMIDITY, PRESSURE READINGS           [2336 - 2390]
        #    RE-ENABLE ALARMS FOR THE TEMPERATURE, HUMIDITY AND PRESSURE READINGS   [2393 - 2399]
        #    CALCULATIONS FOR TEMPERATURE TO COMPENSATE FOR CPU_TEMP AFFECTING TEMPERATURE READINGS [2402 - 2411]
        #    GET TEMPERATURE, HUMIDITY, PRESSURE READINGS FROM ASTROPI SENSORS      [2414 - 2424]
        #    LOG IF THE DISPLAY HAS BEEN MUTED (BLACK BOX STYLE)    [2427 - 2437]
        #    LOG IF THE TEMPERATURE ALARM READING AND IF IT HAS BEEN MUTED (BLACK BOX STYLE)        [2440 - 2452]
        #    TAKE A SNAPSHOT (IMAGE) IF THE TEMPERATURE IS IN ALARM STATE (BLACK BOX STYLE)         [2455 - 2462]   {UPDATED - NEW ADD-ON TO PROGRAM - AUG 2015}
        #    LOG IF THE HUMIDITY ALARM READING AND IF IT HAS BEEN MUTED (BLACK BOX STYLE)           [2465 - 2477]
        #    TAKE A SNAPSHOT (IMAGE) IF THE HUMIDITY IS IN ALARM STATE (BLACK BOX STYLE)            [2480 - 2487]   {UPDATED - NEW ADD-ON TO PROGRAM - AUG 2015}
        #    LOG IF THE PRESSURE ALARM READING AND IF IT HAS BEEN MUTED (BLACK BOX STYLE)           [2450 - 2502]
        #    TAKE A SNAPSHOT (IMAGE) IF THE PRESSURE IS IN ALARM STATE (BLACK BOX STYLE)            [2505 - 2512]   {UPDATED - NEW ADD-ON TO PROGRAM - AUG 2015}
        #    CONVERTS TEMPERATURE, HUMIDITY, PRESSURE READINGS TO A STRING          [2515 - 2525]
        #    ROTATE THE LED MATRIX DISPLAY (IF REQUIRED)            [2528 - 2530]
        #    WRITES VALUES ONTO THE LED MATRIX FOR THE TEMPERATUREAND THE HUMIDITYIDITY             [3533 - 2544]
        #    TEMPERATURE- ERROR STATE CHECKING                      [2547 - 2577]
        #    HUMIDITY - ERROR STATE CHECKING                        [2580 - 2605]
        #    ALLOW ASTRONAUT (TIM) TO READ THE PREVIOUS TEMP & HUMIDITY READINGS ON THE LED MATRIX  [2608 - 2613]
        #    WRITE BOTH TOP_LINE & BOT_LINE - PRESSURE (4 DIGITS)   [2616 - 2623]
        #    PRESSURE - ERROR STATE CHECKING                        [2624 - 2653]
        #    ALLOW ASTRONAUT (TIM) TO READ THE PREVIOUS PRESSURE READINGS ON LED MATRIX             [2658 - 2663]
        #    RESETS THE LOGGING COUNTER & START THE LOOP AGAIN      [2666 - 2666]
# 17 #    PROGRAMMING TO CLEANLY EXIT THE PYTHON PROGRAM AND STOP RECORDING READINGS (IF REQUIRED)  [2669 - 2683]
        #    CLEARS THE LED MATRIX ON ASTROPI                       [2673 - 2685]


# 1 #    CREDITS 
        #   - ASTROPI FORUM MEMBERS, HELP AND SUPPORT FOR SCRIPTS AND FAULT FINDING
        #   - RASPBERRY PI FORUM MEMBERS, HELP AND SUPPORT FOR SCRIPTS AND FAULT FINDING
        #   - Tsena Wand (MUM), ASSESSING THE EASE OF USE FOR THE READING DISPLAYS AND WARNING STATES


# 2 #    IMPORT MODULES REQUIRED FOR PROGRAM

import RPi.GPIO as GPIO
import time, logging
from time import sleep, asctime
import datetime
import sys, os
import astro_pi
from astro_pi import AstroPi
import picamera


# 3 #    SETTING UP PROGRAM

        # SETS ASTROPI MODULES AS FRIENDLY NAME 

ap = astro_pi.AstroPi()

        # SETTING UP RASPBERRYPI FOR FLIGHT BUTTONS TO USE GPIO PINS 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


        # ASSIGNING FRIENDLY NAMES FOR GPIO PINS 

UP = 26
DOWN = 13
LEFT = 20
RIGHT = 19
A = 16
B = 21

        # FORCING PROGRAM TO RUN WITHIN WHILE LOOP 

running = True


# 4 #    CREATE TIMESTAMP AS FRIENDLY NAME

#tmstmp = time.strftime("%Y%m%d-%H%M%S") # REMOVED TO ALLOW ALL TIMESTAMPS TO MATCH ACROSS PROGRAM
tmstmp = datetime.datetime.now().strftime("%d %b %y %H:%M:%S")  # USING DATETIME INPLACE OF ASCTIME TO RESOLVE EXCEL FORMATTING ISSUES

# tmstmp_len = tmstmp[4:]   # REMOVED AS NO LONGER REQUIRED DUE TO COREECT DATE/TIME FORMATTING ABOVE   
    
 
# 5 #    ASSIGNING LEVELS TO LED'S AND COLOURS

        # ADJUSTABLE LED LIGHT LEVELS

led_level = 150     # ASSIGNING DEFAULT PROGRAM START LED MATRIX LIGHT LEVELS

        # ASSIGNING LEVELS TO COLOURS

red = 255                           # HIGH ERROR STATE LED LIGHT LEVEL
blue = 255                          # LOW ERROR STATE LED LIGHT LEVEL


# 6 #    DEFAULT VALUES

        # ASSIGNING DEFAULTS TO TEMP + HUM OR PRESSURE PAGES 

temp_hum_on = 0
psi_on = 0


        # ASSIGNING DEFAULTS VALUES TO ALARM TRIGGERS 

tmp_alarm = 0
hum_alarm = 0
psi_alarm = 0


        # ASSIGNING DEFAULTS TO WARNING PAGES (MUTE / SHOW) 

tmp_mute = 0
hum_mute = 0
psi_mute = 0


# 7 #    CREATES A LOG FILE WITH THE TITLE "log/{timestamp:%Y-%m-%d-%H-%M}watchdog.csv" 
        # THIS ALSO ADDS A TIMESTAMP TO THE START OF THE FILE NAME CREATED 

count = 0
file = open('log/'+(str(tmstmp))+' watchdog-log.csv', 'w')
file.write("\"Time\",\"Display\",\"Temperature\",\"Temp_Reading\",\"Temp_Alarm\",\"Temp_Snapshot\",\"Humidity\",\"Hum_Reading\",\"Hum_Alarm\",\"Hum_Snapshot\",\"Pressure\",\"PSI_Reading\",\"PSI_Alarm\",\"PSI_Snapshot\",\"Pitch\",\"Roll\",\"Yaw\"\n")
    

# 8 #    TEMP LED MATRIX INCLUDING WARNINGS

        # TEMPERATURE NUMBERS MATRIX BELOW 

def temp_num_matrix_1(num):

  if num == '0':
        # number 0_top_left - TEMPERATURE
    ap.set_pixel(0, 0, led_level, 0, 0)   
    ap.set_pixel(0, 1, led_level, 0, 0)   
    ap.set_pixel(0, 2, led_level, 0, 0)   
    ap.set_pixel(0, 3, led_level, 0, 0)
    ap.set_pixel(1, 0, led_level, 0, 0)   
    ap.set_pixel(1, 1, 0, 0, 0)   
    ap.set_pixel(1, 2, 0, 0, 0)   
    ap.set_pixel(1, 3, led_level, 0, 0)
    ap.set_pixel(2, 0, led_level, 0, 0)   
    ap.set_pixel(2, 1, led_level, 0, 0)   
    ap.set_pixel(2, 2, led_level, 0, 0)   
    ap.set_pixel(2, 3, led_level, 0, 0)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '1':
        # number 1_top_left - TEMPERATURE
    ap.set_pixel(0, 0, 0, 0, 0)   
    ap.set_pixel(0, 1, led_level, 0, 0)   
    ap.set_pixel(0, 2, 0, 0, 0)   
    ap.set_pixel(0, 3, led_level, 0, 0)
    ap.set_pixel(1, 0, led_level, 0, 0)   
    ap.set_pixel(1, 1, led_level, 0, 0)   
    ap.set_pixel(1, 2, led_level, 0, 0)   
    ap.set_pixel(1, 3, led_level, 0, 0)
    ap.set_pixel(2, 0, 0, 0, 0)   
    ap.set_pixel(2, 1, 0, 0, 0)   
    ap.set_pixel(2, 2, 0, 0, 0)   
    ap.set_pixel(2, 3, led_level, 0, 0)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '2':
        # number 2_top_left - TEMPERATURE
    ap.set_pixel(0, 0, led_level, 0, 0)   
    ap.set_pixel(0, 1, 0, 0, 0)   
    ap.set_pixel(0, 2, 0, 0, 0)   
    ap.set_pixel(0, 3, led_level, 0, 0)
    ap.set_pixel(1, 0, led_level, 0, 0)   
    ap.set_pixel(1, 1, 0, 0, 0)   
    ap.set_pixel(1, 2, led_level, 0, 0)   
    ap.set_pixel(1, 3, led_level, 0, 0)
    ap.set_pixel(2, 0, led_level, 0, 0)   
    ap.set_pixel(2, 1, led_level, 0, 0)   
    ap.set_pixel(2, 2, 0, 0, 0)   
    ap.set_pixel(2, 3, led_level, 0, 0)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '3':
        # number 3_top_left - TEMPERATURE
    ap.set_pixel(0, 0, led_level, 0, 0)   
    ap.set_pixel(0, 1, 0, 0, 0)   
    ap.set_pixel(0, 2, 0, 0, 0)   
    ap.set_pixel(0, 3, led_level, 0, 0)
    ap.set_pixel(1, 0, led_level, 0, 0)   
    ap.set_pixel(1, 1, led_level, 0, 0)   
    ap.set_pixel(1, 2, 0, 0, 0)   
    ap.set_pixel(1, 3, led_level, 0, 0)
    ap.set_pixel(2, 0, led_level, 0, 0)   
    ap.set_pixel(2, 1, led_level, 0, 0)   
    ap.set_pixel(2, 2, led_level, 0, 0)   
    ap.set_pixel(2, 3, led_level, 0, 0)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '4':
        # number 4_top_left - TEMPERATURE
    ap.set_pixel(0, 0, led_level, 0, 0)   
    ap.set_pixel(0, 1, led_level, 0, 0)   
    ap.set_pixel(0, 2, led_level, 0, 0)   
    ap.set_pixel(0, 3, 0, 0, 0)
    ap.set_pixel(1, 0, 0, 0, 0)   
    ap.set_pixel(1, 1, 0, 0, 0)   
    ap.set_pixel(1, 2, led_level, 0, 0)   
    ap.set_pixel(1, 3, 0, 0, 0)
    ap.set_pixel(2, 0, 0, 0, 0)   
    ap.set_pixel(2, 1, led_level, 0, 0)   
    ap.set_pixel(2, 2, led_level, 0, 0)   
    ap.set_pixel(2, 3, led_level, 0, 0)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '5':
        # number 5_top_left - TEMPERATURE
    ap.set_pixel(0, 0, led_level, 0, 0)   
    ap.set_pixel(0, 1, led_level, 0, 0)   
    ap.set_pixel(0, 2, 0, 0, 0)   
    ap.set_pixel(0, 3, led_level, 0, 0)
    ap.set_pixel(1, 0, led_level, 0, 0)   
    ap.set_pixel(1, 1, 0, 0, 0)   
    ap.set_pixel(1, 2, led_level, 0, 0)   
    ap.set_pixel(1, 3, led_level, 0, 0)
    ap.set_pixel(2, 0, led_level, 0, 0)   
    ap.set_pixel(2, 1, 0, 0, 0)   
    ap.set_pixel(2, 2, 0, 0, 0)   
    ap.set_pixel(2, 3, led_level, 0, 0)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '6':
        # number 6_top_left - TEMPERATURE
    ap.set_pixel(0, 0, led_level, 0, 0)   
    ap.set_pixel(0, 1, led_level, 0, 0)   
    ap.set_pixel(0, 2, led_level, 0, 0)   
    ap.set_pixel(0, 3, led_level, 0, 0)
    ap.set_pixel(1, 0, 0, 0, 0)   
    ap.set_pixel(1, 1, led_level, 0, 0)   
    ap.set_pixel(1, 2, 0, 0, 0)   
    ap.set_pixel(1, 3, led_level, 0, 0)
    ap.set_pixel(2, 0, 0, 0, 0)   
    ap.set_pixel(2, 1, led_level, 0, 0)   
    ap.set_pixel(2, 2, led_level, 0, 0)   
    ap.set_pixel(2, 3, led_level, 0, 0)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '7':
        # number 7_top_left - TEMPERATURE
    ap.set_pixel(0, 0, led_level, 0, 0)   
    ap.set_pixel(0, 1, led_level, 0, 0)   
    ap.set_pixel(0, 2, 0, 0, 0)   
    ap.set_pixel(0, 3, 0, 0, 0)
    ap.set_pixel(1, 0, led_level, 0, 0)   
    ap.set_pixel(1, 1, 0, 0, 0)   
    ap.set_pixel(1, 2, 0, 0, 0)   
    ap.set_pixel(1, 3, 0, 0, 0)
    ap.set_pixel(2, 0, led_level, 0, 0)   
    ap.set_pixel(2, 1, led_level, 0, 0)   
    ap.set_pixel(2, 2, led_level, 0, 0)   
    ap.set_pixel(2, 3, led_level, 0, 0)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)
  
  if num == '8':
        # number 8_top_left - TEMPERATURE
    ap.set_pixel(0, 0, led_level, 0, 0)   
    ap.set_pixel(0, 1, led_level, 0, 0)   
    ap.set_pixel(0, 2, led_level, 0, 0)   
    ap.set_pixel(0, 3, led_level, 0, 0)
    ap.set_pixel(1, 0, led_level, 0, 0)   
    ap.set_pixel(1, 1, 0, 0, 0)   
    ap.set_pixel(1, 2, led_level, 0, 0)   
    ap.set_pixel(1, 3, led_level, 0, 0)
    ap.set_pixel(2, 0, led_level, 0, 0)   
    ap.set_pixel(2, 1, led_level, 0, 0)   
    ap.set_pixel(2, 2, led_level, 0, 0)   
    ap.set_pixel(2, 3, led_level, 0, 0)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '9':
        # number 9_top_left - TEMPERATURE
    ap.set_pixel(0, 0, led_level, 0, 0)   
    ap.set_pixel(0, 1, led_level, 0, 0)   
    ap.set_pixel(0, 2, led_level, 0, 0)   
    ap.set_pixel(0, 3, 0, 0, 0)
    ap.set_pixel(1, 0, led_level, 0, 0)   
    ap.set_pixel(1, 1, 0, 0, 0)   
    ap.set_pixel(1, 2, led_level, 0, 0)   
    ap.set_pixel(1, 3, 0, 0, 0)
    ap.set_pixel(2, 0, led_level, 0, 0)   
    ap.set_pixel(2, 1, led_level, 0, 0)   
    ap.set_pixel(2, 2, led_level, 0, 0)   
    ap.set_pixel(2, 3, led_level, 0, 0)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

def temp_num_matrix_2(num):
    
  if num == '0':
        # number 0_top_right - TEMPERATURE
    ap.set_pixel(4, 0, led_level, 0, 0)   
    ap.set_pixel(4, 1, led_level, 0, 0)   
    ap.set_pixel(4, 2, led_level, 0, 0)   
    ap.set_pixel(4, 3, led_level, 0, 0)
    ap.set_pixel(5, 0, led_level, 0, 0)   
    ap.set_pixel(5, 1, 0, 0, 0)   
    ap.set_pixel(5, 2, 0, 0, 0)   
    ap.set_pixel(5, 3, led_level, 0, 0)
    ap.set_pixel(6, 0, led_level, 0, 0)   
    ap.set_pixel(6, 1, led_level, 0, 0)   
    ap.set_pixel(6, 2, led_level, 0, 0)   
    ap.set_pixel(6, 3, led_level, 0, 0)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '1':
        # number 1_top_right - TEMPERATURE
    ap.set_pixel(4, 0, 0, 0, 0)   
    ap.set_pixel(4, 1, led_level, 0, 0)   
    ap.set_pixel(4, 2, 0, 0, 0)   
    ap.set_pixel(4, 3, led_level, 0, 0)
    ap.set_pixel(5, 0, led_level, 0, 0)   
    ap.set_pixel(5, 1, led_level, 0, 0)   
    ap.set_pixel(5, 2, led_level, 0, 0)   
    ap.set_pixel(5, 3, led_level, 0, 0)
    ap.set_pixel(6, 0, 0, 0, 0)   
    ap.set_pixel(6, 1, 0, 0, 0)   
    ap.set_pixel(6, 2, 0, 0, 0)   
    ap.set_pixel(6, 3, led_level, 0, 0)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '2':
        # number 2_top_right - TEMPERATURE
    ap.set_pixel(4, 0, led_level, 0, 0)   
    ap.set_pixel(4, 1, 0, 0, 0)   
    ap.set_pixel(4, 2, 0, 0, 0)   
    ap.set_pixel(4, 3, led_level, 0, 0)
    ap.set_pixel(5, 0, led_level, 0, 0)   
    ap.set_pixel(5, 1, 0, 0, 0)   
    ap.set_pixel(5, 2, led_level, 0, 0)   
    ap.set_pixel(5, 3, led_level, 0, 0)
    ap.set_pixel(6, 0, led_level, 0, 0)   
    ap.set_pixel(6, 1, led_level, 0, 0)   
    ap.set_pixel(6, 2, 0, 0, 0)   
    ap.set_pixel(6, 3, led_level, 0, 0)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '3':
        # number 3_top_right - TEMPERATURE
    ap.set_pixel(4, 0, led_level, 0, 0)   
    ap.set_pixel(4, 1, 0, 0, 0)   
    ap.set_pixel(4, 2, 0, 0, 0)   
    ap.set_pixel(4, 3, led_level, 0, 0)
    ap.set_pixel(5, 0, led_level, 0, 0)   
    ap.set_pixel(5, 1, led_level, 0, 0)   
    ap.set_pixel(5, 2, 0, 0, 0)   
    ap.set_pixel(5, 3, led_level, 0, 0)
    ap.set_pixel(6, 0, led_level, 0, 0)   
    ap.set_pixel(6, 1, led_level, 0, 0)   
    ap.set_pixel(6, 2, led_level, 0, 0)   
    ap.set_pixel(6, 3, led_level, 0, 0)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '4':
        # number 4_top_right - TEMPERATURE
    ap.set_pixel(4, 0, led_level, 0, 0)   
    ap.set_pixel(4, 1, led_level, 0, 0)   
    ap.set_pixel(4, 2, led_level, 0, 0)   
    ap.set_pixel(4, 3, 0, 0, 0)
    ap.set_pixel(5, 0, 0, 0, 0)   
    ap.set_pixel(5, 1, 0, 0, 0)   
    ap.set_pixel(5, 2, led_level, 0, 0)   
    ap.set_pixel(5, 3, 0, 0, 0)
    ap.set_pixel(6, 0, 0, 0, 0)   
    ap.set_pixel(6, 1, led_level, 0, 0)   
    ap.set_pixel(6, 2, led_level, 0, 0)   
    ap.set_pixel(6, 3, led_level, 0, 0)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '5':
        # number 5_top_right - TEMPERATURE
    ap.set_pixel(4, 0, led_level, 0, 0)   
    ap.set_pixel(4, 1, led_level, 0, 0)   
    ap.set_pixel(4, 2, 0, 0, 0)   
    ap.set_pixel(4, 3, led_level, 0, 0)
    ap.set_pixel(5, 0, led_level, 0, 0)   
    ap.set_pixel(5, 1, 0, 0, 0)   
    ap.set_pixel(5, 2, led_level, 0, 0)   
    ap.set_pixel(5, 3, led_level, 0, 0)
    ap.set_pixel(6, 0, led_level, 0, 0)   
    ap.set_pixel(6, 1, 0, 0, 0)   
    ap.set_pixel(6, 2, 0, 0, 0)   
    ap.set_pixel(6, 3, led_level, 0, 0)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '6':
        # number 6_top_right - TEMPERATURE
    ap.set_pixel(4, 0, led_level, 0, 0)   
    ap.set_pixel(4, 1, led_level, 0, 0)   
    ap.set_pixel(4, 2, led_level, 0, 0)   
    ap.set_pixel(4, 3, led_level, 0, 0)
    ap.set_pixel(5, 0, 0, 0, 0)   
    ap.set_pixel(5, 1, led_level, 0, 0)   
    ap.set_pixel(5, 2, 0, 0, 0)   
    ap.set_pixel(5, 3, led_level, 0, 0)
    ap.set_pixel(6, 0, 0, 0, 0)   
    ap.set_pixel(6, 1, led_level, 0, 0)   
    ap.set_pixel(6, 2, led_level, 0, 0)   
    ap.set_pixel(6, 3, led_level, 0, 0)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '7':
        # number 7_top_right - TEMPERATURE
    ap.set_pixel(4, 0, led_level, 0, 0)   
    ap.set_pixel(4, 1, led_level, 0, 0)   
    ap.set_pixel(4, 2, 0, 0, 0)   
    ap.set_pixel(4, 3, 0, 0, 0)
    ap.set_pixel(5, 0, led_level, 0, 0)   
    ap.set_pixel(5, 1, 0, 0, 0)   
    ap.set_pixel(5, 2, 0, 0, 0)   
    ap.set_pixel(5, 3, 0, 0, 0)
    ap.set_pixel(6, 0, led_level, 0, 0)   
    ap.set_pixel(6, 1, led_level, 0, 0)   
    ap.set_pixel(6, 2, led_level, 0, 0)   
    ap.set_pixel(6, 3, led_level, 0, 0)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '8':
        # number 8_top_right - TEMPERATURE
    ap.set_pixel(4, 0, led_level, 0, 0)   
    ap.set_pixel(4, 1, led_level, 0, 0)   
    ap.set_pixel(4, 2, led_level, 0, 0)   
    ap.set_pixel(4, 3, led_level, 0, 0)
    ap.set_pixel(5, 0, led_level, 0, 0)   
    ap.set_pixel(5, 1, 0, 0, 0)   
    ap.set_pixel(5, 2, led_level, 0, 0)   
    ap.set_pixel(5, 3, led_level, 0, 0)
    ap.set_pixel(6, 0, led_level, 0, 0)   
    ap.set_pixel(6, 1, led_level, 0, 0)   
    ap.set_pixel(6, 2, led_level, 0, 0)   
    ap.set_pixel(6, 3, led_level, 0, 0)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '9':
        # number 9_top_right - TEMPERATURE
    ap.set_pixel(4, 0, led_level, 0, 0)   
    ap.set_pixel(4, 1, led_level, 0, 0)   
    ap.set_pixel(4, 2, led_level, 0, 0)   
    ap.set_pixel(4, 3, 0, 0, 0)
    ap.set_pixel(5, 0, led_level, 0, 0)   
    ap.set_pixel(5, 1, 0, 0, 0)   
    ap.set_pixel(5, 2, led_level, 0, 0)
    ap.set_pixel(5, 3, 0, 0, 0)
    ap.set_pixel(6, 0, led_level, 0, 0)   
    ap.set_pixel(6, 1, led_level, 0, 0)   
    ap.set_pixel(6, 2, led_level, 0, 0)   
    ap.set_pixel(6, 3, led_level, 0, 0)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

        # TEMPERATURE ERROR STATES BELOW 

def temp_num_error_high():
        # error state warning for - HIGH TEMPERATURE
    ap.set_pixel(0, 0, red, 0, 0)   
    ap.set_pixel(0, 1, red, 0, 0)   
    ap.set_pixel(0, 2, red, 0, 0)   
    ap.set_pixel(0, 3, red, 0, 0)
    ap.set_pixel(1, 0, red, 0, 0)   
    ap.set_pixel(1, 1, red, 0, 0)   
    ap.set_pixel(1, 2, red, 0, 0)   
    ap.set_pixel(1, 3, red, 0, 0)
    ap.set_pixel(2, 0, red, 0, 0)   
    ap.set_pixel(2, 1, red, 0, 0)   
    ap.set_pixel(2, 2, red, 0, 0)   
    ap.set_pixel(2, 3, red, 0, 0)
    ap.set_pixel(3, 0, red, 0, 0)   
    ap.set_pixel(3, 1, red, 0, 0)   
    ap.set_pixel(3, 2, red, 0, 0)   
    ap.set_pixel(3, 3, red, 0, 0)
    ap.set_pixel(4, 0, red, 0, 0)   
    ap.set_pixel(4, 1, red, 0, 0)   
    ap.set_pixel(4, 2, red, 0, 0)   
    ap.set_pixel(4, 3, red, 0, 0)
    ap.set_pixel(5, 0, red, 0, 0)   
    ap.set_pixel(5, 1, red, 0, 0)   
    ap.set_pixel(5, 2, red, 0, 0)   
    ap.set_pixel(5, 3, red, 0, 0)
    ap.set_pixel(6, 0, red, 0, 0)   
    ap.set_pixel(6, 1, red, 0, 0)   
    ap.set_pixel(6, 2, red, 0, 0)   
    ap.set_pixel(6, 3, red, 0, 0)
    ap.set_pixel(7, 0, red, 0, 0)   
    ap.set_pixel(7, 1, red, 0, 0)   
    ap.set_pixel(7, 2, red, 0, 0)   
    ap.set_pixel(7, 3, red, 0, 0)
    
def temp_num_error_low():
        # error state warning for - LOW TEMPERATURE
    ap.set_pixel(0, 0, 0, 0, blue)   
    ap.set_pixel(0, 1, 0, 0, blue)   
    ap.set_pixel(0, 2, 0, 0, blue)   
    ap.set_pixel(0, 3, 0, 0, blue)
    ap.set_pixel(1, 0, 0, 0, blue)   
    ap.set_pixel(1, 1, 0, 0, blue)   
    ap.set_pixel(1, 2, 0, 0, blue)   
    ap.set_pixel(1, 3, 0, 0, blue)
    ap.set_pixel(2, 0, 0, 0, blue)   
    ap.set_pixel(2, 1, 0, 0, blue)   
    ap.set_pixel(2, 2, 0, 0, blue)   
    ap.set_pixel(2, 3, 0, 0, blue)
    ap.set_pixel(3, 0, 0, 0, blue)   
    ap.set_pixel(3, 1, 0, 0, blue)   
    ap.set_pixel(3, 2, 0, 0, blue)   
    ap.set_pixel(3, 3, 0, 0, blue)
    ap.set_pixel(4, 0, 0, 0, blue)   
    ap.set_pixel(4, 1, 0, 0, blue)   
    ap.set_pixel(4, 2, 0, 0, blue)   
    ap.set_pixel(4, 3, 0, 0, blue)
    ap.set_pixel(5, 0, 0, 0, blue)   
    ap.set_pixel(5, 1, 0, 0, blue)   
    ap.set_pixel(5, 2, 0, 0, blue)   
    ap.set_pixel(5, 3, 0, 0, blue)
    ap.set_pixel(6, 0, 0, 0, blue)   
    ap.set_pixel(6, 1, 0, 0, blue)   
    ap.set_pixel(6, 2, 0, 0, blue)   
    ap.set_pixel(6, 3, 0, 0, blue)
    ap.set_pixel(7, 0, 0, 0, blue)   
    ap.set_pixel(7, 1, 0, 0, blue)   
    ap.set_pixel(7, 2, 0, 0, blue)   
    ap.set_pixel(7, 3, 0, 0, blue)
 

# 9 #    HUMIDITY LED MATRIX INCLUDING WARNINGS
 
        # HUMIDITY NUMBERS MATRIX BELOW   

def hum_num_matrix_1(num):

  if num == '0':
        # number 0_bot_left - HUMIDITY
    ap.set_pixel(0, 4, 0, led_level, 0)   
    ap.set_pixel(0, 5, 0, led_level, 0)   
    ap.set_pixel(0, 6, 0, led_level, 0)   
    ap.set_pixel(0, 7, 0, led_level, 0)
    ap.set_pixel(1, 4, 0, led_level, 0)   
    ap.set_pixel(1, 5, 0, 0, 0)   
    ap.set_pixel(1, 6, 0, 0, 0)   
    ap.set_pixel(1, 7, 0, led_level, 0)
    ap.set_pixel(2, 4, 0, led_level, 0)   
    ap.set_pixel(2, 5, 0, led_level, 0)   
    ap.set_pixel(2, 6, 0, led_level, 0)   
    ap.set_pixel(2, 7, 0, led_level, 0)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '1':
        # number 1_bot_left - HUMIDITY
    ap.set_pixel(0, 4, 0, 0, 0)   
    ap.set_pixel(0, 5, 0, led_level, 0)   
    ap.set_pixel(0, 6, 0, 0, 0)   
    ap.set_pixel(0, 7, 0, led_level, 0)
    ap.set_pixel(1, 4, 0, led_level, 0)   
    ap.set_pixel(1, 5, 0, led_level, 0)   
    ap.set_pixel(1, 6, 0, led_level, 0)   
    ap.set_pixel(1, 7, 0, led_level, 0)
    ap.set_pixel(2, 4, 0, 0, 0)   
    ap.set_pixel(2, 5, 0, 0, 0)   
    ap.set_pixel(2, 6, 0, 0, 0)   
    ap.set_pixel(2, 7, 0, led_level, 0)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '2':
        # number 2_bot_left - HUMIDITY
    ap.set_pixel(0, 4, 0, led_level, 0)   
    ap.set_pixel(0, 5, 0, 0, 0)   
    ap.set_pixel(0, 6, 0, 0, 0)   
    ap.set_pixel(0, 7, 0, led_level, 0)
    ap.set_pixel(1, 4, 0, led_level, 0)   
    ap.set_pixel(1, 5, 0, 0, 0)   
    ap.set_pixel(1, 6, 0, led_level, 0)   
    ap.set_pixel(1, 7, 0, led_level, 0)
    ap.set_pixel(2, 4, 0, led_level, 0)   
    ap.set_pixel(2, 5, 0, led_level, 0)   
    ap.set_pixel(2, 6, 0, 0, 0)   
    ap.set_pixel(2, 7, 0, led_level, 0)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '3':
        # number 3_bot_left - HUMIDITY
    ap.set_pixel(0, 4, 0, led_level, 0)   
    ap.set_pixel(0, 5, 0, 0, 0)   
    ap.set_pixel(0, 6, 0, 0, 0)   
    ap.set_pixel(0, 7, 0, led_level, 0)
    ap.set_pixel(1, 4, 0, led_level, 0)   
    ap.set_pixel(1, 5, 0, led_level, 0)   
    ap.set_pixel(1, 6, 0, 0, 0)   
    ap.set_pixel(1, 7, 0, led_level, 0)
    ap.set_pixel(2, 4, 0, led_level, 0)   
    ap.set_pixel(2, 5, 0, led_level, 0)   
    ap.set_pixel(2, 6, 0, led_level, 0)   
    ap.set_pixel(2, 7, 0, led_level, 0)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '4':
        # number 4_bot_left - HUMIDITY
    ap.set_pixel(0, 4, 0, led_level, 0)   
    ap.set_pixel(0, 5, 0, led_level, 0)   
    ap.set_pixel(0, 6, 0, led_level, 0)   
    ap.set_pixel(0, 7, 0, 0, 0)
    ap.set_pixel(1, 4, 0, 0, 0)   
    ap.set_pixel(1, 5, 0, 0, 0)   
    ap.set_pixel(1, 6, 0, led_level, 0)   
    ap.set_pixel(1, 7, 0, 0, 0)
    ap.set_pixel(2, 4, 0, 0, 0)   
    ap.set_pixel(2, 5, 0, led_level, 0)   
    ap.set_pixel(2, 6, 0, led_level, 0)   
    ap.set_pixel(2, 7, 0, led_level, 0)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '5':
        # number 5_bot_left - HUMIDITY
    ap.set_pixel(0, 4, 0, led_level, 0)   
    ap.set_pixel(0, 5, 0, led_level, 0)   
    ap.set_pixel(0, 6, 0, 0, 0)   
    ap.set_pixel(0, 7, 0, led_level, 0)
    ap.set_pixel(1, 4, 0, led_level, 0)   
    ap.set_pixel(1, 5, 0, 0, 0)   
    ap.set_pixel(1, 6, 0, led_level, 0)   
    ap.set_pixel(1, 7, 0, led_level, 0)
    ap.set_pixel(2, 4, 0, led_level, 0)   
    ap.set_pixel(2, 5, 0, 0, 0)   
    ap.set_pixel(2, 6, 0, 0, 0)   
    ap.set_pixel(2, 7, 0, led_level, 0)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '6':
        # number 6_bot_left - HUMIDITY
    ap.set_pixel(0, 4, 0, led_level, 0)   
    ap.set_pixel(0, 5, 0, led_level, 0)   
    ap.set_pixel(0, 6, 0, led_level, 0)   
    ap.set_pixel(0, 7, 0, led_level, 0)
    ap.set_pixel(1, 4, 0, 0, 0)   
    ap.set_pixel(1, 5, 0, led_level, 0)   
    ap.set_pixel(1, 6, 0, 0, 0)   
    ap.set_pixel(1, 7, 0, led_level, 0)
    ap.set_pixel(2, 4, 0, 0, 0)   
    ap.set_pixel(2, 5, 0, led_level, 0)   
    ap.set_pixel(2, 6, 0, led_level, 0)   
    ap.set_pixel(2, 7, 0, led_level, 0)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '7':
        # number 7_bot_left - HUMIDITY
    ap.set_pixel(0, 4, 0, led_level, 0)   
    ap.set_pixel(0, 5, 0, led_level, 0)   
    ap.set_pixel(0, 6, 0, 0, 0)   
    ap.set_pixel(0, 7, 0, 0, 0)
    ap.set_pixel(1, 4, 0, led_level, 0)   
    ap.set_pixel(1, 5, 0, 0, 0)   
    ap.set_pixel(1, 6, 0, 0, 0)   
    ap.set_pixel(1, 7, 0, 0, 0)
    ap.set_pixel(2, 4, 0, led_level, 0)   
    ap.set_pixel(2, 5, 0, led_level, 0)   
    ap.set_pixel(2, 6, 0, led_level, 0)   
    ap.set_pixel(2, 7, 0, led_level, 0)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '8':
        # number 8_bot_left - HUMIDITY
    ap.set_pixel(0, 4, 0, led_level, 0)   
    ap.set_pixel(0, 5, 0, led_level, 0)   
    ap.set_pixel(0, 6, 0, led_level, 0)   
    ap.set_pixel(0, 7, 0, led_level, 0)
    ap.set_pixel(1, 4, 0, led_level, 0)   
    ap.set_pixel(1, 5, 0, 0, 0)   
    ap.set_pixel(1, 6, 0, led_level, 0)   
    ap.set_pixel(1, 7, 0, led_level, 0)
    ap.set_pixel(2, 4, 0, led_level, 0)   
    ap.set_pixel(2, 5, 0, led_level, 0)   
    ap.set_pixel(2, 6, 0, led_level, 0)   
    ap.set_pixel(2, 7, 0, led_level, 0)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '9':
        # number 9_bot_left - HUMIDITY
    ap.set_pixel(0, 4, 0, led_level, 0)   
    ap.set_pixel(0, 5, 0, led_level, 0)   
    ap.set_pixel(0, 6, 0, led_level, 0)   
    ap.set_pixel(0, 7, 0, 0, 0)
    ap.set_pixel(1, 4, 0, led_level, 0)   
    ap.set_pixel(1, 5, 0, 0, 0)   
    ap.set_pixel(1, 6, 0, led_level, 0)   
    ap.set_pixel(1, 7, 0, 0, 0)
    ap.set_pixel(2, 4, 0, led_level, 0)   
    ap.set_pixel(2, 5, 0, led_level, 0)   
    ap.set_pixel(2, 6, 0, led_level, 0)   
    ap.set_pixel(2, 7, 0, led_level, 0)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

def hum_num_matrix_2(num):

  if num == '0':
        # number 0_bot_right - HUMIDITY
    ap.set_pixel(4, 4, 0, led_level, 0)   
    ap.set_pixel(4, 5, 0, led_level, 0)   
    ap.set_pixel(4, 6, 0, led_level, 0)   
    ap.set_pixel(4, 7, 0, led_level, 0)
    ap.set_pixel(5, 4, 0, led_level, 0)   
    ap.set_pixel(5, 5, 0, 0, 0)   
    ap.set_pixel(5, 6, 0, 0, 0)   
    ap.set_pixel(5, 7, 0, led_level, 0)
    ap.set_pixel(6, 4, 0, led_level, 0)   
    ap.set_pixel(6, 5, 0, led_level, 0)   
    ap.set_pixel(6, 6, 0, led_level, 0)   
    ap.set_pixel(6, 7, 0, led_level, 0)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)
    
  if num == '1':
        # number 1_bot_right - HUMIDITY
    ap.set_pixel(4, 4, 0, 0, 0)   
    ap.set_pixel(4, 5, 0, led_level, 0)   
    ap.set_pixel(4, 6, 0, 0, 0)   
    ap.set_pixel(4, 7, 0, led_level, 0)
    ap.set_pixel(5, 4, 0, led_level, 0)   
    ap.set_pixel(5, 5, 0, led_level, 0)   
    ap.set_pixel(5, 6, 0, led_level, 0)   
    ap.set_pixel(5, 7, 0, led_level, 0)
    ap.set_pixel(6, 4, 0, 0, 0)   
    ap.set_pixel(6, 5, 0, 0, 0)   
    ap.set_pixel(6, 6, 0, 0, 0)   
    ap.set_pixel(6, 7, 0, led_level, 0)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)
    
  if num == '2':
        # number 2_bot_right - HUMIDITY
    ap.set_pixel(4, 4, 0, led_level, 0)   
    ap.set_pixel(4, 5, 0, 0, 0)   
    ap.set_pixel(4, 6, 0, 0, 0)   
    ap.set_pixel(4, 7, 0, led_level, 0)
    ap.set_pixel(5, 4, 0, led_level, 0)   
    ap.set_pixel(5, 5, 0, 0, 0)   
    ap.set_pixel(5, 6, 0, led_level, 0)   
    ap.set_pixel(5, 7, 0, led_level, 0)
    ap.set_pixel(6, 4, 0, led_level, 0)   
    ap.set_pixel(6, 5, 0, led_level, 0)   
    ap.set_pixel(6, 6, 0, 0, 0)   
    ap.set_pixel(6, 7, 0, led_level, 0)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '3':
        # number 3_bot_right - HUMIDITY
    ap.set_pixel(4, 4, 0, led_level, 0)   
    ap.set_pixel(4, 5, 0, 0, 0)   
    ap.set_pixel(4, 6, 0, 0, 0)   
    ap.set_pixel(4, 7, 0, led_level, 0)
    ap.set_pixel(5, 4, 0, led_level, 0)   
    ap.set_pixel(5, 5, 0, led_level, 0)   
    ap.set_pixel(5, 6, 0, 0, 0)   
    ap.set_pixel(5, 7, 0, led_level, 0)
    ap.set_pixel(6, 4, 0, led_level, 0)   
    ap.set_pixel(6, 5, 0, led_level, 0)   
    ap.set_pixel(6, 6, 0, led_level, 0)   
    ap.set_pixel(6, 7, 0, led_level, 0)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '4':
        # number 4_bot_right - HUMIDITY
    ap.set_pixel(4, 4, 0, led_level, 0)   
    ap.set_pixel(4, 5, 0, led_level, 0)   
    ap.set_pixel(4, 6, 0, led_level, 0)   
    ap.set_pixel(4, 7, 0, 0, 0)
    ap.set_pixel(5, 4, 0, 0, 0)   
    ap.set_pixel(5, 5, 0, 0, 0)   
    ap.set_pixel(5, 6, 0, led_level, 0)   
    ap.set_pixel(5, 7, 0, 0, 0)
    ap.set_pixel(6, 4, 0, 0, 0)   
    ap.set_pixel(6, 5, 0, led_level, 0)   
    ap.set_pixel(6, 6, 0, led_level, 0)   
    ap.set_pixel(6, 7, 0, led_level, 0)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '5':
        # number 5_bot_right - HUMIDITY
    ap.set_pixel(4, 4, 0, led_level, 0)   
    ap.set_pixel(4, 5, 0, led_level, 0)   
    ap.set_pixel(4, 6, 0, 0, 0)   
    ap.set_pixel(4, 7, 0, led_level, 0)
    ap.set_pixel(5, 4, 0, led_level, 0)   
    ap.set_pixel(5, 5, 0, 0, 0)   
    ap.set_pixel(5, 6, 0, led_level, 0)   
    ap.set_pixel(5, 7, 0, led_level, 0)
    ap.set_pixel(6, 4, 0, led_level, 0)   
    ap.set_pixel(6, 5, 0, 0, 0)   
    ap.set_pixel(6, 6, 0, 0, 0)   
    ap.set_pixel(6, 7, 0, led_level, 0)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '6':
        # number 6_bot_right - HUMIDITY
    ap.set_pixel(4, 4, 0, led_level, 0)   
    ap.set_pixel(4, 5, 0, led_level, 0)   
    ap.set_pixel(4, 6, 0, led_level, 0)   
    ap.set_pixel(4, 7, 0, led_level, 0)
    ap.set_pixel(5, 4, 0, 0, 0)   
    ap.set_pixel(5, 5, 0, led_level, 0)   
    ap.set_pixel(5, 6, 0, 0, 0)   
    ap.set_pixel(5, 7, 0, led_level, 0)
    ap.set_pixel(6, 4, 0, 0, 0)   
    ap.set_pixel(6, 5, 0, led_level, 0)   
    ap.set_pixel(6, 6, 0, led_level, 0)   
    ap.set_pixel(6, 7, 0, led_level, 0)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '7':
        # number 7_bot_right - HUMIDITY
    ap.set_pixel(4, 4, 0, led_level, 0)   
    ap.set_pixel(4, 5, 0, led_level, 0)   
    ap.set_pixel(4, 6, 0, 0, 0)   
    ap.set_pixel(4, 7, 0, 0, 0)
    ap.set_pixel(5, 4, 0, led_level, 0)   
    ap.set_pixel(5, 5, 0, 0, 0)
    ap.set_pixel(5, 6, 0, 0, 0)   
    ap.set_pixel(5, 7, 0, 0, 0)
    ap.set_pixel(6, 4, 0, led_level, 0)   
    ap.set_pixel(6, 5, 0, led_level, 0)   
    ap.set_pixel(6, 6, 0, led_level, 0)   
    ap.set_pixel(6, 7, 0, led_level, 0)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '8':
        # number 8_bot_right - HUMIDITY
    ap.set_pixel(4, 4, 0, led_level, 0)   
    ap.set_pixel(4, 5, 0, led_level, 0)   
    ap.set_pixel(4, 6, 0, led_level, 0)   
    ap.set_pixel(4, 7, 0, led_level, 0)
    ap.set_pixel(5, 4, 0, led_level, 0)   
    ap.set_pixel(5, 5, 0, 0, 0)   
    ap.set_pixel(5, 6, 0, led_level, 0)   
    ap.set_pixel(5, 7, 0, led_level, 0)
    ap.set_pixel(6, 4, 0, led_level, 0)   
    ap.set_pixel(6, 5, 0, led_level, 0)   
    ap.set_pixel(6, 6, 0, led_level, 0)   
    ap.set_pixel(6, 7, 0, led_level, 0)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '9':
        # number 9_bot_right - HUMIDITY
    ap.set_pixel(4, 4, 0, led_level, 0)   
    ap.set_pixel(4, 5, 0, led_level, 0)   
    ap.set_pixel(4, 6, 0, led_level, 0)   
    ap.set_pixel(4, 7, 0, 0, 0)
    ap.set_pixel(5, 4, 0, led_level, 0)   
    ap.set_pixel(5, 5, 0, 0, 0)   
    ap.set_pixel(5, 6, 0, led_level, 0)   
    ap.set_pixel(5, 7, 0, 0, 0)
    ap.set_pixel(6, 4, 0, led_level, 0)   
    ap.set_pixel(6, 5, 0, led_level, 0)   
    ap.set_pixel(6, 6, 0, led_level, 0)   
    ap.set_pixel(6, 7, 0, led_level, 0)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)
	
        # HUMIDITY ERROR STATES 

def hum_num_error_high():
        # error state warning for - HIGH HUMIDITY
    ap.set_pixel(0, 4, red, 0, 0)   
    ap.set_pixel(0, 5, red, 0, 0)   
    ap.set_pixel(0, 6, red, 0, 0)   
    ap.set_pixel(0, 7, red, 0, 0)
    ap.set_pixel(1, 4, red, 0, 0)   
    ap.set_pixel(1, 5, red, 0, 0)   
    ap.set_pixel(1, 6, red, 0, 0)   
    ap.set_pixel(1, 7, red, 0, 0)
    ap.set_pixel(2, 4, red, 0, 0)   
    ap.set_pixel(2, 5, red, 0, 0)   
    ap.set_pixel(2, 6, red, 0, 0)   
    ap.set_pixel(2, 7, red, 0, 0)
    ap.set_pixel(3, 4, red, 0, 0)   
    ap.set_pixel(3, 5, red, 0, 0)   
    ap.set_pixel(3, 6, red, 0, 0)   
    ap.set_pixel(3, 7, red, 0, 0)
    ap.set_pixel(4, 4, red, 0, 0)   
    ap.set_pixel(4, 5, red, 0, 0)   
    ap.set_pixel(4, 6, red, 0, 0)   
    ap.set_pixel(4, 7, red, 0, 0)
    ap.set_pixel(5, 4, red, 0, 0)   
    ap.set_pixel(5, 5, red, 0, 0)   
    ap.set_pixel(5, 6, red, 0, 0)   
    ap.set_pixel(5, 7, red, 0, 0)
    ap.set_pixel(6, 4, red, 0, 0)   
    ap.set_pixel(6, 5, red, 0, 0)   
    ap.set_pixel(6, 6, red, 0, 0)   
    ap.set_pixel(6, 7, red, 0, 0)
    ap.set_pixel(7, 4, red, 0, 0)   
    ap.set_pixel(7, 5, red, 0, 0)   
    ap.set_pixel(7, 6, red, 0, 0)   
    ap.set_pixel(7, 7, red, 0, 0)
   	
def hum_num_error_low():
        # error state warning for - LOW HUMIDITY
    ap.set_pixel(0, 4, 0, 0, blue)   
    ap.set_pixel(0, 5, 0, 0, blue)   
    ap.set_pixel(0, 6, 0, 0, blue)   
    ap.set_pixel(0, 7, 0, 0, blue)
    ap.set_pixel(1, 4, 0, 0, blue)   
    ap.set_pixel(1, 5, 0, 0, blue)   
    ap.set_pixel(1, 6, 0, 0, blue)   
    ap.set_pixel(1, 7, 0, 0, blue)
    ap.set_pixel(2, 4, 0, 0, blue)   
    ap.set_pixel(2, 5, 0, 0, blue)   
    ap.set_pixel(2, 6, 0, 0, blue)   
    ap.set_pixel(2, 7, 0, 0, blue)
    ap.set_pixel(3, 4, 0, 0, blue)   
    ap.set_pixel(3, 5, 0, 0, blue)   
    ap.set_pixel(3, 6, 0, 0, blue)   
    ap.set_pixel(3, 7, 0, 0, blue)
    ap.set_pixel(4, 4, 0, 0, blue)   
    ap.set_pixel(4, 5, 0, 0, blue)   
    ap.set_pixel(4, 6, 0, 0, blue)   
    ap.set_pixel(4, 7, 0, 0, blue)
    ap.set_pixel(5, 4, 0, 0, blue)   
    ap.set_pixel(5, 5, 0, 0, blue)   
    ap.set_pixel(5, 6, 0, 0, blue)   
    ap.set_pixel(5, 7, 0, 0, blue)
    ap.set_pixel(6, 4, 0, 0, blue)   
    ap.set_pixel(6, 5, 0, 0, blue)   
    ap.set_pixel(6, 6, 0, 0, blue)   
    ap.set_pixel(6, 7, 0, 0, blue)
    ap.set_pixel(7, 4, 0, 0, blue)   
    ap.set_pixel(7, 5, 0, 0, blue)   
    ap.set_pixel(7, 6, 0, 0, blue)   
    ap.set_pixel(7, 7, 0, 0, blue)


# 10 #    PSI LED MATRIX INCLUDING WARNINGS
    
        # PRESSURE NUMBERS MATRIX BELOW  

def psi_num_matrix_1(num):

  if num == '0':
        # number 0_top_left - PRESSURE
    ap.set_pixel(0, 0, 0, 0, led_level)   
    ap.set_pixel(0, 1, 0, 0, led_level)   
    ap.set_pixel(0, 2, 0, 0, led_level)   
    ap.set_pixel(0, 3, 0, 0, led_level)
    ap.set_pixel(1, 0, 0, 0, led_level)   
    ap.set_pixel(1, 1, 0, 0, 0)   
    ap.set_pixel(1, 2, 0, 0, 0)   
    ap.set_pixel(1, 3, 0, 0, led_level)
    ap.set_pixel(2, 0, 0, 0, led_level)   
    ap.set_pixel(2, 1, 0, 0, led_level)   
    ap.set_pixel(2, 2, 0, 0, led_level)   
    ap.set_pixel(2, 3, 0, 0, led_level)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '1':
        # number 1_top_left - PRESSURE
    ap.set_pixel(0, 0, 0, 0, 0)   
    ap.set_pixel(0, 1, 0, 0, led_level)   
    ap.set_pixel(0, 2, 0, 0, 0)   
    ap.set_pixel(0, 3, 0, 0, led_level)
    ap.set_pixel(1, 0, 0, 0, led_level)   
    ap.set_pixel(1, 1, 0, 0, led_level)   
    ap.set_pixel(1, 2, 0, 0, led_level)   
    ap.set_pixel(1, 3, 0, 0, led_level)
    ap.set_pixel(2, 0, 0, 0, 0)   
    ap.set_pixel(2, 1, 0, 0, 0)   
    ap.set_pixel(2, 2, 0, 0, 0)   
    ap.set_pixel(2, 3, 0, 0, led_level)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '2':
        # number 2_top_left - PRESSURE
    ap.set_pixel(0, 0, 0, 0, led_level)   
    ap.set_pixel(0, 1, 0, 0, 0)   
    ap.set_pixel(0, 2, 0, 0, 0)   
    ap.set_pixel(0, 3, 0, 0, led_level)
    ap.set_pixel(1, 0, 0, 0, led_level)   
    ap.set_pixel(1, 1, 0, 0, 0)   
    ap.set_pixel(1, 2, 0, 0, led_level)   
    ap.set_pixel(1, 3, 0, 0, led_level)
    ap.set_pixel(2, 0, 0, 0, led_level)   
    ap.set_pixel(2, 1, 0, 0, led_level)   
    ap.set_pixel(2, 2, 0, 0, 0)   
    ap.set_pixel(2, 3, 0, 0, led_level)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '3':
        # number 3_top_left - PRESSURE
    ap.set_pixel(0, 0, 0, 0, led_level)   
    ap.set_pixel(0, 1, 0, 0, 0)   
    ap.set_pixel(0, 2, 0, 0, 0)   
    ap.set_pixel(0, 3, 0, 0, led_level)
    ap.set_pixel(1, 0, 0, 0, led_level)   
    ap.set_pixel(1, 1, 0, 0, led_level)   
    ap.set_pixel(1, 2, 0, 0, 0)   
    ap.set_pixel(1, 3, 0, 0, led_level)
    ap.set_pixel(2, 0, 0, 0, led_level)   
    ap.set_pixel(2, 1, 0, 0, led_level)   
    ap.set_pixel(2, 2, 0, 0, led_level)   
    ap.set_pixel(2, 3, 0, 0, led_level)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '4':
        # number 4_top_left - PRESSURE
    ap.set_pixel(0, 0, 0, 0, led_level)   
    ap.set_pixel(0, 1, 0, 0, led_level)   
    ap.set_pixel(0, 2, 0, 0, led_level)   
    ap.set_pixel(0, 3, 0, 0, 0)
    ap.set_pixel(1, 0, 0, 0, 0)   
    ap.set_pixel(1, 1, 0, 0, 0)   
    ap.set_pixel(1, 2, 0, 0, led_level)   
    ap.set_pixel(1, 3, 0, 0, 0)
    ap.set_pixel(2, 0, 0, 0, 0)   
    ap.set_pixel(2, 1, 0, 0, led_level)   
    ap.set_pixel(2, 2, 0, 0, led_level)   
    ap.set_pixel(2, 3, 0, 0, led_level)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '5':
        # number 5_top_left - PRESSURE
    ap.set_pixel(0, 0, 0, 0, led_level)   
    ap.set_pixel(0, 1, 0, 0, led_level)   
    ap.set_pixel(0, 2, 0, 0, 0)   
    ap.set_pixel(0, 3, 0, 0, led_level)
    ap.set_pixel(1, 0, 0, 0, led_level)   
    ap.set_pixel(1, 1, 0, 0, 0)   
    ap.set_pixel(1, 2, 0, 0, led_level)   
    ap.set_pixel(1, 3, 0, 0, led_level)
    ap.set_pixel(2, 0, 0, 0, led_level)   
    ap.set_pixel(2, 1, 0, 0, 0)   
    ap.set_pixel(2, 2, 0, 0, 0)   
    ap.set_pixel(2, 3, 0, 0, led_level)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '6':
        # number 6_top_left - PRESSURE
    ap.set_pixel(0, 0, 0, 0, led_level)   
    ap.set_pixel(0, 1, 0, 0, led_level)   
    ap.set_pixel(0, 2, 0, 0, led_level)   
    ap.set_pixel(0, 3, 0, 0, led_level)
    ap.set_pixel(1, 0, 0, 0, 0)   
    ap.set_pixel(1, 1, 0, 0, led_level)   
    ap.set_pixel(1, 2, 0, 0, 0)   
    ap.set_pixel(1, 3, 0, 0, led_level)
    ap.set_pixel(2, 0, 0, 0, 0)   
    ap.set_pixel(2, 1, 0, 0, led_level)   
    ap.set_pixel(2, 2, 0, 0, led_level)   
    ap.set_pixel(2, 3, 0, 0, led_level)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '7':
        # number 7_top_left - PRESSURE
    ap.set_pixel(0, 0, 0, 0, led_level)   
    ap.set_pixel(0, 1, 0, 0, led_level)   
    ap.set_pixel(0, 2, 0, 0, 0)   
    ap.set_pixel(0, 3, 0, 0, 0)
    ap.set_pixel(1, 0, 0, 0, led_level)   
    ap.set_pixel(1, 1, 0, 0, 0)   
    ap.set_pixel(1, 2, 0, 0, 0)   
    ap.set_pixel(1, 3, 0, 0, 0)
    ap.set_pixel(2, 0, 0, 0, led_level)   
    ap.set_pixel(2, 1, 0, 0, led_level)   
    ap.set_pixel(2, 2, 0, 0, led_level)   
    ap.set_pixel(2, 3, 0, 0, led_level)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '8':
        # number 8_top_left - PRESSURE
    ap.set_pixel(0, 0, 0, 0, led_level)   
    ap.set_pixel(0, 1, 0, 0, led_level)   
    ap.set_pixel(0, 2, 0, 0, led_level)   
    ap.set_pixel(0, 3, 0, 0, led_level)
    ap.set_pixel(1, 0, 0, 0, led_level)   
    ap.set_pixel(1, 1, 0, 0, 0)   
    ap.set_pixel(1, 2, 0, 0, led_level)   
    ap.set_pixel(1, 3, 0, 0, led_level)
    ap.set_pixel(2, 0, 0, 0, led_level)   
    ap.set_pixel(2, 1, 0, 0, led_level)   
    ap.set_pixel(2, 2, 0, 0, led_level)   
    ap.set_pixel(2, 3, 0, 0, led_level)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

  if num == '9':
        # number 9_top_left - PRESSURE
    ap.set_pixel(0, 0, 0, 0, led_level)   
    ap.set_pixel(0, 1, 0, 0, led_level)   
    ap.set_pixel(0, 2, 0, 0, led_level)   
    ap.set_pixel(0, 3, 0, 0, 0)
    ap.set_pixel(1, 0, 0, 0, led_level)   
    ap.set_pixel(1, 1, 0, 0, 0)   
    ap.set_pixel(1, 2, 0, 0, led_level)   
    ap.set_pixel(1, 3, 0, 0, 0)
    ap.set_pixel(2, 0, 0, 0, led_level)   
    ap.set_pixel(2, 1, 0, 0, led_level)   
    ap.set_pixel(2, 2, 0, 0, led_level)   
    ap.set_pixel(2, 3, 0, 0, led_level)
    ap.set_pixel(3, 0, 0, 0, 0)   
    ap.set_pixel(3, 1, 0, 0, 0)   
    ap.set_pixel(3, 2, 0, 0, 0)   
    ap.set_pixel(3, 3, 0, 0, 0)

def psi_num_matrix_2(num):

  if num == '0':
        # number 0_top_right - PRESSURE
    ap.set_pixel(4, 0, 0, 0, led_level)   
    ap.set_pixel(4, 1, 0, 0, led_level)   
    ap.set_pixel(4, 2, 0, 0, led_level)   
    ap.set_pixel(4, 3, 0, 0, led_level)
    ap.set_pixel(5, 0, 0, 0, led_level)   
    ap.set_pixel(5, 1, 0, 0, 0)   
    ap.set_pixel(5, 2, 0, 0, 0)   
    ap.set_pixel(5, 3, 0, 0, led_level)
    ap.set_pixel(6, 0, 0, 0, led_level)   
    ap.set_pixel(6, 1, 0, 0, led_level)   
    ap.set_pixel(6, 2, 0, 0, led_level)   
    ap.set_pixel(6, 3, 0, 0, led_level)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '1':
        # number 1_top_right - PRESSURE
    ap.set_pixel(4, 0, 0, 0, 0)   
    ap.set_pixel(4, 1, 0, 0, led_level)   
    ap.set_pixel(4, 2, 0, 0, 0)   
    ap.set_pixel(4, 3, 0, 0, led_level)
    ap.set_pixel(5, 0, 0, 0, led_level)   
    ap.set_pixel(5, 1, 0, 0, led_level)   
    ap.set_pixel(5, 2, 0, 0, led_level)   
    ap.set_pixel(5, 3, 0, 0, led_level)
    ap.set_pixel(6, 0, 0, 0, 0)   
    ap.set_pixel(6, 1, 0, 0, 0)   
    ap.set_pixel(6, 2, 0, 0, 0)   
    ap.set_pixel(6, 3, 0, 0, led_level)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '2':
        # number 2_top_right - PRESSURE
    ap.set_pixel(4, 0, 0, 0, led_level)   
    ap.set_pixel(4, 1, 0, 0, 0)   
    ap.set_pixel(4, 2, 0, 0, 0)   
    ap.set_pixel(4, 3, 0, 0, led_level)
    ap.set_pixel(5, 0, 0, 0, led_level)   
    ap.set_pixel(5, 1, 0, 0, 0)   
    ap.set_pixel(5, 2, 0, 0, led_level)   
    ap.set_pixel(5, 3, 0, 0, led_level)
    ap.set_pixel(6, 0, 0, 0, led_level)   
    ap.set_pixel(6, 1, 0, 0, led_level)   
    ap.set_pixel(6, 2, 0, 0, 0)   
    ap.set_pixel(6, 3, 0, 0, led_level)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '3':
        # number 3_top_right - PRESSURE
    ap.set_pixel(4, 0, 0, 0, led_level)   
    ap.set_pixel(4, 1, 0, 0, 0)   
    ap.set_pixel(4, 2, 0, 0, 0)   
    ap.set_pixel(4, 3, 0, 0, led_level)
    ap.set_pixel(5, 0, 0, 0, led_level)   
    ap.set_pixel(5, 1, 0, 0, led_level)   
    ap.set_pixel(5, 2, 0, 0, 0)   
    ap.set_pixel(5, 3, 0, 0, led_level)
    ap.set_pixel(6, 0, 0, 0, led_level)   
    ap.set_pixel(6, 1, 0, 0, led_level)   
    ap.set_pixel(6, 2, 0, 0, led_level)   
    ap.set_pixel(6, 3, 0, 0, led_level)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '4':
        # number 4_top_right - PRESSURE
    ap.set_pixel(4, 0, 0, 0, led_level)   
    ap.set_pixel(4, 1, 0, 0, led_level)   
    ap.set_pixel(4, 2, 0, 0, led_level)   
    ap.set_pixel(4, 3, 0, 0, 0)
    ap.set_pixel(5, 0, 0, 0, 0)   
    ap.set_pixel(5, 1, 0, 0, 0)   
    ap.set_pixel(5, 2, 0, 0, led_level)   
    ap.set_pixel(5, 3, 0, 0, 0)
    ap.set_pixel(6, 0, 0, 0, 0)   
    ap.set_pixel(6, 1, 0, 0, led_level)   
    ap.set_pixel(6, 2, 0, 0, led_level)   
    ap.set_pixel(6, 3, 0, 0, led_level)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '5':
        # number 5_top_right - PRESSURE
    ap.set_pixel(4, 0, 0, 0, led_level)   
    ap.set_pixel(4, 1, 0, 0, led_level)   
    ap.set_pixel(4, 2, 0, 0, 0)   
    ap.set_pixel(4, 3, 0, 0, led_level)
    ap.set_pixel(5, 0, 0, 0, led_level)   
    ap.set_pixel(5, 1, 0, 0, 0)   
    ap.set_pixel(5, 2, 0, 0, led_level)   
    ap.set_pixel(5, 3, 0, 0, led_level)
    ap.set_pixel(6, 0, 0, 0, led_level)   
    ap.set_pixel(6, 1, 0, 0, 0)   
    ap.set_pixel(6, 2, 0, 0, 0)   
    ap.set_pixel(6, 3, 0, 0, led_level)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '6':
        # number 6_top_right - PRESSURE
    ap.set_pixel(4, 0, 0, 0, led_level)   
    ap.set_pixel(4, 1, 0, 0, led_level)   
    ap.set_pixel(4, 2, 0, 0, led_level)   
    ap.set_pixel(4, 3, 0, 0, led_level)
    ap.set_pixel(5, 0, 0, 0, 0)   
    ap.set_pixel(5, 1, 0, 0, led_level)   
    ap.set_pixel(5, 2, 0, 0, 0)   
    ap.set_pixel(5, 3, 0, 0, led_level)
    ap.set_pixel(6, 0, 0, 0, 0)   
    ap.set_pixel(6, 1, 0, 0, led_level)   
    ap.set_pixel(6, 2, 0, 0, led_level)   
    ap.set_pixel(6, 3, 0, 0, led_level)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '7':
        # number 7_top_right - PRESSURE
    ap.set_pixel(4, 0, 0, 0, led_level)   
    ap.set_pixel(4, 1, 0, 0, led_level)   
    ap.set_pixel(4, 2, 0, 0, 0)   
    ap.set_pixel(4, 3, 0, 0, 0)
    ap.set_pixel(5, 0, 0, 0, led_level)   
    ap.set_pixel(5, 1, 0, 0, 0)   
    ap.set_pixel(5, 2, 0, 0, 0)   
    ap.set_pixel(5, 3, 0, 0, 0)
    ap.set_pixel(6, 0, 0, 0, led_level)   
    ap.set_pixel(6, 1, 0, 0, led_level)   
    ap.set_pixel(6, 2, 0, 0, led_level)   
    ap.set_pixel(6, 3, 0, 0, led_level)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '8':
        # number 8_top_right - PRESSURE
    ap.set_pixel(4, 0, 0, 0, led_level)   
    ap.set_pixel(4, 1, 0, 0, led_level)   
    ap.set_pixel(4, 2, 0, 0, led_level)   
    ap.set_pixel(4, 3, 0, 0, led_level)
    ap.set_pixel(5, 0, 0, 0, led_level)   
    ap.set_pixel(5, 1, 0, 0, 0)   
    ap.set_pixel(5, 2, 0, 0, led_level)   
    ap.set_pixel(5, 3, 0, 0, led_level)
    ap.set_pixel(6, 0, 0, 0, led_level)   
    ap.set_pixel(6, 1, 0, 0, led_level)   
    ap.set_pixel(6, 2, 0, 0, led_level)   
    ap.set_pixel(6, 3, 0, 0, led_level)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

  if num == '9':
        # number 9_top_right - PRESSURE
    ap.set_pixel(4, 0, 0, 0, led_level)   
    ap.set_pixel(4, 1, 0, 0, led_level)   
    ap.set_pixel(4, 2, 0, 0, led_level)   
    ap.set_pixel(4, 3, 0, 0, 0)
    ap.set_pixel(5, 0, 0, 0, led_level)   
    ap.set_pixel(5, 1, 0, 0, 0)   
    ap.set_pixel(5, 2, 0, 0, led_level)   
    ap.set_pixel(5, 3, 0, 0, 0)
    ap.set_pixel(6, 0, 0, 0, led_level)   
    ap.set_pixel(6, 1, 0, 0, led_level)   
    ap.set_pixel(6, 2, 0, 0, led_level)   
    ap.set_pixel(6, 3, 0, 0, led_level)
    ap.set_pixel(7, 0, 0, 0, 0)   
    ap.set_pixel(7, 1, 0, 0, 0)   
    ap.set_pixel(7, 2, 0, 0, 0)   
    ap.set_pixel(7, 3, 0, 0, 0)

def psi_num_matrix_3(num):

  if num == '0':
        # number 0_bot_left - PRESSURE
    ap.set_pixel(0, 4, 0, 0, led_level)   
    ap.set_pixel(0, 5, 0, 0, led_level)   
    ap.set_pixel(0, 6, 0, 0, led_level)   
    ap.set_pixel(0, 7, 0, 0, led_level)
    ap.set_pixel(1, 4, 0, 0, led_level)   
    ap.set_pixel(1, 5, 0, 0, 0)   
    ap.set_pixel(1, 6, 0, 0, 0)   
    ap.set_pixel(1, 7, 0, 0, led_level)
    ap.set_pixel(2, 4, 0, 0, led_level)   
    ap.set_pixel(2, 5, 0, 0, led_level)   
    ap.set_pixel(2, 6, 0, 0, led_level)   
    ap.set_pixel(2, 7, 0, 0, led_level)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '1':
        # number 1_bot_left - PRESSURE
    ap.set_pixel(0, 4, 0, 0, 0)   
    ap.set_pixel(0, 5, 0, 0, led_level)   
    ap.set_pixel(0, 6, 0, 0, 0)   
    ap.set_pixel(0, 7, 0, 0, led_level)
    ap.set_pixel(1, 4, 0, 0, led_level)   
    ap.set_pixel(1, 5, 0, 0, led_level)   
    ap.set_pixel(1, 6, 0, 0, led_level)   
    ap.set_pixel(1, 7, 0, 0, led_level)
    ap.set_pixel(2, 4, 0, 0, 0)   
    ap.set_pixel(2, 5, 0, 0, 0)   
    ap.set_pixel(2, 6, 0, 0, 0)   
    ap.set_pixel(2, 7, 0, 0, led_level)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '2':
        # number 2_bot_left - PRESSURE
    ap.set_pixel(0, 4, 0, 0, led_level)   
    ap.set_pixel(0, 5, 0, 0, 0)   
    ap.set_pixel(0, 6, 0, 0, 0)   
    ap.set_pixel(0, 7, 0, 0, led_level)
    ap.set_pixel(1, 4, 0, 0, led_level)   
    ap.set_pixel(1, 5, 0, 0, 0)   
    ap.set_pixel(1, 6, 0, 0, led_level)   
    ap.set_pixel(1, 7, 0, 0, led_level)
    ap.set_pixel(2, 4, 0, 0, led_level)   
    ap.set_pixel(2, 5, 0, 0, led_level)   
    ap.set_pixel(2, 6, 0, 0, 0)   
    ap.set_pixel(2, 7, 0, 0, led_level)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '3':
        # number 3_bot_left - PRESSURE
    ap.set_pixel(0, 4, 0, 0, led_level)   
    ap.set_pixel(0, 5, 0, 0, 0)   
    ap.set_pixel(0, 6, 0, 0, 0)   
    ap.set_pixel(0, 7, 0, 0, led_level)
    ap.set_pixel(1, 4, 0, 0, led_level)   
    ap.set_pixel(1, 5, 0, 0, led_level)   
    ap.set_pixel(1, 6, 0, 0, 0)   
    ap.set_pixel(1, 7, 0, 0, led_level)
    ap.set_pixel(2, 4, 0, 0, led_level)   
    ap.set_pixel(2, 5, 0, 0, led_level)   
    ap.set_pixel(2, 6, 0, 0, led_level)   
    ap.set_pixel(2, 7, 0, 0, led_level)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '4':
        # number 4_bot_left - PRESSURE
    ap.set_pixel(0, 4, 0, 0, led_level)   
    ap.set_pixel(0, 5, 0, 0, led_level)   
    ap.set_pixel(0, 6, 0, 0, led_level)   
    ap.set_pixel(0, 7, 0, 0, 0)
    ap.set_pixel(1, 4, 0, 0, 0)   
    ap.set_pixel(1, 5, 0, 0, 0)   
    ap.set_pixel(1, 6, 0, 0, led_level)   
    ap.set_pixel(1, 7, 0, 0, 0)
    ap.set_pixel(2, 4, 0, 0, 0)   
    ap.set_pixel(2, 5, 0, 0, led_level)   
    ap.set_pixel(2, 6, 0, 0, led_level)   
    ap.set_pixel(2, 7, 0, 0, led_level)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '5':
        # number 5_bot_left - PRESSURE
    ap.set_pixel(0, 4, 0, 0, led_level)   
    ap.set_pixel(0, 5, 0, 0, led_level)   
    ap.set_pixel(0, 6, 0, 0, 0)   
    ap.set_pixel(0, 7, 0, 0, led_level)
    ap.set_pixel(1, 4, 0, 0, led_level)   
    ap.set_pixel(1, 5, 0, 0, 0)   
    ap.set_pixel(1, 6, 0, 0, led_level)   
    ap.set_pixel(1, 7, 0, 0, led_level)
    ap.set_pixel(2, 4, 0, 0, led_level)   
    ap.set_pixel(2, 5, 0, 0, 0)   
    ap.set_pixel(2, 6, 0, 0, 0)   
    ap.set_pixel(2, 7, 0, 0, led_level)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '6':
        # number 6_bot_left - PRESSURE
    ap.set_pixel(0, 4, 0, 0, led_level)   
    ap.set_pixel(0, 5, 0, 0, led_level)   
    ap.set_pixel(0, 6, 0, 0, led_level)   
    ap.set_pixel(0, 7, 0, 0, led_level)
    ap.set_pixel(1, 4, 0, 0, 0)   
    ap.set_pixel(1, 5, 0, 0, led_level)   
    ap.set_pixel(1, 6, 0, 0, 0)   
    ap.set_pixel(1, 7, 0, 0, led_level)
    ap.set_pixel(2, 4, 0, 0, 0)   
    ap.set_pixel(2, 5, 0, 0, led_level)   
    ap.set_pixel(2, 6, 0, 0, led_level)   
    ap.set_pixel(2, 7, 0, 0, led_level)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '7':
        # number 7_bot_left - PRESSURE
    ap.set_pixel(0, 4, 0, 0, led_level)   
    ap.set_pixel(0, 5, 0, 0, led_level)   
    ap.set_pixel(0, 6, 0, 0, 0)   
    ap.set_pixel(0, 7, 0, 0, 0)
    ap.set_pixel(1, 4, 0, 0, led_level)   
    ap.set_pixel(1, 5, 0, 0, 0)   
    ap.set_pixel(1, 6, 0, 0, 0)   
    ap.set_pixel(1, 7, 0, 0, 0)
    ap.set_pixel(2, 4, 0, 0, led_level)   
    ap.set_pixel(2, 5, 0, 0, led_level)   
    ap.set_pixel(2, 6, 0, 0, led_level)   
    ap.set_pixel(2, 7, 0, 0, led_level)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '8':
        # number 8_bot_left - PRESSURE
    ap.set_pixel(0, 4, 0, 0, led_level)   
    ap.set_pixel(0, 5, 0, 0, led_level)   
    ap.set_pixel(0, 6, 0, 0, led_level)   
    ap.set_pixel(0, 7, 0, 0, led_level)
    ap.set_pixel(1, 4, 0, 0, led_level)   
    ap.set_pixel(1, 5, 0, 0, 0)   
    ap.set_pixel(1, 6, 0, 0, led_level)   
    ap.set_pixel(1, 7, 0, 0, led_level)
    ap.set_pixel(2, 4, 0, 0, led_level)   
    ap.set_pixel(2, 5, 0, 0, led_level)   
    ap.set_pixel(2, 6, 0, 0, led_level)   
    ap.set_pixel(2, 7, 0, 0, led_level)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

  if num == '9':
        # number 9_bot_left - PRESSURE
    ap.set_pixel(0, 4, 0, 0, led_level)   
    ap.set_pixel(0, 5, 0, 0, led_level)   
    ap.set_pixel(0, 6, 0, 0, led_level)   
    ap.set_pixel(0, 7, 0, 0, 0)
    ap.set_pixel(1, 4, 0, 0, led_level)   
    ap.set_pixel(1, 5, 0, 0, 0)   
    ap.set_pixel(1, 6, 0, 0, led_level)   
    ap.set_pixel(1, 7, 0, 0, 0)
    ap.set_pixel(2, 4, 0, 0, led_level)   
    ap.set_pixel(2, 5, 0, 0, led_level)   
    ap.set_pixel(2, 6, 0, 0, led_level)   
    ap.set_pixel(2, 7, 0, 0, led_level)
    ap.set_pixel(3, 4, 0, 0, 0)   
    ap.set_pixel(3, 5, 0, 0, 0)   
    ap.set_pixel(3, 6, 0, 0, 0)   
    ap.set_pixel(3, 7, 0, 0, 0)

def psi_num_matrix_4(num):

  if num == '0':
        # number 0_bottom_right - PRESSURE
    ap.set_pixel(4, 4, 0, 0, led_level)   
    ap.set_pixel(4, 5, 0, 0, led_level)   
    ap.set_pixel(4, 6, 0, 0, led_level)   
    ap.set_pixel(4, 7, 0, 0, led_level)
    ap.set_pixel(5, 4, 0, 0, led_level)   
    ap.set_pixel(5, 5, 0, 0, 0)   
    ap.set_pixel(5, 6, 0, 0, 0)   
    ap.set_pixel(5, 7, 0, 0, led_level)
    ap.set_pixel(6, 4, 0, 0, led_level)   
    ap.set_pixel(6, 5, 0, 0, led_level)   
    ap.set_pixel(6, 6, 0, 0, led_level)   
    ap.set_pixel(6, 7, 0, 0, led_level)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '1':
        # number 1_bot_right - PRESSURE
    ap.set_pixel(4, 4, 0, 0, 0)   
    ap.set_pixel(4, 5, 0, 0, led_level)   
    ap.set_pixel(4, 6, 0, 0, 0)   
    ap.set_pixel(4, 7, 0, 0, led_level)
    ap.set_pixel(5, 4, 0, 0, led_level)   
    ap.set_pixel(5, 5, 0, 0, led_level)   
    ap.set_pixel(5, 6, 0, 0, led_level)   
    ap.set_pixel(5, 7, 0, 0, led_level)
    ap.set_pixel(6, 4, 0, 0, 0)   
    ap.set_pixel(6, 5, 0, 0, 0)   
    ap.set_pixel(6, 6, 0, 0, 0)   
    ap.set_pixel(6, 7, 0, 0, led_level)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '2':
        # number 2_bot_right - PRESSURE
    ap.set_pixel(4, 4, 0, 0, led_level)   
    ap.set_pixel(4, 5, 0, 0, 0)   
    ap.set_pixel(4, 6, 0, 0, 0)   
    ap.set_pixel(4, 7, 0, 0, led_level)
    ap.set_pixel(5, 4, 0, 0, led_level)   
    ap.set_pixel(5, 5, 0, 0, 0)   
    ap.set_pixel(5, 6, 0, 0, led_level)   
    ap.set_pixel(5, 7, 0, 0, led_level)
    ap.set_pixel(6, 4, 0, 0, led_level)   
    ap.set_pixel(6, 5, 0, 0, led_level)   
    ap.set_pixel(6, 6, 0, 0, 0)   
    ap.set_pixel(6, 7, 0, 0, led_level)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '3':
        # number 3_bot_right - PRESSURE
    ap.set_pixel(4, 4, 0, 0, led_level)   
    ap.set_pixel(4, 5, 0, 0, 0)   
    ap.set_pixel(4, 6, 0, 0, 0)   
    ap.set_pixel(4, 7, 0, 0, led_level)
    ap.set_pixel(5, 4, 0, 0, led_level)   
    ap.set_pixel(5, 5, 0, 0, led_level)   
    ap.set_pixel(5, 6, 0, 0, 0)   
    ap.set_pixel(5, 7, 0, 0, led_level)
    ap.set_pixel(6, 4, 0, 0, led_level)   
    ap.set_pixel(6, 5, 0, 0, led_level)   
    ap.set_pixel(6, 6, 0, 0, led_level)   
    ap.set_pixel(6, 7, 0, 0, led_level)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '4':
        # number 4_bot_right - PRESSURE
    ap.set_pixel(4, 4, 0, 0, led_level)   
    ap.set_pixel(4, 5, 0, 0, led_level)   
    ap.set_pixel(4, 6, 0, 0, led_level)   
    ap.set_pixel(4, 7, 0, 0, 0)
    ap.set_pixel(5, 4, 0, 0, 0)   
    ap.set_pixel(5, 5, 0, 0, 0)   
    ap.set_pixel(5, 6, 0, 0, led_level)   
    ap.set_pixel(5, 7, 0, 0, 0)
    ap.set_pixel(6, 4, 0, 0, 0)   
    ap.set_pixel(6, 5, 0, 0, led_level)   
    ap.set_pixel(6, 6, 0, 0, led_level)   
    ap.set_pixel(6, 7, 0, 0, led_level)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '5':
        # number 5_bot_right - PRESSURE
    ap.set_pixel(4, 4, 0, 0, led_level)   
    ap.set_pixel(4, 5, 0, 0, led_level)   
    ap.set_pixel(4, 6, 0, 0, 0)   
    ap.set_pixel(4, 7, 0, 0, led_level)
    ap.set_pixel(5, 4, 0, 0, led_level)   
    ap.set_pixel(5, 5, 0, 0, 0)   
    ap.set_pixel(5, 6, 0, 0, led_level)   
    ap.set_pixel(5, 7, 0, 0, led_level)
    ap.set_pixel(6, 4, 0, 0, led_level)   
    ap.set_pixel(6, 5, 0, 0, 0)   
    ap.set_pixel(6, 6, 0, 0, 0)   
    ap.set_pixel(6, 7, 0, 0, led_level)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '6':
        # number 6_bot_right - PRESSURE
    ap.set_pixel(4, 4, 0, 0, led_level)   
    ap.set_pixel(4, 5, 0, 0, led_level)   
    ap.set_pixel(4, 6, 0, 0, led_level)   
    ap.set_pixel(4, 7, 0, 0, led_level)
    ap.set_pixel(5, 4, 0, 0, 0)   
    ap.set_pixel(5, 5, 0, 0, led_level)   
    ap.set_pixel(5, 6, 0, 0, 0)   
    ap.set_pixel(5, 7, 0, 0, led_level)
    ap.set_pixel(6, 4, 0, 0, 0)   
    ap.set_pixel(6, 5, 0, 0, led_level)   
    ap.set_pixel(6, 6, 0, 0, led_level)   
    ap.set_pixel(6, 7, 0, 0, led_level)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '7':
        # number 7_bot_right - PRESSURE
    ap.set_pixel(4, 4, 0, 0, led_level)   
    ap.set_pixel(4, 5, 0, 0, led_level)   
    ap.set_pixel(4, 6, 0, 0, 0)   
    ap.set_pixel(4, 7, 0, 0, 0)
    ap.set_pixel(5, 4, 0, 0, led_level)   
    ap.set_pixel(5, 5, 0, 0, 0)
    ap.set_pixel(5, 6, 0, 0, 0)   
    ap.set_pixel(5, 7, 0, 0, 0)
    ap.set_pixel(6, 4, 0, 0, led_level)   
    ap.set_pixel(6, 5, 0, 0, led_level)   
    ap.set_pixel(6, 6, 0, 0, led_level)   
    ap.set_pixel(6, 7, 0, 0, led_level)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '8':
        # number 8_bot_right - PRESSURE
    ap.set_pixel(4, 4, 0, 0, led_level)   
    ap.set_pixel(4, 5, 0, 0, led_level)   
    ap.set_pixel(4, 6, 0, 0, led_level)   
    ap.set_pixel(4, 7, 0, 0, led_level)
    ap.set_pixel(5, 4, 0, 0, led_level)   
    ap.set_pixel(5, 5, 0, 0, 0)   
    ap.set_pixel(5, 6, 0, 0, led_level)   
    ap.set_pixel(5, 7, 0, 0, led_level)
    ap.set_pixel(6, 4, 0, 0, led_level)   
    ap.set_pixel(6, 5, 0, 0, led_level)   
    ap.set_pixel(6, 6, 0, 0, led_level)   
    ap.set_pixel(6, 7, 0, 0, led_level)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)

  if num == '9':
        # number 9_bot_right - PRESSURE
    ap.set_pixel(4, 4, 0, 0, led_level)   
    ap.set_pixel(4, 5, 0, 0, led_level)   
    ap.set_pixel(4, 6, 0, 0, led_level)   
    ap.set_pixel(4, 7, 0, 0, 0)
    ap.set_pixel(5, 4, 0, 0, led_level)   
    ap.set_pixel(5, 5, 0, 0, 0)   
    ap.set_pixel(5, 6, 0, 0, led_level)   
    ap.set_pixel(5, 7, 0, 0, 0)
    ap.set_pixel(6, 4, 0, 0, led_level)   
    ap.set_pixel(6, 5, 0, 0, led_level)   
    ap.set_pixel(6, 6, 0, 0, led_level)   
    ap.set_pixel(6, 7, 0, 0, led_level)
    ap.set_pixel(7, 4, 0, 0, 0)   
    ap.set_pixel(7, 5, 0, 0, 0)   
    ap.set_pixel(7, 6, 0, 0, 0)   
    ap.set_pixel(7, 7, 0, 0, 0)
	
        # PRESSURE ERROR STATES 

def psi_num_error_high():
        # error state warning for - HIGH PRESSURE
    ap.set_pixel(0, 0, red, 0, 0)   
    ap.set_pixel(0, 1, red, 0, 0)   
    ap.set_pixel(0, 2, red, 0, 0)   
    ap.set_pixel(0, 3, red, 0, 0)
    ap.set_pixel(1, 0, red, 0, 0)   
    ap.set_pixel(1, 1, red, 0, 0)   
    ap.set_pixel(1, 2, red, 0, 0)   
    ap.set_pixel(1, 3, red, 0, 0)
    ap.set_pixel(2, 0, red, 0, 0)   
    ap.set_pixel(2, 1, red, 0, 0)   
    ap.set_pixel(2, 2, red, 0, 0)   
    ap.set_pixel(2, 3, red, 0, 0)
    ap.set_pixel(3, 0, red, 0, 0)   
    ap.set_pixel(3, 1, red, 0, 0)   
    ap.set_pixel(3, 2, red, 0, 0)   
    ap.set_pixel(3, 3, red, 0, 0)
    ap.set_pixel(4, 0, red, 0, 0)   
    ap.set_pixel(4, 1, red, 0, 0)   
    ap.set_pixel(4, 2, red, 0, 0)   
    ap.set_pixel(4, 3, red, 0, 0)
    ap.set_pixel(5, 0, red, 0, 0)   
    ap.set_pixel(5, 1, red, 0, 0)   
    ap.set_pixel(5, 2, red, 0, 0)   
    ap.set_pixel(5, 3, red, 0, 0)
    ap.set_pixel(6, 0, red, 0, 0)   
    ap.set_pixel(6, 1, red, 0, 0)   
    ap.set_pixel(6, 2, red, 0, 0)   
    ap.set_pixel(6, 3, red, 0, 0)
    ap.set_pixel(7, 0, red, 0, 0)   
    ap.set_pixel(7, 1, red, 0, 0)   
    ap.set_pixel(7, 2, red, 0, 0)   
    ap.set_pixel(7, 3, red, 0, 0)
    ap.set_pixel(0, 4, red, 0, 0)   
    ap.set_pixel(0, 5, red, 0, 0)   
    ap.set_pixel(0, 6, red, 0, 0)   
    ap.set_pixel(0, 7, red, 0, 0)
    ap.set_pixel(1, 4, red, 0, 0)   
    ap.set_pixel(1, 5, red, 0, 0)   
    ap.set_pixel(1, 6, red, 0, 0)   
    ap.set_pixel(1, 7, red, 0, 0)
    ap.set_pixel(2, 4, red, 0, 0)   
    ap.set_pixel(2, 5, red, 0, 0)   
    ap.set_pixel(2, 6, red, 0, 0)   
    ap.set_pixel(2, 7, red, 0, 0)
    ap.set_pixel(3, 4, red, 0, 0)   
    ap.set_pixel(3, 5, red, 0, 0)   
    ap.set_pixel(3, 6, red, 0, 0)   
    ap.set_pixel(3, 7, red, 0, 0)
    ap.set_pixel(4, 4, red, 0, 0)   
    ap.set_pixel(4, 5, red, 0, 0)   
    ap.set_pixel(4, 6, red, 0, 0)   
    ap.set_pixel(4, 7, red, 0, 0)
    ap.set_pixel(5, 4, red, 0, 0)   
    ap.set_pixel(5, 5, red, 0, 0)   
    ap.set_pixel(5, 6, red, 0, 0)   
    ap.set_pixel(5, 7, red, 0, 0)
    ap.set_pixel(6, 4, red, 0, 0)   
    ap.set_pixel(6, 5, red, 0, 0)   
    ap.set_pixel(6, 6, red, 0, 0)   
    ap.set_pixel(6, 7, red, 0, 0)
    ap.set_pixel(7, 4, red, 0, 0)   
    ap.set_pixel(7, 5, red, 0, 0)   
    ap.set_pixel(7, 6, red, 0, 0)   
    ap.set_pixel(7, 7, red, 0, 0)
	
def psi_num_error_low():
        # error state warning for - LOW PRESSURE
    ap.set_pixel(0, 0, 0, 0, blue)   
    ap.set_pixel(0, 1, 0, 0, blue)   
    ap.set_pixel(0, 2, 0, 0, blue)   
    ap.set_pixel(0, 3, 0, 0, blue)
    ap.set_pixel(1, 0, 0, 0, blue)   
    ap.set_pixel(1, 1, 0, 0, blue)   
    ap.set_pixel(1, 2, 0, 0, blue)   
    ap.set_pixel(1, 3, 0, 0, blue)
    ap.set_pixel(2, 0, 0, 0, blue)   
    ap.set_pixel(2, 1, 0, 0, blue)   
    ap.set_pixel(2, 2, 0, 0, blue)   
    ap.set_pixel(2, 3, 0, 0, blue)
    ap.set_pixel(3, 0, 0, 0, blue)   
    ap.set_pixel(3, 1, 0, 0, blue)   
    ap.set_pixel(3, 2, 0, 0, blue)   
    ap.set_pixel(3, 3, 0, 0, blue)
    ap.set_pixel(4, 0, 0, 0, blue)   
    ap.set_pixel(4, 1, 0, 0, blue)   
    ap.set_pixel(4, 2, 0, 0, blue)   
    ap.set_pixel(4, 3, 0, 0, blue)
    ap.set_pixel(5, 0, 0, 0, blue)   
    ap.set_pixel(5, 1, 0, 0, blue)   
    ap.set_pixel(5, 2, 0, 0, blue)   
    ap.set_pixel(5, 3, 0, 0, blue)
    ap.set_pixel(6, 0, 0, 0, blue)   
    ap.set_pixel(6, 1, 0, 0, blue)   
    ap.set_pixel(6, 2, 0, 0, blue)   
    ap.set_pixel(6, 3, 0, 0, blue)
    ap.set_pixel(7, 0, 0, 0, blue)   
    ap.set_pixel(7, 1, 0, 0, blue)   
    ap.set_pixel(7, 2, 0, 0, blue)   
    ap.set_pixel(7, 3, 0, 0, blue)
    ap.set_pixel(0, 4, 0, 0, blue)   
    ap.set_pixel(0, 5, 0, 0, blue)   
    ap.set_pixel(0, 6, 0, 0, blue)   
    ap.set_pixel(0, 7, 0, 0, blue)
    ap.set_pixel(1, 4, 0, 0, blue)   
    ap.set_pixel(1, 5, 0, 0, blue)   
    ap.set_pixel(1, 6, 0, 0, blue)   
    ap.set_pixel(1, 7, 0, 0, blue)
    ap.set_pixel(2, 4, 0, 0, blue)   
    ap.set_pixel(2, 5, 0, 0, blue)   
    ap.set_pixel(2, 6, 0, 0, blue)   
    ap.set_pixel(2, 7, 0, 0, blue)
    ap.set_pixel(3, 4, 0, 0, blue)   
    ap.set_pixel(3, 5, 0, 0, blue)   
    ap.set_pixel(3, 6, 0, 0, blue)   
    ap.set_pixel(3, 7, 0, 0, blue)
    ap.set_pixel(4, 4, 0, 0, blue)   
    ap.set_pixel(4, 5, 0, 0, blue)   
    ap.set_pixel(4, 6, 0, 0, blue)   
    ap.set_pixel(4, 7, 0, 0, blue)
    ap.set_pixel(5, 4, 0, 0, blue)   
    ap.set_pixel(5, 5, 0, 0, blue)   
    ap.set_pixel(5, 6, 0, 0, blue)   
    ap.set_pixel(5, 7, 0, 0, blue)
    ap.set_pixel(6, 4, 0, 0, blue)   
    ap.set_pixel(6, 5, 0, 0, blue)   
    ap.set_pixel(6, 6, 0, 0, blue)   
    ap.set_pixel(6, 7, 0, 0, blue)
    ap.set_pixel(7, 4, 0, 0, blue)   
    ap.set_pixel(7, 5, 0, 0, blue)   
    ap.set_pixel(7, 6, 0, 0, blue)   
    ap.set_pixel(7, 7, 0, 0, blue)

    
# 11 #    SETTING UP FLIGHT BUTTONS FOR USE AND ASSIGNING COMMANDS

        # LOOKING FOR BUTTON PRESSES FROM FLIGHT BUTTONS
   
def button_pressed(button):             ## CONTINUOUSLY MONITORS FOR BUTTON EVENTS
    global running
    global ap
    global led_level
    global temp_hum_on
    global psi_on
    global tmp_mute
    global hum_mute
    global alarm_count
    
        # UP BUTTON (BRIGHTNESS INCREASE) 
    if button == UP and led_level < 250:    ## ADJUST LED MATRIX BRIGHTNESS - UP
        led_level = led_level + 10

        # DOWN BUTTON (BRIGHTNESS DECRASE) 
    if button == DOWN and led_level > 40:   ## ADJUST LED MATRIX BRIGHTNESS - DOWN
        led_level = led_level - 10

        # LEFT BUTTON (TEMPERATURE & HUMIDITY PAGE ON)
    if button == LEFT:                  ## FORCE TEMPERATURE AND HUMIDITY PAGE ON (5s)
        temp_hum_on = 1                 
        
        temp_num_matrix_1(temp[0])      ## FIRST DIGIT - TEMPERATURE
        temp_num_matrix_2(temp[1])      ## SECOND DIGIT - TEMPERATURE
        hum_num_matrix_1(hum[0])        ## FIRST DIGIT - HUMIDITY
        hum_num_matrix_2(hum[1])        ## SECOND DIGIT - HUMIDITY
        
        time.sleep(5.0)                 ## WAIT 5 SECONDS TO ENSURE READING CAN BE RECORDED
        
        temp_hum_on = 0                 ## CLOSE TEMPERATURE AND HUMIDITY PAGE OFF
        
        tmp_mute = 0                    ## SHOWS THE WARNING FOR TEMPERATURE
        hum_mute = 0                    ## SHOWS THE WARNING FOR HUMIDITY
        
        # RIGHT BUTTON (PRESSURE PAGE ON) 
    if button == RIGHT:                 ## FORCE PRESSURE PAGE ON (5s)
        psi_on = 1                      
        
        psi_num_matrix_1(psi[0])        ## FIRST DIGIT - PRESSURE
        psi_num_matrix_2(psi[1])        ## SECOND DIGIT - PRESSURE
        psi_num_matrix_3(psi[2])        ## THIRD DIGIT - PRESSURE
        psi_num_matrix_4(psi[3])        ## FOURTH DIGIT - PRESSURE
        
        time.sleep(5.0)                 ## WAIT 5 SECONDS TO ENSURE READING CAN BE RECORDED
        
        psi_on = 0                      ## FORCE PRESSURE PAGE OFF
     
        # B BUTTON (MUTES ALARMS)    
    if button == A:                     ## ALLOWS ASTRONAUT (Tim) TO MUTE ALARMS
        alarm_count = 0                 # RESETS 'alarm_count' TO ZERO TO START COUNTDOWN
        tmp_mute = 1                    # MUTES THE WARNING FOR TEMPERATURE
        hum_mute = 1                    # MUTES THE WARNING FOR HUMIDITY
        psi_mute = 1                    # MUTES THE WARNING FOR PRESSURE
        
        # A BUTTON (UN-MUTES ALARMS) 
    if button == B:                     ## ALLOWS ASTRONAUT (Tim) TO UN-MUTE ALARMS
        alarm_count = 0                 # RESETS 'alarm_count' TO ZERO TO START COUNTDOWN
        tmp_mute = 0                    # SHOWS THE WARNING FOR TEMPERATURE
        hum_mute = 0                    # SHOWS THE WARNING FOR HUMIDITY
        psi_mute = 0                    # SHOWS THE WARNING FOR PRESSURE
                
for pin in [UP, DOWN, LEFT, RIGHT, A, B]:## SETUP GPIP PIN VALUES
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=button_pressed, bouncetime=500)
   
   
# 12 #    RESETTING PREVIOUS READINGS TO START CLEAN
   
        # SET PREVIOUS TEMPERATURE, HUMIDITY, & PRESSURE VALUES TO ZERO  

temp_prev = 0                           # PREVIOUS TEMPERATURE READING
temp_int = 0                            # CURRENT TEMPERATURE READING
hum_prev = 0                            # PREVIOUS HUMIDITY READING
hum_int = 0                             # CURRENT HUMIDITY READING
psi_prev = 0                            # PREVIOUS PRESSURE READING
psi_int = 0                             # CURRENT PRESSURE READING
pitch = 0                               # CURRENT PITCH (ORIENTATION) READING
roll = 0                                # CURRENT ROLL (ORIENTATION) READING
yaw = 0                                 # CURRENT YAW (ORIENTATION) READING

sec_count = 0                           # CURRENT TRIGGER READING FOR RECORDING RESULTS INTO LOG

alarm_count = 0                         # TRIGGER FOR RE-ENABLING ALARM AFTER A SET PERIOD OF TIME
alarm_timer = 0


# 13 #    NEW ASTROPI CLASS FILE TO ENSURE ORIENTATION READING IS DISPLAYED CORRECTLY

ap = AstroPi()


class AstroPiContinuous(AstroPi):
    """
    A class which continuously reads orientation data from AstroPi as without
    it the orientation data looses sync
    """
    def __init__(self,
            fb_device='/dev/fb1',
            imu_settings_file='RTIMULib',
            text_assets='astro_pi_text',
            sample_rate = 0.1):

        AstroPi.__init__(self, fb_device, imu_settings_file, text_assets)
       
        self.sample_rate = sample_rate
        self.stopped = True
        self.running = False
       
    def start(self):
        """
        starts the thread that continuously reads the astro pi orientation data
        """
        #initialise the IMU by getting the orientation
        self.get_orientation()
        #start the orientation thread
        thread.start_new_thread(self._get_orientation_threaded, ())
       
    def _get_orientation_threaded(self):
        """
        reads the orientation data every sample rate to ensure astro pi is kept in sync
        """
        self.stopped = False
        self.running = True

        #keep reading the orientation data, this keeps AstroPi in sync
        while(not self.stopped):
            self.get_orientation()
            sleep(self.sample_rate)
           
        self.running = False
   
    def stop(self):
        """
        stops the continuous read thread
        """
        self.stopped = True
        #wait for the thread to stop
        while(self.running):
            sleep(0.01)
           
    def __enter__(self):
        self.start()
        return self

    def __exit__(self, type, value, traceback):
        self.stop() 

  
# 14 #    NEW CLASS FILE TO ALLOW CPU_TEMP TO BE RECALLED AS NEEDED
        
class CPUTemp:
    def __init__(self, tempfilename = "/sys/class/thermal/thermal_zone0/temp"):
        self.tempfilename = tempfilename

    def __enter__(self):
        self.open()
        return self

    def open(self):
        self.tempfile = open(self.tempfilename, "r")
    
    def read(self):
        self.tempfile.seek(0)
        return self.tempfile.read().rstrip()

    def get_temperature(self):
        return self.get_temperature_in_c()

    def get_temperature_in_c(self):
        tempraw = self.read()
        return float(tempraw[:-3] + "." + tempraw[-3:])

    def get_temperature_in_f(self):
        return self.convert_c_to_f(self.get_temperature_in_c())
    
    def convert_c_to_f(self, c):
        return c * 9.0 / 5.0 + 32.0

    def __exit__(self, type, value, traceback):
        self.close()
            
    def close(self):
        self.tempfile.close()

        
# 15 #    CAMERA SYSTEM FOR SNAPSHOTS

def snapshot_cam():
    list_ex = ['sports'] ## TURNS OFF AUTOMATIC EXPOSURE AND SETS IT TO 'sports' ##
    list_awb =['horizon'] ## TURNS OFF AUTOMATIC WHITE BALANCE AND SETS IT TO 'horizon' ##

    photo_ev = 0 ## SET IMAGE EXPOSURE TO ZERO ##

    time.sleep(2.0) ## GIVES THE CAMERA TIME TO WARM UP ##

    with picamera.PiCamera() as camera:
        # Turn the camera's LED off
        camera.led = False
        
        # Set camera resolution for small file size
        camera.resolution = (768, 432)
  

# 16 #    MAIN PROGRAM LOOP
  
try:  

        # SETUP INITIAL MODULES FOR PROGRAM LOOP
  while running:                        ## ENSURES THAT THE SCRIPT IS ALWAYS RUNNING IN A LOOP
    #import thread                       ## ALLOWS THE SCRIPT TO IMPORT THE NEW CLASS FILE {REMOVED AS NOT COMPATIBLE WITH RASPBERRYPI B+}
    #with AstroPiContinuous() as ap:     ## FORCES SYSTEM TO USE NEW ORIENTATION CLASS FILE {REMOVED AS NOT COMPATIBLE WITH RASPBERRYPI B+}
    while(True):                    ## SCRIPT LOOP FOR DISPLAYING READINGS AND RECORDING DATA
            o = ap.get_orientation()
            pitch = o["pitch"]          # SEPARATES OUT THE PITCH SECTION FROM ORIENTATION READINGS
            roll = o["roll"]            # SEPARATES OUT THE ROLL SECTION FROM ORIENTATION READING
            yaw = o["yaw"]              # SEPARATES OUT THE YAW SECTION FROM ORIENTATION READING
            
            
        # ALLOWS THE LOG SECTION TO RECALL INFORMATION FROM THE VARIOUS SECTIONS OF THIS SCRIPT
            
            global display_f
            global temp_f
            global temp_reading_f
            global temp_alarm_f
            global hum_f
            global hum_reading_f
            global hum_alarm_f
            global psi_f
            global psi_reading_f
            global psi_alarm_f
            global snapshot_t
            global snapshot_h
            global snapshot_p
                   
        
        # SET VALUES FOR LOGGING INFORMATION
   
            if sec_count == 13:          ## ONLY WRITES THE LOGGING INFORMATION EVERY 30 SECONDS(APPROX.) 
            
            
                ## ENSURE THAT SNAPSHOT AND LOG INPUT HAVE THE SAME TIME
                
                #same_time = asctime()
                same_time = datetime.datetime.now().strftime("%d %b %y %H:%M:%S")  
   
        # SAME_TIME SWAPPED FROM ASCTIME() TO ALLOW FORMATTING WITHIN EXCEL IS CORRECT
                # RECORDED AS dd/mm/yy hh:mm:ss (DAY/MONTH/YEAR HOURS:MINUTES:SECONDS)
                
        
        # TAKE SNAPSHOT IF THE ASTROPI IS IN AN ERROR STATE - TEMPERATURE / HUMIDITY / PRESSURE
                
                if snapshot_t == 1:
                
                    print "\nTemperature Snapshot Taken"
                    
                    snapshot_cam()
                    
                    with picamera.PiCamera() as camera:
                        # Capture Image with file name to match log file
                        camera.capture('images/'+same_time+' image_temp.jpg')
                        
                elif snapshot_h == 1:
                    print "\nHumidity Snapshot Taken"
                    
                    snapshot_cam()
                    
                    with picamera.PiCamera() as camera:
                        # Capture Image with file name to match log file
                        camera.capture('images/'+same_time+' image_hum.jpg')
                        
                elif snapshot_p == 1:
                    print "\nPressure Snapshot Taken"
                    
                    snapshot_cam()
                    
                    with picamera.PiCamera() as camera:
                        # Capture Image with file name to match log file
                        camera.capture('images/'+same_time+' image_psi.jpg')
               

        # LOG ALL INFORMATION REQUIRED FOR ASTROPI
                
                print("Logged {}".format(count))  #KEEPS ASTRONAUT (Tim) UP TO DATE WITH READINGS RECORDED IF CONECTED TO A SCREEN
                file.write("\"{}\",\"{:0.2f}\",\"{:0.2f}\",\"{:0.2f}\",\"{:0.2f}\",\"{:0.2f}\",\"{:0.2f}\",\"{:0.2f}\",\"{:0.2f}\",\"{:0.2f}\",\"{:0.2f}\",\"{:0.2f}\",\"{:0.2f}\",\"{:0.2f}\",\"{:0.2f}\",\"{:0.2f}\",\"{:0.2f}\"\n".format(same_time,display_f,temp_f,tmp_reading_f,tmp_alarm_f,snapshot_t,hum_f,hum_reading_f,hum_alarm_f,snapshot_h,psi_f,psi_reading_f,psi_alarm_f,snapshot_p,pitch,roll,yaw))
                sec_count = 0 
                count+=1
                alarm_timer+=1          # ADDS 1 TO THE 'alarm_timer' TRIGGER
                
                            
        # COUNTER TO RE-ENABLE ALARMS FOR THE TEMPERATURE, HUMIDITY AND PRESSURE READINGS 
                
            if alarm_timer >= 2:        # ALARM_TIMER SET TO '2' 
                alarm_count+=1          # ONCE 'alarm_timer' EQUALS 5, ADDS ONE TO 'alarm_count',
                alarm_timer = 0         # THIS ENSURES THE TIMERS ARE CLEARED ON A BUTTON PRESS

                
        # RE-ENABLE ALARMS FOR THE TEMPERATURE, HUMIDITY AND PRESSURE READINGS 
            
            if alarm_count >= 29:       # ALARM_COUNT SET TO '29' TO RESET THE ALARMS AFTER 30mins (APPROX.) BEFORE RE-ENABLING 
                tmp_mute = 0            
                hum_mute = 0
                psi_mute = 0
                alarm_count = 0          # RESETS 'alarm_count' TO ZERO TO START COUNTDOWN AGAIN
            
            
        # CALCULATIONS FOR TEMPERATURE TO COMPENSATE FOR CPU_TEMP AFFECTING TEMPERATURE READINGS
                    
            t = ap.get_temperature()
            p = ap.get_temperature_from_pressure()
            h = ap.get_temperature_from_humidity()
            with CPUTemp() as cpu_temp:
                c = cpu_temp.get_temperature()
    
            temp_calc = ((t+p+h)/3) - (c/5)     # CALCULATION FOR CORRECTING FOR THE CPU TEMPERATURE AFFECT ON TEMPERATURE SENSORS
                                                # VERIFIED AGAINST A STANDALONE TEMPERATURE GAUGE FOR RASPBERRYPI B+ 
    
  
        # GET TEMPERATURE, HUMIDITY, & PRESSURE READINGS FROM ASTROPI SENSORS
        # also CREATES INTERGAR FOR LOGGING INFORMATION CORRECTLY ON A TABLE
 
            temp_f = temp_calc              ## STORES TEMPERATURE READING WITHIN temp_f
            temp_int = int(temp_f)          ## CREATES INTERGAR FROM TEMPERATURE READING
 
            hum_f = ap.get_humidity()       ## STORES TEMPERATURE READING WITHIN hum_f                
            hum_int = int(hum_f)            ## CREATES INTERGAR FROM HUMIDITY READING
 
            psi_f = ap.get_pressure()       ## STORES TEMPERATURE READING WITHIN psi_f
            psi_int = int(psi_f)            ##CREATES INTERGAR FROM PRESSURE READING
        
    
        # LOG IF THE DISPLAY HAS BEEN MUTED (BLACK BOX STYLE) 
    
            if led_level < 50:              # DOUBLE CHECK LED LIGHT LEVELS TO CONFIRM DISPLAY ACTIVE
                display_mute = 1
            elif led_level > 40:
                display_mute = 0
            
            if display_mute == 1:           # TRANSLATES DISPLAY MUTE TO ON AND OFF FOR LOG FILE
                display_f = 0
            elif display_mute == 0:
                display_f = 1
    
    
        # LOG THE TEMPERATURE ALARM READING AND IF IT HAS BEEN MUTED (BLACK BOX STYLE) 
    
            if tmp_mute == 1:               # TRANSLATES THE ALARM MUTE INTO ON AND OFF FOR LOG FILE
                tmp_alarm_f = 0
            elif tmp_mute == 0:
                tmp_alarm_f = 1
        
            if tmp_alarm == 2:              # TRANSLATES THE READINGS INTO HIGH, LOW AND OK FOR LOG FILE
                tmp_reading_f = 1
            elif tmp_alarm == 1:
                tmp_reading_f = -1
            elif tmp_alarm == 0:
                tmp_reading_f = 0 

                    
        # TAKE A SNAPSHOT (IMAGE) IF THE TEMPERATURE IS IN ALARM STATE (BLACK BOX STYLE)
    
            if tmp_reading_f == 1:
                snapshot_t = 1
            elif tmp_reading_f == -1:
                snapshot_t = 1
            elif tmp_alarm == 0:
                snapshot_t = 0
                
                
        # LOG THE HUMIDITY ALARM READING AND IF IT HAS BEEN MUTED (BLACK BOX STYLE)  
    
            if hum_mute == 1:               # TRANSLATES THE ALARM MUTE INTO ON AND OFF FOR LOG FILE
                hum_alarm_f = 0
            elif hum_mute == 0:
                hum_alarm_f = 1
        
            if hum_alarm == 2:              # TRANSLATES THE READINGS INTO HIGH, LOW AND OK FOR LOG FILE
                hum_reading_f = 1
            elif hum_alarm == 1:
                hum_reading_f = -1
            elif hum_alarm == 0:
                hum_reading_f = 0
    
    
        # TAKE A SNAPSHOT (IMAGE) IF THE HUMIDITY IS IN ALARM STATE (BLACK BOX STYLE)
    
            if hum_reading_f == 1:
                snapshot_h = 1
            if hum_reading_f == -1:
                snapshot_h = 1
            elif hum_alarm == 0:
                snapshot_h = 0
    
          
        # LOG THE PRESSURE ALARM READING AND IF IT HAS BEEN MUTED (BLACK BOX STYLE) 
    
            if psi_mute == 1:               # TRANSLATES THE ALARM MUTE INTO ON AND OFF FOR LOG FILE
                psi_alarm_f = 0
            elif psi_mute == 0:
                psi_alarm_f = 1
        
            if psi_alarm == 2:              # TRANSLATES THE READINGS INTO HIGH, LOW AND OK FOR LOG FILE
                psi_reading_f = 1
            elif psi_alarm == 1:
                psi_reading_f = -1
            elif psi_alarm == 0:
                psi_reading_f = 0
                                
                
        # TAKE A SNAPSHOT (IMAGE) IF THE PRESSURE IS IN ALARM STATE (BLACK BOX STYLE)
    
            if psi_reading_f == 1:
                snapshot_p = 1
            if psi_reading_f == -1:
                snapshot_p = 1
            elif psi_alarm == 0:
                snapshot_p = 0

            
        # CONVERTS TEMPERATURE, HUMIDITY, PRESSURE READINGS INTO A STRING 
        # also OVERWRITES AND STORES SENSOR READINGS WITHIN PREVIOUS READINGS

            temp_prev = temp_int            # STORE READING IN temp_prev
            temp =  str(temp_int)           # CONVERT TEMPERATURE READING TO STRING ##

            hum_prev = hum_int              # STORE READING IN hum_prev
            hum =  str(hum_int)             # CONVERT HUMIDITY READING TO STRING ##

            psi_prev = psi_int              # STORE READING IN psi_prev
            #psi =  str(psi_int)            # CONVERT PRESSURE READING TO STRING ## - REMOVED TO SOLVE <1000 PRESSURE LOCKUPS (fixed by Dave Honess 24th Aug 2015)
            psi = str(psi_int).zfill(4)     # CONVERT PRESSURE READING TO STRING ##
 
 
        # ROTATE THE LED MATRIX DISPLAY
    
            ap.set_rotation(270)           ## ROTATION ENABLED TO WORK WITH ASTROPI NASA CASE
 
 
        # WRITES VALUES ONTO THE LED MATRIX FOR THE TEMPERATURE AND HUMIDITY 
        
            ## WRITES TO TOP_LINE ONLY - TEMPERATURE (2 DIGITS)##
    
            temp_num_matrix_1(temp[0])          # FIRST DIGIT - TEMPERATURE
            temp_num_matrix_2(temp[1])          # SECOND DIGIT - TEMPERATURE
    
    
            ## WRITE TO BOTTOM_LINE ONLY - HUMIDITY (2 DIGITS)##
    
            hum_num_matrix_1(hum[0])            # FIRST DIGIT - HUMIDITY
            hum_num_matrix_2(hum[1])            # SECOND DIGIT - HUMIDITY
 
    
        # TEMPERATURE - ERROR STATE CHECKING     
    
            if temp_hum_on == 1:                # IF TEMP+HUMIDITY PAGE ACTIVE DISPLAY PREVIOUS READING FOR 5s
                time.sleep(5.0)
            elif temp_hum_on == 0:
                time.sleep(0.5)                 # IF NOT ONLY WAIT FOR 0.5s
      
            if tmp_mute == 0:                   # ONLY WORKOUT ALARM STATES FOR READINGS WITHIN TEMPERATURE IF NOT MUTED
                if temp_int - 3 > temp_prev:    # IF RISE OF 3 DEGREES BETWEEN READINGS - ALARM STATE
                    temp_num_error_high()
                    t_h_wait = 1
                    tmp_alarm = 2
        
                elif temp_int + 3 < temp_prev:  # IF FALL OF 3 DEGREES BETWEEN READING - ALARM STATE
                    temp_num_error_low()
                    t_h_wait = 1
                    tmp_alarm = 1
        
                elif temp_int > 36:             ## CHECKED AGAINST ISS REQUIREMENTS INCLUDING CPU READING
                    temp_num_error_high()
                    t_h_wait = 1
                    tmp_alarm = 2
        
                elif temp_int < 18:             ## CHECKED AGAINST ISS REQUIREMENTS INCLUDING CPU READING
                    temp_num_error_low()
                    t_h_wait = 1
                    tmp_alarm = 1
    
                else:
                    t_h_wait = 1                # IF NOTHING MATCHES WAIT ANOTHER 0.5s BEFORE MOVING FORWARD
                    tmp_alarm = 0
        
    
        ## HUMIDITY - ERROR STATE CHECKING
    
            if hum_mute == 0:                   # ONLY WORKOUT ALARM STATES FOR READINGS WITHIN HUMIDITY IF NOT MUTED
                if hum_int - 3 > hum_prev:      # IF RISE OF 3 BETWEEN READINGS - ALARM STATE
                    hum_num_error_high()
                    t_h_wait = 1
                    hum_alarm = 2
        
                elif hum_int + 3 < hum_prev:    # IF FALL OF 3 BETWEEN READINGS - ALARM STATE
                    hum_num_error_low()
                    t_h_wait = 1
                    hum_alarm = 1
        
                elif hum_int > 78:              ## CHECKED AGAINST ISS REQUIREMENTS
                    hum_num_error_high()
                    t_h_wait = 1
                    hum_alarm = 2
        
                elif hum_int < 42:              ## CHECKED AGAINST ISS REQUIREMENTS
                    hum_num_error_low()
                    t_h_wait = 1
                    hum_alarm = 1
        
                else:
                    t_h_wait = 1                # IF NOTHING MATCHES WAIT ANOTHER 0.5s BEFORE MOVING FORWARD
                    hum_alarm = 0

        
        # ALLOW ASTRONAUT (Tim) TO READ THE PREVIOUS TEMPERATURE & HUMIDITY READINGS ON THE LED MATRIX 
    
            if t_h_wait == 1:
                time.sleep(0.5)
            else:
                time.sleep(0.5)


        # WRITE TO BOTH TOP_LINE & BOTTOM_LINE - PRESSURE (4 DIGITS) 
    
            psi_num_matrix_1(psi[0])            # FIRST DIGIT - PRESSURE
            psi_num_matrix_2(psi[1])            # SECOND DIGIT - PRESSURE
            psi_num_matrix_3(psi[2])            # THIRD DIGIT - PRESSURE
            psi_num_matrix_4(psi[3])            # FOURTH DIGIT - PRESSURE
            
    
        # PRESSURE - ERROR STATE CHECKING 
    
            if psi_on == 1:                     # IF PRESSURE PAGE ACTIVE DISPLAY PREVIOUS READING FOR 5s
                time.sleep(5.0)
            elif psi_on == 0:
                time.sleep(0.5)                 # IF NOT ONLY WAIT FOR 0.5s
        
            if psi_int - 5 > psi_prev:          # ONLY WORKOUT ALARM STATES FOR READINGS WITHIN PRESSURE IF NOT MUTED
                psi_num_error_high()            # IF RISE OF 5 BETWEEN READINGS - ALARM STATE
                psi_wait = 1
                psi_alarm = 2
        
            elif psi_int + 5 < psi_prev:        # IF FALL OF 5 BETWEEN READINGS - ALARM STATE
                psi_num_error_low()
                psi_wait = 1
                psi_alarm = 1
        
            elif psi_int > 1040:                ## CHECKED AGAINST ISS REQUIREMENTS
                psi_num_error_high()
                psi_wait = 1
                psi_alarm = 2
        
            elif psi_int < 1000:                ## CHECKED AGAINST ISS REQUIREMENTS
                psi_num_error_low()
                psi_wait = 1
                psi_alarm = 1
        
            else:        
                psi_wait = 1
                psi_alarm = 0
    
    
        # ALLOW ASTRONAUT (Tim) TO READ THE PREVIOUS PRESSURE READING ON THE LED MATRIX 
    
            if psi_wait == 1:
                time.sleep(0.5)
            else:
                time.sleep(0.5)
            
            
        # RESETS THE LOGGING COUNTER & START LOOP AGAIN 

            sec_count+=1                    ## ADD 1 TO SEC_COUNT FOR LOGGING
  

# 17 #    PROGRAMMING TO CLEANLY EXIT THE PYTHON PROGRAM AND STOP RECORDING READINGS (if required)
    
finally:

        # CLEARS THE LED MATRIX ON ASTROPI 
    
    file.close()                    ## CLOSE CSV FILE TO ENSURE READINGS ARE RECORDED
    
    ap.show_letter(    " ", back_colour = [0, 0, 0])    ## SETS BACKGROUND COLOUR TO BLACK (off)
    
    ap.clear                        ## CLEARS LED MATRIX

    os.system("clear")              ## CLEARS THE SSH DISPLAY

    sys.exit()                      ## FORCES THE PYTHON PROGRAM TO EXIT
