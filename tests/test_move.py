from main import Move
from main import Size

class TestMove:
    def setup_method(self):
        self.move = Move(True, 1, 1)

    def test_init(self):
        x = self.move

    def test_get_move_type(self):
        tests = [
            [[True, 1, 1], '--relative'],
            [[False, 1, 1], '']
        ]
        for x in tests:
            self.move = Move(x[0][0], x[0][1], x[0][2])
            a = self.move.get_move_type()
            assert a == x[1]

    def test_get_current(self):
        a = self.move.get_current()
        assert a == '0x' + a[2:]
        assert len(a) == 10

    def test_move_command_gen(self):
        tests = [
            [[10, 20], 'xdotool windowmove'],
            [[30, 50], 'xdotool windowmove']
        ]
        for x in tests:
            a = self.move.move_command_gen(x[0][0], x[0][1])
            b = a.split(' ')
            assert b[0] == 'xdotool'
            assert b[1] == 'windowmove'
            assert int(b[-1]) == x[0][1]
            assert int(b[-2]) == x[0][0]
    
    def test_move_win(self):
        a = self.move.move_win()
        b = a.split(' ')
        assert b[0] == 'xdotool'
        assert b[1] == 'windowmove'
        assert int(b[-1]) == 1
        assert int(b[-2]) == 1

class TestSize:
    def setup_method(self):
        self.size = Size(40, 60)

    def test_init(self):
        x = self.size

    def test_get_current(self):
        a = self.size.get_current()
        assert a == '0x' + a[2:]
        assert len(a) == 10

    def test_size_command_gen(self):
        tests = [
            [[10, 20], 'xdotool windowmove'],
            [[30, 50], 'xdotool windowmove']
        ]
        for x in tests:
            a = self.size.size_command_gen(x[0][0], x[0][1])
            b = a.split(' ')
            assert b[0] == 'xdotool'
            assert b[1] == 'windowsize'
            assert b[2][:2] == '0x'
            assert b[3] == f'{x[0][0]}%'
            assert b[4] == f'{x[0][1]}%'

    def test_size_win(self):
        a = self.size.size_win()
        b = a.split(' ')
        assert b[0] == 'xdotool'
        assert b[1] == 'windowsize'
        assert b[3] == '40%'
        assert b[4] == '60%'

