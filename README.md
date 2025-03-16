# enable_led & disable_led <br>
Two simple Python 3.x based scripts for toggling the status of the keyboard's scrolllock LED <br>

<br>

## Required Packages: <br>
* `colorama`: `pip3 install colorama`
* `pyinstaller`: `pip3 install pyinstaller`
* it probably only works on ubuntu based linux distributions only.



## How to compile into distributable binaries?: <br>
**In order to compile these Python script files into Linux binaries, you must have `pyinstaller` installed, alongwith `auto-py-to-exe` when necessary** <br>

### Quick Compilation Guide: <br>
* Download both of the scripts `enable_led` and `disable_led` <br>
* Make a working directory. <br>
```sh
cd ~
mkdir working-dir
cd working-dir
``` 
<br>

* Copy scripts from your `Downloads` folder to the `working-dir` you have just made. <br>
```sh
cp enable_led.py ~/working-dir/enable_led.py
cp disable_led.py ~/working-dir/disable_led.py
```
<br>

* Compile them with `pyinstaller` <br>

```sh
pyinstaller --onefile enable_led.py
pyinstaller --onefile disable_led.py
```
<br>

* Copy them into `/usr/bin` for easier access later. <br>

```sh
sudo cp -fv ./enable_led /usr/bin/enable_led
sudo cp -fv ./disable_led /usr/bin/disable_led
```

<br>

##### **I don't think I have to tell you that you must have to enter your `sudo` password to copy to `/usr/bin`.**

<br>

* Enjoy! <br>

```sh
# to enable keyboard backlight
enable_led 
# to disable keyboard backlight
disable_led
# no sudo needed
```

<br>


## License <br>
these are just some basic 2 script files i don't have to put a license for them.
