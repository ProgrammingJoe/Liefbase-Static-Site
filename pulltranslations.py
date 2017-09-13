import re

def main():
  with open('messages.po', 'r') as myfile:
    data=myfile.read().replace('\n', '').replace('msgid', '$').replace('msgstr', '$')

  regex = ur"\$ [^$]*\$"
  strings_to_translate = re.findall(regex, data)

  counter = 0
  f = open('example.txt','w')
  for sentence in strings_to_translate:
      if counter == 3 and '#' not in sentence:
        f.write(sentence[3:-2].replace('"', '').replace('\n', '').replace('\t', '') + "\n")
      else:
        counter += 1
  f.close()

if __name__ == '__main__':
   main()
