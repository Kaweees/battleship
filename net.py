import os
import socket
import sys
import time

SELF_PORT = 10001
ENEMY_HOST = 'localhost'
ENEMY_PORT = 10003

# returns coordinates of the location of enemy's shot
def get_shot_from_enemy(self_port=SELF_PORT) :
	locx = 0
	locy = 0
	ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)	
	ss.bind(('', self_port))
	ss.listen(1)
	conn, addr = ss.accept()
	data = conn.recv(2)
	locx = int(data[0])
	locy = int(data[1])
	conn.close()
	ss.close()
	return [locx, locy]

# send location of fired shot to the enemy
def send_shot_to_enemy(locx,locy,enemy_host=ENEMY_HOST,enemy_port=ENEMY_PORT) :
	cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	cs.connect((enemy_host, enemy_port))
	cs.send(str(locx)+str(locy))
	cs.close()
	return 0;

# get from enemy whether my shot was a hit 1 or a miss 0
def get_reply_from_enemy(self_port=SELF_PORT) : 
	rep = 0
	ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	ss.bind(('', self_port+1))
	ss.listen(1)
	conn, addr = ss.accept()
	data = conn.recv(1)
	rep = int(data[0])
	conn.close()
	ss.close()
	return rep 

# send to enemy whether it's shot was a hit 1 or a miss 0
def send_reply_to_enemy(reply,enemy_host=ENEMY_HOST,enemy_port=ENEMY_PORT) :
	cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	cs.connect((enemy_host, enemy_port+1))
	cs.send(str(reply))
	cs.close()
	return 0;