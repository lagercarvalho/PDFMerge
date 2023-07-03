import sys
import os
from os.path import isfile, join
import PyPDF2

def main():
  args = sys.argv[1:]
  all = False
  input_path = ''
  pattern = None
  
  if '--h' in args or '--help' in args:
    print('Help message')
  
  if '--all' in args:
    all = True
  
  if '--pattern' in args:
    pattern = get_flag_value('--pattern', args)

  if '--input_path' in args:
    input_path = get_flag_value('--input_path', args)

  if '--output_path' in args:
    output_path = get_flag_value('--input_path', args)
  else
    output_path = 'merge.pdf'

  input_paths = get_input_paths(all, pattern, input_path, current_dir)

  merge_pdfs(output_path)


def get_flag_value(flag, args):
  try:
    index = args.index(flag)
    if '--' in args[index + 1]:
      print(f"{flag} cannot be followed by a flag, please try again")
    return args[index + 1]
  except (IndexError):
    print(f"{flag} must be followed by a value")
    return None
  
def merge_pdfs(output_path, *input_paths):
  pdf_merger = PyPDF2.PdfFileMerger()

  for path in input_paths:
    with open(path, 'rb') as file:
      pdf_merger.append(file)
  
  with open(output_path, 'wb') as file:
    pdf_merger.write(file)

def get_input_paths(all, pattern, input_path, current_dir):
  current_dir = os.getcwd()
  arr = []
  files = [file for file in os.listdir(current_dir) if isfile(join(current_dir, file))]
  if all:
    arr = files
  elif pattern:
    arr = files.map

if __name__ == "__main__":
  main()