from main import send_tcp_request
from time import sleep

send_tcp_request('M03')
sleep(5)
send_tcp_request('M05')
