import time
from plyer import notification

def lembrete_beber_agua(intervalo_minutos=1):
    while True:
        notification.notify(
        title = "bebe agua",
        message = "não esqueça!",
        timeout = 10
        )
        time.sleep(intervalo_minutos*60)
lembrete_beber_agua()