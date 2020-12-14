import re


def handy_haversacks(rules):
  color_contents = {}

  def does_contain_color(color):
    if color == 'shiny gold':
      return True
    if color in color_contents:
      for nested_color in color_contents[color]:
        if does_contain_color(nested_color):
          return True
    return False

  for rule in rules.split('\n'):
    if rule.find(' no ') > -1:
      continue
    color, contents = re.findall(r'^(.*) bags contain (.*)\.$', rule)[0]
    contents = [re.match(r'^\d (.*) bag', bags).group(1) for bags in contents.split(', ')]
    color_contents[color] = contents
  color_contents.pop('shiny gold')

  count = 0
  for color in color_contents:
    if does_contain_color(color):
      count += 1
  return count