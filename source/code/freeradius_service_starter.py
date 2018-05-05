#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import time

freeradius_service_settings_ico = """
#########################################################
#           FREERADIUS SERVICE LAUNCHER T00L            #
#########################################################
#                       C0NTACT                         #
#########################################################
#              DEVELOPER : İSMAİL TAŞDELEN              #
#        Mail Address : pentestdatabase@gmail.com       #
# LINKEDIN : https://www.linkedin.com/in/ismailtasdelen #
#       GitHub : https://github.com/ismailtasdelen/     #
#########################################################
"""

print freeradius_service_settings_ico

freeradius_service_launcher_settings_ico = """
(1) FreeRADIUS Service Start
(2) FreeRADIUS Service Restart
(3) FreeRADIUS Service Stop
"""

print freeradius_service_launcher_settings_ico

def freeradius_service():
	islem = input("Yapmak istediğiniz işlem numarasını giriniz : ")
	if islem == 1:
		os.system("service" + " " + "freeradius" + " " + "start")
	if islem == 2:
		os.system("service" + " " + "freeradius" + " " + "restart")
	if islem == 3:
		os.system("service" + " " + "freeradius" + " " + "stop")

freeradius_service()
