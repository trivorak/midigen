# MIDIgen

### Refocus
---
Refocus of this project to use a Raspberry Pi Zero 2 W with a camera to take pictures and generate midi output from those images. Research will stay in project but the main focus of the project is changed.

### Roadmap
---
 Generate an array based on notes in scale
- [x] Snap to Key
- [ ] RPI camera module
- [ ] Image Color Look up
- [ ] Ever changing image every step (take picture between notes)
- [ ] Midi Not Output



#### "ToDo" Break Down

- [x] Randomly select root note
- [x] Generate a scale array to use for note looking (snap to key/scale)
  - [x] Refactor for loop into a while true loop (cleaner)
- [x] Snap note to Key.
- [x] Setup a folder structure for cleaner function imports
- [x] Randomly select scale (From an Array of Scales)
- [x] Figure out import sys for import errors I get on modules (Thanks Podcast)



### Install Instructions

---

The planning process of project is underway, so there is no path yet into what will be required to run this code. It will be based around Python3. All current requirements have been included in the requirements.txt file

#### Required

```bash
pip install -r requirements.txt
```
#### Extra
##### Update PIP & Install PILLOW (instead of using PIL) - This is not needed but how I setup my environment

```bash
python3 -m pip install --upgrade pip
```
```bash
python3 -m pip install --upgrade Pillow
```
