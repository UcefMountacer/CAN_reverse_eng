
from src.utils import *
from matplotlib.animation import FuncAnimation
import can
import pandas as pd

def animate(i):

    # start sniffing
    msg = can0.recv(30.0)

    # filtering
    Id = msg.arbitration_id
    if Id == selected_id:
        data = msg.data
        dlc = msg.dlc
        ts = msg.timestamp

        hex_data = []
        for i in range(dlc):
            hex_data.append(data[i])

        plt.cla()
        for i in range(dlc):
            plt.plot(ts, hex_data[i])


def main():

    init_can()

    global can0
    can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')

    # select id
    global selected_id
    selected_id = input('enter selected id to be plotted in rt')

    anim = FuncAnimation(plt.gcf() , animate)



if __name__ == "__main__":
    main()


    