## BIRBS
a collection of python libaries, scripts and notes used in automating the process of documenting my birdfeeder using a GoPro Hero 3+ Black.

## SET UP
- GoPro Hero 3+ Black
- GoPro Original Battery
- GoPro Battery BacPac
- GoPro Charging Cable
- [Transparent Bird House](https://www.amazon.com/iFCOW-Transparent-Acrylic-Absorption-Installation/dp/B084L14RCT/ref=sr_1_29?dchild=1&keywords=acrylic+bird+feeders&qid=1587835858&sr=8-29)
- [Vogelbescgerming Bird Feed](https://www.vogelbeschermingshop.nl/4-seizoenenstrooivoer-met-meelwormen-25-kg)
- 32GB Micro SD Card

*hopefully in the future it will also include*
- Suction Cup & GorillaPod Arm
- GoPro Skeleton Case


## SOFTWARE

#### REMOTE CONTROL OF THE GOPRO 
`avoid having to press buttons`

No need to `cd` into a folder

[install latest version of python](https://www.python.org/downloads/)

latest version of python includes the pip command

but if pip is giving you trouble execute in the terminal

```bash
pip3 install --upgrade pip
```

This set up uses [Goprohero](https://github.com/joshvillbrandt/goprohero) a library and a command line interface that can interface with GoPro HERO3, HERO3+, and HERO4 cameras over http.
Following the instructions of Goprohero:

Install the `goprohero` library:

```bash
pip3 install goprohero
```

- turn GoPro On
- turn on the wifi on your GoPro
- join the camera network

in the python shell

```python
from goprohero import GoProHero
camera = GoProHero(password='yourpassword')
camera.command('record', 'on')
camera.command('record', 'off')
```

###### **❐ WOOHOO CHECKPOINT ❐** YOU HAVE JUST RECORDED YOUR BIRBS REMOTELY


most used commands :

Parameter | Values
--- |:---
power | `sleep`, `on`
record | `off`, `on`

Check out the [API](https://github.com/joshvillbrandt/goprohero/blob/master/docs/API.md) for the complete command and parameter list.

  
#### AUTOMATE TURN ON & RECORD 
`so it happens every morning because the birbs wake up before you`


This part uses [shedule](https://pypi.org/project/schedule/).An in-process scheduler for periodic jobs that uses the builder pattern for configuration.


```bash
pip3 install schedule
```
then

```bash
git clone https://github.com/vdoukadoukopoulou/birbs
cd birbs
open .
```

in the `birdcam.py` file 
change password to your password 


If you know what and [.env](https://pypi.org/project/python-dotenv/) file is | If you don't know what it is
--- |:---
create a .env file with `KEY='your_password_of_choice'` | fill in your GoPro password where indicated bellow makes sure it looks like this `camera = GoProHero(password='your_password_of_choice')`

```python
camera = GoProHero(password=your_password)
```

decide **when** you want your camera to turn on and record.

the current version is set to turn on at 05:30 and record for 2 hours
```python
schedule.every().day.at("05:30").do(job)
```

other possible `schedule` options:
```python
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)
```

finally choose for **how long** you would like to record :

- [hours to seconds converter](https://www.calculateme.com/time/hours/to-seconds/)
- [morning civil twilight calculator](https://www.suntoday.org/sunrise-sunset/tomorrow.html)
- *birbs feed early in the morning*


```python
camera.command('record', 'on')
time.sleep(time you want to record in seconds)
camera.command('record', 'off')
```   


**save everything!**


in the terminal

```bash
cd to ~/your/path/birbs
python3 birdcam.py
```

When running `birdcam.py` make sure you have turned on the wifi on your camera and joined the camera network.



###### **❐ WOOHOO CHECKPOINT ❐** YOU CAN NOW SEE THE BIRBS YOU MISSED WHEN YOU WERE ASLEEP



##### HARDWARE NOTES
the device running `birdcam.py` needs to be on and connected to the GoPro camera network in order to execute the steps for the whole duration.
GoPro Hero 3+ (black edition) needs to be plugged in to additional power to last. For now I use sock power, that means that the bacpac is fitted (the internal battery can't be removed and still have the gopro 3+ black edition operational, it seems possible on the silver edition though) the charging cable needs to be 5V:1A (be aware most charging cables are 2A). 
It overheats (without excessive testing) it looks like it heats slightly less when using the GoPro Original internal battery and the GoPro Charging Cable.

At `1080p` 2 hours are something less that `32GB`

##### NEXT STEPS
1. Get the program on a rasberry pi so it can run uninterrupted and won't require the laptop to stay on
2. Offload the files remotely, so you don't to remove the camera to access the SD
3. Monitor the heatup of the GoPro (when recording in shadow, when recording in heat, when asleep in the sun etc.) Possibly looking into a Aluminum Heat Sink Case.
4. Explore ways of powering the GoPro without the internal battery (such battery eliminator etc.)
5. Look into setuping a livestream
