# dragalia-dialogue-runner

dragalia-dialogue-runner is a Ren'Py project that mimics the UI of the story screen from the game Dragalia Lost.

## Installation

Either clone the repository into your Ren'Py project directory

```bash
git clone https://github.com/chaosspam/dragalia-dialogue-runner.git
```

Or if those words don't make sense, download the project as a ZIP file by clicking the "Code" button (next to "Add file") and click on "Download ZIP". Extract the ZIP file into your Ren'Py project directory (This will be the folder listed under launcher > preferences (bottom right) > Projects Directory).

Make sure the structure is `[Project Directory]/dragalia-dialogue-runner/game` and not `[Project Directory]/dragalia-dialogue-runner/dragalia-dialogue-runner/game`

## Planned

- [ ] Finish animating emotion balloons
- [x] Chararcter rpy file generator (still need improvement)
- [ ] UI for choice screen, not really a Dragalia feature but think about the possibilities

## Probably Too Much Work for Chao

- [ ] Animated backgrounds (There is an example in the project with moving clouds)

## Usage

There is not really a lot done yet. But I'll document this as I go

### script.rpy

This is the file where the dialogue goes (If you are familiar with Ren'Py this shouldn't look too alien).
Just a few things that might make life a bit easier

#### Defining characters
```python
define character_variable = Character("character_name", kind=character_base, callback=speaker("callback_identifier")
```
`character_variable` - used in say statements to make this character say things, ex: `character_variable "Lorem Ipsum"`

`kind=character_base` - make sure to include this for the click to continue arrow to appear

`character_name` - this will appear in the name box on screen

`callback_identifier` - this is used for lip flaping when speaking, see `characters/\[character\].rpy` section for details

#### Showing portraits


#### Emotions
This may change in the future, but for now, use 2 show statements, one for the bubble and one for the emotion (`Composite` does weird things to the anchor if someone knows how to fix it pls make a PR)

```python
# Change left to right for right balloon (not implemented yet)
# default_emo_l is the default position for emotions, use default_emo_r for right (also not implemented yet)

show balloon left at default_emo_l
show note at default_emo_l

fleur "It even makes sound effects."

# Hide them away after dialogue
hide balloon
hide note
```

### characters/\[character\].rpy

This is the file that defines a character. It should include images used for the portrait of a character. (To save data, I did not include the portrait data files for all of the characters, you can download portrait data from [DLPortraits](https://github.com/sh0wer1ee/DLPortraits), just copy the folder containing the character in `portrait_data` to `images/portrait_data` folder in the project, Fleur is included as an example). The file itself probably has better documentation than I can write here so just read the comments there for now.

You can generate the `.rpy` file with [charagen](https://spam.bychao.com/dialogue-runner-charagen/), but you will have to download the portrait images separately as described above

Just make sure
```python
(447, 297), WhileSpeaking("callback_identifier", "fleur mouth normal", "portrait_output/110319_01/110319_01_parts_c018.png")
```
has the right offset number (check `data.json` in `portrait_data/[charId]`), and the `callback_identifier` matches what is used when defining a character

If lipflap is not required, just replace the mouth part with a regular image path, ex.
```python
(447, 297), "portrait_output/110319_01/110319_01_parts_c018.png"
```

### definitions.rpy

This is where most of the emotion stuff / default positions are defined

## Build
I have no idea how building distribution works in Ren'Py will probably update this section later. Go watch a Youtube video for this or sth sorry.

## Contributing
Pull requests are welcome (especially for filling `character.rpy` and `background.rpy` files). For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
