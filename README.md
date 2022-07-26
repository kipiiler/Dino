# Dinosaur Tactic

Get away from dinosaurs as a cavemen in the Pre Historic Period.

### How to play
1. Download and run `main.exe`
2. Press `space` to start (Mute music by `M`)
3. `W`, `D`, `S` to move
4. Earn point by collecting food

### Image

![image](https://user-images.githubusercontent.com/56223669/180946255-d7cb4474-9c64-4f61-90bd-6d763c82eddb.png)

![image](https://user-images.githubusercontent.com/56223669/180946496-19f43f95-0db0-45bc-9a16-b2b3ffb63824.png)

### Comming Feats

- [ ] Inventory system
- [ ] Power up
- [ ] Combat system
- [ ] Shop
- [ ] Bosses

### For developer

**Clone the repo**
'git clone https://github.com/kipiiler/Dino/'

**Requirements**

[Python 3.10 or above](https://www.python.org/downloads/release/python-3100/)

[pip 22.2 or above](https://pypi.org/project/pip/)

[pyxel 1.7.1](https://github.com/kitao/pyxel)


Python with specfic version: `py -3.? -m pip ...`

List all version python: `py --list`

**Useful command**
- Download package: `pip install -r requirement.txt`
- Make changed and run the file: `pyxel run main.py`
- Open and edit the assets file: `pyxel edit assets/resources.pyxres`
- Compile into executable file: `nuitka --standalone --onefile --windows-disable-console --include-data dir=PATH_TO_ASSET_FOLDER=assets main.py`
