#!/usr/bin/python
# This script allows you to send a text to (the most common) carriers.
# Usage: python sendmsg.py phone_number carrier message 
# where the last three arguments are all strings
# carrier must be 'att', 'ver', 'tmo', or 'spr' 

import sys
import message as msg
# Parse system arguments 
if len(sys.argv)==1:
    raise(ValueError('Please provide arguments. \n\tFormat: phone_number carrier message '))

phone_number = sys.argv[1]
if len(phone_number)!=10:
    raise(ValueError('phone number (1st argument) must be 10 digits.'))
    
if sys.argv[2] == 'att':
    carrier_address = '@txt.att.net'
elif sys.argv[2] == 'ver':
    carrier_address = '@vtext.com'
elif sys.argv[2] == 'tmo':
    carrier_address = '@tmomail.net'
elif sys.argv[2] == 'spr':
    carrier_address = '@messaging.sprintpcs.com'
else:
    raise(ValueError('Use valid carrier string (2nd argument): att/ver/tmo/spr'))

message = sys.argv[3]
if len(message)==0:
    raise(ValueError('message (3rd argument) must be nonempty.'))

recipient = phone_number+carrier_address
msg.send_email(recipient, message)
