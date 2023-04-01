# mode.py
from collections import Counter
import typing


def idk(a, b):
  return a * b

def mode(data: typing.Sequence[typing.Any]) -> list[typing.Any]:
  """_summary_

  Parameters
  ----------
  data : typing.Sequence[typing.Any]
      _description_

  Returns
  -------
  list[typing.Any]
      _description_
  """
  counter = Counter(data)
  _, top_count = counter.most_common(1)[0]
  return [point for point, count in counter.items() if count == top_count]

def mode2(data: typing.Sequence[typing.Any]) -> list[typing.Any]:
  """_summary_

  Parameters
  ----------
  data : typing.Sequence[typing.Any]
      _description_

  Returns
  -------
  list[typing.Any]
      _description_
  """
  counter = Counter(data)
  _, top_count = counter.most_common(1)[0]
  return [point for point, count in counter.items() if count == top_count]

def mode3(data: typing.Sequence[typing.Any]) -> list[typing.Any]:
  """_summary_

  Parameters
  ----------
  data : typing.Sequence[typing.Any]
      _description_

  Returns
  -------
  list[typing.Any]
      _description_
  """
  counter = Counter(data)
  _, top_count = counter.most_common(1)[0]
  return [point for point, count in counter.items() if count == top_count]

def mode4(data: typing.Sequence[typing.Any]) -> list[typing.Any]:
  """_summary_

  Parameters
  ----------
  data : typing.Sequence[typing.Any]
      _description_

  Returns
  -------
  list[typing.Any]
      _description_
  """
  counter = Counter(data)
  _, top_count = counter.most_common(1)[0]
  return [point for point, count in counter.items() if count == top_count]
