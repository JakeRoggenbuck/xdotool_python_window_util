import subprocess


class Move:
    def __init__(self, move_type, x, y):
        self.move_type = move_type
        self.x = x
        self.y = y
    
    def get_move_type(self):
        if self.move_type:
            return '--relative'
        else:
            return ''

    def get_current(self):
        bspc_window = "bspc query -N -n"
        current_window = subprocess.check_output(bspc_window, shell=True)
        return current_window.decode("utf-8").strip('\n')

    def move_command_gen(self, x, y):
        command_prefx = "xdotool windowmove "
        command = f"{self.get_move_type()} {self.get_current()} {x} {y}"
        return command_prefx + command

    def move_win(self):
        move_command = self.move_command_gen(self.x, self.y)
        subprocess.run(move_command, shell=True)
        return str(move_command)
