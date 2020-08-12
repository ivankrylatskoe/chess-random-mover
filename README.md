# chess-random-mover
Random Mover Chess Player (UCI Engine)

This program is a UCI engine, which makes random legal moves.

How to use
---
In your UCI program, just setup path to the compiled executable binary file (exe file for Windows) .

How to get an executable file
---
You can use a precompiled exe file for Windows (look in `precompiled` folder).
Or you can compile it yourself.

You may need:
* python (https://www.python.org/)
* pip (https://pip.pypa.io/en/stable/installing/)
* pyinstaller (run `pip install pyinstaller`)
* python-chess  (run `pip install python-chess`)

To build an executable from source, run `build.sh`. The file will appear in the `dist` folder.

Options
---
Use `--log` program argument to log sent and received UCI data.
