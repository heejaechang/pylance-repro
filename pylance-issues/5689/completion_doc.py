# ENV: reuse .venv
# DEPS: install from requirements.txt if package-backed prerequisites are missing
# SCENARIO: completion on simplekml document under Pylance
# TARGET: `doc.` on the last line below
# TRIGGER: open this file, place the cursor after `doc.`, and trigger completions
# EXPECT: the selected interpreter is the workspace `.venv`, `simplekml` resolves successfully, and no missing-import diagnostics are present
# VERIFY: the completion list contains `newfolder`
# RECOVER: none
from simplekml import Kml

kml = Kml(name='Tracks', open=1)
doc = kml.newdocument(name='PMX Track')

doc.