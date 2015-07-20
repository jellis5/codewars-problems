#From http://www.codewars.com/kata/5235c913397cbf2508000048

#Description:

#Create a simple calculator that given a string of operators (+ - * and /) and numbers separated by spaces returns the value of that expression

#Example:

#Calculator.new.evaluate("2 / 2 + 3 * 4 - 6") # => 7

#Remember about the order of operations! Multiplications and divisions have a higher priority and should be performed left-to-right. Additions and subtractions have a lower priority and should also be performed left-to-right.

class Calculator
  def evaluate(string)
    divMultRegex = /-?\d+\s+[\*\/]+\s+-?\d+/ # "int (*|/) int"
    addSubRegex = /-?\d+\s+[\-\+]+\s+-?\d+/ # "int (+|-) int"
    # while instances of "int (*|/) int"...
    while m = string.match(divMultRegex)
      # store indices that make up match
      startInd = string.index(divMultRegex)
      endInd = startInd + m.to_s.length - 1
      # evaluate match and replace indices with evaluation in original string
      string = string[0...startInd] + evalSimple(m.to_s).to_s + string[endInd+1...string.length]
    end
    # while instances of "int (+|-) int"...
    while m = string.match(addSubRegex)
      startInd = string.to_s.index(addSubRegex)
      endInd = startInd + m.to_s.length - 1
      string = string[0...startInd] + evalSimple(m.to_s).to_s + string[endInd+1...string.length]
    end
  string.to_i
  end
  def evalSimple(string)
    operand1, operator, operand2 = string.split
    operand1 = operand1.to_i
    operand2 = operand2.to_i
    case operator
    when '+'
      operand1 + operand2
    when '-'
      operand1 - operand2
    when '*'
      operand1 * operand2
    when '/'
      operand1 / operand2
    end
  end
end
