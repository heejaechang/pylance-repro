# ENV: reuse .venv
# DEPS: install from requirements.txt if package-backed prerequisites are missing
# SCENARIO: simplekml document member completion under Pylance
# TARGET: `doc.` on the last line below with the cursor immediately after the dot
# TRIGGER: invoke completion at the target location
# EXPECT: the selected interpreter is the workspace `.venv` and `simplekml` resolves without missing-import diagnostics
# VERIFY: the completion list contains `newschema`
# RECOVER: dismiss the completion list without committing a selection
from simplekml import Kml

kml = Kml(name='Tracks', open=1)
doc = kml.newdocument(name='PMX Track')

doc.