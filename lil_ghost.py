import random
import tkinter as tk
import time

class pet():
    def __init__(self):
        self.window = tk.Tk()
        self.actions = {
            "idle_right" : [tk.PhotoImage(file='lil_ghost_idle_right.gif', format='gif -index %i' % (i)) for i in range(4)],
            "idle_left" : [tk.PhotoImage(file='lil_ghost_idle_left.gif', format='gif -index %i' % (i)) for i in range(4)],
            "move_right" : [tk.PhotoImage(file='lil_ghost_move_right.gif', format='gif -index %i' % (i)) for i in range(4)],
            "move_left" : [tk.PhotoImage(file='lil_ghost_move_left.gif', format='gif -index %i' % (i)) for i in range(4)],
            "up_left" : [tk.PhotoImage(file='lil_ghost_up_left.gif', format='gif -index %i' % (i)) for i in range(4)],
            "up_right" : [tk.PhotoImage(file='lil_ghost_up_right.gif', format='gif -index %i' % (i)) for i in range(4)],
            "down_left" : [tk.PhotoImage(file='lil_ghost_down_left.gif', format='gif -index %i' % (i)) for i in range(4)],
            "down_right" : [tk.PhotoImage(file='lil_ghost_down_right.gif', format='gif -index %i' % (i)) for i in range(4)],
        }
        self.frame_index = 0
        self.action_name = ""
        self.choose_action()
        self.img = self.actions[self.action_name][self.frame_index]
        self.count_frames = 0

        self.timestamp = time.time()

        self.window.config(highlightbackground='black')

        self.window.overrideredirect(True)
        self.window.attributes('-topmost', True)
        self.window.wm_attributes('-transparentcolor', 'black')

        self.label = tk.Label(self.window, bd=0, bg='black')

        self.x = 1000
        self.y = 500

        self.window.geometry('320x320+{x}+0'.format(x=str(self.x)))
        self.label.configure(image=self.img)
        self.label.pack()
        self.window.after(0, self.update)
        self.window.mainloop()

    def choose_action(self):
        if "idle" in self.action_name:
            options = ["move_left", "up_left", "down_left", "move_right", "up_right", "down_right"]
            if "left" in self.action_name:
                for opt in options:
                    if "right" in options:
                        options.remove(opt)
                if self.x < 500:
                    options.remove("move_left")
            elif "right" in self.action_name:
                for opt in options:
                    if "left" in options:
                        options.remove(opt)
                if self.x < 1000:
                    options.remove("move_right")
            if self.y > 500:
                try:
                    options.remove("down_left")
                except:
                    options.remove("down_right")
            elif self.y < 250:
                try:
                    options.remove("up_left")
                except:
                    options.remove("up_right")
            self.action_name = random.choice(options)
        else:
            self.action_name = "idle_left" if "right" in self.action_name else "idle_right"
        self.action_length = len(self.actions[self.action_name]) - 1
        self.num_of_actions = random.randint(2, 4)

    def update(self):
        if time.time() > self.timestamp + 0.15:
            self.timestamp = time.time()
            self.frame_index = (self.frame_index + 1) % 4
            self.img = self.actions[self.action_name][self.frame_index]
            if self.action_name == "move_right":
                self.x += 3
            elif self.action_name == "move_left":
                self.x -= 3
            elif "up" in self.action_name:
                self.y -= 3
            elif "down" in self.action_name:
                self.y += 3
            if self.frame_index == self.action_length:
                self.count_frames += 1

        self.window.geometry(f'320x320+{self.x}+{self.y}')
        self.label.configure(image=self.img)
        self.label.pack()
        self.window.after(10, self.update)

        if self.count_frames == self.num_of_actions:
            self.choose_action()
            self.count_frames = 0

if __name__ == "__main__":
    pet()