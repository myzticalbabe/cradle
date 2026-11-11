# CRADLE

One command over the whole chain, for someone who has Python and a model.

CRADLE is not a fifth part. It is the composition of four that already existed and did
not know about each other:

| Part | Name | What it does |
| --- | --- | --- |
| `sword.py` | **FLAMING SWORD** | sweeps a codebase: find → queue → fix → prove → land |
| `defender.py` | **defender** | turns a prompt into a frame that can be satisfied or refused |
| `sentinel.py` | **REAPER** | reaps a frame whose claims do not resolve, and shows the claim that failed |
| `memory_bridge.py` | **GRIMOIRE** | the written book: every lesson a failed verification authored, recalled by the next frame |
| `chain_server.py` | **server** | one endpoint in the shape your own model already speaks |

CRADLE adds no judgement of its own. Every check it runs is one of those parts, called in
the order that makes each answer meaningful. `CRADLE.md` is the long document; this file
is the front door.

## Install

```bash
# 1. the built wheel, attached to the release (works today, no index needed)
pip install https://github.com/myzticalbabe/cradle/releases/download/v0.1.1/krampus_cradle-0.1.1-py3-none-any.whl

# 2. straight from the repository
pip install "krampus-cradle @ git+https://github.com/myzticalbabe/cradle.git@v0.1.1"

# 3. from a checkout, with the tests
pip install -e ".[test]"
```

`pip install krampus-cradle` works the moment the PyPI trusted publisher exists; the
publish workflow is gated on the repository variable `PYPI_TRUSTED_PUBLISHER` so a tag
that cannot publish leaves a green repository rather than a red X.

Stdlib only — no runtime dependencies. The five parts ship inside the package
(`krampus_cradle/tools/`) because `cradle.py` loads each one from a real file path.

## Use

```bash
cradle --doctor                     # is this machine ready, and what is missing
cradle --demo                       # prove the loop end to end, no model needed
cradle --grimoire                   # read the book back: what it learned
cradle --serve --model-url http://127.0.0.1:11434/v1 --model-name llama3.1
```

`--doctor` prints one line per requirement and exits 1 on any failure — a doctor that
says READY on a broken install sends the user looking in the wrong place.

`--demo` runs the real parts against a real file in a throwaway state directory, and it
includes a **deliberate failed verification** so you can watch a lesson being written. A
demo that only walks the happy path teaches nothing about what the gates refuse.

With hardware and no local model yet (Ollama serves an OpenAI-compatible API):

```bash
ollama pull llama3.1 && ollama serve
cradle --serve --model-url http://127.0.0.1:11434/v1 --model-name llama3.1
```

No model is a supported state: `--serve` still runs and `/ask` answers `503` with that
reason, rather than pretending.

## Layout

```
cradle.py                 the launcher: --doctor, --demo, --grimoire, --serve
tools/sword.py            FLAMING SWORD
tools/defender.py         defender
tools/sentinel.py         REAPER
tools/memory_bridge.py    GRIMOIRE
tools/chain_server.py     server
tests/test_cradle.py      12 tests: the controls, not just the happy path
```

The names are vocabulary, not file names: five gates, a task file and three documents
quote `sentinel.py` and `lessons.jsonl`, so the tool says REAPER where it means the
reaper and the disk says what it always said.

## Tests

```bash
python -m pytest tests -q          # 12 passed
```

## License

CDDL-1.1 — see `LICENSE` and `NOTICE`.
