import sys
import time


def extract(argv):
    if argv[0] == "pcan":
        pcan(argv[1:])
    else:
        print_useage()
    # do thing


def pcan(argv):
    starttime = time.time()
    recordingstarted = False
    with open(argv[0], "r") as ip:
        with open(argv[1], "w") as output:
            for line in ip:
                if recordingstarted:
                    data = line.split()
                    timedif = float(data[1]) / 1000
                    output.write(f"({(starttime + timedif):.6f}) can0 {data[3]}#{''.join(data[5:])}\n")
                    """hi"""
                elif ";---+--   ----+----  --+--  ----+---  +  -+ -- -- -- -- -- -- --" in line:
                    recordingstarted = True


def print_useage():
    print("extractor.py <file type> <file location> <output name>")


if __name__ == "__main__":
    extract(sys.argv[1:])
