from kivy.uix.togglebutton import ToggleButton
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.switch import Switch
from kivy.uix.stacklayout import StackLayout
import asyncio
import serial_asyncio
from kivy.graphics.vertex_instructions import Point
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.graphics import Rotate, Ellipse, Color
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse, Line
from kivy.properties import NumericProperty
Window.size = (1920, 1080)

n = '30'
n1 = '15'
n2 = '20'
n3 = '25'
n4 = '30'
n5 = '35'
n6 = '40'
n7 = '45'
n8 = '50'
n9 = '55'
n10 = '60'
n11 = '65'
n12 = '70'
n13 = '75'
n14 = '80'
n15 = '85'
n16 = '90'
n17 = '95'
n18 = '100'
n19 = '105'
n20 = '110'
n21 = '115'
n22 = '120'

class Speedometer(Widget):
    speed = NumericProperty(10)

    def on_size(self, *args):
        self.on_speed(self, self.speed)  # Update the speedometer when the size changes

    def on_speed(self, instance, value):
        self.canvas.clear()
        with self.canvas:
            Color(1, 1, 1, 1)
            size = min(self.width, self.height) * 0.15
            Ellipse(pos=(self.center_x - size / 2, self.center_y - size / 2), size=(size, size))

            # Плавный переход цветов
            if value <= 76:
                color = self.interpolate_color((1, 0, 0), (1, 0.65, 0), value / 76)
            elif value <= 153:
                color = self.interpolate_color((1, 0.65, 0), (1, 1, 0), (value - 76) / (153 - 76))
            elif value <= 204:
                color = self.interpolate_color((1, 1, 0), (0, 1, 0), (value - 153) / (204 - 153))
            else:
                color = (0, 1, 0)

            Color(*color, 1)
            angle = (value / 255) * 360
            Line(circle=(self.center_x, self.center_y, size / 2, 0, angle), width=5)
    def interpolate_color(self, start_color, end_color, factor):
        """Интерполяция между двумя цветами."""
        return tuple(start + (end - start) * factor for start, end in zip(start_color, end_color))

class SerialReader(asyncio.Protocol):
    def __init__(self, text_input_l, text_input_w,speedometer):  # переменные
        self.text_input_l = text_input_l  # переменные
        self.text_input_w = text_input_w
        self.speedometer = speedometer
        # переменные
        self.buffer = ""
        self.data_list = []

    def connection_made(self, transport):
        self.transport = transport
        print("Connection established")

    def data_received(self, data):
        self.buffer += data.decode('utf-8', errors='ignore')
        lines = self.buffer.splitlines(keepends=True)
        self.buffer = lines.pop()
        for line in lines:
            print(f"{line.strip()}")
            self.check_for_data(line.strip())

    def check_for_data(self, line):
        if "ID: 0x00000000;" in line:
            start_index = line.find("Data:") + len("Data:")
            end_index = line.find(";", start_index)
            if end_index != -1:
                data = line[start_index:end_index].strip()
                while len(self.data_list) <= 0:
                    self.data_list.append(None)
                self.data_list[0] = data


        if "ID: 0x81010001;" in line:
            start_index = line.find("Data:") + len("Data:")
            end_index = line.find(";", start_index)
            if end_index != -1:
                data = line[start_index:end_index].strip()
                while len(self.data_list) <= 1:
                    self.data_list.append(None)
                self.data_list[1] = data

                m = self.data_list[1]
                l = m[6:8]
                q = self.data_list[1]
                w = q[4:6]
                self.update_text_input(l, w)

        if "ID: 0x81020001;" in line:
            start_index = line.find("Data:") + len("Data:")
            end_index = line.find(";", start_index)
            if end_index != -1:
                data = line[start_index:end_index].strip()
                while len(self.data_list) <= 2:
                    self.data_list.append(None)
                self.data_list[2] = data

        if "ID: 0x81030001;" in line:
            start_index = line.find("Data:") + len("Data:")
            end_index = line.find(";", start_index)
            if end_index != -1:
                data = line[start_index:end_index].strip()
                while len(self.data_list) <= 3:
                    self.data_list.append(None)
                self.data_list[3] = data

        if "ID: 0x81040001;" in line:
            start_index = line.find("Data:") + len("Data:")
            end_index = line.find(";", start_index)
            if end_index != -1:
                data = line[start_index:end_index].strip()
                while len(self.data_list) <= 4:
                    self.data_list.append(None)
                self.data_list[4] = data

        if "ID: 0x81050001;" in line:
            start_index = line.find("Data:") + len("Data:")
            end_index = line.find(";", start_index)
            if end_index != -1:
                data = line[start_index:end_index].strip()
                while len(self.data_list) <= 5:
                    self.data_list.append(None)
                self.data_list[5] = data

        if "ID: 0x81060001;" in line:
            start_index = line.find("Data:") + len("Data:")
            end_index = line.find(";", start_index)
            if end_index != -1:
                data = line[start_index:end_index].strip()
                while len(self.data_list) <= 6:
                    self.data_list.append(None)
                self.data_list[6] = data

        if "ID: 0x81070001;" in line:
            start_index = line.find("Data:") + len("Data:")
            end_index = line.find(";", start_index)
            if end_index != -1:
                data = line[start_index:end_index].strip()
                while len(self.data_list) <= 7:
                    self.data_list.append(None)
                self.data_list[7] = data

        if "ID: 0x81080001;" in line:
            start_index = line.find("Data:") + len("Data:")
            end_index = line.find(";", start_index)
            if end_index != -1:
                data = line[start_index:end_index].strip()
                while len(self.data_list) <= 8:
                    self.data_list.append(None)
                self.data_list[8] = data

        if "ID: 0x81090001;" in line:
            start_index = line.find("Data:") + len("Data:")
            end_index = line.find(";", start_index)
            if end_index != -1:
                data = line[start_index:end_index].strip()
                while len(self.data_list) <= 9:
                    self.data_list.append(None)
                self.data_list[9] = data

        if "ID: 0x810A0001;" in line:
            start_index = line.find("Data:") + len("Data:")
            end_index = line.find(";", start_index)
            if end_index != -1:
                data = line[start_index:end_index].strip()
                while len(self.data_list) <= 10:
                    self.data_list.append(None)
                self.data_list[10] = data

        if "ID: 0x810B0001;" in line:
            start_index = line.find("Data:") + len("Data:")
            end_index = line.find(";", start_index)
            if end_index != -1:
                data = line[start_index:end_index].strip()
                while len(self.data_list) <= 11:
                    self.data_list.append(None)
                self.data_list[11] = data

        if "ID: 0x810C0001;" in line:
            start_index = line.find("Data:") + len("Data:")
            end_index = line.find(";", start_index)
            if end_index != -1:
                data = line[start_index:end_index].strip()
                while len(self.data_list) <= 12:
                    self.data_list.append(None)
                self.data_list[12] = data

        if "ID: 0x810D0001;" in line:
            start_index = line.find("Data:") + len("Data:")
            end_index = line.find(";", start_index)
            if end_index != -1:
                data = line[start_index:end_index].strip()
                while len(self.data_list) <= 13:
                    self.data_list.append(None)
                self.data_list[13] = data

        if "ID: 0x810E0001;" in line:
            start_index = line.find("Data:") + len("Data:")
            end_index = line.find(";", start_index)
            if end_index != -1:
                data = line[start_index:end_index].strip()
                while len(self.data_list) <= 14:
                    self.data_list.append(None)
                self.data_list[14] = data
        if "ID: 0x810F0001;" in line:
            start_index = line.find("Data:") + len("Data:")
            end_index = line.find(";", start_index)
            if end_index != -1:
                data = line[start_index:end_index].strip()
                while len(self.data_list) <= 15:
                    self.data_list.append(None)
                self.data_list[15] = data
                print(f"Current data list: {self.data_list}")
                self.data_list.clear()
                print(f"Current data list: {self.data_list}")

    def update_text_input(self, l, w):  # переменные
        try:
            # Преобразование из шестнадцатеричного в десятичное
            decimal_l = str(int(l, 16))  # переменные
            decimal_w = str(int(w, 16))  # переменные

            # Обновление текстовых полей
            self.text_input_l.text = decimal_l  # переменные
            self.text_input_w.text = decimal_w  # переменные
            self.speedometer.speed = int(decimal_l)
        except ValueError:
            self.text_input_l.text = "Ошибка преобразования"  # переменные
            self.text_input_w.text = "Ошибка преобразования"  # переменные

    def connection_lost(self, exc):
        print("Connection lost")
class MyApp(App):

    def build(self):
        tb = TabbedPanel(do_default_tab=True, tab_pos="top_left", default_tab_text="Status CAN",tab_width=200 )

        tbi = TabbedPanelItem(text="Data monitoring",font_size=15)
        fl = FloatLayout()

        fl.add_widget(Image(source="img/fon.jpg", x=0, y=90))
        fl.add_widget(Image(source="img/fon2.jpg", x=0, y=-300))
        fl.add_widget(Image(source="img/moto.jpg", x=-500, y=250))
        fl.add_widget(Image(source="img/strelka.jpg", x=-500, y=180))
        fl.add_widget(Image(source="img/moto.jpg", x=200, y=250))
        fl.add_widget(Image(source="img/strelka.jpg", x=200, y=180))
        fl.add_widget(Image(source="img/zn.jpg", x=750, y=420))


        fl.add_widget(Label(
            text='SumVolt,V:', color=[0, 1, 0, 1],
            font_size=40, bold=True, x=-500, y=380))
        fl.add_widget(Label(
            text='Curr,A:', color=[0, 1, 0, 1],
            font_size=40, bold=True, x=200, y=380))
        fl.add_widget(Label(
            text='SOC%:', color=[0, 1, 0, 1],
            font_size=40, bold=True, x=-150, y=380))

        fl.add_widget(Label(#Max Volt
            text='Max Volt: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-900, y=50))
        fl.add_widget(Label(
            text=n +' V', color=[0, 1, 0, 1],
            font_size=15, bold=True, x=-850, y=50))

        fl.add_widget(Label(#Min Volt
            text='Min Volt: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-900, y=25))
        fl.add_widget(Label(
            text=n2 +' V', color=[0, 1, 0, 1],
            font_size=15, bold=True, x=-850, y=25))

        fl.add_widget(Label(#Cell num
            text='Cell num: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-900, y=0))
        fl.add_widget(Label(
            text=n3, color=[0, 1, 0, 1],
            font_size=15, bold=True, x=-850, y=0))

        fl.add_widget(Label(#DI1 status:
            text='DI1 status: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-900, y=-25))
        fl.add_widget(Label(
            text=n4, color=[0, 1, 0, 1],
            font_size=15, bold=True, x=-850, y=-25))

        fl.add_widget(Label(#DO1 status:
            text='DO1 status: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-900, y=-50))
        fl.add_widget(Label(
            text=n5, color=[0, 1, 0, 1],
            font_size=15, bold=True, x=-850, y=-50))

        fl.add_widget(Label(#Max Cell Pos:
            text='Max Cell Pos: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-760, y=50))
        fl.add_widget(Label(
            text=n6, color=[0, 1, 0, 1],
            font_size=15, bold=True, x=-700, y=50))

        fl.add_widget(Label(#Min Cell Pos:
            text='Min Cell Pos: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-760, y=25))
        fl.add_widget(Label(
            text=n7, color=[0, 1, 0, 1],
            font_size=15, bold=True, x=-700, y=25))

        fl.add_widget(Label(#NTC num:
            text='NTC num: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-760, y=0))
        fl.add_widget(Label(
            text=n8, color=[0, 1, 0, 1],
            font_size=15, bold=True, x=-700, y=0))

        fl.add_widget(Label(#DI2 status:
            text='DI2 status: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-760, y=-25))
        fl.add_widget(Label(
            text=n9, color=[0, 1, 0, 1],
            font_size=15, bold=True, x=-700, y=-25))

        fl.add_widget(Label(#DO2 status:
            text='DO2 status: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-760, y=-50))
        fl.add_widget(Label(
            text=n10, color=[0, 1, 0, 1],
            font_size=15, bold=True, x=-700, y=-50))

        fl.add_widget(Label(#Max Temp:
            text='Max Temp: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-620, y=50))
        fl.add_widget(Label(
            text=n11+'°C', color=[0, 1, 0, 1],
            font_size=15, bold=True, x=-560, y=50))

        fl.add_widget(Label(#Min Temp:
            text='Min Temp: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-620, y=25))
        fl.add_widget(Label(
            text=n12+'°C', color=[0, 1, 0, 1],
            font_size=15, bold=True, x=-560, y=25))

        fl.add_widget(Label(#Remain cap:
            text='Remain cap: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-620, y=0))
        fl.add_widget(Label(
            text=n13+'Ah', color=[0, 1, 0, 1],
            font_size=15, bold=True, x=-560, y=0))

        fl.add_widget(Label(#DI3 status:
            text='DI3 status: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-620, y=-25))
        fl.add_widget(Label(
            text=n14, color=[0, 1, 0, 1],
            font_size=15, bold=True, x=-560, y=-25))

        fl.add_widget(Label(#DO3 status:
            text='DO3 status: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-620, y=-50))
        fl.add_widget(Label(
            text=n15, color=[0, 1, 0, 1],
            font_size=15, bold=True, x=-560, y=-50))

        fl.add_widget(Label(#Max Temp Pos:
            text='Max Temp Pos: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-480, y=50))
        fl.add_widget(Label(
            text=n16, color=[0, 1, 0, 1],
            font_size=15, bold=True, x=-420, y=50))

        fl.add_widget(Label(#Min Temp Pos:
            text='Min Temp Pos: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-480, y=25))
        fl.add_widget(Label(
            text=n17, color=[0, 1, 0, 1],
            font_size=15, bold=True, x=-420, y=25))

        fl.add_widget(Label(#BMS Life:
            text='BMS Life: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-480, y=0))
        fl.add_widget(Label(
            text=n18, color=[0, 1, 0, 1],
            font_size=15, bold=True, x=-420, y=0))

        fl.add_widget(Label(#DI4 status:
            text='DI4 status: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-480, y=-25))
        fl.add_widget(Label(
            text=n19, color=[0, 1, 0, 1],
            font_size=15, bold=True, x=-420, y=-25))


        fl.add_widget(Label(#DO4 status:
            text='DO4 status: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-480, y=-50))
        fl.add_widget(Label(
            text=n20, color=[0, 1, 0, 1],
            font_size=15, bold=True, x=-420, y=-50))

        fl.add_widget(Label(#Relay Switch:
            text='Relay Switch: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-340, y=-25))
        fl.add_widget(Label(
            text=n1 + ' : ' + n2, color=[0, 1, 0, 1],
            font_size=15, bold=True, x=-275, y=-25))

        fl.add_widget(Label(#Cycle Times:
            text='Cycle Times: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-340, y=-50))
        fl.add_widget(Label(
            text=n1, color=[0, 1, 0, 1],
            font_size=15, bold=True, x=-280, y=-50))

        fl.add_widget(Label(#:Battery Status
            text='Battery Status: ', color=[1, 1, 1, 1],
            font_size=35, bold=True, x=-800, y=80))

        fl.add_widget(Label(#:Cell Voltage
            text='Cell: ', color=[1, 1, 1, 1],
            font_size=20, bold=True, x=-850, y=-150))

        fl.add_widget(Label(#:TEMP1
            text='Temp: ', color=[1, 1, 1, 1],
            font_size=20, bold=True, x=-850, y=-270))

        fl.add_widget(Label(#:Battery Status
            text='Block1: ', color=[1, 1, 1, 1],
            font_size=35, bold=True, x=-850, y=-100))


        fl.add_widget(Label(#:Cell Voltage
            text='Cell: ', color=[1, 1, 1, 1],
            font_size=20, bold=True, x=-50, y=-150))

        fl.add_widget(Label(#:TEMP1
            text='Temp: ', color=[1, 1, 1, 1],
            font_size=20, bold=True, x=-50, y=-270))

        fl.add_widget(Label(#:Battery Status
            text='Block2: ', color=[1, 1, 1, 1],
            font_size=35, bold=True, x=-50, y=-100))




        gl1=GridLayout(cols=8, row_force_default=True, row_default_height=40, spacing=0, x=50, y=-650)
        gl1.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl1.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl1.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl1.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl1.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl1.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl1.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl1.add_widget(TextInput(text='', size_hint_x=None, width=80))

        gl1.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl1.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl1.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl1.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl1.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl1.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl1.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl1.add_widget(TextInput(text='', size_hint_x=None, width=80))
        self.text_input_l = TextInput(size_hint=(0.1, 0.1), font_size='20sp', multiline=True, readonly=True) #переменные
        self.text_input_w = TextInput(size_hint=(0.1, 0.1), font_size='20sp', multiline=True, readonly=True) #переменные
        self.text_input_l.pos_hint = {'x': 0.1, 'y': 0.8}
        self.text_input_w.pos_hint = {'x': 0.1, 'y': 0.5}
        fl.add_widget(self.text_input_l)
        fl.add_widget(self.text_input_w)
        self.speedometer = Speedometer()
        self.speedometer.pos_hint = {'center_x': 0.425, 'center_y': 0.75}
        fl.add_widget(self.speedometer)
        # fl1.add_widget(TextInput(text="",
        #                         multiline=False,
        #                         readonly=False,
        #                         font_size=10,
        #                         padding=10,
        #                         size_hint=(0.05, 0.03),
        #                         x = 200, y = 550))
        # x = str((float(self.text_input_l)/2.55))
        # fl.add_widget(Label(
        #     text=x, color=[0, 1, 0, 1],
        #     font_size=40, bold=True, x=-500, y=380))

        gl2 = GridLayout(cols=3, row_force_default=True, row_default_height=40, spacing=0, x=50, y=-770)
        gl2.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl2.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl2.add_widget(TextInput(text='', size_hint_x=None, width=80))


        gl3=GridLayout(cols=8, row_force_default=True, row_default_height=40, spacing=0, x=850, y=-650)
        gl3.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl3.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl3.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl3.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl3.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl3.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl3.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl3.add_widget(TextInput(text='', size_hint_x=None, width=80))

        gl3.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl3.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl3.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl3.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl3.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl3.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl3.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl3.add_widget(TextInput(text='', size_hint_x=None, width=80))

        gl4 = GridLayout(cols=3, row_force_default=True, row_default_height=40, spacing=0, x=850, y=-770)
        gl4.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl4.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl4.add_widget(TextInput(text='', size_hint_x=None, width=80))

        main_layout = StackLayout()
        lbl = Label(text="OFF",font_size=30, bold=True, size_hint=(0.25, 0.075),color=[0, 0, 0, 1])
        main_layout.add_widget(lbl)
        switch = Switch(size_hint=(0.1, 0.055), active=True)
        def on_active(instance, value):
            if value:
                lbl.text = "OFF"
            else:
                lbl.text = "ON"
        switch.bind(active=on_active)
        main_layout.add_widget(switch)

        fl.add_widget(Label(#:Cell Voltage
            text='Status BMS: ', color=[0, 0, 0, 1],
            font_size=30, bold=True, x=-850, y=450))




        fl.add_widget(main_layout)

        fl.add_widget(gl4)
        fl.add_widget(gl3)
        fl.add_widget(gl2)
        fl.add_widget(gl1)

        tbi.add_widget(fl)
        tb.add_widget(tbi)
        # tbi.add_widget(layout)
        # tb.add_widget(tbi)





        tbi2 = TabbedPanelItem(text="Parameter settings",font_size=15)
        fl1 = FloatLayout()

        fl1.add_widget(Image(source="img/fon.jpg", x=0, y=90))
        fl1.add_widget(Image(source="img/fon2.jpg", x=0, y=-300))
        fl1.add_widget(Image(source="img/moto.jpg", x=-500, y=250))
        fl1.add_widget(Image(source="img/strelka.jpg", x=-500, y=180))
        fl1.add_widget(Image(source="img/moto.jpg", x=200, y=250))
        fl1.add_widget(Image(source="img/strelka.jpg", x=200, y=180))
        fl1.add_widget(Image(source="img/zn.jpg", x=750, y=420))
        if n == '10':
            fl1.add_widget(Image(source="img/battery1.jpg", x=-150, y=270))
        if n == '20':
            fl1.add_widget(Image(source="img/battery2.jpg", x=-150, y=270))
        if n == '30':
            fl1.add_widget(Image(source="img/battery3.jpg", x=-150, y=270))
        if n == '40':
            fl1.add_widget(Image(source="img/battery4.jpg", x=-150, y=270))
        if n == '50':
            fl1.add_widget(Image(source="img/battery5.jpg", x=-150, y=270))

        fl1.add_widget(Label(
            text='SumVolt,V:', color=[0, 1, 0, 1],
            font_size=40, bold=True, x=-500, y=380))
        fl1.add_widget(Label(
            text='Curr,A:', color=[0, 1, 0, 1],
            font_size=40, bold=True, x=200, y=380))
        fl1.add_widget(Label(
            text='SOC%:', color=[0, 1, 0, 1],
            font_size=40, bold=True, x=-150, y=380))
        #////////////////////////////////////////////////////////
        fl1.add_widget(TextInput(text="",
                                multiline=False,
                                readonly=False,
                                font_size=10,
                                padding=10,
                                size_hint=(0.05, 0.03),
                                x = 200, y = 550))
        fl1.add_widget(TextInput(text="",
                                multiline=False,
                                readonly=False,
                                font_size=10,
                                padding=10,
                                size_hint=(0.05, 0.03),
                                x = 200, y = 520))
        fl1.add_widget(TextInput(text="",
                                multiline=False,
                                readonly=False,
                                font_size=10,
                                padding=10,
                                size_hint=(0.05, 0.03),
                                x = 200, y = 480))
        fl1.add_widget(TextInput(text="",
                                multiline=False,
                                readonly=False,
                                font_size=10,
                                padding=10,
                                size_hint=(0.05, 0.03),
                                x = 200, y = 450))
        fl1.add_widget(TextInput(text="",
                                multiline=False,
                                readonly=False,
                                font_size=10,
                                padding=10,
                                size_hint=(0.05, 0.03),
                                x = 200, y = 390))
        fl1.add_widget(Label(#:Battery Status
            text='Rated Cap(Ah): ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-850, y=80))
        fl1.add_widget(Label(#:Battery Status
            text='Rated CellVolt(V): ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-850, y=50))
        fl1.add_widget(Label(#:Battery Status
            text='Cumulative charge(Ah): ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-850, y=10))
        fl1.add_widget(Label(#:Battery Status
            text='Cumulative discharge(Ah): ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-850, y=-20))
        fl1.add_widget(Label(#:Battery Status
            text='NO. of acquisition board: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-850, y=-80))

        fl1.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.05, 0.03),
                                 x=600, y=550))
        fl1.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.05, 0.03),
                                 x=600, y=520))
        fl1.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.05, 0.03),
                                 x=600, y=480))
        fl1.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.05, 0.03),
                                 x=600, y=450))
        fl1.add_widget(Label(  #:Battery Status
            text='Balance start Volt(V): ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-450, y=80))
        fl1.add_widget(Label(  #:Battery Status
            text='Bal start diff Volt(V): ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-450, y=50))
        fl1.add_widget(Label(  #:Battery Status
            text='Short Current(A): ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-450, y=10))
        fl1.add_widget(Label(  #:Battery Status
            text='Cur sampling Res(mΩ): ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-450, y=-20))
        gl8 = GridLayout(cols=3, row_force_default=True, row_default_height=30, spacing=0, x=456, y=-540)
        gl8.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl8.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl8.add_widget(TextInput(text='', size_hint_x=None, width=80))

        gl9 = GridLayout(cols=3, row_force_default=True, row_default_height=30, spacing=0, x=456, y=-575)
        gl9.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl9.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl9.add_widget(TextInput(text='', size_hint_x=None, width=80))

        fl1.add_widget(Label(  #:Battery Status
            text='Board 1~3 Cell No.: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-580, y=-70))
        fl1.add_widget(Label(  #:Battery Status
            text='Board 1~3 NTC No.: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-580, y=-100))


        fl1.add_widget(Button(text="Set",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.035,
                          size_hint_y=0.025,
                          x=300, y=535))
        fl1.add_widget(Button(text="Set",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.035,
                          size_hint_y=0.025,
                          x=300, y=465))
        fl1.add_widget(Button(text="Set",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.035,
                          size_hint_y=0.025,
                          x=700, y=465))
        fl1.add_widget(Button(text="Set",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.035,
                          size_hint_y=0.025,
                          x=700, y=535))
        fl1.add_widget(Button(text="Set",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.035,
                          size_hint_y=0.025,
                          x=700, y=385))

        fl1.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.05, 0.03),
                                 x=200, y=310))
        fl1.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.05, 0.03),
                                 x=200, y=270))
        fl1.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.05, 0.03),
                                 x=200, y=230))
        fl1.add_widget(Label(  #:Battery Status
            text='Sleep time(S): ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-850, y=-160))
        fl1.add_widget(Label(  #:Battery Status
            text='Current wave(A): ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-850, y=-200))
        fl1.add_widget(Label(  #:Battery Status
            text='Battery type: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-850, y=-240))
        fl1.add_widget(Label(  #:Battery Status
            text='Battery production date: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-850, y=-280))
        fl1.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.1, 0.03),
                                 x=200, y=190))
        fl1.add_widget(Label(  #:Battery Status
            text='Battery operation mode: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-850, y=-320))
        fl1.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.07, 0.03),
                                 x=200, y=150))
        fl1.add_widget(Button(text="Set",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.035,
                          size_hint_y=0.025,
                          x=350, y=150))
        fl1.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.2, 0.03),
                                 x=940, y=550))
        fl1.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.2, 0.03),
                                 x=940, y=510))
        fl1.add_widget(Label(  #:Battery Status
            text='Firmware index No: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-100, y=80))
        fl1.add_widget(Label(  #:Battery Status
            text='Battery code: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-100, y=40))
        fl1.add_widget(Button(text="Set",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.035,
                          size_hint_y=0.025,
                          x=1328, y=553))
        fl1.add_widget(Button(text="Set",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.035,
                          size_hint_y=0.025,
                          x=1328, y=513))
        fl1.add_widget(Label(  #:Battery Status
            text='RTC: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=480, y=80))
        fl1.add_widget(Label(  #:Battery Status
            text='IP: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=480, y=40))
        fl1.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.15, 0.03),
                                 x=1480, y=510))
        fl1.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.15, 0.03),
                                 x=1480, y=550))
        fl1.add_widget(Button(text="Set",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.035,
                          size_hint_y=0.025,
                          x=1772, y=513))
        fl1.add_widget(Button(text="Set",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.035,
                          size_hint_y=0.025,
                          x=1772, y=553))

        fl1.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.15, 0.03),
                                 x=940, y=450))
        fl1.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.15, 0.03),
                                 x=940, y=410))
        fl1.add_widget(Label(  #:Battery Status
            text='BMS SW version: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-100, y=-20))
        fl1.add_widget(Label(  #:Battery Status
            text='WNT SW version: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-100, y=-60))
        fl1.add_widget(Button(text="Set",
                              italic=True, bold=True,
                              font_size=15, color=[0, 0, 0, 1],
                              background_color=[1, 1, 1, 1],
                              background_normal="",
                              size_hint_x=0.035,
                              size_hint_y=0.025,
                              x=1232, y=453))
        fl1.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.15, 0.03),
                                 x=940, y=450))
        fl1.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.15, 0.03),
                                 x=940, y=410))
        fl1.add_widget(Label(  #:Battery Status
            text='BMS SW version: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-100, y=-20))
        fl1.add_widget(Label(  #:Battery Status
            text='WNT SW version: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-100, y=-60))
        fl1.add_widget(Button(text="Set",
                              italic=True, bold=True,
                              font_size=15, color=[0, 0, 0, 1],
                              background_color=[1, 1, 1, 1],
                              background_normal="",
                              size_hint_x=0.035,
                              size_hint_y=0.025,
                              x=1232, y=453))

        fl1.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.15, 0.03),
                                 x=1480, y=450))
        fl1.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.15, 0.03),
                                 x=1480, y=410))
        fl1.add_widget(Label(  #:Battery Status
            text='BMS HD version: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=440, y=-20))
        fl1.add_widget(Label(  #:Battery Status
            text='WNT HD version: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=440, y=-60))
        fl1.add_widget(Button(text="Set",
                              italic=True, bold=True,
                              font_size=15, color=[0, 0, 0, 1],
                              background_color=[1, 1, 1, 1],
                              background_normal="",
                              size_hint_x=0.035,
                              size_hint_y=0.025,
                              x=1772, y=453))

        gl10 = GridLayout(cols=15, row_force_default=True, row_default_height=50, spacing=0, x=456, y=-670)
        gl10.add_widget(TextInput(text='Lev', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='cell volt high',size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='cell volt low', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='sum volt high', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='sum volt low', size_hint_x=None, width=80))

        gl10.add_widget(TextInput(text='discharge curr large', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='charge curr large', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='volt diff large', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='temp diff large', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='SOC high', size_hint_x=None, width=80))

        gl10.add_widget(TextInput(text='SOC low', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='charge temp high', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='charge temp low', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='discharge temp high', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='discharge temp low', size_hint_x=None, width=80))

        gl10.add_widget(TextInput(text='1', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='', size_hint_x=None, width=80))

        gl10.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='', size_hint_x=None, width=80))

        gl10.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='', size_hint_x=None, width=80))

        gl10.add_widget(TextInput(text='2', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='', size_hint_x=None, width=80))

        gl10.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='', size_hint_x=None, width=80))

        gl10.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl10.add_widget(TextInput(text='', size_hint_x=None, width=80))

        fl1.add_widget(Button(text="-->",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.041,
                          size_hint_y=0.025,
                          x=457, y=123))

        fl1.add_widget(Button(text="Set",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.041,
                          size_hint_y=0.025,
                          x=537, y=123))
        fl1.add_widget(Button(text="Set",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.041,
                          size_hint_y=0.025,
                          x=697, y=123))
        fl1.add_widget(Button(text="Set",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.041,
                          size_hint_y=0.025,
                          x=857, y=123))
        fl1.add_widget(Button(text="Set",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.041,
                          size_hint_y=0.025,
                          x=1017, y=123))
        fl1.add_widget(Button(text="Set",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.041,
                          size_hint_y=0.025,
                          x=1177, y=123))
        fl1.add_widget(Button(text="Set",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.082,
                          size_hint_y=0.025,
                          x=1337, y=123))
        fl1.add_widget(Button(text="Set All",
                          italic=True, bold=False,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.082,
                          size_hint_y=0.025,
                          x=1500, y=70))
        fl1.add_widget(Button(text="Save config",
                          italic=True, bold=False,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.082,
                          size_hint_y=0.025,
                          x=1340, y=70))
        fl1.add_widget(Button(text="Load config",
                          italic=True, bold=False,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.082,
                          size_hint_y=0.025,
                          x=1180, y=70))
        fl1.add_widget(Button(text="Quick Set",
                          italic=True, bold=False,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.082,
                          size_hint_y=0.025,
                          x=1020, y=70))
        fl1.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.041, 0.027),
                                 x = 617, y = 123))
        fl1.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.041, 0.027),
                                 x = 777, y = 123))
        fl1.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.041, 0.027),
                                 x = 937, y = 123))
        fl1.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.041, 0.027),
                                 x = 1097, y = 123))
        fl1.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.041, 0.027),
                                 x = 1257, y = 123))
        fl1.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.084, 0.027),
                                 x = 1495, y = 123))





        fl1.add_widget(gl8)
        fl1.add_widget(gl9)
        fl1.add_widget(gl10)




        tbi2.add_widget(fl1)
        tb.add_widget(tbi2)

        tbi3 = TabbedPanelItem(text="Readparam",font_size=15)
        fl2 = FloatLayout()

        fl2.add_widget(Image(source="img/fon.jpg", x=0, y=90))
        fl2.add_widget(Image(source="img/fon2.jpg", x=0, y=-300))
        fl2.add_widget(Image(source="img/moto.jpg", x=-500, y=250))
        fl2.add_widget(Image(source="img/strelka.jpg", x=-500, y=180))
        fl2.add_widget(Image(source="img/moto.jpg", x=200, y=250))
        fl2.add_widget(Image(source="img/strelka.jpg", x=200, y=180))
        fl2.add_widget(Image(source="img/zn.jpg", x=750, y=420))
        if n == '10':
            fl2.add_widget(Image(source="img/battery1.jpg", x=-150, y=270))
        if n == '20':
            fl2.add_widget(Image(source="img/battery2.jpg", x=-150, y=270))
        if n == '30':
            fl2.add_widget(Image(source="img/battery3.jpg", x=-150, y=270))
        if n == '40':
            fl2.add_widget(Image(source="img/battery4.jpg", x=-150, y=270))
        if n == '50':
            fl2.add_widget(Image(source="img/battery5.jpg", x=-150, y=270))

        fl2.add_widget(Label(
            text='SumVolt,V:', color=[0, 1, 0, 1],
            font_size=40, bold=True, x=-500, y=380))
        fl2.add_widget(Label(
            text='Curr,A:', color=[0, 1, 0, 1],
            font_size=40, bold=True, x=200, y=380))
        fl2.add_widget(Label(
            text='SOC%:', color=[0, 1, 0, 1],
            font_size=40, bold=True, x=-150, y=380))
        fl2.add_widget(TextInput(text="",
                                multiline=False,
                                readonly=False,
                                font_size=10,
                                padding=10,
                                size_hint=(0.05, 0.03),
                                x = 200, y = 550))
        fl2.add_widget(TextInput(text="",
                                multiline=False,
                                readonly=False,
                                font_size=10,
                                padding=10,
                                size_hint=(0.05, 0.03),
                                x = 200, y = 520))
        fl2.add_widget(TextInput(text="",
                                multiline=False,
                                readonly=False,
                                font_size=10,
                                padding=10,
                                size_hint=(0.05, 0.03),
                                x = 200, y = 480))
        fl2.add_widget(TextInput(text="",
                                multiline=False,
                                readonly=False,
                                font_size=10,
                                padding=10,
                                size_hint=(0.05, 0.03),
                                x = 200, y = 450))
        fl2.add_widget(TextInput(text="",
                                multiline=False,
                                readonly=False,
                                font_size=10,
                                padding=10,
                                size_hint=(0.05, 0.03),
                                x = 200, y = 390))
        fl2.add_widget(Label(#:Battery Status
            text='Rated Cap(Ah): ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-850, y=80))
        fl2.add_widget(Label(#:Battery Status
            text='Rated CellVolt(V): ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-850, y=50))
        fl2.add_widget(Label(#:Battery Status
            text='Cumulative charge(Ah): ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-850, y=10))
        fl2.add_widget(Label(#:Battery Status
            text='Cumulative discharge(Ah): ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-850, y=-20))
        fl2.add_widget(Label(#:Battery Status
            text='NO. of acquisition board: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-850, y=-80))

        fl2.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.05, 0.03),
                                 x=600, y=550))
        fl2.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.05, 0.03),
                                 x=600, y=520))
        fl2.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.05, 0.03),
                                 x=600, y=480))
        fl2.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.05, 0.03),
                                 x=600, y=450))
        fl2.add_widget(Label(  #:Battery Status
            text='Balance start Volt(V): ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-450, y=80))
        fl2.add_widget(Label(  #:Battery Status
            text='Bal start diff Volt(V): ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-450, y=50))
        fl2.add_widget(Label(  #:Battery Status
            text='Short Current(A): ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-450, y=10))
        fl2.add_widget(Label(  #:Battery Status
            text='Cur sampling Res(mΩ): ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-450, y=-20))
        gl5 = GridLayout(cols=3, row_force_default=True, row_default_height=30, spacing=0, x=456, y=-540)
        gl5.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl5.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl5.add_widget(TextInput(text='', size_hint_x=None, width=80))

        gl6 = GridLayout(cols=3, row_force_default=True, row_default_height=30, spacing=0, x=456, y=-575)
        gl6.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl6.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl6.add_widget(TextInput(text='', size_hint_x=None, width=80))

        fl2.add_widget(Label(  #:Battery Status
            text='Board 1~3 Cell No.: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-580, y=-70))
        fl2.add_widget(Label(  #:Battery Status
            text='Board 1~3 NTC No.: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-580, y=-100))


        fl2.add_widget(Button(text="Read",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.035,
                          size_hint_y=0.025,
                          x=300, y=535))
        fl2.add_widget(Button(text="Read",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.035,
                          size_hint_y=0.025,
                          x=300, y=465))
        fl2.add_widget(Button(text="Read",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.035,
                          size_hint_y=0.025,
                          x=700, y=465))
        fl2.add_widget(Button(text="Read",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.035,
                          size_hint_y=0.025,
                          x=700, y=535))
        fl2.add_widget(Button(text="Read",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.035,
                          size_hint_y=0.025,
                          x=700, y=385))

        fl2.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.05, 0.03),
                                 x=200, y=310))
        fl2.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.05, 0.03),
                                 x=200, y=270))
        fl2.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.05, 0.03),
                                 x=200, y=230))
        fl2.add_widget(Label(  #:Battery Status
            text='Sleep time(S): ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-850, y=-160))
        fl2.add_widget(Label(  #:Battery Status
            text='Current wave(A): ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-850, y=-200))
        fl2.add_widget(Label(  #:Battery Status
            text='Battery type: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-850, y=-240))
        fl2.add_widget(Label(  #:Battery Status
            text='Battery production date: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-850, y=-280))
        fl2.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.1, 0.03),
                                 x=200, y=190))
        fl2.add_widget(Label(  #:Battery Status
            text='Battery operation mode: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-850, y=-320))
        fl2.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.07, 0.03),
                                 x=200, y=150))
        fl2.add_widget(Button(text="Read",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.035,
                          size_hint_y=0.025,
                          x=350, y=150))
        fl2.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.2, 0.03),
                                 x=940, y=550))
        fl2.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.2, 0.03),
                                 x=940, y=510))
        fl2.add_widget(Label(  #:Battery Status
            text='Firmware index No: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-100, y=80))
        fl2.add_widget(Label(  #:Battery Status
            text='Battery code: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-100, y=40))
        fl2.add_widget(Button(text="Read",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.035,
                          size_hint_y=0.025,
                          x=1328, y=553))
        fl2.add_widget(Button(text="Read",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.035,
                          size_hint_y=0.025,
                          x=1328, y=513))
        fl2.add_widget(Label(  #:Battery Status
            text='RTC: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=480, y=80))
        fl2.add_widget(Label(  #:Battery Status
            text='IP: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=480, y=40))
        fl2.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.15, 0.03),
                                 x=1480, y=510))
        fl2.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.15, 0.03),
                                 x=1480, y=550))
        fl2.add_widget(Button(text="Read",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.035,
                          size_hint_y=0.025,
                          x=1772, y=513))
        fl2.add_widget(Button(text="Read",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.035,
                          size_hint_y=0.025,
                          x=1772, y=553))

        fl2.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.15, 0.03),
                                 x=940, y=450))
        fl2.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.15, 0.03),
                                 x=940, y=410))
        fl2.add_widget(Label(  #:Battery Status
            text='BMS SW version: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-100, y=-20))
        fl2.add_widget(Label(  #:Battery Status
            text='WNT SW version: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-100, y=-60))
        fl2.add_widget(Button(text="Read",
                              italic=True, bold=True,
                              font_size=15, color=[0, 0, 0, 1],
                              background_color=[1, 1, 1, 1],
                              background_normal="",
                              size_hint_x=0.035,
                              size_hint_y=0.025,
                              x=1232, y=453))
        fl2.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.15, 0.03),
                                 x=940, y=450))
        fl2.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.15, 0.03),
                                 x=940, y=410))
        fl2.add_widget(Label(  #:Battery Status
            text='BMS SW version: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-100, y=-20))
        fl2.add_widget(Label(  #:Battery Status
            text='WNT SW version: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=-100, y=-60))
        fl2.add_widget(Button(text="Read",
                              italic=True, bold=True,
                              font_size=15, color=[0, 0, 0, 1],
                              background_color=[1, 1, 1, 1],
                              background_normal="",
                              size_hint_x=0.035,
                              size_hint_y=0.025,
                              x=1232, y=453))

        fl2.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.15, 0.03),
                                 x=1480, y=450))
        fl2.add_widget(TextInput(text="",
                                 multiline=False,
                                 readonly=False,
                                 font_size=10,
                                 padding=10,
                                 size_hint=(0.15, 0.03),
                                 x=1480, y=410))
        fl2.add_widget(Label(  #:Battery Status
            text='BMS HD version: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=440, y=-20))
        fl2.add_widget(Label(  #:Battery Status
            text='WNT HD version: ', color=[1, 1, 1, 1],
            font_size=15, bold=True, x=440, y=-60))
        fl2.add_widget(Button(text="Read",
                              italic=True, bold=True,
                              font_size=15, color=[0, 0, 0, 1],
                              background_color=[1, 1, 1, 1],
                              background_normal="",
                              size_hint_x=0.035,
                              size_hint_y=0.025,
                              x=1772, y=453))

        gl7 = GridLayout(cols=15, row_force_default=True, row_default_height=50, spacing=0, x=456, y=-670)
        gl7.add_widget(TextInput(text='Lev', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='cell volt high',size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='cell volt low', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='sum volt high', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='sum volt low', size_hint_x=None, width=80))

        gl7.add_widget(TextInput(text='discharge curr large', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='charge curr large', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='volt diff large', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='temp diff large', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='SOC high', size_hint_x=None, width=80))

        gl7.add_widget(TextInput(text='SOC low', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='charge temp high', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='charge temp low', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='discharge temp high', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='discharge temp low', size_hint_x=None, width=80))

        gl7.add_widget(TextInput(text='1', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='', size_hint_x=None, width=80))

        gl7.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='', size_hint_x=None, width=80))

        gl7.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='', size_hint_x=None, width=80))

        gl7.add_widget(TextInput(text='2', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='', size_hint_x=None, width=80))

        gl7.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='', size_hint_x=None, width=80))

        gl7.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='', size_hint_x=None, width=80))
        gl7.add_widget(TextInput(text='', size_hint_x=None, width=80))

        fl2.add_widget(Button(text="-->",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.041,
                          size_hint_y=0.025,
                          x=457, y=123))

        fl2.add_widget(Button(text="Read",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.041,
                          size_hint_y=0.025,
                          x=537, y=123))
        fl2.add_widget(Button(text="Read",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.041,
                          size_hint_y=0.025,
                          x=697, y=123))
        fl2.add_widget(Button(text="Read",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.041,
                          size_hint_y=0.025,
                          x=857, y=123))
        fl2.add_widget(Button(text="Read",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.041,
                          size_hint_y=0.025,
                          x=1017, y=123))
        fl2.add_widget(Button(text="Read",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.041,
                          size_hint_y=0.025,
                          x=1177, y=123))
        fl2.add_widget(Button(text="Read",
                          italic=True, bold=True,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.082,
                          size_hint_y=0.025,
                          x=1337, y=123))
        fl2.add_widget(Button(text="Read All",
                          italic=True, bold=False,
                          font_size=15, color=[0, 0, 0, 1],
                          background_color=[1, 1, 1, 1],
                          background_normal="",
                          size_hint_x=0.082,
                          size_hint_y=0.025,
                          x=1500, y=70))



        fl2.add_widget(gl7)
        fl2.add_widget(gl5)
        fl2.add_widget(gl6)
        tbi3.add_widget(fl2)
        tb.add_widget(tbi3)
        asyncio.ensure_future(self.start_serial())
        return tb

    async def start_serial(self):
        loop = asyncio.get_running_loop()
        try:
            await serial_asyncio.create_serial_connection(
                loop, lambda: SerialReader(self.text_input_l, self.text_input_w, self.speedometer), 'COM5', baudrate=74880 #переменные
            )
        except Exception as e:
            print(f"Error: {e}")

    async def on_stop(self):
        print("Stopping the application...")

if __name__ == '__main__':
    try:
        asyncio.run(MyApp().async_run())
    except KeyboardInterrupt:
        print("Application stopped by user.")
