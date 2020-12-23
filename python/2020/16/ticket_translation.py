# --- Day 16: Ticket Translation ---
# As you're walking to yet another connecting flight, you realize that one of the legs of your re-routed trip coming up is on a high-speed train. However, the train ticket you were given is in a language you don't understand. You should probably figure out what it says before you get to the train station after the next flight.

# Unfortunately, you can't actually read the words on the ticket. You can, however, read the numbers, and so you figure out the fields these tickets must have and the valid ranges for values in those fields.

# You collect the rules for ticket fields, the numbers on your ticket, and the numbers on other nearby tickets for the same train service (via the airport security cameras) together into a single document you can reference (your puzzle input).

# The rules for ticket fields specify a list of fields that exist somewhere on the ticket and the valid ranges of values for each field. For example, a rule like class: 1-3 or 5-7 means that one of the fields in every ticket is named class and can be any value in the ranges 1-3 or 5-7 (inclusive, such that 3 and 5 are both valid in this field, but 4 is not).

# Each ticket is represented by a single line of comma-separated values. The values are the numbers on the ticket in the order they appear; every ticket has the same format. For example, consider this ticket:

# .--------------------------------------------------------.
# | ????: 101    ?????: 102   ??????????: 103     ???: 104 |
# |                                                        |
# | ??: 301  ??: 302             ???????: 303      ??????? |
# | ??: 401  ??: 402           ???? ????: 403    ????????? |
# '--------------------------------------------------------'
# Here, ? represents text in a language you don't understand. This ticket might be represented as 101,102,103,104,301,302,303,401,402,403; of course, the actual train tickets you're looking at are much more complicated. In any case, you've extracted just the numbers in such a way that the first number is always the same specific field, the second number is always a different specific field, and so on - you just don't know what each position actually means!

# Start by determining which tickets are completely invalid; these are tickets that contain values which aren't valid for any field. Ignore your ticket for now.

# For example, suppose you have the following notes:

# class: 1-3 or 5-7
# row: 6-11 or 33-44
# seat: 13-40 or 45-50

# your ticket:
# 7,1,14

# nearby tickets:
# 7,3,47
# 40,4,50
# 55,2,20
# 38,6,12
# It doesn't matter which position corresponds to which field; you can identify invalid nearby tickets by considering only whether tickets contain values that are not valid for any field. In this example, the values on the first nearby ticket are all valid for at least one field. This is not true of the other three nearby tickets: the values 4, 55, and 12 are are not valid for any field. Adding together all of the invalid values produces your ticket scanning error rate: 4 + 55 + 12 = 71.

# Consider the validity of the nearby tickets you scanned. What is your ticket scanning error rate?


def create_def(lower_min, lower_max, upper_min, upper_max):
  return lambda num: (num >= lower_min and num <= lower_max) or (num >= upper_min and num <= upper_max)


def ticket_translation(notes):
  rules, _, nearby = [note.split('\n') for note in notes.split('\n\n')]
  nearby = nearby[1:]

  rule_defs = []
  for rule in rules:
    rule_split = rule[rule.index(': ') + 2:].split(' ')
    first_hyphen_i = rule_split[0].index('-')
    second_hyphen_i = rule_split[2].index('-')
    lower_min = int(rule_split[0][:first_hyphen_i])
    lower_max = int(rule_split[0][first_hyphen_i + 1:])
    upper_min = int(rule_split[2][:second_hyphen_i])
    upper_max = int(rule_split[2][second_hyphen_i + 1:])
    rule_defs.append(create_def(lower_min, lower_max, upper_min, upper_max))

  invalid_nums = []
  for ticket in nearby:
    nums = [int(num) for num in ticket.split(',')]
    for num in nums:
      is_valid = False
      for rule_def in rule_defs:
        if rule_def(num):
          is_valid = True
          break
      if is_valid == False:
        invalid_nums.append(num)

  return sum(invalid_nums)


# TODO: part 2


def ticket_translation_part_2(notes):
  rules, mine, nearby = [note.split('\n') for note in notes.split('\n\n')]
  mine = [[int(num) for num in ticket.split(',')] for ticket in mine[1:]]
  nearby = [[int(num) for num in ticket.split(',')] for ticket in nearby[1:]]
  all_tickets = mine + nearby

  rule_defs = {}
  for rule in rules:
    colon_index = rule.index(': ')
    rule_name = rule[:colon_index]
    rule_split = rule[colon_index + 2:].split(' ')
    first_hyphen_i = rule_split[0].index('-')
    second_hyphen_i = rule_split[2].index('-')
    lower_min = int(rule_split[0][:first_hyphen_i])
    lower_max = int(rule_split[0][first_hyphen_i + 1:])
    upper_min = int(rule_split[2][:second_hyphen_i])
    upper_max = int(rule_split[2][second_hyphen_i + 1:])
    rule_defs[rule_name] = create_def(lower_min, lower_max, upper_min, upper_max)

  # discard invalid tickets
  i = 0
  while i < len(all_tickets):
    for num in all_tickets[i]:
      is_valid = False
      for name in rule_defs:
        if rule_defs[name](num):
          is_valid = True
          break
      if is_valid == False:
        all_tickets.pop(i)
        i -= 1
    i += 1

  rule_names = list(rule_defs.keys())

  def set_rule_order(col, rule_order):
    if col == len(mine[0]):
      return rule_order

    order = None
    for name in rule_names:
      if name not in rule_order:
        is_valid_name = True
        for ticket in all_tickets:
          if rule_defs[name](ticket[col]) == False:
            is_valid_name = False
            break
        if is_valid_name == True:
          new_order = {name: col}
          order = set_rule_order(col + 1, {**rule_order, **new_order})
    return order

  order = set_rule_order(0, {})

  if order is not None:
    my_ticket = {name: mine[0][order[name]] for name in list(order.keys())}
    return my_ticket


print(
    ticket_translation_part_2('''class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9'''))