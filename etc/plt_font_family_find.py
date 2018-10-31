import matplotlib.font_manager

avail_font_names = [f.name for f in matplotlib.font_manager.fontManager.ttflist if 'nanum' in f.name.lower()]

print(avail_font_names)
