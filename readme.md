# NES-Memory-Visualization
Scripts and data used for [visualizing the internal memory of an NES as it runs a game][blog].



## Collector
`collector.lua` is the Lua script used to collect memory snapshots and game screenshots.


## Scripts 
Python scripts used to generate the visualizations. Requires python 3. To get started:

```bash
$ pip install -r requirements.txt
```

Scripts must be edited to change the palette, image scaling, and other options

#### `scripts/show.py`
Open a visualization for a single memory dump:

```bash
$ python scripts/show.py data/ducktales/430.data
```

Optionally takes a second argument for a screenshot:

```bash
$ python scripts/show.py data/ducktales/430.data data/ducktales/430.png
```


#### `scripts/main.py`
Generate multiple visualizations and write them to a folder:

```bash
$ python3 scripts/main.py data/drmario-level/ ./out
```

This is useful for creating videos. Optionally takes start and end frames:

```bash
$ python3 scripts/main.py data/drmario-level/ ./out --start 400 --end 1100
```

To combine output images into a video, use `ffmpeg`:

```bash
ffmpeg -framerate 60 -i 'out/%d.png' -vf format=yuv420p output.mp4
```


[blog]: https://blog.mattbierner.com/nes-memory-visualization