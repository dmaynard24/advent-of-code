# --- Day 2: Password Philosophy ---
# Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

# The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

# Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

# To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

# For example, suppose you have the following list:

# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

# In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

# How many passwords are valid according to their policies?


def password_philosophy(l):
  l = l.split('\n')

  valid_count = 0
  for item in l:
    dash_index = item.index('-')
    min_count = int(item[:dash_index])
    space_index = item.index(' ', dash_index)
    max_count = int(item[dash_index + 1:space_index])
    char = item[space_index + 1]
    password = item[space_index + 4:]
    char_count = 0
    for letter in password:
      if letter == char:
        char_count += 1
    if char_count >= min_count and char_count <= max_count:
      valid_count += 1
  return valid_count