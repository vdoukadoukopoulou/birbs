## birbs
a collection of python scripts used in automating the process of recording and offloading material from a GoPro Hero 3+ Black that I use to observe my birdfeeder.

## SET UP
⋅⋅⋅ GoPro Hero 3+ Black
⋅⋅⋅ GoPro Original Battery
⋅⋅⋅ GoPro Battery BacPac
⋅⋅⋅ GoPro Charging Cable
⋅⋅⋅ [Transparent Bird House](https://www.amazon.com/iFCOW-Transparent-Acrylic-Absorption-Installation/dp/B084L14RCT/ref=sr_1_29?dchild=1&keywords=acrylic+bird+feeders&qid=1587835858&sr=8-29)
⋅⋅⋅ [Vogelbescgerming Bird Feed](https://www.vogelbeschermingshop.nl/4-seizoenenstrooivoer-met-meelwormen-25-kg)
32GB Micro SD Card

*hopefully in the future it will also include*
⋅⋅⋅ Suction Cup & GorillaPod Arm
⋅⋅⋅ GoPro Skeleton Case


## SOFTWARE
[install latest version of python](https://www.python.org/downloads/)

python latest version come with pip hooray!
if pip is giving you hustell

```bash
pip3 install --upgrade pip
```

Then this set builds upong [Goprohero](https://github.com/joshvillbrandt/goprohero) a library and a command line interface that can interface with GoPro HERO3, HERO3+, and HERO4 cameras over http.
Following the instructions of Goprohero:

Install the `goprohero` library:

```bash
pip3 install goprohero
```
turn the wifi on on your camera
join the camera network
in the python shell

```python
from goprohero import GoProHero
camera = GoProHero(password='password')
camera.command('record', 'on')
camera.command('record', 'off')
```

woohoo! you have just have recorded your birbs remotely!

Check out the [API](https://github.com/joshvillbrandt/goprohero/blob/master/docs/API.md) for the complete command list.

most often commands used :

Parameter | Values
--- |:---
power | `sleep`, `on`
record | `off`, `on`
  
#### MAKE THIS INTO A PROGRAM THAT HAPPENS EVERY MORNING BECAUSE BIRBS WAKE UP BEFORE YOU

```bash
pip3 install --upgrade pip
```
then

```bash
git clone https://github.com/vdoukadoukopoulou/birbs
cd birbs
open .
```

open `birdcam.py` file 
change the password to your password

```python
camera = GoProHero(password='password')
```
then choose when you want your camera to turn on and record.
this uses [shedule](https://pypi.org/project/schedule/)

the current version is set to turn on at 05:30 and record for 2 hours
```python
schedule.every().day.at("05:30").do(job)
```

other possible schedule options:
```python
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)
```

to choose for how long you would like to record edit :
⋅⋅⋅[hours to seconds converter](https:(//www.calculateme.com/time/hours/to-seconds/)
⋅⋅⋅[morning civil twilight calculator](https://www.suntoday.org/sunrise-sunset/tomorrow.html)
⋅⋅⋅ *birbs feed early in the morning*

```python
    camera.command('record', 'on')
    time.sleep(time you want to record in seconds)
    camera.command('record', 'off')
    ```
save everything!

in the terminal

```bash
cd to ~/your/path/birbs
python3 birdcam.py
```
WOOHOO! YOU CAN NOW SEE IF THE BIRBS CAME TO YOUR BIRDFEEDER WITHOUT WAKING UP



##### HARDWARE NOTES
the laptop needs to be on and connected to the gopro network in order to execute the steps.
GoPro Hero 3+ (black edition) needs to be plugged in to electric power to last .That means that the bacpac is fitted (the internal battery can't be removed and still have the gopro operational) the charging cable needs to be 5V,1A (be aware most charging cables are 2A)
it overheats.

At `1080p` 2 hours are something less that `32GB`

###### NEXT STEPS
1. Get the program on a rasberry pi so it can run uninterrupted and won't require the laptop to stay on
2. Offload the files remotely, so you don't to remove the camera to access the SD
3. Monitor the heatup of the GoPro (when recording in shadow, when recording in heat, when asleep in the sun)
4. Explore ways of powering the GoPro without the internal battery.
5. Look into setuping a livestream
