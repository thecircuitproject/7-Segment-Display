from machine import Pin
from time import sleep
l1 =  Pin(0,Pin.OUT)
l2 =  Pin(1,Pin.OUT)
l3 =  Pin(2,Pin.OUT)
l4 =  Pin(3,Pin.OUT)
l5 =  Pin(16,Pin.OUT)
l6 =  Pin(17,Pin.OUT)
l7 =  Pin(18,Pin.OUT)

def cero():
    l1.value(0)
    l2.value(1)
    l3.value(1)
    l4.value(1)
    l5.value(1)
    l6.value(1)
    l7.value(1)

def uno():
    l1.value(0)
    l2.value(0)
    l3.value(0)
    l4.value(1)
    l5.value(0)
    l6.value(0)
    l7.value(1)

def dos():
    l1.value(1)
    l2.value(0)
    l3.value(1)
    l4.value(1)
    l5.value(1)
    l6.value(1)
    l7.value(0)
    
def tres():
    l1.value(1)
    l2.value(0)
    l3.value(1)
    l4.value(1)
    l5.value(0)
    l6.value(1)
    l7.value(1)

def cuatro():
    l1.value(1)
    l2.value(1)
    l3.value(0)
    l4.value(1)
    l5.value(0)
    l6.value(0)
    l7.value(1)

def cinco():
    l1.value(1)
    l2.value(1)
    l3.value(1)
    l4.value(0)
    l5.value(0)
    l6.value(1)
    l7.value(1)

def seis():
    l1.value(1)
    l2.value(1)
    l3.value(1)
    l4.value(0)
    l5.value(1)
    l6.value(1)
    l7.value(1)
    
def siete():
    l1.value(0)
    l2.value(0)
    l3.value(1)
    l4.value(1)
    l5.value(0)
    l6.value(0)
    l7.value(1)

def ocho():
    l1.value(1)
    l2.value(1)
    l3.value(1)
    l4.value(1)
    l5.value(1)
    l6.value(1)
    l7.value(1)

def nueve():
    l1.value(1)
    l2.value(1)
    l3.value(1)
    l4.value(1)
    l5.value(0)
    l6.value(0)
    l7.value(1)
    
def main():
    while True:
        cero()
        sleep(1)
        uno()
        sleep(1)
        dos()
        sleep(1)
        tres()
        sleep(1)
        cuatro()
        sleep(1)
        cinco()
        sleep(1)
        seis()
        sleep(1)
        siete()
        sleep(1)
        ocho()
        sleep(1)
        nueve()
        sleep(1)
main()