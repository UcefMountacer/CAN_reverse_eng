
from src.utils import *
from matplotlib.animation import FuncAnimation
import can


def main():

    init_can()
    finalize_can()

    can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan_ctypes')

    # select id
    selected_id = input('enter selected id to be plotted in rt')

    # real time
    animation = FuncAnimation(plt.gcf() , rcv_can_msgs(selected_id, can0))
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()


    