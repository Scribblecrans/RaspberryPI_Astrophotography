import subprocess
class Canon():
    def __init__(self):
        result = subprocess.run(
            ["gphoto2", "--auto-detect"],
            capture_output=True,
            text=True
        )
        connect_text = result.stdout
        split_text = connect_text.split()
        name = ""
        curr_idx = None

        if "Canon" not in split_text:
            print("Camera not found")
        else: 
            for idx, t in enumerate(split_text):
                if t == "Canon":
                    curr_idx = idx
                    break
            curr_text = split_text[curr_idx]
            while "usb" not in curr_text:
                name += f"{curr_text} "
                curr_idx += 1
                curr_text = split_text[curr_idx]
            print(f"Connected to {name}")


    def focus(self, mode):
        """ALLOWED OPTIONS FOR MANUAL MODE
        Current: Manual
        Choice: 0 One Shot
        Choice: 1 AI Focus
        Choice: 2 AI Servo
        Choice: 3 Manual"""

        result = subprocess.run(
            ["gphoto2", "--set-config", f"focusmode={mode}"],
            capture_output = True,
            text=True)

    def shooting_mode(self, mode):
        """POPULAR EXPOSURE MODES
        Choice: 0 P
        Choice: 1 TV
        Choice: 2 AV
        Choice: 3 Manual
        Choice: 4 Bulb
        Choice: 5 A_DEP
        Choice: 6 DEP
        Choice: 7 Custom"""
        result = subprocess.run(
            ["gphoto2", "--set-config", f"autoexposuremode={mode}"]
        )

    def shutter_speed(self, length):
        """POSSIBLE TIME OPTIONS        Choice: 0 bulb
        Choice: 1 30
        Choice: 2 25
        Choice: 3 20
        Choice: 4 15
        Choice: 5 13
        Choice: 6 10.3
        Choice: 7 8
        Choice: 8 6.3
        Choice: 9 5
        Choice: 10 4
        Choice: 11 3.2
        Choice: 12 2.5
        Choice: 13 2
        Choice: 14 1.6
        Choice: 15 1.3
        Choice: 16 1
        Choice: 17 0.8
        Choice: 18 0.6
        Choice: 19 0.5
        Choice: 20 0.4
        Choice: 21 0.3
        Choice: 22 1/4
        Choice: 23 1/5
        Choice: 24 1/6
        Choice: 25 1/8
        Choice: 26 1/10
        Choice: 27 1/13
        Choice: 28 1/15
        Choice: 29 1/20
        Choice: 30 1/25
        Choice: 31 1/30
        Choice: 32 1/40
        Choice: 33 1/50
        Choice: 34 1/60
        Choice: 35 1/80
        Choice: 36 1/100
        Choice: 37 1/125
        Choice: 38 1/160
        Choice: 39 1/200
        Choice: 40 1/250
        Choice: 41 1/320
        Choice: 42 1/400
        Choice: 43 1/500
        Choice: 44 1/640
        Choice: 45 1/800
        Choice: 46 1/1000
        Choice: 47 1/1250
        Choice: 48 1/1600
        Choice: 49 1/2000
        Choice: 50 1/2500
        Choice: 51 1/3200
        Choice: 52 1/4000"""
        subprocess.run([
            "gphoto2",
            "--set-config",
            f"shutterspeed={length}"
        ])

    def capture(self, filepath, name):
        # result = subprocess.run([
        #     "gphoto2",
        #     "--get-config",
        #     f"shutterspeed"
        # ])
        # lengths = result.stdout
        # for idx, txt in enumerate(lengths.split(" ")):
        #     print(txt)
        #     if txt == "Current:":
        #         length = lengths.split[idx + 1]
        #         print(length)

        # if length == "bulb": print("true")
        # else: 
        subprocess.run([
            "gphoto2",
            "--capture-image-and-download",
            "--filename",
            f"{filepath}/{name}.CR2"
        ])

if __name__ == "__main__":
    c = Canon()
    c.shooting_mode(mode="Manual")
    c.focus(mode="Manual")
    c.shutter_speed("bulb")
    c.capture(filepath="/home/scribblecrans/Desktop/RaspberryPI_Astrophotography/Backend/Images", name="test")