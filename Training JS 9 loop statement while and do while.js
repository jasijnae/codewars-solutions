function padIt(str,n){
  let i = 1;
  
  while(i <= n){
    if (i % 2 === 0){str = str +'*'} 
    else{str = '*' + str} 
    i++
  }
  return str
}

/* 
add the string to the pad
while the number of * is less than n

if left/ odd add * the left
or
if right/ even add * the right
reassign str
increment up
*/