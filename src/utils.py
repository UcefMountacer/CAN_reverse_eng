
import os
import can
# import matplotlib.pyplot as plt


def init_can():

    os.system('sudo ip link set can0 type can bitrate 500000')
    os.system('sudo ifconfig can0 up')
    print('can initialized')

def finalize_can():

    os.system('sudo ifconfig can0 down')
    print('can down')

def rcv_can_msgs(selected_id , can ):

    # start sniffing
    msg = can.recv(30.0)
    #print(msg.arbitration_id)

    # filtering
    #'''
    Id = msg.arbitration_id
    if Id == int(selected_id):
        data = msg.data
        dlc = msg.dlc
        ts = msg.timestamp

        hex_data = []
        for i in range(dlc):
            hex_data.append(data[i])

        print(hex_data)
    #'''


       
