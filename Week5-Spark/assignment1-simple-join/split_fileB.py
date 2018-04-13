def split_fileB(line):
  date, word_count = line.split(' ')
  word, count_string = word_count.split(',')
  return (word, date + " " + count_string)
