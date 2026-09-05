# Wii Homebrew Template

A reusable template project for building homebrew applications for the Nintendo Wii with devkitPPC.

It includes a working build setup and an example that shows how C code can call routines written in PowerPC assembly.

## Contents

- `Makefile` - build setup for devkitPPC
- `source/main.c` - main C entry point
- `source/math.asm` - example PowerPC assembly routines
- `main.py` - packs the built `.dol` into a `.zip` (with `boot.dol`, `meta.xml`, `icon.png`)
- `meta.xml` - Wii homebrew metadata

## Requirements

- [devkitPPC](https://devkitpro.org/) with `DEVKITPPC` set in your environment
- A Wii or an emulator (for testing)

## Getting started

1. Copy this folder and rename it for your project.
2. Set the output target. By default the `Makefile` uses the current directory name.
3. Edit `source/main.c` and `source/math.asm` for your own code.
4. Build:

```sh
make
```

This produces a `.dol` file.

## Packaging

After building, package the app into a `.zip` that can be run from a loader (for example USB Loader GX or the Homebrew Channel):

```sh
python3 main.py
```

The script will:

1. Rename your `.dol` to `boot.dol`.
2. Create a default `meta.xml` if none exists.
3. Include `icon.png` if it is present.
4. Create a `.zip` containing `boot.dol`, `meta.xml` and `icon.png`.

## Running

Use `make run` to load the `.dol` via `wiiload`, or copy the built `.zip` to your SD card.

## Assembly example

`source/main.c` calls a few functions implemented directly in PowerPC assembly (`source/math.asm`):

- `asm_add(a, b)` - addition
- `asm_mul(a, b)` - multiplication
- `asm_sub(a, b)` - subtraction

Press the HOME button on your Wii Remote to exit the demo.

## Clean up

```sh
make clean
```
