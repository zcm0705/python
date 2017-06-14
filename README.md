# python
Crawl with Python
Target Website: https://learn.adafruit.com/

Function:
	Crawl every single guide-block on the web page. Go to the guide page and grab info(side bar/main content/related guides). Pagination is enabled.

Need to improve:
  1. Finish the main content part. Come up with a general way to crawl the main content info for different guide page.
  2. Organize the data with more readable format.
  3. User can scrap any webpage from the "Learn" section when an URL parameter is added to the end of the command (e.g. `./crawler.py -l [URL]`) in terminal

Data sample:

ISS Pin
{
    "Guide Info": {
        "Author": "Leslie Birch", 
        "Description": "A Particle Photon microcontroller and an Adafruit Neopixel ring combine to make a pin that's fit for NASA fans. It displays an orbiting white blip when idle and then turns blue, white and red when the ISS flies by. The code makes use of IFTTT (If This Then That), a free site that makes connecting IoT devices as easy as a few clicks. This project was inspired by my first NASA Space Apps Challenge with friend Brooks Rampersad--an ISS Orbit Skirt.", 
        "Link": "https://learn.adafruit.com/iss-pin", 
        "Tagline": "You'll be star gazing when this NeoPixel pin lights up to notify you of the International Space Station flying overhead.", 
        "Title": "ISS Pin"
    }, 
    "Page Info": {
        "Left Sidebar": {
            "Subtitle": "You'll be star gazing when this NeoPixel pin lights up to notify you of the International Space Station flying overhead.", 
            "Title": "ISS Pin", 
            "Topics": [
                "Overview", 
                "Tools & Supplies", 
                "Solder Circuit", 
                "Create Cover", 
                "Code", 
                "Set Up IFTTT", 
                "Wear It!"
            ]
        }, 
        "Related Guides": [
            "Circuit Playground Class Scheduler", 
            "LED Masquerade Masks", 
            "Light-Up Angler Fish Embroidery", 
            "Flora TSL2561 Lux Sensor"
        ]
    }
}
NXP Precision 9DoF Breakout
{
    "Guide Info": {
        "Author": "Kevin Townsend", 
        "Description": "This learning guide gives you everything you need to get started using out high precision 9DoF breakout board based on NXP's FXOS8700 and FXAS21002 sensors.", 
        "Link": "https://learn.adafruit.com/nxp-precision-9dof-breakout", 
        "Tagline": "Getting up and running (literally?) with our high precision orientation breakout board.", 
        "Title": "NXP Precision 9DoF Breakout"
    }, 
    "Page Info": {
        "Left Sidebar": {
            "Subtitle": "Getting up and running (literally?) with our high precision orientation breakout board.", 
            "Title": "NXP Precision 9DoF Breakout", 
            "Topics": [
                "Overview", 
                "Pinout", 
                "Wiring & Test", 
                "Calibration (USB)", 
                "Orientation Test (USB)", 
                "Downloads"
            ]
        }, 
        "Related Guides": [
            "Adafruit 128x64 OLED Bonnet for Raspberry Pi", 
            "Sensors in MakeCode", 
            "Digital Fidget Spinner", 
            "Hydro Dipping 3D Prints"
        ]
    }
}