from pathlib import Path
import sys
BASE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(BASE/'skill/campus-gap-diagnoser/scripts'))
sys.path.insert(0,str(BASE/'tools'))
