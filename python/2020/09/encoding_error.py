def encoding_error(series, preamble_len):
  series = list(map(int, series.split('\n')))

  for i in range(preamble_len, len(series)):
    is_sum = False
    for j in range(i - preamble_len, i):
      for k in range(j, i):
        if series[j] + series[k] == series[i]:
          is_sum = True
          break
      if is_sum:
        break
    if is_sum == False:
      return series[i]