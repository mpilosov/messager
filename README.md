## messager
---
A lightweight, totally not-secure way to send yourself a text message (or email).
The work is done in `message.py` and you use `send_message.py` to send the message from the command line. 

### Setup
---
_Dependencies_: smtplib

You need to create _your own_ `credentials.py` file that has two variables defined in it: `gmail_user` and `gmail_pwd` with your credentials.
We suggest using a dummy account that is not linked to any personal information. 
For example, your `credentials.py` file might be create as such from the command line:

```
echo " gmail_user, gmail_pwd = 'myusername', 'mypassword' " > credentials.py
```

### Disclaimer
---
**THIS IS NOT A SECURE METHOD OF COMMUNICATION.** 
If you can figure out how to use the Gmail API...Great! Get in touch and help me out please, because I know it is way better. But for now, this does the job. 

Mostly I use this code to send reminders and updates on remote jobs.


---
### Usage

To use, follow the comments in `send_message.py` or the following example (be aware that some characters need to be specially encoded. If you want to add support for this, please submit a PR):

```
python send_message.py 3038675309 ver "Hey there buddy. Your simulation results are ready for you."

```
