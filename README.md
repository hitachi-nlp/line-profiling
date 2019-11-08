# Profiler
[line-profiler](https://github.com/rkern/line_profiler)のデコーレータ(`@profile`)が使用されている場合，line-profiler未使用時にも，エラーが出ないようにする．

## Installation
```sh
pip install git+https://gitlab.rdcloud.intra.hitachi.co.jp/71389710/kern-profiler
```

## How to use.
* line-profilerのデコレータ(`@profile`)を使うプログラムで，`import profiler`をする．
* [サンプル](./sample.py)
