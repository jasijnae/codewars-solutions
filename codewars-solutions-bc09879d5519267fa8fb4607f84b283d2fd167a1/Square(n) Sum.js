function squareSum(numbers){
  return numbers.reduce((acc, cur) => (cur ** 2)+ acc, 0)
  
}
