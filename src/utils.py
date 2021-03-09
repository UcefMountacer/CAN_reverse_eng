
import os
import can
import matplotlib.pyplot as plt

def init_can():

    os.system('sudo ip link set can0 type can bitrate 500000')
    os.system('sudo ifconfig can0 up')
    print('can initialized')

def finalize_can():

    os.system('sudo ifconfig can0 down')
    print('can down')

def plot_can_id(msg):



def rcv_can_msgs(selected_id, chan = 'can0')

    '''
    ids = [{"can_id": 0x11, "can_mask": 0x21, "extended": False}] format
    '''

    can0 = can.interface.Bus(channel = chan, bustype = 'socketcan_ctypes')
    while True:

        # start sniffing
        msg = can0.recv(30.0)

        # filtering
        Id = msg.arbitration_id
        if Id = selected_id:
            data = msg.data
            dlc = msg.dlc
            ts = msg.timestamp

            hex_data = []
            for i in dlc:
                hex_data.append(data[i])

                # plot
                plt.scatter(ts , tuple(hex_data))
                plt.pause(0.05)


            

            







        


    
    
       
