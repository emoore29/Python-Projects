import re
import operator
from typing import get_args


def arithmetic_arranger(problems, show_results=False):

  # Check that there are no more than five problems in the list
  if len(problems) > 5:
    return "Error: Too many problems."

  # Define split_problem_list outside loop
  split_problem_list = list()

  for problem in problems:
    # Check that problems are in the correct format
    regex = re.compile(r"^\d{1,4}\s[\+\-]\s\d{1,4}$")
    if regex.match(problem) is None:
      print("Error: This problem is in the wrong format:", problem)
      # Check why the problem is invalid:
      # Check for numbers longer than 4 digits
      number_length_check = re.compile(r"\d{5,}")
      if number_length_check.search(problem):
        return "Error: Numbers cannot be more than four digits."

      # Check for incorrect operators
      operator_check = re.compile(r"\s[\*\/]\s")  # e.g. " * " or " / "
      if operator_check.search(problem):
        return "Error: Operator must be '+' or '-'."

      # Check for nondigit characters
      non_digit_check = re.compile(
          r"[^\d\s]")  # e.g. "dfs" or ")4=?" or "*29-"
      if non_digit_check.search(problem):
        return "Error: Numbers must only contain digits."

    # After all tests are passed, arrange problems for easy access

    split_problem_list = [problem.split() for problem in problems]

  # Define lines outside of loop to avoid resetting the line every time it loops
  top_line = ""
  bottom_line = ""
  dashes_line = ""
  totals_line = ""
  NEW_LINE = "\n"

  ops = {"+": operator.add, "-": operator.sub}

  for idx, split_problem in enumerate(split_problem_list):
    # Initialising variables for use
    GAP_BETWEEN_PROBLEMS = "    "  # Constant 4 spaces between each problem
    TOP_GAP = "  "  # Constant operator plus a space in second line
    top_number, operator_string, bottom_number = split_problem
    top_length, bottom_length = len(top_number), len(bottom_number)
    num_top_spaces = 0
    num_bottom_spaces = 0
    num_dashes = 0

    if idx == len(
        split_problem_list
    ) - 1:  # If we are at the last element in the loop, there is no gap between problems and we go straight to \n
      GAP_BETWEEN_PROBLEMS = ""

    # Calculate the totals of each problem (and convert to string)
    total = str(ops[operator_string](int(top_number), int(bottom_number)))

    # Find which number (top or bottom) is longer to determine which line needs additional spaces and how many to add
    if top_length > bottom_length:
      longest = "top"
      num_bottom_spaces = top_length - bottom_length
    else:
      longest = "bottom"
      num_top_spaces = bottom_length - top_length

    # Calculate how many dashes are in third line based on longest number in problem
    if longest == "top":
      num_dashes = top_length + 2  # 2 is constant due to the inclusion of the operator_string and a space on the second line
    else:
      num_dashes = bottom_length + 2

    # Create strings based on above calculations
    top_spaces = " " * num_top_spaces
    bottom_spaces = " " * num_bottom_spaces
    dashes = "-" * num_dashes
    total_spaces = " " * (num_dashes - len(total))

    # Create line strings for each problem
    top_line += TOP_GAP + top_spaces + top_number + GAP_BETWEEN_PROBLEMS
    bottom_line += operator_string + " " + bottom_spaces + bottom_number + GAP_BETWEEN_PROBLEMS
    dashes_line += dashes + GAP_BETWEEN_PROBLEMS
    totals_line += total_spaces + total + GAP_BETWEEN_PROBLEMS

  if show_results:
    return top_line + NEW_LINE + bottom_line + NEW_LINE + dashes_line + NEW_LINE + totals_line
  else:
    return top_line + NEW_LINE + bottom_line + NEW_LINE + dashes_line


result = arithmetic_arranger(['3801 - 2', '123 + 49'], True)
print(result)
