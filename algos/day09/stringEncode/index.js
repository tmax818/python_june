/* 
  Given in an alumni interview in 2021.
  String Encode
  You are given a string that may contain sequences of consecutive characters.
  Create a function to shorten a string by including the character,
  then the number of times it appears. 
  
  
  If final result is not shorter (such as "bb" => "b2" ),
  return the original string.
  R read/restate
  I input
  O output
  T talk
  */
// a: 4
// b: 2
// c: 1
// d: 3
// var a = 4
// var b = 2
//0: 'tyler'
//1: 39
// 2: 555-67-9898
// person = {'name': 'Tyler', 'age': 39}
// object 
"a4b2c1d3"
const freqTable = {}
  const str1 = "aaaabbcddd";
  // {a: 4, b:2, c:1, d:3}
//   freqTable['a'] = 1
//   freqTable['a']+=1
//   freqTable['a']+=1
//   freqTable['a']+=1
//   freqTable['b'] = 1
//   freqTable['b']+=1
//   freqTable['c'] = 1
//   freqTable['d'] = 1
//   freqTable['d']+=1
//   freqTable['d']+=1
//  let newstr = ""
//   for (const property in freqTable) {
//     newstr += `${property}${freqTable[property]}`
//   }
//   console.log(newstr)

//   console.log(freqTable)
  const expected1 = "a4b2c1d3";

  function genFreqTable(str){
    const freqTable = {}
    // {b:1}
    for(let i = 0; i < str.length; i++){
        if(freqTable[str[i]]){
            freqTable[str[i]] += 1
        } else {
          freqTable[str[i]] = 1
        }
    }
    return freqTable

  }
 
console.log(genFreqTable(str1))
  const str2 = "";
  const expected2 = "";
  
  const str3 = "a";
  const expected3 = "a";
  
  const str4 = "bbcc";
  const expected4 = "bbcc";

  /**
   * Encodes the given string such that duplicate characters appear once followed
   * by a number representing how many times the char occurs. Only encode strings
   * when the result yields a shorter length.
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str The string to encode.
   * @returns {string} The given string encoded.
   * "aaa" => "a3"
   * "xx" => "xx"
   */

  function encodeStr(str) {
    const table = genFreqTable(str)
     let newstr = ""
  for (const property in table) {
    newstr += `${property}${table[property]}`
  }
  console.log(newstr)
  if(newstr.length >= str.length){
    return str
  }
  return newstr
  }

console.log(encodeStr(str1) === expected1)
console.log(encodeStr(str2) === expected2)
console.log(encodeStr(str3) === expected3)
console.log(encodeStr(str4) === expected4)