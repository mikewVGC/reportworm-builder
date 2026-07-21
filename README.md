# Reportworm Builder

This is the site builder I wrote for [Reportworm Standings](https://standings.reportworm.com/) which I don't really recommend using yourself because there are probably more robust and better supported versions of this elsewhere. I am mostly doing this to learn how to write reusable Python modules so I don't have to keep copying code to different repos. I'll eventually add better documentation to this, probably.

## Installing

```
pip install git+https://github.com/mikewVGC/reportworm-builder.git@1.0.0
```

## Usage

Once installed, create a file named `build.json` relative to where your scripts are being run (the class assumes it's in the current working directory). The format can be much more complicated, but this is a very basic example:

```
{
    "builder": {
        "steps": [
            "test_step",
        ],
        "refs": {
            "tpl": "tests/templates"
        },
        "test_step": {
            "type": "html",
            "base-ref": "home",
            "out": "public/index.html"
        }
    }
}
```

Then in your code:

```
# first argument is config, second is cached data
builder = Builder({}, {})

builder.build()
```

This is not at all exhaustive, more documentation will be added later, maybe.

## Build The Module

Build the module:

```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python setup.py sdist bdist_wheel
```

## Testing

To run the very small amount of unit tests:

```
python -m unittest discover -v
```

## License

Reportworm Builder is licensed with the BSD license. See `LICENSE`.
