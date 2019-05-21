import time
import threading
import pyautogui
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode


delay = 0.000001
button = Button.left
start_stop_key = KeyCode(char='c')
exit_key = KeyCode(char='e')
position_key = KeyCode(char='s')


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False
        
    def get_position(self):
      return mouse.position
      
    def move_to(self,pos):
      original_position = (306, 449)
      mouse.position = pos      
      time.sleep(0.3)
      mouse.click(self.button)      
      time.sleep(0.3)
      mouse.position = original_position
      print(1)
    
    def get_coods(self):
      cookie = pyautogui.locateOnScreen('cookie.png', confidence=.5)
      if(cookie != None):
        print((cookie[0], cookie[1]))
        print(mouse.position)
        self.move_to((cookie[0], cookie[1]))
      
      
    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
                #self.get_coods()
            time.sleep(0.1)

class FindCookie(threading.Thread):
  def __init__(self):
    super(FindCookie, self).__init__()
    self.start_look = True
      
  def start_looking(self):
      self.start_look = True
  def stop_looking(self):
      self.start_look = False
    
  def run(self):
    while(self.start_look):
      cookie = pyautogui.locateOnScreen('cookie.png', confidence=.5)
      if(cookie != None):
          print((cookie[0], cookie[1]))
          print(mouse.position)
          click_thread.move_to((cookie[0], cookie[1]))
    


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()
look_thread = FindCookie()
look_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == position_key:
        look_thread.start_looking()
    elif key == exit_key:
        look_thread.stop_looking()
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()