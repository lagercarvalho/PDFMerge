import sys
import os
from os.path import isfile, join
import PyPDF2

def main():
  args = sys.argv[1:]
  all = True
  input_path = os.getcwd()
  pattern = None
  
  if '--h' in args or '--help' in args:
    print('Help message')
  
  if '--pattern' in args:
    all = False
    pattern = get_flag_value('--pattern', args)

  if '--input_path' in args:
    input_path = get_flag_value('--input_path', args)

  if '--output_path' in args:
    output_path = get_flag_value('--input_path', args)
  else:
    output_path = input_path + '\merge.pdf'

  input_paths = get_input_paths(all, pattern, input_path)
  print(f"The following files with {'the ' + pattern.lower() + ' pattern' if pattern else 'no pattern'} will be merged to {output_path}:\n")
  for path in input_paths:
    print("  * " + path)
  print("")

  merge_pdfs(output_path, input_paths)
  print("Merge complete")


def get_flag_value(flag, args):
  try:
    index = args.index(flag)
    if '--' in args[index + 1]:
      print(f"{flag} cannot be followed by a flag, please try again")
    return args[index + 1]
  except (IndexError):
    print(f"{flag} must be followed by a value")
    return None
  
def merge_pdfs(output_path, input_paths):
  pdf_merger = PyPDF2.PdfMerger()

  for path in input_paths:
    with open(path, 'rb') as file:
      pdf_merger.append(file)
  
  with open(output_path, 'wb') as file:
    pdf_merger.write(file)

def get_input_paths(all, pattern, path):
  arr = []
  files = [file for file in os.listdir(path) if isfile(join(path, file))]
  if all:
    arr = [join(path, file) for file in files]
  elif pattern:
    arr = [join(path, file) for file in files if pattern.lower() in file.lower()]
  return arr

if __name__ == "__main__":
  main()