
from src.utils import *
from matplotlib.animation import FuncAnimation
import can
import pandas as pd


def main():

    init_can()

    can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')

    # select id
    selected_id = input('enter selected id to be plotted in rt')

    rcv_can_msgs(selected_id, can0)



if __name__ == "__main__":
    main()


    