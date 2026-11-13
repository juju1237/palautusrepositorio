# Copilot instructions for this repository

Tämä tiedosto koskee ensisijaisesti Flask-sovellusta `viikko3/login`. Tämä repo sisältää useita eri harjoituskansioita, joten älä yleistä tätä muuhun kuin tähän projektiin.

Tämä on uv-projekti. Suorita komennot aina muodossa `uv run ...` projektikansiosta `viikko3/login`.

## Sovelluksen käynnistäminen

- `cd viikko3/login`
- `uv run python src/index.py`
- Sovellus käynnistyy Flaskin kehityspalvelimena ja toimii osoitteessa `http://localhost:5001` (host `0.0.0.0:5001`).

## Robot Framework -testit

- Suorita testit projektikansiosta:
  - `uv run robot src/tests`
- Testit käyttävät appin HTTP-rajapintaa ja vaativat, että sovellus on jo käynnissä ennen testien ajoa.
- Yhden testitiedoston ajaminen:
  - `uv run robot src/tests/home.robot`
  - `uv run robot src/tests/login.robot`
  - `uv run robot src/tests/register.robot`

## Validointi ja arkkitehtuuri

- Käyttäjätunnuksen ja salasanan validointi tapahtuu `src/services/user_service.py` -tiedostossa `UserService.validate()` ja `check_credentials()` -metodeissa.
- Koko sovellus on pieni Flask-arkkitehtuuri: `src/app.py` (routes) -> `src/services` (business logic) -> `src/repositories` (in-memory storage).
- Robot-testit löytyvät kansiosta `src/tests/` ja odottavat sivujen otsikoita kuten `Login`, `Register` ja `Welcome to Ohtu Application!`.
