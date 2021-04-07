# golatex
Converts Golang source code to fancvrb for inserting in LaTeX.

## Running
First clone the repository:
```shell
git clone https://github.com/mestru17/golatex.git
```

Then install the dependencies from the cloned repo with pip:
```shell
cd golatex
pip3 install -r requirements.txt
```

You can now run the script with either python:
```shell
python3 golatex somefile.go
```
Or directly in the shell:
```shell
./golatex somefile.go
```

You will have to run it at least once with the `-p`/`--preamble` flag to generate the style setup to paste in your LaTeX preamble:
```shell
./golatex -p somefile.go
```
