# Copilot Instructions

## Project and workspace

- This is a small Python TDD exercise project under `viikko4/tdd-ostoskori`.
- Run all commands from this project directory with `uv`.
- The project requires Python 3.14 or newer, as defined in `pyproject.toml`.
- pytest is the development dependency; there is no separate lint or build command configured.

## Commands

Run the full test suite:

```bash
uv run pytest
```

Run one test file:

```bash
uv run pytest src/tests/ostoskori_test.py
```

Run one test method:

```bash
uv run pytest src/tests/ostoskori_test.py::TestOstoskori::test_ostoskorin_hinta_ja_tavaroiden_maara_alussa
```

The tests use pytest's unittest integration. Source modules are imported as top-level modules (for example `from ostoskori import Ostoskori`) and pytest is configured to discover tests under `src/tests`.

## Architecture

- `src/tuote.py` contains `Tuote`, the product model. It exposes the product name and price through `nimi()` and `hinta()`.
- `src/ostos.py` contains `Ostos`, which associates one `Tuote` with a quantity. `lukumaara()` reports the quantity, `muuta_lukumaaraa(muutos)` changes it without allowing negative quantities, and `hinta()` returns quantity times unit price.
- `src/ostoskori.py` contains `Ostoskori`, the cart aggregate. It should track product purchases, calculate item count and total price, add/remove products, clear the cart, and return the contained `Ostos` objects.
- `src/tests/ostoskori_test.py` contains the unittest-style pytest tests. `src/index.py` is currently a placeholder.

## Implementation conventions

- The public API and test names are in Finnish. Preserve the existing method names and signatures in `Ostoskori`.
- An `Ostoskori` entry is represented by `Ostos`; use product identity consistently when combining or removing the same `Tuote`.
- `Ostos.hinta()` and quantity changes are already implemented. Reuse them through `Ostoskori` rather than duplicating that behavior.
- `Tuote` and `Ostos` contain the established product and cart-line behavior. Implement the cart behavior primarily in `src/ostoskori.py`.
- Make absolutely minimal code changes that satisfy the tests.
- Do not change `src/ostos.py` or `src/tuote.py`.
- Do not edit tests unless explicitly requested.
