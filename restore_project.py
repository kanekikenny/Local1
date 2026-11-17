"""Restore the complete verified project from repository archive parts."""
from pathlib import Path
import hashlib,io,zipfile
ROOT=Path(__file__).resolve().parent
PARTS=['Local_LLM_Science_Project.zip.001', 'Local_LLM_Science_Project.zip.002', 'Local_LLM_Science_Project.zip.003', 'Local_LLM_Science_Project.zip.004', 'Local_LLM_Science_Project.zip.005', 'Local_LLM_Science_Project.zip.006']
EXPECTED='4a3264cec91ad55d8f5c73191381087616112f3147b5c5f014fa62888fa8e6fa'
data=b''.join((ROOT/n).read_bytes() for n in PARTS)
if hashlib.sha256(data).hexdigest()!=EXPECTED:
 raise RuntimeError('Checksum mismatch: download all archive parts again.')
target=ROOT/'local_science_project'
if target.exists():
 raise RuntimeError('local_science_project already exists; restore into a fresh directory.')
with zipfile.ZipFile(io.BytesIO(data)) as z:
 for info in z.infolist():
  dest=(ROOT/info.filename).resolve()
  if not dest.is_relative_to(ROOT.resolve()):raise RuntimeError('Unsafe archive member')
 if z.testzip() is not None:raise RuntimeError('Corrupted ZIP archive')
 z.extractall(ROOT)
print('Restored:',target)
print('Read local_science_project/README.md for dependencies, model download and execution.')
