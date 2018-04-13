def split_show_views(line):
  show, views = line.split(',')
  views = int(views)
  return (show, views)
