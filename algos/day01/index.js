

// Print 1 - 255
// print1To255() Print all the integers from 1 to 255


// function print1To255(){
//     for(var i = 1; i < 256; i++){
//         console.log(i)
//     }
// }

// print1To255()

// Print Odds 1 - 255
// printOdds1To255() Print all the odd integers from 1 to 255

// function printOdds1To255(){
//     for(var i = 1; i < 256; i++){
//         if(i % 2 !== 0){
//             console.log(i)
//         }
//     }
// }

// printOdds1To255()

// Print Sum 0-255
//Print integers from 0 to 255, and with each integer print the sum so far.

// function printSum1To255(){
//     var sum = 0;
//     for(var i = 0; i <= 255; i++){
//         sum = sum + i;
//         console.log(sum)
//     }
// }

// printSum1To255()


//Find and Print Max
//Given an array, find and print its largest element.
max = 204
const arr1 = [4,6,2,8,9,204]
function printMaxOfArray(arrParam){
    var max = arrParam[0]    
    for(var i = 0; i < arrParam.length;i++){
        if(arrParam[i] > max){
            max = arrParam[i]
        }
    }
    console.log(max)
}


printMaxOfArray(arr1)
// printMaxOfArray([4,5,6,7,9])
// printMaxOfArray("Hi mom")