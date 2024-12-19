from src import Debug, Reader, Chrono


class Computer:
    __slots__ = ["a", "b", "c", "pointer", "results"]

    def __init__(self, reg_a: int, reg_b: int, reg_c: int, pointer: int = 0):
        self.a = reg_a
        self.b = reg_b
        self.c = reg_c
        self.pointer = pointer

        self.results = list()

    def __str__(self) -> str:
        return f"A={self.a} B={self.b} C={self.c} | @{self.pointer}"

    def reset(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.pointer = 0
        self.results.clear()

    def combo(self, operand: int) -> int:
        if operand <= 3:
            combo = operand
        elif operand == 4:
            combo = self.a
        elif operand == 5:
            combo = self.b
        elif operand == 6:
            combo = self.c
        elif operand == 7:
            combo = -1
            debug("ERROR: 7 FOUND")

        return combo

    def adv(self, operand: int):
        a = self.a
        self.a = int(self.a / pow(2, self.combo(operand)))
        self.pointer += 2
        debug(f"adv {operand}: A {a} -> {self.a}")

    def bxl(self, operand: int):
        b = self.b
        self.b = self.b ^ operand
        self.pointer += 2
        debug(f"bxl {operand}: B {b} ->{self.b}")

    def bst(self, operand: int):
        b = self.b
        self.b = self.combo(operand) % 8
        self.pointer += 2
        debug(f"bst {operand}: B {b} -> {self.b}")

    def jnz(self, operand: int):
        if self.a != 0:
            result = "jump"
            self.pointer = operand
        else:
            result = "nothing"
            self.pointer += 2
        debug(f"jnz {result} -> @{self.pointer}")

    def bxc(self, operand: int):
        b = self.b
        self.b = self.b ^ self.c
        self.pointer += 2
        debug(f"bxc {operand}: B {b} -> {self.b}")

    def out(self, operand: int):
        result = self.combo(operand) % 8
        self.pointer += 2
        self.results.append(result)
        debug(f"out {operand} -> {result}")

    def bdv(self, operand: int):
        b = self.b
        self.b = int(self.a / pow(2, self.combo(operand)))
        self.pointer += 2
        debug(f"bdv {operand}: B {b} -> {self.b}")

    def cdv(self, operand: int):
        c = self.c
        self.c = int(self.a / pow(2, self.combo(operand)))
        self.pointer += 2
        debug(f"cdv {operand}: C {c} -> {self.c}")


debug = Debug()
example = False


with Reader(17, example) as reader:
    # Registers
    registers: list[int] = list()
    for _ in range(3):
        _, n = reader.get_line(": ", str, int)
        registers.append(n)
    # Empty line
    reader.raw_line()
    # Instructions
    reader.skip(9)
    program: list[int] = reader.get_line(",", int)

# debug(registers)
# debug(program)

## Parts 1

computer = Computer(*registers)
actions = {
    0: computer.adv,
    1: computer.bxl,
    2: computer.bst,
    3: computer.jnz,
    4: computer.bxc,
    5: computer.out,
    6: computer.bdv,
    7: computer.cdv,
}

debug.enable()
while computer.pointer < len(program):
    debug("Program:", program)
    debug("Computer:", computer)
    opcode = program[computer.pointer]
    operand = program[computer.pointer + 1]

    action = actions[opcode]
    action(operand)

    debug("Computer:", computer)
    debug()


print("Part 1:", ",".join(str(x) for x in computer.results))
