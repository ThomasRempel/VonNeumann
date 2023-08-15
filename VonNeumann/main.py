def main():
    io = IO()
    ram = RAM(7)
    cpu = CPU(ram, io)
    ram.write(10, 120)
    ram.write(11, 127)
    cpu.run(10)


if __name__ == '__main__':
        main()
