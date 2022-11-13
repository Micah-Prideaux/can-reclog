import sys
import time
import re
from datetime import datetime


def extract(argv):
    try:
        if argv[0] == "pcan":
            pcan(argv[1:])
        else:
            print_useage()
    except Exception as e:
        print(e)
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
                elif ";---+--   ----+----  --+--  ----+---  +  -+ -- -- -- -- -- -- --" in line:
                    recordingstarted = True
                elif "Start time:" in line:
                    date_match = re.search(r'\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}', line)
                    if date_match == None:
                        date_match = re.search(r'\d{1}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}', line)
                    try:
                        timetuple = datetime.strptime(date_match.group(), '%d/%m/%Y %H:%M:%S').timetuple()
                        starttime = time.mktime(timetuple)
                    except Exception as e:
                        print(e)

def print_useage():
    print("extractor.py <file type> <file location> <output name>")


if __name__ == "__main__":
    extract(sys.argv[1:])
