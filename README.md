## messager
---
A lightweight, totally not-secure way to send yourself a text message (or email).
The work is done in `message.py` and you need to create _your own_ `credentials.py` file that has two variables defined in it: `gmail_usr` and `gmail_pwd` with your credentials.
We suggest using a dummy account that is not linked to any personal information. 

**THIS IS NOT A SECURE METHOD OF COMMUNICATION.** 
If you can figure out how to use the gmail API, great! get in touch and help me out, because I know that is way better. But for now, this does the job. 

Mostly it's used to send reminders and updates on remote jobs.

_Dependencies_: smtplib

---
### Usage

To use, follow the comments in `send_message.py` or the following example:

```
python send_message.py 3038675309 verizon "Hey there buddy! Your simulation results are ready for you!"

```
