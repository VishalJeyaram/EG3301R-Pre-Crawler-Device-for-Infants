# EG3301R Pre-Crawler Device for Infants Python Scripts, Team EIM-306, National University of Singapore


## Year 2 Academic Year 2021-2022, Semester 2 to Year 3 Academic Year 2022-2023, Semester 1 

These scripts were developed for a team project I was in for the module EG3301R: DCP Dissertation, in which we designed and developed a Pre-Crawler Device for Infants. It is an assistive rehabilitation system designed to support infants with Cerebral Palsy and other neuromotor disorders during early-stage motor development. The goal of the project was to create a safe, automated device that guides infants through repeated crawling motions, helping to stimulate neuroplasticity and promote foundational motor skills during a critical developmental period. 

## Master Control (send.py ; app.py)

In the Pre-Crawler Device, I developed two Python scripts that together formed the device’s control and safety layer. app.py served as the main control application: it provided a simple GUI (built with guizero) for caregivers to choose the crawling style (e.g., Classic or Bear Crawl) and adjust speed, while driving a multi-servo exoskeleton through an Adafruit PCA9685 controller using adafruit_servokit. The script coordinated six servo channels (arms, thighs, legs), mapped motion phases into smooth angle sequences, and implemented timed routines with live angle readouts so the team could calibrate and validate movement patterns. In parallel, send.py acted as a hardware stop mechanism: it used a Raspberry Pi GPIO input to detect a physical button press and exposed that signal over a lightweight local socket server. app.py continuously polled this socket during motion loops, allowing an immediate stop and return-to-neutral behavior when the safety button was pressed. Together, these scripts enabled an end-to-end system where clinicians/caregivers could run controlled crawling routines while maintaining a simple, reliable emergency stop pathway.

## External Links

You can read the detailed project report [here](https://drive.google.com/file/d/1vV-UTGqWJJNqgNdslRfhN0m5amG98sm2/view?usp=sharing).

You may also watch the video of the Pre-Crawler Device's motion demnonstration [here](https://drive.google.com/file/d/1nfAfzPiWCSRIUcdT271-98vXUrIAV540/view?usp=sharing)

