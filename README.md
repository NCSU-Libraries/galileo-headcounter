# GalileoHeadcounter
#### Created by Augustus Vieweg and Aaron Arthur at NCSU Libraries

The Galileo Headcounter is an automated headcounter, keeping track of the number of people who have entered a venue, in our case, the D.H. Hill Makerspace at North Carolina State University.

The code runs on the Arduino firmware. Our specific example uses the Intel Galileo Gen 2 hardware, but it should work on any Arduino-based board that has an Ethernet port.

## Open Source

Galileo Headcounter is open-sourced; there are only a few things that need changing.

####Code Updates
* auth.json
	* Lines 2 through 5 need to reference a Google Developers Sheets Application.
* GalileoHeadcounter.ino
	* Line 16 should be the hardware's MAC address, formatted as specified.
	* Lines 49 and 50 should contain the public and private keys for a database on [SparkFun's free database](https://data.sparkfun.com).
	* Line 51 should correspond to your region's UTC offset.
* datalogger.py
	* Python dependencies include the libraries gspread and oauth2client
	* For further documentation on datalogger.py, check out our [Card Access System](https://github.ncsu.edu/ncsu-libraries/card-system-config).
	

