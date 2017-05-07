# d3-preppers
Python functions to help prepare data for D3.

## Basic usage

### D3graph

Convenience method for building d3 style node and link arrays in Python.

```
data = [
    ['a','b',5],
    ['a','c',5],
    ['b','c',5],
    ['c','d',10],
    ['c','e',10],
    ['f','a',10],
    ['g','a',10],
    ['f','b',10],
    ['g','c',10],
]
for row in data:
    g.add_link(row[0], row[1], row[2])
g.export('test.json')
```

## Helpful tutorials

- [Understanding D3.js Force Layout - 1: The Simplest Possible Graph](http://bl.ocks.org/sathomas/11550728) (a series)
- [Mike Bostock’s Les Misérables graph](https://bl.ocks.org/mbostock/4062045)
- [Basics of d3 force directed graphs](http://www.puzzlr.org/basics-of-d3-force-directed-graphs/)
- [d3-force: minimal working example](https://bl.ocks.org/puzzler10/4efcb280a23c2f9b824879771ae41592)
