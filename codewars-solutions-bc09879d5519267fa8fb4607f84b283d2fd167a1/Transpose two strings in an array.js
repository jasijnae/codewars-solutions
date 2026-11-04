function transposeTwoStrings(array) {

  let long = Math.max(array[0].length, array[1].length)
  return Array.from({ length : long }, (_,i) => 
    (array[0][i] || ' ') + " " + (array[1][i] || ' ')
  ).join('\n')  
  
}
