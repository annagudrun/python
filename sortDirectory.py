import os
import re

def sortDirectory(dir):

    files = [os.path.join(root, file) for root, _, files in os.walk(dir) for file in files]

    st =  '''RuPaul's Drag Race s02e01.avi
    Arrested Development S04E05.avi
    Breaking.Bad.S04E04.HDTV.XviD-FQM.Bullet.Points.avi
    Friends - [1x20] - The One with the Evil Orthodontist.mkv
    House.of.Cards 2x06 - Chapter 19.mp4
    Modern.Family.S06E13.HDTV.x264-KILLERS.mp4'''

#\[[0-9]+x[0-9]+\]|[0-9]+x[0-9]+
#[Ss]\s*[0-9]+\s*[Ee]\s*[0-9]+
