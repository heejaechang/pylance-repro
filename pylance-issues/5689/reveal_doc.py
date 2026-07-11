# ENV: reuse .venv
# DEPS: install from requirements.txt if package-backed prerequisites are missing
# SCENARIO: reveal_type on simplekml document under Pylance
# TARGET: `reveal_type(doc)` on the last line below
# TRIGGER: open this file, wait for diagnostics to settle, and show the Problems panel
# EXPECT: the selected interpreter is the workspace `.venv`, `simplekml` resolves successfully, and Pylance analyzes the file without missing-import diagnostics
# VERIFY: Problems contains `Type of "doc" is "Geometry | Any"`
# RECOVER: none
from simplekml import Kml

kml = Kml(name='Tracks', open=1)
doc = kml.newdocument(name='PMX Track')

reveal_type(doc)