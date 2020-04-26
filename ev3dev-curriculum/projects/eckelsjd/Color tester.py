import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


def main():
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title = "Tester"

    main_frame = ttk.Frame(root, width=200, height=200)
    main_frame.grid()

    color = ttk.Button(main_frame, text='color')
    color.grid(row=0, column=0)
    color['command'] = lambda: print_color(mqtt_client)

    root.mainloop()


def print_color(mqtt_client):
    mqtt_client.send_message('print_current_color')


main()
