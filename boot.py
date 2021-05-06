# This file is executed on every boot (including wake-boot from deepsleep)
import machine
import uos
import gc
import esp
esp.osdebug(None)

# uos.dupterm(None, 1) # disable REPL on UART(0)
#import webrepl
# webrepl.start()
gc.collect()
