class DigitalCounter:
    def __init__(self, start=0, min_value=0, max_value=10):
        if min_value >= max_value:
            raise ValueError("Minimum value must be less than maximum value.")
        if not (min_value <= start <= max_value):
            raise ValueError("Start value must be between min and max values.")

        self._value = start
        self._min_value = min_value
        self._max_value = max_value

    def set_max_value(self, max_value):
        if max_value <= self._min_value:
            raise ValueError("Max value must be greater than min value.")
        if self._value > max_value:
            raise ValueError("Current value is greater than the new maximum.")
        self._max_value = max_value

    def set_min_value(self, min_value):
        if min_value >= self._max_value:
            raise ValueError("Min value must be less than max value.")
        if self._value < min_value:
            raise ValueError("Current value is less than the new minimum.")
        self._min_value = min_value

    def set_current_value(self, value):
        if not (self._min_value <= value <= self._max_value):
            raise ValueError("Value must be within the min and max limits.")
        self._value = value

    def step_up(self):
        if self._value >= self._max_value:
            raise ValueError("Досягнуто максимуму")
        self._value += 1

    def step_down(self):
        if self._value <= self._min_value:
            raise ValueError("Досягнутий мінімум")
        self._value -= 1

    def get_current_value(self):
        return self._value


if __name__ == "__main__":
    try:
        counter = DigitalCounter(start=0, min_value=0, max_value=3)
        print(f"Start: {counter.get_current_value()}")

        counter.step_up()
        counter.step_up()
        counter.step_up()
        print(f"Current after +3: {counter.get_current_value()}")


        counter.step_down()
        print(f"Current after -1: {counter.get_current_value()}")

        counter.set_min_value(1)

    except ValueError as e:
        print(f"Error: {e}")