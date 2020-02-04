

from operator import add
import sys

if len(sys.argv) < 2:
    print("No file provided. Exiting")
    sys.exit(1)

filename = sys.argv[1]

print(filename)

try:
    with open(filename, 'r') as f:
        lines = f.readlines()
except:
    print("File error: path probably does not exist. Exiting")
    sys.exit(2)

descriptor_time = []
detector_time = []
keypoints = []
matches = []

for line in lines:
    keyword = line.split(" ")[1]
    if keyword == "descriptor":
        descriptor_time.append(float(line.split(" ")[-2]))
    elif keyword == "detector":
        detector_time.append(float(line.split(" ")[-2]))
    elif keyword == "keypoints":
        keypoints.append(line.split(" ")[0])
    elif keyword == "matches":
        matches.append(line.split(" ")[0])

print("Keypoints on preceding Vehicle")
print(" | ".join(keypoints))
print("Matched points")
print(" | ".join(matches))
print("total time")
total_time = list(map(add, descriptor_time, detector_time))
print(" | ".join([str(t) for t in total_time]))