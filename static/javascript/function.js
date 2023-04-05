/*
JavaScript 練習 & 測試
*/


// console.log("測試 1: function");

// function sum(n1, n2) {
//     return n1 + n2;
// }

// let result = sum(456, 789);
// console.log(result);

// let multiply = function(n1, n2) {
//     return n1 * n2;
// }

// result = multiply(10, 100);
// console.log(result);



// console.log("測試 2: Object");

// let obj = new Object();
// obj.num = 456;
// obj.plus_one = function(num) {
//     return this.num + num;
// }

// result = obj.plus_one(123);
// console.log(result);


// let obj_json = {
//     age: 456,
//     name: "Rex",
//     profile: function() {
//         console.log("age:", this.age, " ", "name:", this.name);
//     }
// };

// obj_json.profile();


// console.log("array");

// let array = new Array();

// for (let i = 0; i < 5; i++) {
//     array.push(i);
// }

// for (let i = 0; i < array.length; i++) {
//     console.log("all data: " + array);
// }

/**
 * 
 * @param {string} s 
 * @returns 
 */

function vaild_parentheses(s) {
    let isVaild = false;
    
    if (s != null && s.length % 2 === 0) {
        let left = ['(', '[', '{'];
        let right = [')', ']', '}'];

        let stack = [];
        let i = 0;
        while (i < s.length) {
            for (let j = 0; j < left.length; j++) {
                if (s[i] === left[j]) {
                    stack.push(s[i]);
                }
                else if (s[i] === right[j]) {
                    stack.pop();
                }
            }
            i++;
        }

        if (stack.length === 0) {
            isVaild = true;
        }
        return isVaild;
    }
    else {
        return isVaild;
    }
}

// let s = prompt("輸入括號 限制: ()、[]、{}");
// let result = vaild_parentheses(s);
// console.log(result);






