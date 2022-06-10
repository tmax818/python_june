/* 
  Acronyms
  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 
  Do it with .split first if you need to, then try to do it without
  R read/restate
  I input
  O output
  T talk
*/


const str1_arg = "there's no free lunch - gotta pay yer way.";
const expected1 = "TNFL-GPYW";

const str2_arg = "Live from New York, it's Saturday Night!";
const expected2 = "LFNYISN";

/**
 * Turns the given str into an acronym.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string to be turned into an acronym.
 * @returns {string} The given str converted into an acronym.
 */
// const str1_arg = " there's no free lunch - gotta pay yer way. ";
// const expected1 = "TNFL-GPYW";
function acronymize(str_param) {
  let new_str = ""
  const arr = str_param.split(" ")
  for (let i = 0; i < arr.length; i++) {
    console.log(i, arr[i][0])
    new_str += arr[i][0]
  }
    console.log(new_str)
    return new_str.toUpperCase()

}

console.log(acronymize(str1_arg))
console.log(acronymize(str2_arg))
