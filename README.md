# enable_led & disable_led <br>
Basically a simple group of 2 redistributable **Python script files** to help fix the problem of Keyboard LEDs that doesn't want to turn on When running on **Linux**. <br>

<br>

## How to compile into distributable binaries?: <br>
**In order to compile these Python script files into Linux binaries, you must have `pyinstaller` installed, alongwith `auto-py-to-exe` when necessary** <br>

### Quick Compilation Guide: <br>
* Download both of the scripts `enable_led` and `disable_led` <br>
* Make a working directory. <br>
```sh
mkdir working-dir
cd working-dir
``` 
<br>

* Copy scripts from your `Downloads` folder to the `working-dir` you have just made. <br>
```sh
cp enable_led.py /working-dir/enable_led.py
cp disable_led.py /working-dir/disable_led.py
```
<br>

* Compile them with `pyinstaller` <br>

```sh
pyinstaller enable_led.py
pyinstaller disable_led.py
```
<br>

* Copy them into `/usr/bin` for easier access later. <br>

```sh
sudo cp enable_led /usr/bin/enable_led
sudo cp disable_led /usr/bin/disable_led
```

<br>

##### **I don't think I have to tell you that you must have to enter your `sudo` password to copy to `/usr/bin`.**

<br>

* Enjoy using them! <br>

```sh
# to enable keyboard backlight
enable_led 
# to disable keyboard backlight
disable_led
# no sudo needed
```

<br>


## License <br>
This script file is licensed under the **Public Domain License**.
