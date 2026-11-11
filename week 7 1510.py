"""
RECORD CHECK  -  my version
===========================

Name  :  Hania SHerif
Lane  :  Cybersecurity
Date  :  11/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# ======================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict.

def parse_line(raw_line):
    """Clean and parse a raw server record line into a dictionary."""
    hostname_part, rest = raw_line.strip().split(",", 1)
    data = {"hostname": hostname_part.strip().lower()}
    
    for piece in rest.split(","):
        key, value = piece.split("=")
        data[key.strip().lower()] = float(value.strip())
        
    return data

raw_records = [
    "  Srv-01 , used=87 , total=100  ",
    "SRV-02,USED=120,TOTAL=100",
    "  srv-03 ,  Used = 45.5 , Total = 200 ",
    "Web-01, used=95, total=100",
    "  DB-MAIN , used=512 , TOTAL=1024  "
]

for raw_record in raw_records:
    cleaned_dict = parse_line(raw_record)
    print(cleaned_dict)

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
