#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from gopigo import *
import sys
import time
import easygopigo3 as easy
import random
#Move the GoPiGo forward
def fwd(dist=0): #distance is in cm
	"""
	Starts moving the GoPiGo forward at the currently set motor speeds.
	Takes an optional parameter to indicate a specific distance to move
	forward. If not given, negative, or zero then it will move forward until
	another direction or stop function is called.
	Returns -1 if the action fails.
	:param int dist: The distance in cm to move forward.
	:return: A value indicating if the action suceeded.
	:rtype: int
	"""
	try:
		if dist>0:
			# this casting to int doesn't seem necessary
			pulse=int(PPR*(dist//WHEEL_CIRC) )
			enc_tgt(1,1,pulse)
	except Exception as e:
		print ("gopigo fwd: {}".format(e))
		pass
	return write_i2c_block(motor_fwd_cmd, [0,0,0])


#Move GoPiGo back
def bwd(dist=0):
	"""
	Starts moving the GoPiGo backward at the currently set motor speeds.
	Takes an optional parameter to indicate a specific distance to move
	backward. If not given, negative, or zero then it will move backward
	until another direction or stop function is called.
	Returns -1 if the action fails.
	:param int dist: The distance in cm to move backward.
	:return: A value indicating if the action suceeded.
	:rtype: int
	"""
	try:
		if dist>0:
			# this casting to int doesn't seem necessary
			pulse=int(PPR*(dist//WHEEL_CIRC) )
			enc_tgt(1,1,pulse)
	except Exception as e:
		print ("gopigo bwd: {}".format(e))
		pass
	return write_i2c_block(motor_bwd_cmd, [0,0,0])


#Turn GoPiGo Left slow (one motor off, better control)
def left():
	return write_i2c_block(left_cmd, [0,0,0])


#Turn GoPiGo right slow (one motor off, better control)
def right():
	return write_i2c_block(right_cmd, [0,0,0])


#Stop the GoPiGo
def stop():
	"""
	Brings the GoPiGo to a full stop.
	Returns -1 if the action fails.
	:return: A value indicating if the action suceeded.
	:rtype: int
	"""
	return write_i2c_block(stop_cmd, [0,0,0])


#Increase the speed
def increase_speed():
	return write_i2c_block(ispd_cmd, [0,0,0])

#Decrease the speed
def decrease_speed():
	return write_i2c_block(dspd_cmd, [0,0,0])


#Set speed of the both motors
#	arg:
#		speed-> 0-255
def set_speed(speed):
	"""
	Sets the speed of the left and right motors to the given speed. The speed
	should be in the range of [0, 255].
	Sleeps for 0.1 seconds in between setting the left and right motor speeds.
	:param int speed: The speed to set the motors to. [0, 255]
	"""
	if speed >255:
		speed =255
	elif speed <0:
		speed =0
	set_left_speed(speed)
	time.sleep(.1)
	set_right_speed(speed)
    
    
def meet_object():
    stop()
    randNum = randint(0,1)
    if(randNum == 0):
        right()
    else:
        left()
    time.sleep(.1)

# In[ ]:


#Temp
DPR = 360.0/64
# turn x degrees to the right
def turn_right(degrees):
	pulse = int(degrees//DPR)
	enc_tgt(1,0,pulse)
	right()

def turn_right_wait_for_completion(degrees):
	'''
	Same as turn_right() but blocking
	'''
	turn_right(degrees)
	pulse = int(degrees//DPR)
	while enc_read(0) < pulse:
		pass


# turn x degrees to the left
def turn_left(degrees):
	pulse = int(degrees//DPR)
	enc_tgt(0,1,pulse)
	left()

def turn_left_wait_for_completion(degrees):
	'''
	same as turn_left() but blocking.
	'''
	turn_left(degrees)
	pulse = int(degrees//DPR)
	while enc_read(1) < pulse:
		pass




#Move robot through the room
def move_through_room():
    distance_to_stop = 20 #So if robot is 20cm away from object it stops
    walld_distance_sensor = gpg.init_distance_sensor()
    
    fwd()                 #otherwise move forward
    while True:
        currentDistance = int(walld_distance_sensor.read())
        if currentDistance < distance_to_stop:
            time.sleep(.5)
            meet_object()






