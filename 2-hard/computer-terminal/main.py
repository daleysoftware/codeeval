import sys

class Screen:
    _SCREEN_ROWS = 10
    _SCREEN_COLS = 10

    def __init__(self, terminal_input):

        self.terminal_input = terminal_input
        # Rendering variables.
        self._in_overwrite_mode = True
        self._current_row = 0
        self._current_col = 0
        self._image = Screen._generate_empty_image()
        # Render the screen image.
        self._render()

    @staticmethod
    def _generate_empty_image():
        result = []
        for i in range(0, Screen._SCREEN_ROWS):
            result.append([' '] * Screen._SCREEN_COLS)
        return result

    def _control_c(self):
        self._image = Screen._generate_empty_image()

    def _control_h(self):
        self._current_row = 0
        self._current_col = 0

    def _control_b(self):
        self._current_col = 0

    def _control_d(self):
        self._current_row = min(self._current_row+1, Screen._SCREEN_ROWS-1)

    def _control_u(self):
        self._current_row = max(self._current_row-1, 0)

    def _control_l(self):
        self._current_col = max(self._current_col-1, 0)

    def _control_r(self):
        self._current_col = min(self._current_col+1, Screen._SCREEN_COLS-1)

    def _control_e(self):
        for i in range(self._current_col, Screen._SCREEN_COLS):
            self._image[self._current_row][i] = ' '

    def _control_i(self):
        self._in_overwrite_mode = False

    def _control_o(self):
        self._in_overwrite_mode = True

    def _control_circumflex(self):
        self._write('^')

    def _move_to(self, row, col):
        self._current_row = row
        self._current_col = col

    def _write(self, char):
        # If we are in insert mode, shift the row over first.
        if not self._in_overwrite_mode:
            for i in range(Screen._SCREEN_COLS-1, self._current_col, -1):
                self._image[self._current_row][i] = self._image[self._current_row][i-1]

        # Write the char in place (for both modes).
        self._image[self._current_row][self._current_col] = char
        # Move the cursor right one col (for both modes).
        self._control_r()

    def _render(self):
        i = 0
        while i < len(self.terminal_input):
            c = self.terminal_input[i]
            if c == '^':
                if self.terminal_input[i+1].isdigit():
                    control = self.terminal_input[i+1:i+3]
                    i += 2
                else:
                    control = self.terminal_input[i+1]
                    i += 1

                # Map control to actionable function.
                functions = {
                    'c': self._control_c,
                    'h': self._control_h,
                    'b': self._control_b,
                    'd': self._control_d,
                    'u': self._control_u,
                    'l': self._control_l,
                    'r': self._control_r,
                    'e': self._control_e,
                    'i': self._control_i,
                    'o': self._control_o,
                    '^': self._control_circumflex
                }
                if control in functions:
                    function = functions[control]
                    function()
                else:
                    # In this case we have reached a ^DD.
                    self._move_to(int(control[0]), int(control[1]))
            else:
                if c != '\n':
                    self._write(c)
                else:
                    # Do nothing for newlines.
                    pass

            # Loop increment. Don't use for since we modify the looping variable.
            i += 1

    def __str__(self):
        result = []
        for i in self._image:
            result.append(''.join(i).rstrip())
        return '\n'.join(result)

def main():
    with open(sys.argv[1], 'r') as input_file:
        screen = Screen(input_file.read())
        print(screen)

if __name__ == '__main__':
    main()
