# TPC

[![PyPI - Version](https://img.shields.io/pypi/v/tpc.svg)](https://pypi.org/project/tpc)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tpc.svg)](https://pypi.org/project/tpc)

-----

**Table of Contents**

- [Installation](#installation)
- [Development](#development)
- [License](#license)

## Installation

```console
pip install tpc
```

## Development

Logs to separate terminal. See https://textual.textualize.io/guide/devtools/#console

In one terminal run the console output

```console
hatch run devconsole
```

... in another terminal run the app in dev mode ...

```console
hatch run dev
```

... and then you should be able to see the output in the first terminal!

Note, you may need to run `hatch config set dirs.env.virtual .hatch` to create the virual environment in the .hatch directory in this dir so that VSCode and similar can be pointed to the right place.

## License

`tpc` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
